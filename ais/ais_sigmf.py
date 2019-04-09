#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Ais Sigmf
# Generated: Fri Feb 22 17:26:02 2019
# GNU Radio version: 3.7.12.0
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from datetime import datetime as dt; import string
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import ais
import math
import pyqt
import sigmf
import sip
import sys
import time
from gnuradio import qtgui


class ais_sigmf(gr.top_block, Qt.QWidget):

    def __init__(self, cyborg_version='v0.1.0', mod_order=2, mod_scheme='GMSK', rx_ant_model='COMET SMA703', rx_db_ser='na', rx_db_type='na', rx_ser_tag='30DCE50', rx_ser_uhd='30DCE50', rx_type='B200', signal_name='AIS', symbol_rate=9600):
        gr.top_block.__init__(self, "Ais Sigmf")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Ais Sigmf")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "ais_sigmf")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.cyborg_version = cyborg_version
        self.mod_order = mod_order
        self.mod_scheme = mod_scheme
        self.rx_ant_model = rx_ant_model
        self.rx_db_ser = rx_db_ser
        self.rx_db_type = rx_db_type
        self.rx_ser_tag = rx_ser_tag
        self.rx_ser_uhd = rx_ser_uhd
        self.rx_type = rx_type
        self.signal_name = signal_name
        self.symbol_rate = symbol_rate

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.samp_rate = samp_rate = 250e3
        self.fn = fn = "{:s}_{:s}".format(signal_name, ts_str)
        self.decim = decim = 5
        self.baud = baud = 9600
        self.tune = tune = 0
        self.samp_per_sym = samp_per_sym = (samp_rate/decim/50*48)/baud
        self.rx_gain = rx_gain = 55
        self.rx_freq = rx_freq = 162e6
        self.fsk_deviation = fsk_deviation = 10e3
        self.fp = fp = "/captures/ais/{:s}".format(fn)

        ##################################################
        # Blocks
        ##################################################
        self._tune_tool_bar = Qt.QToolBar(self)
        self._tune_tool_bar.addWidget(Qt.QLabel("tune"+": "))
        self._tune_line_edit = Qt.QLineEdit(str(self.tune))
        self._tune_tool_bar.addWidget(self._tune_line_edit)
        self._tune_line_edit.returnPressed.connect(
        	lambda: self.set_tune(eng_notation.str_to_num(str(self._tune_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._tune_tool_bar, 8, 2, 1, 2)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel("rx_gain"+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_gain_tool_bar, 8, 0, 1, 2)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_center_freq(rx_freq, 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.sigmf_sink_0 = sigmf.sink("cf32", fp, sigmf.sigmf_time_mode_absolute, False)
        self.sigmf_sink_0.set_global_meta("core:sample_rate", samp_rate)
        self.sigmf_sink_0.set_global_meta("core:description", '')
        self.sigmf_sink_0.set_global_meta("core:author", '')
        self.sigmf_sink_0.set_global_meta("core:license", '')
        self.sigmf_sink_0.set_global_meta("core:hw", '')
        self.sigmf_sink_0.set_global_meta('usrp:rx_type', 'B200')
        self.sigmf_sink_0.set_global_meta('usrp:rx_ser_uhd', '30DCE50')
        self.sigmf_sink_0.set_global_meta('usrp:rx_ser_tag', '30DCE50')
        self.sigmf_sink_0.set_global_meta('usrp:rx_db_type', 'na')
        self.sigmf_sink_0.set_global_meta('usrp:rx_db_ser', 'na')
        self.sigmf_sink_0.set_global_meta('modulation:scheme', 'GMSK')
        self.sigmf_sink_0.set_global_meta('modulation:order', 2)
        self.sigmf_sink_0.set_global_meta('cyborg:symbol_rate', 9600)
        self.sigmf_sink_0.set_global_meta('cyborg:version', 'v0.1.0')
        self.sigmf_sink_0.set_global_meta('usrp:version', 'v0.1.0')
        self.sigmf_sink_0.set_global_meta('usrp:rx_rf_gain', 55)
        self.sigmf_sink_0.set_global_meta('usrp:rx_freq', 162000000.0)
        self.sigmf_sink_0.set_global_meta('usrp:rx_ant_model', 'COMET SMA703')

        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=2,
                taps=None,
                fractional_bw=None,
        )
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
        self.qtgui_waterfall_sink_x_0_1 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate/2, #bw
        	"Channel", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_1.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_1.enable_grid(True)
        self.qtgui_waterfall_sink_x_0_1.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_1.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_1.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_1.set_intensity_range(-140, -40)

        self._qtgui_waterfall_sink_x_0_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_1_win, 2, 0, 2, 8)
        for r in range(2, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate/2, #bw
        	"AIS", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.01)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, -40)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 2, 8)
        for r in range(0, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.pyqt_text_output_0_0 = pyqt.text_output()
        self._pyqt_text_output_0_0_win = self.pyqt_text_output_0_0;
        self.top_grid_layout.addWidget(self._pyqt_text_output_0_0_win, 4, 0, 1, 4)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.pyqt_text_output_0 = pyqt.text_output()
        self._pyqt_text_output_0_win = self.pyqt_text_output_0;
        self.top_grid_layout.addWidget(self._pyqt_text_output_0_win, 4, 4, 1, 4)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.low_pass_filter_0_0 = filter.fir_filter_ccf(decim, firdes.low_pass(
        	1, samp_rate, 7e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(decim, firdes.low_pass(
        	1, samp_rate, 7e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.digital_hdlc_deframer_bp_0_0 = digital.hdlc_deframer_bp(11, 1000)
        self.digital_hdlc_deframer_bp_0 = digital.hdlc_deframer_bp(11, 1000)
        self.digital_diff_decoder_bb_0_0 = digital.diff_decoder_bb(2)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2)
        self.digital_clock_recovery_mm_xx_0_0 = digital.clock_recovery_mm_ff(samp_per_sym*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(samp_per_sym*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_0_0 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_socket_pdu_0 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '52001', 10000, False)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_message_debug_0_1 = blocks.message_debug()
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 25e3, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, tune, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -25e3, 1, 0)
        self.analog_quadrature_demod_cf_0_0 = analog.quadrature_demod_cf((samp_rate/decim)/(2*math.pi*fsk_deviation/8.0))
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf((samp_rate/decim)/(2*math.pi*fsk_deviation/8.0))
        self.analog_agc2_xx_0_0 = analog.agc2_cc(1e-3, 1e-1, 1.0, 1.0)
        self.analog_agc2_xx_0_0.set_max_gain(65536)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-3, 1e-1, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)
        self.ais_pdu_to_nmea_0_0 = ais.pdu_to_nmea('B')
        self.ais_pdu_to_nmea_0 = ais.pdu_to_nmea('A')
        self.ais_invert_0_0 = ais.invert()
        self.ais_invert_0 = ais.invert()



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.ais_pdu_to_nmea_0, 'out'), (self.blocks_message_debug_0_1, 'print'))
        self.msg_connect((self.ais_pdu_to_nmea_0, 'out'), (self.blocks_message_debug_0_1, 'print_pdu'))
        self.msg_connect((self.ais_pdu_to_nmea_0, 'out'), (self.blocks_socket_pdu_0, 'pdus'))
        self.msg_connect((self.ais_pdu_to_nmea_0, 'out'), (self.pyqt_text_output_0_0, 'pdus'))
        self.msg_connect((self.ais_pdu_to_nmea_0_0, 'out'), (self.blocks_message_debug_0_1, 'print'))
        self.msg_connect((self.ais_pdu_to_nmea_0_0, 'out'), (self.blocks_message_debug_0_1, 'print_pdu'))
        self.msg_connect((self.ais_pdu_to_nmea_0_0, 'out'), (self.blocks_socket_pdu_0, 'pdus'))
        self.msg_connect((self.ais_pdu_to_nmea_0_0, 'out'), (self.pyqt_text_output_0, 'pdus'))
        self.msg_connect((self.digital_hdlc_deframer_bp_0, 'out'), (self.ais_pdu_to_nmea_0, 'to_nmea'))
        self.msg_connect((self.digital_hdlc_deframer_bp_0_0, 'out'), (self.ais_pdu_to_nmea_0_0, 'to_nmea'))
        self.connect((self.ais_invert_0, 0), (self.digital_hdlc_deframer_bp_0, 0))
        self.connect((self.ais_invert_0_0, 0), (self.digital_hdlc_deframer_bp_0_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.analog_agc2_xx_0_0, 0), (self.analog_quadrature_demod_cf_0_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0, 0), (self.digital_diff_decoder_bb_0_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0_0, 0), (self.digital_binary_slicer_fb_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.ais_invert_0, 0))
        self.connect((self.digital_diff_decoder_bb_0_0, 0), (self.ais_invert_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.analog_agc2_xx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.digital_clock_recovery_mm_xx_0_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.qtgui_waterfall_sink_x_0_1, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.sigmf_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "ais_sigmf")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_cyborg_version(self):
        return self.cyborg_version

    def set_cyborg_version(self, cyborg_version):
        self.cyborg_version = cyborg_version

    def get_mod_order(self):
        return self.mod_order

    def set_mod_order(self, mod_order):
        self.mod_order = mod_order

    def get_mod_scheme(self):
        return self.mod_scheme

    def set_mod_scheme(self, mod_scheme):
        self.mod_scheme = mod_scheme

    def get_rx_ant_model(self):
        return self.rx_ant_model

    def set_rx_ant_model(self, rx_ant_model):
        self.rx_ant_model = rx_ant_model

    def get_rx_db_ser(self):
        return self.rx_db_ser

    def set_rx_db_ser(self, rx_db_ser):
        self.rx_db_ser = rx_db_ser

    def get_rx_db_type(self):
        return self.rx_db_type

    def set_rx_db_type(self, rx_db_type):
        self.rx_db_type = rx_db_type

    def get_rx_ser_tag(self):
        return self.rx_ser_tag

    def set_rx_ser_tag(self, rx_ser_tag):
        self.rx_ser_tag = rx_ser_tag

    def get_rx_ser_uhd(self):
        return self.rx_ser_uhd

    def set_rx_ser_uhd(self, rx_ser_uhd):
        self.rx_ser_uhd = rx_ser_uhd

    def get_rx_type(self):
        return self.rx_type

    def set_rx_type(self, rx_type):
        self.rx_type = rx_type

    def get_signal_name(self):
        return self.signal_name

    def set_signal_name(self, signal_name):
        self.signal_name = signal_name
        self.set_fn("{:s}_{:s}".format(self.signal_name, self.ts_str))

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_fn("{:s}_{:s}".format(self.signal_name, self.ts_str))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_per_sym((self.samp_rate/self.decim/50*48)/self.baud)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(self.rx_freq, self.samp_rate/2)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate/2)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 7e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 7e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_quadrature_demod_cf_0_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))

    def get_fn(self):
        return self.fn

    def set_fn(self, fn):
        self.fn = fn
        self.set_fp("/captures/ais/{:s}".format(self.fn))

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

    def get_tune(self):
        return self.tune

    def set_tune(self, tune):
        self.tune = tune
        Qt.QMetaObject.invokeMethod(self._tune_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.tune)))
        self.analog_sig_source_x_0_0.set_frequency(self.tune)

    def get_samp_per_sym(self):
        return self.samp_per_sym

    def set_samp_per_sym(self, samp_per_sym):
        self.samp_per_sym = samp_per_sym
        self.digital_clock_recovery_mm_xx_0_0.set_omega(self.samp_per_sym*(1+0.0))
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samp_per_sym*(1+0.0))

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)


    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self.uhd_usrp_source_0.set_center_freq(self.rx_freq, 0)
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(self.rx_freq, self.samp_rate/2)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate/2)

    def get_fsk_deviation(self):
        return self.fsk_deviation

    def set_fsk_deviation(self, fsk_deviation):
        self.fsk_deviation = fsk_deviation
        self.analog_quadrature_demod_cf_0_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))

    def get_fp(self):
        return self.fp

    def set_fp(self, fp):
        self.fp = fp


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--cyborg-version", dest="cyborg_version", type="string", default='v0.1.0',
        help="Set cyborg_version [default=%default]")
    parser.add_option(
        "", "--mod-order", dest="mod_order", type="intx", default=2,
        help="Set mod_order [default=%default]")
    parser.add_option(
        "", "--mod-scheme", dest="mod_scheme", type="string", default='GMSK',
        help="Set mod_scheme [default=%default]")
    parser.add_option(
        "", "--rx-ant-model", dest="rx_ant_model", type="string", default='COMET SMA703',
        help="Set rx_ant_model [default=%default]")
    parser.add_option(
        "", "--rx-db-ser", dest="rx_db_ser", type="string", default='na',
        help="Set rx_db_ser [default=%default]")
    parser.add_option(
        "", "--rx-db-type", dest="rx_db_type", type="string", default='na',
        help="Set rx_db_type [default=%default]")
    parser.add_option(
        "", "--rx-ser-tag", dest="rx_ser_tag", type="string", default='30DCE50',
        help="Set rx_ser_tag [default=%default]")
    parser.add_option(
        "", "--rx-ser-uhd", dest="rx_ser_uhd", type="string", default='30DCE50',
        help="Set rx_ser_uhd [default=%default]")
    parser.add_option(
        "", "--rx-type", dest="rx_type", type="string", default='B200',
        help="Set rx_type [default=%default]")
    parser.add_option(
        "", "--signal-name", dest="signal_name", type="string", default='AIS',
        help="Set signal_name [default=%default]")
    parser.add_option(
        "", "--symbol-rate", dest="symbol_rate", type="eng_float", default=eng_notation.num_to_str(9600),
        help="Set symbol_rate [default=%default]")
    return parser


def main(top_block_cls=ais_sigmf, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(cyborg_version=options.cyborg_version, mod_order=options.mod_order, mod_scheme=options.mod_scheme, rx_ant_model=options.rx_ant_model, rx_db_ser=options.rx_db_ser, rx_db_type=options.rx_db_type, rx_ser_tag=options.rx_ser_tag, rx_ser_uhd=options.rx_ser_uhd, rx_type=options.rx_type, signal_name=options.signal_name, symbol_rate=options.symbol_rate)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
