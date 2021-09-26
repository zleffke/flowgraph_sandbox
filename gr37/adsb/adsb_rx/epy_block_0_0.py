#!/usr/bin/env python


import numpy as np
import pmt
import binascii
import math
import datetime
import struct
import sys
from gnuradio import gr

# Uplink Format, 5 bits
# Aeronautical Telecommunications: Annex 10 to the Convention on International Civil Aviation, Volume IV Surveillance and Collision Avoidance Systems. International Civil Aviation Organization (ICAO), fifth edition, July 2015
# Figure 3-7. Summary of Mode S interrogation or uplink formats
# Page 3-91 (pdf page 115)
UF_STR_LUT = (
    'Short Air-Air Surveillance (ACAS)',
    'Reserved',
    'Reserved',
    'Reserved',
    'Surveillance Altitude Request',
    'Surveillance Identity Request',
    'Reserved',
    'Reserved',
    'Reserved',
    'Reserved',
    'Reserved',
    'Mode-S Only All-Call',
    'Reserved',
    'Reserved',
    'Reserved',
    'Reserved',
    'Long Air-Air Surveillance (ACAS)',
    'Reserved',
    'Reserved',
    'Reserved for Military Use',
    'Comm-B Altitude Request',
    'Comm-B Identity Request',
    'Reserved for Military Use',
    'Reserved',
    'Comm-D (ELM)'
)

