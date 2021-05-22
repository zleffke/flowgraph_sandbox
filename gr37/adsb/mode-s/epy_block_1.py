#!/usr/bin/env python


import numpy
import pmt
import binascii
import numpy
import math
import datetime
from gnuradio import gr

SEARCH = 1
COPY = 2

class uf_frame_sync(gr.sync_block):
    """
    Expects Correlate Access Code - Tag block upstream.
    Tag indicates the last bit of the UF frame sync
    Operates on unpacked byte stream.

    Logic:
     Detects a packet tag.
     pulls out the following 112 bits (max UF frame)
     Emits a PMT/PDU Message of decoded frame
    
    Time Control:
     If 'rx_time' tag exists (from UHD / SigMF), use to create 'datetime'

    OUTPUT:
     async PDU with metadata and UNPACKED 112 bit frame

    """
    def __init__(self, tag_name="packet", msg_len=112, samp_rate = 8e6, sps = 2):
        gr.sync_block.__init__(self,
            name="(UF) Sync",
            in_sig=[numpy.int8],
            out_sig=None)

        self.tag_name = tag_name
        self.offset_key = self.tag_name + "_offset"
        self.message_port_register_out(pmt.intern("out"))
        self.msg_len = msg_len
        self.samp_rate = samp_rate
        self.sps = sps
        self.samp_period = 1.0 / (samp_rate/sps) #seconds per sample
        
    def work(self, input_items, output_items):
        in0 = input_items[0]
        num_input_items = len(in0)
        return_value = num_input_items
        nread = self.nitems_read(0)

        #read in all tags - convert to dict
        tags = self.get_tags_in_window(0, 0, num_input_items)
        self.tag = {}
        for t in tags:
            key = pmt.to_python(t.key) # convert from PMT to python string
            value = pmt.to_python(t.value) 
            self.tag[key] = value
            if key == self.tag_name:
                offset = t.offset
                self.tag[self.offset_key] = offset-nread #offset within window
        
        #look for specific trigger tag (probably 'sync') to indicate frame delimiter
        if all(x in self.tag.keys() for x in [self.tag_name, 'rx_time', 'es::event_time']):
            #print self.tag[self.tag_name]
            if self.tag[self.tag_name] == 1:
                idx_start = self.tag[self.offset_key]
            else: 
                idx_start = self.tag[self.offset_key]+1
            idx_stop  = idx_start + self.msg_len
            msg = in0[idx_start:idx_stop]
            
            #Correct timestamp for sample offset in window            
            time_offset = self.samp_period * self.tag[self.offset_key]
            time_delta = self.tag['es::event_time'] / (self.samp_rate * self.sps)
            rx_int_sec = self.tag['rx_time'][1][0]
            rx_frac_sec = self.tag['rx_time'][1][1]
            td = math.modf(time_delta)
            dt = (numpy.int64(rx_int_sec + td[1]) , rx_frac_sec + td[0])
            ts = numpy.datetime64(datetime.datetime.utcfromtimestamp(dt[0]))
            ts = ts + numpy.timedelta64(int(dt[1]*1e9), 'ns') + numpy.timedelta64(int(time_offset*1e9), 'ns')
            ts_ns = numpy.datetime_as_string(ts) +"Z"
            self.tag['datetime'] = ts_ns
            
            #Create output pdu and emit
            meta = pmt.to_pmt(self.tag)
            vector = pmt.to_pmt(msg)
            pdu = pmt.cons(meta, vector)
            self.message_port_pub(pmt.intern('out'), pdu)
        
        return num_input_items


