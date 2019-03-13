#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Uhd Adsb 6
# Generated: Tue Dec 13 22:52:41 2016
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import adsb


class uhd_adsb_6(gr.top_block):

    def __init__(self, dc_block_len=4, rx_gain=40):
        gr.top_block.__init__(self, "Uhd Adsb 6")

        ##################################################
        # Parameters
        ##################################################
        self.dc_block_len = dc_block_len
        self.rx_gain = rx_gain

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.freq = freq = 1090e6
        self.filename = filename = "./bytes_" + str(dc_block_len) + ".csv"

        ##################################################
        # Message Queues
        ##################################################
        adsb_decoder_0_msgq_out = blocks_message_source_0_msgq_in = gr.msg_queue(2)
        adsb_framer_0_msgq_out = adsb_decoder_0_msgq_in = gr.msg_queue(2)

        ##################################################
        # Blocks
        ##################################################
        self.digital_correlate_access_code_tag_bb_0 = digital.correlate_access_code_tag_bb('1010000101000000', 0, 'adsb_preamble')
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(dc_block_len, True)
        self.blocks_message_source_0 = blocks.message_source(gr.sizeof_char*1, blocks_message_source_0_msgq_in)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/leffke/sandbox/adsb/adsb_20161212_2M_2.32fc', False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, filename, True)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.adsb_framer_0 = adsb.framer(tx_msgq=adsb_framer_0_msgq_out)
        self.adsb_decoder_0 = adsb.decoder(rx_msgq=adsb_decoder_0_msgq_in,tx_msgq=adsb_decoder_0_msgq_out,output_type="csv",check_parity=True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_message_source_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_correlate_access_code_tag_bb_0, 0))
        self.connect((self.digital_correlate_access_code_tag_bb_0, 0), (self.adsb_framer_0, 0))

    def get_dc_block_len(self):
        return self.dc_block_len

    def set_dc_block_len(self, dc_block_len):
        self.dc_block_len = dc_block_len
        self.set_filename("./bytes_" + str(self.dc_block_len) + ".csv")

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
        self.blocks_file_sink_0.open(self.filename)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "-d", "--dc-block-len", dest="dc_block_len", type="intx", default=4,
        help="Set dc_block_len [default=%default]")
    parser.add_option(
        "", "--rx-gain", dest="rx_gain", type="eng_float", default=eng_notation.num_to_str(40),
        help="Set rx_gain [default=%default]")
    return parser


def main(top_block_cls=uhd_adsb_6, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(dc_block_len=options.dc_block_len, rx_gain=options.rx_gain)
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
