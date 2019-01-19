#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: /home/zleffke/captures/misc/SIM_USRP_20181103_180104.292187_UTC_250k.fc32
# Generated: Sat Nov  3 13:01:55 2018
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
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import kiss
import math
import pmt
import sip
import sys
import vcc
import vtgs
from gnuradio import qtgui


class nbfm_afsk_file(gr.top_block, Qt.QWidget):

    def __init__(self, radio_id='USRP', sat_name='SIM'):
        gr.top_block.__init__(self, "/home/zleffke/captures/misc/SIM_USRP_20181103_180104.292187_UTC_250k.fc32")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("/home/zleffke/captures/misc/SIM_USRP_20181103_180104.292187_UTC_250k.fc32")
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

        self.settings = Qt.QSettings("GNU Radio", "nbfm_afsk_file")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.radio_id = radio_id
        self.sat_name = sat_name

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y%m%d_%H%M%S.%f" )+'_UTC'
        self.samp_rate = samp_rate = 250e3
        self.fn = fn = "{:s}_{:s}_{:s}_{:s}k.fc32".format(sat_name, radio_id, ts_str, str(int(samp_rate)/1000))
        self.baud = baud = 1200

        self.xlate_taps = xlate_taps = firdes.low_pass(1.0, samp_rate, samp_rate/2, 1000, firdes.WIN_HAMMING, 6.76)

        self.volume = volume = 0.02
        self.throttle_factor = throttle_factor = 1.0
        self.samps_per_symb = samps_per_symb = 48000 / baud
        self.rx_freq = rx_freq = 440.389e6
        self.offset = offset = 1e3
        self.fsk_deviation_hz = fsk_deviation_hz = 4000
        self.fp = fp = "/home/zleffke/captures/misc/{:s}".format(fn)
        self.fll_loop_bw = fll_loop_bw = math.pi/200
        self.decim = decim = 5
        self.audio_lpf_cutoff = audio_lpf_cutoff = 10e3

        ##################################################
        # Blocks
        ##################################################
        self._volume_tool_bar = Qt.QToolBar(self)
        self._volume_tool_bar.addWidget(Qt.QLabel("volume"+": "))
        self._volume_line_edit = Qt.QLineEdit(str(self.volume))
        self._volume_tool_bar.addWidget(self._volume_line_edit)
        self._volume_line_edit.returnPressed.connect(
        	lambda: self.set_volume(eng_notation.str_to_num(str(self._volume_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._volume_tool_bar, 10, 2, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._throttle_factor_tool_bar = Qt.QToolBar(self)
        self._throttle_factor_tool_bar.addWidget(Qt.QLabel('Throttle'+": "))
        self._throttle_factor_line_edit = Qt.QLineEdit(str(self.throttle_factor))
        self._throttle_factor_tool_bar.addWidget(self._throttle_factor_line_edit)
        self._throttle_factor_line_edit.returnPressed.connect(
        	lambda: self.set_throttle_factor(eng_notation.str_to_num(str(self._throttle_factor_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._throttle_factor_tool_bar, 10, 0, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._offset_tool_bar = Qt.QToolBar(self)
        self._offset_tool_bar.addWidget(Qt.QLabel('OFFSET'+": "))
        self._offset_line_edit = Qt.QLineEdit(str(self.offset))
        self._offset_tool_bar.addWidget(self._offset_line_edit)
        self._offset_line_edit.returnPressed.connect(
        	lambda: self.set_offset(eng_notation.str_to_num(str(self._offset_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._offset_tool_bar, 10, 5, 1, 2)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 7):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._audio_lpf_cutoff_tool_bar = Qt.QToolBar(self)
        self._audio_lpf_cutoff_tool_bar.addWidget(Qt.QLabel("audio_lpf_cutoff"+": "))
        self._audio_lpf_cutoff_line_edit = Qt.QLineEdit(str(self.audio_lpf_cutoff))
        self._audio_lpf_cutoff_tool_bar.addWidget(self._audio_lpf_cutoff_line_edit)
        self._audio_lpf_cutoff_line_edit.returnPressed.connect(
        	lambda: self.set_audio_lpf_cutoff(eng_notation.str_to_num(str(self._audio_lpf_cutoff_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._audio_lpf_cutoff_tool_bar, 10, 3, 1, 2)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.vtgs_ax25_deframer_0 = vtgs.ax25_deframer()
        self.vtgs_afskdemod_0 = vtgs.afskdemod(samps_per_symb, baud, 1200, 2200)
        self.vcc_qt_hex_text_0 = vcc.qt_hex_text()
        self._vcc_qt_hex_text_0_win = self.vcc_qt_hex_text_0;
        self.top_grid_layout.addWidget(self._vcc_qt_hex_text_0_win, 4, 4, 2, 4)
        for r in range(4, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)

        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('FREQ'+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_freq_tool_bar, 10, 1, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=48,
                decimation=50,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, -40)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate / decim / 50 * 48, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 4, 0, 2, 4)
        for r in range(4, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, -40)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.low_pass_filter_0_0_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate/decim/50*48, audio_lpf_cutoff, 2e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(decim, firdes.low_pass(
        	1, samp_rate, 25e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.kiss_pdu_to_kiss_0 = kiss.pdu_to_kiss()
        self.hilbert_fc_0 = filter.hilbert_fc(65, firdes.WIN_HAMMING, 6.76)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, (xlate_taps), offset, samp_rate)
        self._fll_loop_bw_tool_bar = Qt.QToolBar(self)
        self._fll_loop_bw_tool_bar.addWidget(Qt.QLabel("fll_loop_bw"+": "))
        self._fll_loop_bw_line_edit = Qt.QLineEdit(str(self.fll_loop_bw))
        self._fll_loop_bw_tool_bar.addWidget(self._fll_loop_bw_line_edit)
        self._fll_loop_bw_line_edit.returnPressed.connect(
        	lambda: self.set_fll_loop_bw(eng_notation.str_to_num(str(self._fll_loop_bw_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._fll_loop_bw_tool_bar, 6, 2, 1, 2)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate * throttle_factor,True)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '8000', 10000, False)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/zleffke/captures/misc/SIM_USRP_20181102_011046.737916_UTC_250k.fc32', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(samp_rate/(2*math.pi*fsk_deviation_hz/8.0))
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.kiss_pdu_to_kiss_0, 'out'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.kiss_pdu_to_kiss_0, 'out'), (self.blocks_socket_pdu_0, 'pdus'))
        self.msg_connect((self.kiss_pdu_to_kiss_0, 'out'), (self.vcc_qt_hex_text_0, 'pdus'))
        self.msg_connect((self.vtgs_ax25_deframer_0, 'valid_frames'), (self.kiss_pdu_to_kiss_0, 'in'))
        self.connect((self.analog_agc2_xx_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.low_pass_filter_0_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.hilbert_fc_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.hilbert_fc_0, 0), (self.vtgs_afskdemod_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.vtgs_afskdemod_0, 0), (self.vtgs_ax25_deframer_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "nbfm_afsk_file")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_radio_id(self):
        return self.radio_id

    def set_radio_id(self, radio_id):
        self.radio_id = radio_id
        self.set_fn("{:s}_{:s}_{:s}_{:s}k.fc32".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate)/1000)))

    def get_sat_name(self):
        return self.sat_name

    def set_sat_name(self, sat_name):
        self.sat_name = sat_name
        self.set_fn("{:s}_{:s}_{:s}_{:s}k.fc32".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate)/1000)))

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_fn("{:s}_{:s}_{:s}_{:s}k.fc32".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate)/1000)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.decim / 50 * 48)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim/50*48, self.audio_lpf_cutoff, 2e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 25e3, 2e3, firdes.WIN_HAMMING, 6.76))
        self.set_fn("{:s}_{:s}_{:s}_{:s}k.fc32".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate)/1000)))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate * self.throttle_factor)
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz/8.0))

    def get_fn(self):
        return self.fn

    def set_fn(self, fn):
        self.fn = fn
        self.set_fp("/home/zleffke/captures/misc/{:s}".format(self.fn))

    def get_baud(self):
        return self.baud

    def set_baud(self, baud):
        self.baud = baud
        self.set_samps_per_symb(48000 / self.baud)

    def get_xlate_taps(self):
        return self.xlate_taps

    def set_xlate_taps(self, xlate_taps):
        self.xlate_taps = xlate_taps
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.xlate_taps))

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        Qt.QMetaObject.invokeMethod(self._volume_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.volume)))
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))

    def get_throttle_factor(self):
        return self.throttle_factor

    def set_throttle_factor(self, throttle_factor):
        self.throttle_factor = throttle_factor
        Qt.QMetaObject.invokeMethod(self._throttle_factor_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.throttle_factor)))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate * self.throttle_factor)

    def get_samps_per_symb(self):
        return self.samps_per_symb

    def set_samps_per_symb(self, samps_per_symb):
        self.samps_per_symb = samps_per_symb

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        Qt.QMetaObject.invokeMethod(self._offset_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.offset)))
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.offset)

    def get_fsk_deviation_hz(self):
        return self.fsk_deviation_hz

    def set_fsk_deviation_hz(self, fsk_deviation_hz):
        self.fsk_deviation_hz = fsk_deviation_hz
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz/8.0))

    def get_fp(self):
        return self.fp

    def set_fp(self, fp):
        self.fp = fp

    def get_fll_loop_bw(self):
        return self.fll_loop_bw

    def set_fll_loop_bw(self, fll_loop_bw):
        self.fll_loop_bw = fll_loop_bw
        Qt.QMetaObject.invokeMethod(self._fll_loop_bw_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.fll_loop_bw)))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.decim / 50 * 48)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim/50*48, self.audio_lpf_cutoff, 2e3, firdes.WIN_HAMMING, 6.76))

    def get_audio_lpf_cutoff(self):
        return self.audio_lpf_cutoff

    def set_audio_lpf_cutoff(self, audio_lpf_cutoff):
        self.audio_lpf_cutoff = audio_lpf_cutoff
        Qt.QMetaObject.invokeMethod(self._audio_lpf_cutoff_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.audio_lpf_cutoff)))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim/50*48, self.audio_lpf_cutoff, 2e3, firdes.WIN_HAMMING, 6.76))


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--radio-id", dest="radio_id", type="string", default='USRP',
        help="Set radio_id [default=%default]")
    parser.add_option(
        "", "--sat-name", dest="sat_name", type="string", default='SIM',
        help="Set sat_name [default=%default]")
    return parser


def main(top_block_cls=nbfm_afsk_file, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(radio_id=options.radio_id, sat_name=options.sat_name)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
