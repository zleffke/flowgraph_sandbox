#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: VOR Decoder
# Author: Zach Leffke
# Description: Generic SigMF Recorder
# GNU Radio version: 3.7.13.4
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
from datetime import datetime as dt; import string; import math
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import gr_sigmf
import sip
import sys
from gnuradio import qtgui


class vor_playback_sigmf_2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "VOR Decoder")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("VOR Decoder")
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

        self.settings = Qt.QSettings("GNU Radio", "vor_playback_sigmf_2")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250e3
        self.decim = decim = 5
        self.throttle_rate = throttle_rate = 1
        self.lo_cut = lo_cut = 1e3
        self.hi_cut = hi_cut = 1050
        self.fine = fine = 1e3
        self.audio_rate = audio_rate = samp_rate/decim/25*24
        self.audio_gain = audio_gain = 1
        self.alpha = alpha = .02

        ##################################################
        # Blocks
        ##################################################
        self._throttle_rate_tool_bar = Qt.QToolBar(self)
        self._throttle_rate_tool_bar.addWidget(Qt.QLabel("throttle_rate"+": "))
        self._throttle_rate_line_edit = Qt.QLineEdit(str(self.throttle_rate))
        self._throttle_rate_tool_bar.addWidget(self._throttle_rate_line_edit)
        self._throttle_rate_line_edit.returnPressed.connect(
        	lambda: self.set_throttle_rate(eng_notation.str_to_num(str(self._throttle_rate_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._throttle_rate_tool_bar, 0, 6, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel("samp_rate"+": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._samp_rate_tool_bar, 0, 4, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.sigmf_source_0 = gr_sigmf.source('/captures/20191228/VOR_2019-12-28T19:07:15Z.sigmf-data', "cf32" + ("_le" if sys.byteorder == "little" else "_be"), True)
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_ccc(
                interpolation=24,
                decimation=25*5,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024*2, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate / decim, #bw
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

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 4, 0, 2, 4)
        for r in range(4, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	256, #size
        	audio_rate / 3 / 8, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.0010)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-180, 180)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, .25, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()

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
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win, 6, 4, 2, 4)
        for r in range(6, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	8192 /2, #size
        	samp_rate / decim /25 * 24, #samp_rate
        	"30 Hz Variable", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.0010)
        self.qtgui_time_sink_x_0.set_y_axis(-4, 4)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['ref', 'var', '', '', '',
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

        for i in xrange(2):
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 4, 4, 2, 4)
        for r in range(4, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate / decim / 25 * 24, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0.enable_grid(True)
        self.qtgui_freq_sink_x_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_1_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1_0.set_plot_pos_half(not False)

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
                self.qtgui_freq_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_f(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not False)

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
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win, 3, 4, 1, 4)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.low_pass_filter_0_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	10, samp_rate / decim / 25 *24, 1e3, 500, firdes.WIN_HAMMING, 6.76))
        self._lo_cut_tool_bar = Qt.QToolBar(self)
        self._lo_cut_tool_bar.addWidget(Qt.QLabel("lo_cut"+": "))
        self._lo_cut_line_edit = Qt.QLineEdit(str(self.lo_cut))
        self._lo_cut_tool_bar.addWidget(self._lo_cut_line_edit)
        self._lo_cut_line_edit.returnPressed.connect(
        	lambda: self.set_lo_cut(eng_notation.str_to_num(str(self._lo_cut_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._lo_cut_tool_bar, 2, 4, 1, 2)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._hi_cut_tool_bar = Qt.QToolBar(self)
        self._hi_cut_tool_bar.addWidget(Qt.QLabel("hi_cut"+": "))
        self._hi_cut_line_edit = Qt.QLineEdit(str(self.hi_cut))
        self._hi_cut_tool_bar.addWidget(self._hi_cut_line_edit)
        self._hi_cut_line_edit.returnPressed.connect(
        	lambda: self.set_hi_cut(eng_notation.str_to_num(str(self._hi_cut_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._hi_cut_tool_bar, 2, 6, 1, 2)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.goertzel_fc_0_0 = fft.goertzel_fc(int(audio_rate), 1024, 30)
        self.goertzel_fc_0 = fft.goertzel_fc(int(audio_rate), 1024, 30)
        self._fine_tool_bar = Qt.QToolBar(self)
        self._fine_tool_bar.addWidget(Qt.QLabel('Fine [Hz]'+": "))
        self._fine_line_edit = Qt.QLineEdit(str(self.fine))
        self._fine_tool_bar.addWidget(self._fine_line_edit)
        self._fine_line_edit.returnPressed.connect(
        	lambda: self.set_fine(eng_notation.str_to_num(str(self._fine_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._fine_tool_bar, 1, 4, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.dc_blocker_xx_0_0 = filter.dc_blocker_ff(1024, True)
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(1024, True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate*throttle_rate,True)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((180/math.pi, ))
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(10, .1, 4000, 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.band_pass_filter_0_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, samp_rate / decim / 25 * 24 , 25, 35, 5, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	1, samp_rate / decim / 25 * 24 , 25, 35, 5, firdes.WIN_HAMMING, 6.76))
        self._audio_gain_tool_bar = Qt.QToolBar(self)
        self._audio_gain_tool_bar.addWidget(Qt.QLabel('vol30'+": "))
        self._audio_gain_line_edit = Qt.QLineEdit(str(self.audio_gain))
        self._audio_gain_tool_bar.addWidget(self._audio_gain_line_edit)
        self._audio_gain_line_edit.returnPressed.connect(
        	lambda: self.set_audio_gain(eng_notation.str_to_num(str(self._audio_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._audio_gain_tool_bar, 1, 7, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(7, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.analog_sig_source_x_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 9960, 1, 0)
        self.analog_pll_carriertracking_cc_0 = analog.pll_carriertracking_cc(math.pi/200, math.pi/10, -math.pi/10)
        self.analog_fm_demod_cf_0 = analog.fm_demod_cf(
        	channel_rate=samp_rate / decim / 25 * 24,
        	audio_decim=1,
        	deviation=1e3,
        	audio_pass=100,
        	audio_stop=200,
        	gain=1.0,
        	tau=75e-6,
        )
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=48e3,
        	audio_decim=1,
        	audio_pass=12000,
        	audio_stop=13000,
        )
        self.analog_agc2_xx_2 = analog.agc2_ff(1e-4, 1e-4, 1, 1.0)
        self.analog_agc2_xx_2.set_max_gain(65536)
        self.analog_agc2_xx_1 = analog.agc2_ff(1e-4, 1e-4, 1, 1)
        self.analog_agc2_xx_1.set_max_gain(65536)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-2, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)
        self._alpha_tool_bar = Qt.QToolBar(self)
        self._alpha_tool_bar.addWidget(Qt.QLabel('alpha'+": "))
        self._alpha_line_edit = Qt.QLineEdit(str(self.alpha))
        self._alpha_tool_bar.addWidget(self._alpha_line_edit)
        self._alpha_line_edit.returnPressed.connect(
        	lambda: self.set_alpha(eng_notation.str_to_num(str(self._alpha_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._alpha_tool_bar, 1, 6, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 7):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.analog_pll_carriertracking_cc_0, 0))
        self.connect((self.analog_agc2_xx_1, 0), (self.goertzel_fc_0, 0))
        self.connect((self.analog_agc2_xx_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.analog_agc2_xx_2, 0), (self.goertzel_fc_0_0, 0))
        self.connect((self.analog_agc2_xx_2, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.analog_am_demod_cf_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.analog_am_demod_cf_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.analog_am_demod_cf_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_fm_demod_cf_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.analog_pll_carriertracking_cc_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.band_pass_filter_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.dc_blocker_xx_0_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.analog_fm_demod_cf_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.analog_agc2_xx_1, 0))
        self.connect((self.dc_blocker_xx_0_0, 0), (self.analog_agc2_xx_2, 0))
        self.connect((self.goertzel_fc_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.goertzel_fc_0_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.low_pass_filter_0_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.analog_am_demod_cf_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.qtgui_freq_sink_x_1_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.sigmf_source_0, 0), (self.blocks_throttle_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "vor_playback_sigmf_2")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.set_audio_rate(self.samp_rate/self.decim/25*24)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.decim /25 * 24)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim / 25 * 24)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(10, self.samp_rate / self.decim / 25 *24, 1e3, 500, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.throttle_rate)
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate / self.decim / 25 * 24 , 25, 35, 5, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate / self.decim / 25 * 24 , 25, 35, 5, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_audio_rate(self.samp_rate/self.decim/25*24)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.decim /25 * 24)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim / 25 * 24)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(10, self.samp_rate / self.decim / 25 *24, 1e3, 500, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate / self.decim / 25 * 24 , 25, 35, 5, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate / self.decim / 25 * 24 , 25, 35, 5, firdes.WIN_HAMMING, 6.76))

    def get_throttle_rate(self):
        return self.throttle_rate

    def set_throttle_rate(self, throttle_rate):
        self.throttle_rate = throttle_rate
        Qt.QMetaObject.invokeMethod(self._throttle_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.throttle_rate)))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.throttle_rate)

    def get_lo_cut(self):
        return self.lo_cut

    def set_lo_cut(self, lo_cut):
        self.lo_cut = lo_cut
        Qt.QMetaObject.invokeMethod(self._lo_cut_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.lo_cut)))

    def get_hi_cut(self):
        return self.hi_cut

    def set_hi_cut(self, hi_cut):
        self.hi_cut = hi_cut
        Qt.QMetaObject.invokeMethod(self._hi_cut_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.hi_cut)))

    def get_fine(self):
        return self.fine

    def set_fine(self, fine):
        self.fine = fine
        Qt.QMetaObject.invokeMethod(self._fine_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.fine)))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.audio_rate / 3 / 8)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.audio_rate)
        self.goertzel_fc_0_0.set_rate(int(self.audio_rate))
        self.goertzel_fc_0.set_rate(int(self.audio_rate))

    def get_audio_gain(self):
        return self.audio_gain

    def set_audio_gain(self, audio_gain):
        self.audio_gain = audio_gain
        Qt.QMetaObject.invokeMethod(self._audio_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.audio_gain)))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        Qt.QMetaObject.invokeMethod(self._alpha_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.alpha)))


def main(top_block_cls=vor_playback_sigmf_2, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
