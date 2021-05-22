#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Fox1D Playback Sigmf
# Generated: Wed Oct 31 18:39:22 2018
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import math
import pmt
import sigmf
import sip
import sys
from gnuradio import qtgui


class fox1d_playback_sigmf(gr.top_block, Qt.QWidget):

    def __init__(self, meta_rate=10):
        gr.top_block.__init__(self, "Fox1D Playback Sigmf")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fox1D Playback Sigmf")
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

        self.settings = Qt.QSettings("GNU Radio", "fox1d_playback_sigmf")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.meta_rate = meta_rate

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250e3
        self.decim = decim = 5
        self.baud = baud = 9600

        self.xlate_taps_old = xlate_taps_old = firdes.low_pass(1.0, samp_rate, samp_rate/2, 1000, firdes.WIN_HAMMING, 6.76)


        self.xlate_taps = xlate_taps = firdes.low_pass(1.0, samp_rate, 15e3, 1000, firdes.WIN_HAMMING, 6.76)

        self.volume = volume = 0.01
        self.throttle_factor = throttle_factor = 1
        self.samps_per_symb = samps_per_symb = samp_rate/decim/ baud
        self.rf_lpf_cutoff = rf_lpf_cutoff = 8e3
        self.fsk_deviation_hz = fsk_deviation_hz = 4000
        self.fll_loop_bw_fine = fll_loop_bw_fine = 0.0001
        self.fll_loop_bw = fll_loop_bw = math.pi/200
        self.audio_lpf_cutoff = audio_lpf_cutoff = 7e3

        ##################################################
        # Blocks
        ##################################################
        self._volume_tool_bar = Qt.QToolBar(self)
        self._volume_tool_bar.addWidget(Qt.QLabel("volume"+": "))
        self._volume_line_edit = Qt.QLineEdit(str(self.volume))
        self._volume_tool_bar.addWidget(self._volume_line_edit)
        self._volume_line_edit.returnPressed.connect(
        	lambda: self.set_volume(eng_notation.str_to_num(str(self._volume_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._volume_tool_bar, 7, 4, 1, 2)
        for r in range(7, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._throttle_factor_tool_bar = Qt.QToolBar(self)
        self._throttle_factor_tool_bar.addWidget(Qt.QLabel("throttle_factor"+": "))
        self._throttle_factor_line_edit = Qt.QLineEdit(str(self.throttle_factor))
        self._throttle_factor_tool_bar.addWidget(self._throttle_factor_line_edit)
        self._throttle_factor_line_edit.returnPressed.connect(
        	lambda: self.set_throttle_factor(eng_notation.str_to_num(str(self._throttle_factor_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._throttle_factor_tool_bar, 6, 4, 1, 2)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rf_lpf_cutoff_tool_bar = Qt.QToolBar(self)
        self._rf_lpf_cutoff_tool_bar.addWidget(Qt.QLabel("rf_lpf_cutoff"+": "))
        self._rf_lpf_cutoff_line_edit = Qt.QLineEdit(str(self.rf_lpf_cutoff))
        self._rf_lpf_cutoff_tool_bar.addWidget(self._rf_lpf_cutoff_line_edit)
        self._rf_lpf_cutoff_line_edit.returnPressed.connect(
        	lambda: self.set_rf_lpf_cutoff(eng_notation.str_to_num(str(self._rf_lpf_cutoff_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rf_lpf_cutoff_tool_bar, 6, 0, 1, 2)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._fll_loop_bw_fine_tool_bar = Qt.QToolBar(self)
        self._fll_loop_bw_fine_tool_bar.addWidget(Qt.QLabel("fll_loop_bw_fine"+": "))
        self._fll_loop_bw_fine_line_edit = Qt.QLineEdit(str(self.fll_loop_bw_fine))
        self._fll_loop_bw_fine_tool_bar.addWidget(self._fll_loop_bw_fine_line_edit)
        self._fll_loop_bw_fine_line_edit.returnPressed.connect(
        	lambda: self.set_fll_loop_bw_fine(eng_notation.str_to_num(str(self._fll_loop_bw_fine_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._fll_loop_bw_fine_tool_bar, 7, 2, 1, 2)
        for r in range(7, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self._audio_lpf_cutoff_tool_bar = Qt.QToolBar(self)
        self._audio_lpf_cutoff_tool_bar.addWidget(Qt.QLabel("audio_lpf_cutoff"+": "))
        self._audio_lpf_cutoff_line_edit = Qt.QLineEdit(str(self.audio_lpf_cutoff))
        self._audio_lpf_cutoff_tool_bar.addWidget(self._audio_lpf_cutoff_line_edit)
        self._audio_lpf_cutoff_line_edit.returnPressed.connect(
        	lambda: self.set_audio_lpf_cutoff(eng_notation.str_to_num(str(self._audio_lpf_cutoff_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._audio_lpf_cutoff_tool_bar, 7, 0, 1, 2)
        for r in range(7, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.sigmf_sink_0 = sigmf.sink("cf32", '', sigmf.sigmf_time_mode_relative, False)
        self.sigmf_sink_0.set_global_meta("core:sample_rate", samp_rate)
        self.sigmf_sink_0.set_global_meta("core:description", '')
        self.sigmf_sink_0.set_global_meta("core:author", '')
        self.sigmf_sink_0.set_global_meta("core:license", '')
        self.sigmf_sink_0.set_global_meta("core:hw", '')

        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=48,
                decimation=50,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"corrected", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-80, 0)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 2, 4, 2, 4)
        for r in range(2, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"Pre-D", #name
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

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-80, 0)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 0, 4, 2, 4)
        for r in range(0, 2):
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 8, 0, 1, 8)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0_0_0.set_title("")

        labels = ['SNR', '', '', '', '',
                  '', '', '', '', '']
        units = ['dB', '', '', '', '',
                 '', '', '', '', '']
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_0_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0_0_0_0.set_max(i, 30)
            self.qtgui_number_sink_0_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_0_0_win, 6, 6, 1, 1)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 7):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0_0_0_0.set_update_time(0.010)
        self.qtgui_number_sink_0_0_0_0.set_title("")

        labels = ['Freq Offset', 'Phase', 'Error', '', '',
                  '', '', '', '', '']
        units = ['Hz', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_0_0.set_min(i, -32767)
            self.qtgui_number_sink_0_0_0_0.set_max(i, 32767)
            self.qtgui_number_sink_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_0_win, 6, 7, 1, 1)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(7, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"Pre-D", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-60, 0)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['pre-d', 'corr', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
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
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/decim, rf_lpf_cutoff, 2e3, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(decim, (xlate_taps), 0, samp_rate)
        self.digital_fll_band_edge_cc_0_0 = digital.fll_band_edge_cc(samps_per_symb, .5, 1024, fll_loop_bw_fine)
        self.digital_fll_band_edge_cc_0 = digital.fll_band_edge_cc(samps_per_symb, .5, 1024, fll_loop_bw)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate*throttle_factor,True)
        self.blocks_tagged_stream_to_pdu_0_0 = blocks.tagged_stream_to_pdu(blocks.float_t, 'snr')
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.float_t, 'rfo')
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_float, 1, 1, "snr")
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_float, 1, 1, "rfo")
        self.blocks_socket_pdu_0_0 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '52002', 10000, False)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '52001', 10000, False)
        self.blocks_null_sink_0_1 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_nlog10_ff_0_1 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((-1*samp_rate/decim/(2*math.pi), ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.blocks_moving_average_xx_0_0_1 = blocks.moving_average_ff(10000, 0.0001, 4000, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(100000, 0.00001, 4000, 1)
        self.blocks_keep_one_in_n_0_0_0 = blocks.keep_one_in_n(gr.sizeof_float*1, int(samp_rate/decim /meta_rate))
        self.blocks_keep_one_in_n_0_0 = blocks.keep_one_in_n(gr.sizeof_float*1, int(samp_rate*meta_rate))
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_float*1, int(samp_rate/4*meta_rate))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/zleffke/captures/fox1d/20180913/FOX-1D_USRP_20180913_151002.518249_UTC_250k.fc32', False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, samp_rate/decim/4, 1, 0)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(samp_rate/(2*math.pi*fsk_deviation_hz/8.0))
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.blocks_socket_pdu_0, 'pdus'))
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0_0, 'pdus'), (self.blocks_socket_pdu_0_0, 'pdus'))
        self.connect((self.analog_agc2_xx_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.low_pass_filter_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_divide_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_divide_xx_0, 1))
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_nlog10_ff_0_1, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.sigmf_sink_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))
        self.connect((self.blocks_keep_one_in_n_0_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_keep_one_in_n_0_0_0, 0), (self.qtgui_number_sink_0_0_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_keep_one_in_n_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0_1, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0_1, 0), (self.qtgui_number_sink_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_keep_one_in_n_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_nlog10_ff_0_1, 0), (self.blocks_moving_average_xx_0_0_1, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_tagged_stream_to_pdu_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.blocks_tagged_stream_to_pdu_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 1), (self.blocks_add_xx_0, 1))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 2), (self.blocks_null_sink_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 3), (self.blocks_null_sink_0_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0_0, 1), (self.blocks_add_xx_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0_0, 3), (self.blocks_null_sink_0_0_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0_0, 2), (self.blocks_null_sink_0_1, 0))
        self.connect((self.digital_fll_band_edge_cc_0_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.digital_fll_band_edge_cc_0_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.digital_fll_band_edge_cc_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.digital_fll_band_edge_cc_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_complex_to_mag_squared_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fox1d_playback_sigmf")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_meta_rate(self):
        return self.meta_rate

    def set_meta_rate(self, meta_rate):
        self.meta_rate = meta_rate
        self.blocks_keep_one_in_n_0_0_0.set_n(int(self.samp_rate/self.decim /self.meta_rate))
        self.blocks_keep_one_in_n_0_0.set_n(int(self.samp_rate*self.meta_rate))
        self.blocks_keep_one_in_n_0.set_n(int(self.samp_rate/4*self.meta_rate))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samps_per_symb(self.samp_rate/self.decim/ self.baud)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.decim / 50 * 48)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim/50*48, self.audio_lpf_cutoff, 2e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.rf_lpf_cutoff, 2e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.throttle_factor)
        self.blocks_multiply_const_vxx_1.set_k((-1*self.samp_rate/self.decim/(2*math.pi), ))
        self.blocks_keep_one_in_n_0_0_0.set_n(int(self.samp_rate/self.decim /self.meta_rate))
        self.blocks_keep_one_in_n_0_0.set_n(int(self.samp_rate*self.meta_rate))
        self.blocks_keep_one_in_n_0.set_n(int(self.samp_rate/4*self.meta_rate))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_frequency(self.samp_rate/self.decim/4)
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz/8.0))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_samps_per_symb(self.samp_rate/self.decim/ self.baud)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.decim / 50 * 48)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim/50*48, self.audio_lpf_cutoff, 2e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.rf_lpf_cutoff, 2e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_1.set_k((-1*self.samp_rate/self.decim/(2*math.pi), ))
        self.blocks_keep_one_in_n_0_0_0.set_n(int(self.samp_rate/self.decim /self.meta_rate))
        self.analog_sig_source_x_0.set_frequency(self.samp_rate/self.decim/4)

    def get_baud(self):
        return self.baud

    def set_baud(self, baud):
        self.baud = baud
        self.set_samps_per_symb(self.samp_rate/self.decim/ self.baud)

    def get_xlate_taps_old(self):
        return self.xlate_taps_old

    def set_xlate_taps_old(self, xlate_taps_old):
        self.xlate_taps_old = xlate_taps_old

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
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.throttle_factor)

    def get_samps_per_symb(self):
        return self.samps_per_symb

    def set_samps_per_symb(self, samps_per_symb):
        self.samps_per_symb = samps_per_symb

    def get_rf_lpf_cutoff(self):
        return self.rf_lpf_cutoff

    def set_rf_lpf_cutoff(self, rf_lpf_cutoff):
        self.rf_lpf_cutoff = rf_lpf_cutoff
        Qt.QMetaObject.invokeMethod(self._rf_lpf_cutoff_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rf_lpf_cutoff)))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.rf_lpf_cutoff, 2e3, firdes.WIN_HAMMING, 6.76))

    def get_fsk_deviation_hz(self):
        return self.fsk_deviation_hz

    def set_fsk_deviation_hz(self, fsk_deviation_hz):
        self.fsk_deviation_hz = fsk_deviation_hz
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*self.fsk_deviation_hz/8.0))

    def get_fll_loop_bw_fine(self):
        return self.fll_loop_bw_fine

    def set_fll_loop_bw_fine(self, fll_loop_bw_fine):
        self.fll_loop_bw_fine = fll_loop_bw_fine
        Qt.QMetaObject.invokeMethod(self._fll_loop_bw_fine_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.fll_loop_bw_fine)))
        self.digital_fll_band_edge_cc_0_0.set_loop_bandwidth(self.fll_loop_bw_fine)

    def get_fll_loop_bw(self):
        return self.fll_loop_bw

    def set_fll_loop_bw(self, fll_loop_bw):
        self.fll_loop_bw = fll_loop_bw
        Qt.QMetaObject.invokeMethod(self._fll_loop_bw_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.fll_loop_bw)))
        self.digital_fll_band_edge_cc_0.set_loop_bandwidth(self.fll_loop_bw)

    def get_audio_lpf_cutoff(self):
        return self.audio_lpf_cutoff

    def set_audio_lpf_cutoff(self, audio_lpf_cutoff):
        self.audio_lpf_cutoff = audio_lpf_cutoff
        Qt.QMetaObject.invokeMethod(self._audio_lpf_cutoff_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.audio_lpf_cutoff)))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim/50*48, self.audio_lpf_cutoff, 2e3, firdes.WIN_HAMMING, 6.76))


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--meta-rate", dest="meta_rate", type="eng_float", default=eng_notation.num_to_str(10),
        help="Set meta_rate [default=%default]")
    return parser


def main(top_block_cls=fox1d_playback_sigmf, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(meta_rate=options.meta_rate)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
