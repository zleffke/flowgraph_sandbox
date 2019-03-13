#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Ais Rx
# Generated: Sat May 27 23:29:54 2017
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import ais
import math
import time


class ais_rx(gr.top_block):

    def __init__(self, addr='0.0.0.0', port='52001', rx_gain=38):
        gr.top_block.__init__(self, "Ais Rx")

        ##################################################
        # Parameters
        ##################################################
        self.addr = addr
        self.port = port
        self.rx_gain = rx_gain

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250e3
        self.decim = decim = 5
        self.baud = baud = 9600
        self.samp_per_sym = samp_per_sym = (samp_rate/decim/50*48)/baud
        self.fsk_deviation = fsk_deviation = 10e3
        self.freq = freq = 162e6
        self.filter_taps = filter_taps = firdes.low_pass(1,samp_rate, samp_rate/2, 50000, firdes.WIN_FLATTOP, 6.76)

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_subdev_spec('A:B', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(freq, samp_rate/2), 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=50,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=50,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(decim, firdes.low_pass(
        	1, samp_rate, 7e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(decim, firdes.low_pass(
        	1, samp_rate, 7e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.digital_map_bb_0_0 = digital.map_bb((1,0))
        self.digital_map_bb_0 = digital.map_bb((1,0))
        self.digital_hdlc_deframer_bp_0_0 = digital.hdlc_deframer_bp(11, 1000)
        self.digital_hdlc_deframer_bp_0 = digital.hdlc_deframer_bp(11, 1000)
        self.digital_diff_decoder_bb_0_0 = digital.diff_decoder_bb(2)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2)
        self.digital_clock_recovery_mm_xx_0_0 = digital.clock_recovery_mm_ff(samp_per_sym*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(samp_per_sym*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_0_0 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/dev/stdout', True)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 25e3, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -25e3, 1, 0)
        self.analog_quadrature_demod_cf_0_0 = analog.quadrature_demod_cf((samp_rate/decim)/(2*math.pi*fsk_deviation/8.0))
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf((samp_rate/decim)/(2*math.pi*fsk_deviation/8.0))
        self.analog_agc2_xx_0_0 = analog.agc2_cc(1e-3, 1e-1, 1.0, 1.0)
        self.analog_agc2_xx_0_0.set_max_gain(65536)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-3, 1e-1, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)
        self.ais_pdu_to_nmea_0_0 = ais.pdu_to_nmea('B')
        self.ais_pdu_to_nmea_0 = ais.pdu_to_nmea('A')

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.ais_pdu_to_nmea_0, 'out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.ais_pdu_to_nmea_0_0, 'out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.digital_hdlc_deframer_bp_0, 'out'), (self.ais_pdu_to_nmea_0, 'to_nmea'))
        self.msg_connect((self.digital_hdlc_deframer_bp_0_0, 'out'), (self.ais_pdu_to_nmea_0_0, 'to_nmea'))
        self.connect((self.analog_agc2_xx_0, 0), (self.analog_quadrature_demod_cf_0_0, 0))
        self.connect((self.analog_agc2_xx_0_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0, 0), (self.digital_diff_decoder_bb_0_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0_0, 0), (self.digital_binary_slicer_fb_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_diff_decoder_bb_0_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.digital_hdlc_deframer_bp_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.digital_hdlc_deframer_bp_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.analog_agc2_xx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.digital_clock_recovery_mm_xx_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_multiply_xx_1, 1))

    def get_addr(self):
        return self.addr

    def set_addr(self, addr):
        self.addr = addr

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_per_sym((self.samp_rate/self.decim/50*48)/self.baud)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq, self.samp_rate/2), 0)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 7e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 7e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.set_filter_taps(firdes.low_pass(1,self.samp_rate, self.samp_rate/2, 50000, firdes.WIN_FLATTOP, 6.76))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_quadrature_demod_cf_0_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_samp_per_sym((self.samp_rate/self.decim/50*48)/self.baud)
        self.analog_quadrature_demod_cf_0_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))

    def get_baud(self):
        return self.baud

    def set_baud(self, baud):
        self.baud = baud
        self.set_samp_per_sym((self.samp_rate/self.decim/50*48)/self.baud)

    def get_samp_per_sym(self):
        return self.samp_per_sym

    def set_samp_per_sym(self, samp_per_sym):
        self.samp_per_sym = samp_per_sym
        self.digital_clock_recovery_mm_xx_0_0.set_omega(self.samp_per_sym*(1+0.0))
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samp_per_sym*(1+0.0))

    def get_fsk_deviation(self):
        return self.fsk_deviation

    def set_fsk_deviation(self, fsk_deviation):
        self.fsk_deviation = fsk_deviation
        self.analog_quadrature_demod_cf_0_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq, self.samp_rate/2), 0)

    def get_filter_taps(self):
        return self.filter_taps

    def set_filter_taps(self, filter_taps):
        self.filter_taps = filter_taps


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--addr", dest="addr", type="string", default='0.0.0.0',
        help="Set addr [default=%default]")
    parser.add_option(
        "", "--port", dest="port", type="string", default='52001',
        help="Set port [default=%default]")
    parser.add_option(
        "", "--rx-gain", dest="rx_gain", type="intx", default=38,
        help="Set rx_gain [default=%default]")
    return parser


def main(top_block_cls=ais_rx, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(addr=options.addr, port=options.port, rx_gain=options.rx_gain)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