class uf_decode(gr.sync_block):
    """
    Expected Upstream Block:  UF Sync (Uplink Frame Sync)
    Expected input:  PDU with 112 bits, UNPACKED byte format

    Goal:
        Attempts to decode packet, 
        determine UF type (i.e. UF0 = ACAS short air surveillance)
        Decode address (ICAO) and check parity

    Output:
        JSON Object with decoded information
    """
    def __init__(self, msg_filter='All Messages', verbose = True):
        gr.sync_block.__init__(self,
            name="UF Decode",
            in_sig=None,
            out_sig=None)

        self.msg_filter = msg_filter
        self.verbose = verbose
        self.message_port_register_in(pmt.intern("in"))
        self.set_msg_handler(pmt.intern('in'), self.handler)
        self.message_port_register_out(pmt.intern("out"))

        # Initialize plane dictionary
        self.plane_dict = dict([])

        self.decoded = {}
        
    def work(self, input_items, output_items):
        assert(false)


    def handler(self, pdu):

        # Grab packet PDU data
        meta = pmt.to_python(pmt.car(pdu))
        vector = pmt.cdr(pdu)
        if not pmt.is_u8vector(vector):
            print "[ERROR] Received invalid message type. Expected u8vector"
            return

        vector = pmt.to_python(pmt.cdr(pdu))

        self.snr = meta['snr']
        self.meta = meta
        # print 'vector\n', vector
        # print 'vector.dtype\n', vector.dtype
        # print 'type(vector)\n', type(vector)
        self.bits = vector

        #print meta
        #print self.bits
        
        #data = list(pmt.u8vector_elements(msg))
        #packed = self._pack_bytes(data)
        #hex_str = binascii.hexlify(packed)
        #print data, hex_str
        #self._decode_type(packed)
        try:
            self._decode_header()
            self._parse_payload()
            parity_passed = self._check_parity()
        except Exception as e: # catch *all* exceptions
            print e
        #print self.decoded


    

    


    # http://www.bucharestairports.ro/files/pages_files/Vol_IV_-_4yh_ed,_July_2007.pdf
    # http://www.icao.int/APAC/Documents/edocs/cns/SSR_%20modesii.pdf
    # http://www.anteni.net/adsb/Doc/1090-WP30-18-DRAFT_DO-260B-V42.pdf
    # http://www.cats.com.kh/download.php?path=vdzw4dHS08mjtKi6vNi31Mbn0tnZ2eycn6ydmqPE19rT7Mze4cSYpsetmdXd0w==
    # http://www.sigidwiki.com/images/1/15/ADS-B_for_Dummies.pdf
    def _decode_header(self):  
        # Uplink Format, 5 bits
        self.uf = self.bin2dec(self.bits[0:0+5])
        self.uf_str = "UF{:d}".format(self.uf)
        if self.uf in [0,4,5]:
            # 56 bit payload
            self.payload_length = 56
            self.payload = self.bits[0:self.payload_length]
            #print len(self.payload), self.payload
 
    def bin2dec(self, bits):
        return int(''.join(map(str, bits)), 2)

    def _parse_payload(self):
        if self.uf_str == 'UF0':
            self.rl = self.payload[8]
            self.aq = self.payload[13]
            self.ds = self.payload[14:22]
            self.ap = self.payload[32:32+24]
            
            if self.verbose:
                #print '\n'
                print '----------------------------------------------------------------------'
                print self.meta
                print len(self.payload), self.payload
                print 'datetime: {:s}'.format(self.meta['datetime'])
                print '     SNR: {:2.2f} dB'.format(self.meta['snr'])
                print '    SYNC: {:d}'.format(self.meta['sync'])
                print '      UF: {:d} {:s}'.format(self.uf, UF_STR_LUT[self.uf])
                print '      RL: {:d}'.format(self.rl)
                print '      AQ: {:d}'.format(self.aq)
                print '      DS: 0x{:04x}'.format(self.bin2dec(self.ds))
                print ' bits AP:', self.ap
                print '  hex AP: 0x{:06x}'.format(self.bin2dec(self.ap))

            #Create output pdu and emit
            meta = pmt.to_pmt(self.meta)
            vector = pmt.to_pmt(self.payload)
            pdu = pmt.cons(meta, vector)
            self.message_port_pub(pmt.intern('out'), pdu)

    

    # http://jetvision.de/sbs/adsb/crc.htm
    def _check_parity(self):
        # DF CRC polynomial (0xFFFA048) = 1 + x + x^2 + x^3 + x^4 + x^5 + x^6 + x^7 + x^8 + x^9 + x^10 + x^11 + x^12 + x^14 + x^21 + x^24
        crc_poly = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,1,0,0,1])        
        # UF CRC polynomial (0x1205FFF) = 1 + x^3 + x^10 + x^12 + x^13 + x^14 + x^15 + X^16 + x^17 + x^18 + x^19 + X^20 + x^21 + x^22 + x^23 + x^24
        #crc_poly = np.array([1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1])

        if self.uf in [0,4,5]:
            # 56 bit payload
            self.payload_length = 56
            #payload = self.bits[0:self.payload_length]
            #print len(payload), payload

            # Address/Parity, 24 bits
            ap_bits = self.bits[32:32+24]
            crc_bits = self.compute_crc(self.bits[0:self.payload_length-24], crc_poly)            
            crc = self.bin2dec(crc_bits)

            # XOR the computed CRC with the AP, the result should be the
            # interrogated plane's ICAO address
            self.aa_bits = crc_bits ^ ap_bits
            self.aa = self.bin2dec(self.aa_bits)
            self.aa_str = '%06x' % (self.aa)

            parity_passed = self.plane_dict.has_key(self.aa_str) == True
            if parity_passed:
                self.plane_dict[self.aa_str] += 1
            else:
                self.plane_dict[self.aa_str] = 0

            if self.verbose:
                print '      AA: 0x{:06x}'.format(self.aa)
                print 'AA count: {:d}'.format(self.plane_dict[self.aa_str])
                print '----------------------------------------------------------------------'

        return 0




    # http://jetvision.de/sbs/adsb/crc.htm
    def _check_parity_old(self):
        # DF CRC polynomial (0xFFFA048) = 1 + x + x^2 + x^3 + x^4 + x^5 + x^6 + x^7 + x^8 + x^9 + x^10 + x^11 + x^12 + x^14 + x^21 + x^24
        crc_poly = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,1,0,0,1])        
        # UF CRC polynomial (0x1205FFF) = 1 + x^3 + x^10 + x^12 + x^13 + x^14 + x^15 + X^16 + x^17 + x^18 + x^19 + X^20 + x^21 + x^22 + x^23 + x^24
        #crc_poly = np.array([1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1])

        if self.msg_filter == 'All Messages':
            if self.uf in [0,4,5]:
                # 56 bit payload
                self.payload_length = 56
                payload = self.bits[0:self.payload_length]
                print len(payload), payload

                # Address/Parity, 24 bits
                ap_bits = self.bits[32:32+24]

                crc_bits = self.compute_crc(self.bits[0:self.payload_length-24], crc_poly)            
                crc = self.bin2dec(crc_bits)

                # XOR the computed CRC with the AP, the result should be the
                # interrogated plane's ICAO address
                self.aa_bits = crc_bits ^ ap_bits
                self.aa = self.bin2dec(self.aa_bits)
                self.aa_str = '%06x' % (self.aa)

                # If the ICAO address is in our plane dictionary,
                # then it's safe to assume the CRC passes
                parity_passed = self.plane_dict.has_key(self.aa_str) == True

                if parity_passed == True:
                    if self.verbose:
                        print 'CRC:'.ljust(16) + 'Passed (Recognized AA from AP)'
                        print 'AA:'.ljust(16) + '%s' % (self.aa_str)
                    return 1
                else:
                    if self.verbose:
                        print 'CRC:'.ljust(16) + 'Failed (Unrecognized AA from AP)'
                        print 'AA:'.ljust(16) + '%s' % (self.aa_str)
                    return 0

            elif self.uf in [11]:
                # 56 bit payload
                self.payload_length = 56

                # Parity/Interrogator ID, 24 bits
                pi_bits = self.bits[32:32+24]
                pi = self.bin2dec(pi_bits)

                crc_bits = self.compute_crc(self.bits[0:self.payload_length-24], crc_poly)            
                crc = self.bin2dec(crc_bits)

                # result_bits = pi_bits ^ crc_bits
                # print 'pi_bits', pi_bits
                # print 'crc_bits', crc_bits
                # print 'result_bits', result_bits
                # parity_passed = (pi_bits[:7] == crc_bits[:7])

                parity_passed = (pi == crc)

                # 17 0s
                # Code Label, 3 bits (3.1.2.5.2.1.3)
                # Interrogator Code, 4 bits (3.1.2.5.2.1.2)

                if parity_passed == True:
                    if self.verbose:
                        print 'CRC:'.ljust(16) + 'Passed'
                    return 1
                else:
                    if self.verbose:
                        print 'CRC:'.ljust(16) + 'Failed (PI-CRC = %d)' % (pi-crc)
                    return 0

            elif self.uf in [16,20,21,24]:
                # 112 bit payload
                self.payload_length = 112

                # Address/Parity, 24 bits
                ap_bits = self.bits[88:88+24]

                crc_bits = self.compute_crc(self.bits[0:self.payload_length-24], crc_poly)            
                crc = self.bin2dec(crc_bits)

                # XOR the computed CRC with the AP, the result should be the
                # interrogated plane's ICAO address
                self.aa_bits = crc_bits ^ ap_bits
                self.aa = self.bin2dec(self.aa_bits)
                self.aa_str = '%06x' % (self.aa)

                # If the ICAO address is in our plane dictionary,
                # then it's safe to assume the CRC passes
                parity_passed = self.plane_dict.has_key(self.aa_str) == True

                if parity_passed == True:
                    if self.verbose:
                        print 'CRC:'.ljust(16) + 'Passed (Recognized AA from AP)'
                        print 'AA:'.ljust(16) + '%s' % (self.aa_str)
                    return 1
                else:
                    if self.verbose:
                        print 'CRC:'.ljust(16) + 'Failed (Unrecognized AA from AP)'
                        print 'AA:'.ljust(16) + '%s' % (self.aa_str)
                    return 0

        if self.msg_filter == 'All Messages' or self.msg_filter == 'Extended Squitter Only':
            if self.uf in [17,18,19]:
                # 112 bit payload
                self.payload_length = 112

                # Parity/Interrogator ID, 24 bits
                pi = self.bin2dec(self.bits[88:88+24])

                crc_bits = self.compute_crc(self.bits[0:self.payload_length-24], crc_poly)
                crc = self.bin2dec(crc_bits)

                parity_passed = (pi == crc)

                if parity_passed == True:
                    if self.verbose:
                        print 'CRC:'.ljust(16) + 'Passed'
                    return 1
                else:
                    if self.verbose:
                        print 'CRC:'.ljust(16) + 'Failed (PI-CRC = %d)' % (pi-crc)
                    return 0

        # Unsupported downlink format
        #print 'Unsupported downlink format'
        return 0 # Parity failed


    # http://www.radarspotters.eu/forum/index.php?topic=5617.msg41293#msg41293
    # http://www.eurocontrol.int/eec/gallery/content/public/document/eec/report/1994/022_CRC_calculations_for_Mode_S.pdf
    def compute_crc(self, data, poly):
        print data
        num_data_bits = len(data)
        num_crc_bits = len(poly)-1

        # Multiply the data by x^(num_crc_bits), which is equivalent to a 
        # left shift operation which is equivalent to appending zeros
        data = np.append(data, np.zeros(num_crc_bits, dtype=int))

        for ii in range(0,num_data_bits):
            if data[ii] == 1:
                # XOR the data with the CRC polynomial
                # NOTE: The data polynomial and CRC polynomial are Galois Fields
                # in GF(2)
                data[ii:ii+num_crc_bits+1] ^= poly

        crc = data[num_data_bits:num_data_bits+num_crc_bits]

        return crc

    def _decode_type_old(self,data):
        print type(data), binascii.hexlify(data)
        
        #Frame Type:  bits 0-4 (1-5)
        a = data[0]
        uf = (a >> 3) & 0x1F #Hi Nibble
        if self.verbose: 
            #print "Type field: {:08b}".format(uf)
            if    uf==0: print "DF0: Short Air-to-air surveillance (ACAS)"
            elif  uf==4: print "DF4: Surveillance, altitude request"
            elif  uf==5: print "DF5: Surveillance, identify request"
            elif uf==11: print "DF11: Mode-S only all call"
            elif uf==16: print "DF16: Long Air-to-air surveillance (ACAS)"
            elif uf==20: print "DF20: Comm-A, altitude request"
            elif uf==21: print "DF21: Comm-A, identify request"
            elif uf==21: print "DF21: Comm-A, identify request"
            elif uf==24: print "DF24: Comm-C, ELM"
            elif uf==19 or uf==22: print "DF{:d}: Reserved, Military Use".format(uf)
            else: print "DF{:d}: Reserved".format(uf)
        self.decoded['type'] = "UF{:d}".format(uf)
        
        #RL And AQ
        rl_aq_byte = data[1]
        self.decoded['RL'] = (rl_aq_byte >> 7) & 0x01
        self.decoded['AQ'] = (rl_aq_byte >> 1) & 0x01

        #BDS
        bds_bytes = data[1:3]
        if self.verbose: 
            print len(bds_bytes), numpy.uint16(bds_bytes)# & 0xFFFF)

        bds = numpy.uint16(struct.unpack('<H',bds_bytes))[0] # >> 1) & 0x7FFFFF)
        
        print bds, binascii.hexlify(data[1:3]), binascii.hexlify(bds)
        #self.decoded['BDS'] = binascii.hexlify(numpy.uint16(bds_bytes & 0xFF))

    # http://www.bucharestairports.ro/files/pages_files/Vol_IV_-_4yh_ed,_July_2007.pdf
    # http://www.icao.int/APAC/Documents/edocs/cns/SSR_%20modesii.pdf
    # http://www.anteni.net/adsb/Doc/1090-WP30-18-DRAFT_DO-260B-V42.pdf
    # http://www.cats.com.kh/download.php?path=vdzw4dHS08mjtKi6vNi31Mbn0tnZ2eycn6ydmqPE19rT7Mze4cSYpsetmdXd0w==
    # http://www.sigidwiki.com/images/1/15/ADS-B_for_Dummies.pdf
    def _decode_header_old(self):  
        # Uplink Format, 5 bits
        self.uf = self.bin2dec(self.bits[0:0+5])
        self.uf_str = "UF{:d}".format(self.uf)
        if self.uf <=24:
            if self.verbose:
                if self.msg_filter == 'All Messages':
                    print '\n'
                    print '----------------------------------------------------------------------'
                    print 'datetime:'.ljust(16) + '%s' % (self.meta['datetime'])
                    print 'SNR:'.ljust(16) + '%1.2f dB' % (self.meta['snr'])
		            #print 'UF{:d}'.format(self.uf)
                    print 'UF:'.ljust(16) + '%d %s' % (self.uf, UF_STR_LUT[self.uf])


    def _pack_bytes_old(self, unpacked):
        #self.msg_count += 1
        a = [int("".join(map(str, unpacked[i:i+8])), 2) for i in range(0, len(unpacked), 8)]
        packed = bytearray(a)
        return packed
