#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Radio Jove RTL-SDR Receiver
# Author: Zach Leffke, KJ4QLP
# Description: Receive Jupiter Emissions with RTL-SDR on 20.1MHz
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
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class radio_jove_dual_rtlsdr_sigmf_3(gr.top_block, Qt.QWidget):

    def __init__(self, path="/captures/radio_jove", signal_type='RADIO-JOVE'):
        gr.top_block.__init__(self, "Radio Jove RTL-SDR Receiver")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Radio Jove RTL-SDR Receiver")
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

        self.settings = Qt.QSettings("GNU Radio", "radio_jove_dual_rtlsdr_sigmf_3")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.path = path
        self.signal_type = signal_type

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y-%m-%dT%H:%M:%SZ")
        self.samp_rate = samp_rate = 2048000
        self.pol = pol = "linear"
        self.interp_2 = interp_2 = 48
        self.interp_1 = interp_1 = 1000
        self.decim_2 = decim_2 = 500
        self.decim_1 = decim_1 = 2048*2
        self.antenna_1 = antenna_1 = "EW"
        self.antenna_0 = antenna_0 = "NS"
        self.phase_shift_rad = phase_shift_rad = math.pi/2
        self.fn_wav = fn_wav = "{:s}_{:s}_{:s}.wav".format(signal_type.upper(), pol.upper(),ts_str)
        self.fn_1 = fn_1 = "{:s}_{:s}_{:s}".format(signal_type.upper(), antenna_1.upper(),ts_str)
        self.fn_0 = fn_0 = "{:s}_{:s}_{:s}".format(signal_type.upper(), antenna_0.upper(),ts_str)
        self.audio_rate_in = audio_rate_in = samp_rate/(decim_1*decim_2) *(interp_1*interp_2)
        self.vol_right = vol_right = 100
        self.vol_left = vol_left = 100
        self.rx_freq = rx_freq = 20.125e6
        self.phase_shift_complex = phase_shift_complex = complex(math.cos(phase_shift_rad),math.sin(phase_shift_rad))
        self.offset = offset = samp_rate/4
        self.lpf_cut = lpf_cut = 20e3
        self.iir_alpha = iir_alpha = 0.5
        self.fp_wav = fp_wav = "{:s}/{:s}".format(path, fn_wav)
        self.fp_1 = fp_1 = "{:s}/{:s}".format(path, fn_1)
        self.fp_0 = fp_0 = "{:s}/{:s}".format(path, fn_0)
        self.audio_rate_out = audio_rate_out = audio_rate_in/3
        self.audio_lpf_cut = audio_lpf_cut = 5e3

        ##################################################
        # Blocks
        ##################################################
        self.main_tab = Qt.QTabWidget()
        self.main_tab_widget_0 = Qt.QWidget()
        self.main_tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_0)
        self.main_tab_grid_layout_0 = Qt.QGridLayout()
        self.main_tab_layout_0.addLayout(self.main_tab_grid_layout_0)
        self.main_tab.addTab(self.main_tab_widget_0, 'Channel')
        self.main_tab_widget_1 = Qt.QWidget()
        self.main_tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_1)
        self.main_tab_grid_layout_1 = Qt.QGridLayout()
        self.main_tab_layout_1.addLayout(self.main_tab_grid_layout_1)
        self.main_tab.addTab(self.main_tab_widget_1, 'Filter + Sense')
        self.main_tab_widget_2 = Qt.QWidget()
        self.main_tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_2)
        self.main_tab_grid_layout_2 = Qt.QGridLayout()
        self.main_tab_layout_2.addLayout(self.main_tab_grid_layout_2)
        self.main_tab.addTab(self.main_tab_widget_2, 'Audio')
        self.main_tab_widget_3 = Qt.QWidget()
        self.main_tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_3)
        self.main_tab_grid_layout_3 = Qt.QGridLayout()
        self.main_tab_layout_3.addLayout(self.main_tab_grid_layout_3)
        self.main_tab.addTab(self.main_tab_widget_3, 'Power')
        self.top_grid_layout.addWidget(self.main_tab, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._vol_right_range = Range(0, 200, .1, 100, 200)
        self._vol_right_win = RangeWidget(self._vol_right_range, self.set_vol_right, "vol_right", "counter_slider", float)
        self.main_tab_grid_layout_2.addWidget(self._vol_right_win, 8, 0, 1, 4)
        for r in range(8, 9):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self._vol_left_range = Range(0, 200, .1, 100, 200)
        self._vol_left_win = RangeWidget(self._vol_left_range, self.set_vol_left, "vol_left", "counter_slider", float)
        self.main_tab_grid_layout_2.addWidget(self._vol_left_win, 7, 0, 1, 4)
        for r in range(7, 8):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('Freq [Hz]'+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._rx_freq_tool_bar, 4, 0, 1, 2)
        for r in range(4, 5):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 2):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self._iir_alpha_range = Range(0, 1, .001, 0.5, 200)
        self._iir_alpha_win = RangeWidget(self._iir_alpha_range, self.set_iir_alpha, "iir_alpha", "counter_slider", float)
        self.main_tab_grid_layout_3.addWidget(self._iir_alpha_win, 8, 4, 1, 4)
        for r in range(8, 9):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self._audio_lpf_cut_tool_bar = Qt.QToolBar(self)
        self._audio_lpf_cut_tool_bar.addWidget(Qt.QLabel("audio_lpf_cut"+": "))
        self._audio_lpf_cut_line_edit = Qt.QLineEdit(str(self.audio_lpf_cut))
        self._audio_lpf_cut_tool_bar.addWidget(self._audio_lpf_cut_line_edit)
        self._audio_lpf_cut_line_edit.returnPressed.connect(
        	lambda: self.set_audio_lpf_cut(eng_notation.str_to_num(str(self._audio_lpf_cut_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_2.addWidget(self._audio_lpf_cut_tool_bar, 8, 5, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(5, 6):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.single_pole_iir_filter_xx_0_1 = filter.single_pole_iir_filter_ff(iir_alpha, 1)
        self.single_pole_iir_filter_xx_0_0_0 = filter.single_pole_iir_filter_ff(iir_alpha, 1)
        self.single_pole_iir_filter_xx_0_0 = filter.single_pole_iir_filter_ff(iir_alpha, 1)
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(iir_alpha, 1)
        self.rational_resampler_xxx_2_0 = filter.rational_resampler_ccc(
                interpolation=interp_2,
                decimation=decim_2,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=interp_1,
                decimation=decim_1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_ccc(
                interpolation=interp_2,
                decimation=decim_2,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=interp_1,
                decimation=decim_1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_1_0 = qtgui.waterfall_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate_out, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_1_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_1_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_1_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_1_0.disable_legend()

        if "float" == "float" or "float" == "msg_float":
          self.qtgui_waterfall_sink_x_1_0.set_plot_pos_half(not False)

        labels = ['NS-Left', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_1_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_1_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_1_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_1_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_waterfall_sink_x_1_0_win, 4, 0, 2, 4)
        for r in range(4, 6):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_1_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate_out, #bw
        	"RHCP", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_1_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_1_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_1_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_1_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_1_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_1_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_1_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_waterfall_sink_x_0_1_0_win, 4, 4, 2, 4)
        for r in range(4, 6):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_1 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/(decim_1*decim_2) *(interp_1*interp_2), #bw
        	"N/S", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_1.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_1.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_1.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
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

        self.qtgui_waterfall_sink_x_0_1.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_waterfall_sink_x_0_1_win, 4, 0, 2, 4)
        for r in range(4, 6):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_0_0_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate_out, #bw
        	"LHCP", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0_0_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_waterfall_sink_x_0_0_0_0_win, 6, 4, 2, 4)
        for r in range(6, 8):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_0_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/(decim_1*decim_2) *(interp_1*interp_2), #bw
        	"E/W", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_waterfall_sink_x_0_0_0_win, 6, 0, 2, 4)
        for r in range(6, 8):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate/decim_1*interp_1, #bw
        	"E/W", #name
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

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 2, 4, 2, 4)
        for r in range(2, 4):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate/decim_1*interp_1, #bw
        	"N/S", #name
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
        self.main_tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win, 0, 4, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	audio_rate_out, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['NS - Left', 'EW - Right', '', '', '',
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
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_time_sink_x_0_0_win, 7, 4, 1, 4)
        for r in range(7, 8):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1000, #size
        	samp_rate, #samp_rate
        	"", #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.1)
        self.qtgui_time_sink_x_0.set_y_axis(-110, -10)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['LHCP', 'RHCP', 'NS', 'EW', '',
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

        for i in xrange(4):
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
        self.main_tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            4
        )
        self.qtgui_number_sink_0.set_update_time(0.010)
        self.qtgui_number_sink_0.set_title('RSSI')

        labels = ['LHCP', 'RHCP', 'NS', 'EW', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("blue", "red"), ("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(4):
            self.qtgui_number_sink_0.set_min(i, -140)
            self.qtgui_number_sink_0.set_max(i, -40)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_3.addWidget(self._qtgui_number_sink_0_win, 4, 4, 1, 4)
        for r in range(4, 5):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_f(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate_out, #bw
        	"Audio Spectrum", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.010)
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

        labels = ['NS-Left', 'EW-Right', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_freq_sink_x_1_win, 0, 0, 4, 8)
        for r in range(0, 4):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 8):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate_out, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not True)

        labels = ['RHCP', 'LHCP', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_0_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/(decim_1*decim_2) *(interp_1*interp_2), #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['N/S', 'E/W', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq*0, #fc
        	samp_rate / decim_1 *interp_1, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['N/S', 'E/W', '', '', '',
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
        self.main_tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.osmosdr_source_0_0 = osmosdr.source( args="numchan=" + str(1) + " " + "rtl=1,direct_samp=2" )
        self.osmosdr_source_0_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0_0.set_center_freq(rx_freq-offset, 0)
        self.osmosdr_source_0_0.set_freq_corr(0, 0)
        self.osmosdr_source_0_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0_0.set_gain_mode(False, 0)
        self.osmosdr_source_0_0.set_gain(10, 0)
        self.osmosdr_source_0_0.set_if_gain(20, 0)
        self.osmosdr_source_0_0.set_bb_gain(20, 0)
        self.osmosdr_source_0_0.set_antenna('', 0)
        self.osmosdr_source_0_0.set_bandwidth(0, 0)

        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "rtl=0,direct_samp=2" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(rx_freq - offset, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(20, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self._lpf_cut_tool_bar = Qt.QToolBar(self)
        self._lpf_cut_tool_bar.addWidget(Qt.QLabel('Freq [Hz]'+": "))
        self._lpf_cut_line_edit = Qt.QLineEdit(str(self.lpf_cut))
        self._lpf_cut_tool_bar.addWidget(self._lpf_cut_line_edit)
        self._lpf_cut_line_edit.returnPressed.connect(
        	lambda: self.set_lpf_cut(eng_notation.str_to_num(str(self._lpf_cut_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_1.addWidget(self._lpf_cut_tool_bar, 8, 0, 1, 2)
        for r in range(8, 9):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.low_pass_filter_0_1_0 = filter.fir_filter_ccf(int(audio_rate_in/audio_rate_out), firdes.low_pass(
        	1, audio_rate_in, audio_lpf_cut, 500, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1 = filter.fir_filter_ccf(int(audio_rate_in/audio_rate_out), firdes.low_pass(
        	1, audio_rate_in, audio_lpf_cut, 500, firdes.WIN_HAMMING, 6.76))
        self.blocks_nlog10_ff_0_0_0_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_nlog10_ff_0_0_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1_0_1 = blocks.multiply_const_vcc((complex(0,1), ))
        self.blocks_multiply_const_vxx_1_0_0_0 = blocks.multiply_const_vcc((complex(0,-1), ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((vol_right, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((vol_left, ))
        self.blocks_complex_to_real_0_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_mag_squared_0_1 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.audio_sink_0 = audio.sink(16000, '', True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1 * (offset), 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_waterfall_sink_x_0_1_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_freq_sink_x_0_0_0, 1))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_waterfall_sink_x_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.single_pole_iir_filter_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.single_pole_iir_filter_xx_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0_0, 0), (self.single_pole_iir_filter_xx_0_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_1, 0), (self.single_pole_iir_filter_xx_0_0_0, 0))
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_real_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_waterfall_sink_x_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.audio_sink_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_freq_sink_x_1, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_2, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.qtgui_number_sink_0, 1))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_nlog10_ff_0_0_0, 0), (self.qtgui_number_sink_0, 3))
        self.connect((self.blocks_nlog10_ff_0_0_0, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.blocks_nlog10_ff_0_0_0_0, 0), (self.qtgui_number_sink_0, 2))
        self.connect((self.blocks_nlog10_ff_0_0_0_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_complex_to_mag_squared_0_0_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_complex_to_real_0_0, 0))
        self.connect((self.low_pass_filter_0_1_0, 0), (self.blocks_complex_to_mag_squared_0_1, 0))
        self.connect((self.low_pass_filter_0_1_0, 0), (self.blocks_complex_to_real_0_0_0, 0))
        self.connect((self.low_pass_filter_0_1_0, 0), (self.blocks_multiply_const_vxx_1_0_0_0, 0))
        self.connect((self.low_pass_filter_0_1_0, 0), (self.blocks_multiply_const_vxx_1_0_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.osmosdr_source_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.low_pass_filter_0_1, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.qtgui_waterfall_sink_x_0_1, 0))
        self.connect((self.rational_resampler_xxx_2, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.rational_resampler_xxx_2, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_2, 0), (self.rational_resampler_xxx_2_0, 0))
        self.connect((self.rational_resampler_xxx_2_0, 0), (self.low_pass_filter_0_1_0, 0))
        self.connect((self.rational_resampler_xxx_2_0, 0), (self.qtgui_freq_sink_x_0_0, 1))
        self.connect((self.rational_resampler_xxx_2_0, 0), (self.qtgui_waterfall_sink_x_0_0_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0_0, 0), (self.blocks_nlog10_ff_0_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0_0_0, 0), (self.blocks_nlog10_ff_0_0_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0_1, 0), (self.blocks_nlog10_ff_0_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "radio_jove_dual_rtlsdr_sigmf_3")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        self.set_fp_wav("{:s}/{:s}".format(self.path, self.fn_wav))
        self.set_fp_1("{:s}/{:s}".format(self.path, self.fn_1))
        self.set_fp_0("{:s}/{:s}".format(self.path, self.fn_0))

    def get_signal_type(self):
        return self.signal_type

    def set_signal_type(self, signal_type):
        self.signal_type = signal_type

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_fn_wav("{:s}_{:s}_{:s}.wav".format(signal_type.upper(), pol.upper(),self.ts_str))
        self.set_fn_1("{:s}_{:s}_{:s}".format(signal_type.upper(), antenna_1.upper(),self.ts_str))
        self.set_fn_0("{:s}_{:s}_{:s}".format(signal_type.upper(), antenna_0.upper(),self.ts_str))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_offset(self.samp_rate/4)
        self.set_audio_rate_in(self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim_1 *self.interp_1)
        self.osmosdr_source_0_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_pol(self):
        return self.pol

    def set_pol(self, pol):
        self.pol = pol

    def get_interp_2(self):
        return self.interp_2

    def set_interp_2(self, interp_2):
        self.interp_2 = interp_2
        self.set_audio_rate_in(self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))

    def get_interp_1(self):
        return self.interp_1

    def set_interp_1(self, interp_1):
        self.interp_1 = interp_1
        self.set_audio_rate_in(self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim_1 *self.interp_1)

    def get_decim_2(self):
        return self.decim_2

    def set_decim_2(self, decim_2):
        self.decim_2 = decim_2
        self.set_audio_rate_in(self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))

    def get_decim_1(self):
        return self.decim_1

    def set_decim_1(self, decim_1):
        self.decim_1 = decim_1
        self.set_audio_rate_in(self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/(self.decim_1*self.decim_2) *(self.interp_1*self.interp_2))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim_1 *self.interp_1)

    def get_antenna_1(self):
        return self.antenna_1

    def set_antenna_1(self, antenna_1):
        self.antenna_1 = antenna_1

    def get_antenna_0(self):
        return self.antenna_0

    def set_antenna_0(self, antenna_0):
        self.antenna_0 = antenna_0

    def get_phase_shift_rad(self):
        return self.phase_shift_rad

    def set_phase_shift_rad(self, phase_shift_rad):
        self.phase_shift_rad = phase_shift_rad
        self.set_phase_shift_complex(complex(math.cos(self.phase_shift_rad),math.sin(self.phase_shift_rad)))

    def get_fn_wav(self):
        return self.fn_wav

    def set_fn_wav(self, fn_wav):
        self.fn_wav = fn_wav
        self.set_fp_wav("{:s}/{:s}".format(self.path, self.fn_wav))

    def get_fn_1(self):
        return self.fn_1

    def set_fn_1(self, fn_1):
        self.fn_1 = fn_1
        self.set_fp_1("{:s}/{:s}".format(self.path, self.fn_1))

    def get_fn_0(self):
        return self.fn_0

    def set_fn_0(self, fn_0):
        self.fn_0 = fn_0
        self.set_fp_0("{:s}/{:s}".format(self.path, self.fn_0))

    def get_audio_rate_in(self):
        return self.audio_rate_in

    def set_audio_rate_in(self, audio_rate_in):
        self.audio_rate_in = audio_rate_in
        self.set_audio_rate_out(self.audio_rate_in/3)
        self.low_pass_filter_0_1_0.set_taps(firdes.low_pass(1, self.audio_rate_in, self.audio_lpf_cut, 500, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.audio_rate_in, self.audio_lpf_cut, 500, firdes.WIN_HAMMING, 6.76))

    def get_vol_right(self):
        return self.vol_right

    def set_vol_right(self, vol_right):
        self.vol_right = vol_right
        self.blocks_multiply_const_vxx_0_0.set_k((self.vol_right, ))

    def get_vol_left(self):
        return self.vol_left

    def set_vol_left(self, vol_left):
        self.vol_left = vol_left
        self.blocks_multiply_const_vxx_0.set_k((self.vol_left, ))

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim_1 *self.interp_1)
        self.osmosdr_source_0_0.set_center_freq(self.rx_freq-self.offset, 0)
        self.osmosdr_source_0.set_center_freq(self.rx_freq - self.offset, 0)

    def get_phase_shift_complex(self):
        return self.phase_shift_complex

    def set_phase_shift_complex(self, phase_shift_complex):
        self.phase_shift_complex = phase_shift_complex

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self.osmosdr_source_0_0.set_center_freq(self.rx_freq-self.offset, 0)
        self.osmosdr_source_0.set_center_freq(self.rx_freq - self.offset, 0)
        self.analog_sig_source_x_0.set_frequency(-1 * (self.offset))

    def get_lpf_cut(self):
        return self.lpf_cut

    def set_lpf_cut(self, lpf_cut):
        self.lpf_cut = lpf_cut
        Qt.QMetaObject.invokeMethod(self._lpf_cut_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.lpf_cut)))

    def get_iir_alpha(self):
        return self.iir_alpha

    def set_iir_alpha(self, iir_alpha):
        self.iir_alpha = iir_alpha
        self.single_pole_iir_filter_xx_0_1.set_taps(self.iir_alpha)
        self.single_pole_iir_filter_xx_0_0_0.set_taps(self.iir_alpha)
        self.single_pole_iir_filter_xx_0_0.set_taps(self.iir_alpha)
        self.single_pole_iir_filter_xx_0.set_taps(self.iir_alpha)

    def get_fp_wav(self):
        return self.fp_wav

    def set_fp_wav(self, fp_wav):
        self.fp_wav = fp_wav

    def get_fp_1(self):
        return self.fp_1

    def set_fp_1(self, fp_1):
        self.fp_1 = fp_1

    def get_fp_0(self):
        return self.fp_0

    def set_fp_0(self, fp_0):
        self.fp_0 = fp_0

    def get_audio_rate_out(self):
        return self.audio_rate_out

    def set_audio_rate_out(self, audio_rate_out):
        self.audio_rate_out = audio_rate_out
        self.qtgui_waterfall_sink_x_1_0.set_frequency_range(0, self.audio_rate_out)
        self.qtgui_waterfall_sink_x_0_1_0.set_frequency_range(0, self.audio_rate_out)
        self.qtgui_waterfall_sink_x_0_0_0_0.set_frequency_range(0, self.audio_rate_out)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.audio_rate_out)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.audio_rate_out)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.audio_rate_out)

    def get_audio_lpf_cut(self):
        return self.audio_lpf_cut

    def set_audio_lpf_cut(self, audio_lpf_cut):
        self.audio_lpf_cut = audio_lpf_cut
        Qt.QMetaObject.invokeMethod(self._audio_lpf_cut_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.audio_lpf_cut)))
        self.low_pass_filter_0_1_0.set_taps(firdes.low_pass(1, self.audio_rate_in, self.audio_lpf_cut, 500, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.audio_rate_in, self.audio_lpf_cut, 500, firdes.WIN_HAMMING, 6.76))


def argument_parser():
    description = 'Receive Jupiter Emissions with RTL-SDR on 20.1MHz'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "", "--path", dest="path", type="string", default="/captures/radio_jove",
        help="Set path [default=%default]")
    parser.add_option(
        "", "--signal-type", dest="signal_type", type="string", default='RADIO-JOVE',
        help="Set signal_type [default=%default]")
    return parser


def main(top_block_cls=radio_jove_dual_rtlsdr_sigmf_3, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(path=options.path, signal_type=options.signal_type)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
