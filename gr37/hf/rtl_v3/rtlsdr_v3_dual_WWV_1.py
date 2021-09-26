#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Dual RTL-SDR, WWV Receiver / Analyzer
# Author: Zach Leffke, KJ4QLP
# Description: Analyze power, doppler, polarization of WWV emissions
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
from datetime import datetime as dt; import string; import math; import numpy as np
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import gr_sigmf
import sip
import sys
import threading
import time
from gnuradio import qtgui


class rtlsdr_v3_dual_WWV_1(gr.top_block, Qt.QWidget):

    def __init__(self, path="/captures/radio_jove", signal_type='WWV'):
        gr.top_block.__init__(self, "Dual RTL-SDR, WWV Receiver / Analyzer")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Dual RTL-SDR, WWV Receiver / Analyzer")
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

        self.settings = Qt.QSettings("GNU Radio", "rtlsdr_v3_dual_WWV_1")
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
        self.interp_1 = interp_1 = 100
        self.decim_1 = decim_1 = 2048*2
        self.antenna_1 = antenna_1 = "EW"
        self.antenna_0 = antenna_0 = "NS"
        self.samp_rate = samp_rate = 2048000/decim_1*interp_1
        self.pol = pol = "linear"
        self.phase_rad = phase_rad = 0
        self.phase_deg = phase_deg = 0
        self.idx_max = idx_max = 0
        self.fn_1 = fn_1 = "{:s}_{:s}_{:s}".format(signal_type.upper(), antenna_1.upper(),ts_str)
        self.fn_0 = fn_0 = "{:s}_{:s}_{:s}".format(signal_type.upper(), antenna_0.upper(),ts_str)
        self.rx_gain = rx_gain = 10
        self.rx_freq = rx_freq = 15e6
        self.ppm = ppm = 0
        self.pll_lbw = pll_lbw = 200
        self.pll_freq = pll_freq = 100
        self.phase_rad2 = phase_rad2 = phase_deg*math.pi/180.0
        self.phase_label = phase_label = phase_rad*180.0/math.pi
        self.offset = offset = samp_rate/4
        self.ns_delay = ns_delay = 0
        self.nfft = nfft = 1024*16
        self.lpf_cut = lpf_cut = 3e3
        self.idx_label = idx_label = idx_max
        self.fp_1 = fp_1 = "{:s}/{:s}".format(path, fn_1)
        self.fp_0 = fp_0 = "{:s}/{:s}".format(path, fn_0)
        self.fn_wav = fn_wav = "{:s}_{:s}_{:s}.wav".format(signal_type.upper(), pol.upper(),ts_str)
        self.ew_delay = ew_delay = 0
        self.avg_len = avg_len = 1

        ##################################################
        # Blocks
        ##################################################
        self.max_idx_probe1 = blocks.probe_signal_f()
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
        self.main_tab.addTab(self.main_tab_widget_1, 'Filter + Resamp')
        self.main_tab_widget_2 = Qt.QWidget()
        self.main_tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_2)
        self.main_tab_grid_layout_2 = Qt.QGridLayout()
        self.main_tab_layout_2.addLayout(self.main_tab_grid_layout_2)
        self.main_tab.addTab(self.main_tab_widget_2, 'Xcorr')
        self.main_tab_widget_3 = Qt.QWidget()
        self.main_tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_3)
        self.main_tab_grid_layout_3 = Qt.QGridLayout()
        self.main_tab_layout_3.addLayout(self.main_tab_grid_layout_3)
        self.main_tab.addTab(self.main_tab_widget_3, 'Phase')
        self.main_tab_widget_4 = Qt.QWidget()
        self.main_tab_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_4)
        self.main_tab_grid_layout_4 = Qt.QGridLayout()
        self.main_tab_layout_4.addLayout(self.main_tab_grid_layout_4)
        self.main_tab.addTab(self.main_tab_widget_4, 'Cpol')
        self.top_grid_layout.addWidget(self.main_tab, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self._pll_lbw_tool_bar = Qt.QToolBar(self)
        self._pll_lbw_tool_bar.addWidget(Qt.QLabel("pll_lbw"+": "))
        self._pll_lbw_line_edit = Qt.QLineEdit(str(self.pll_lbw))
        self._pll_lbw_tool_bar.addWidget(self._pll_lbw_line_edit)
        self._pll_lbw_line_edit.returnPressed.connect(
        	lambda: self.set_pll_lbw(eng_notation.str_to_num(str(self._pll_lbw_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_4.addWidget(self._pll_lbw_tool_bar, 8, 1, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self._pll_freq_tool_bar = Qt.QToolBar(self)
        self._pll_freq_tool_bar.addWidget(Qt.QLabel("pll_freq"+": "))
        self._pll_freq_line_edit = Qt.QLineEdit(str(self.pll_freq))
        self._pll_freq_tool_bar.addWidget(self._pll_freq_line_edit)
        self._pll_freq_line_edit.returnPressed.connect(
        	lambda: self.set_pll_freq(eng_notation.str_to_num(str(self._pll_freq_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_4.addWidget(self._pll_freq_tool_bar, 8, 0, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.phase_probe = blocks.probe_signal_f()
        self._ns_delay_tool_bar = Qt.QToolBar(self)
        self._ns_delay_tool_bar.addWidget(Qt.QLabel('ns_delay'+": "))
        self._ns_delay_line_edit = Qt.QLineEdit(str(self.ns_delay))
        self._ns_delay_tool_bar.addWidget(self._ns_delay_line_edit)
        self._ns_delay_line_edit.returnPressed.connect(
        	lambda: self.set_ns_delay(eng_notation.str_to_num(str(self._ns_delay_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_2.addWidget(self._ns_delay_tool_bar, 4, 0, 1, 1)
        for r in range(4, 5):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
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

        def _idx_max_probe():
            while True:
                val = self.max_idx_probe1.level()
                try:
                    self.set_idx_max(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _idx_max_thread = threading.Thread(target=_idx_max_probe)
        _idx_max_thread.daemon = True
        _idx_max_thread.start()

        self._ew_delay_tool_bar = Qt.QToolBar(self)
        self._ew_delay_tool_bar.addWidget(Qt.QLabel('ew_delay'+": "))
        self._ew_delay_line_edit = Qt.QLineEdit(str(self.ew_delay))
        self._ew_delay_tool_bar.addWidget(self._ew_delay_line_edit)
        self._ew_delay_line_edit.returnPressed.connect(
        	lambda: self.set_ew_delay(eng_notation.str_to_num(str(self._ew_delay_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_2.addWidget(self._ew_delay_tool_bar, 4, 1, 1, 1)
        for r in range(4, 5):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self._avg_len_tool_bar = Qt.QToolBar(self)
        self._avg_len_tool_bar.addWidget(Qt.QLabel('avg_len'+": "))
        self._avg_len_line_edit = Qt.QLineEdit(str(self.avg_len))
        self._avg_len_tool_bar.addWidget(self._avg_len_line_edit)
        self._avg_len_line_edit.returnPressed.connect(
        	lambda: self.set_avg_len(eng_notation.str_to_num(str(self._avg_len_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_4.addWidget(self._avg_len_tool_bar, 3, 8, 1, 2)
        for r in range(3, 4):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(8, 10):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.sigmf_source_1 = gr_sigmf.source('/captures/wwv/WWV_EW_2021-06-01T04:02:22Z.sigmf-data', "cf32" + ("_le" if sys.byteorder == "little" else "_be"), False)
        self.sigmf_source_0 = gr_sigmf.source('/captures/wwv/WWV_NS_2021-06-01T04:02:22Z.sigmf-data', "cf32" + ("_le" if sys.byteorder == "little" else "_be"), False)
        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel('Gain'+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._rx_gain_tool_bar, 4, 2, 1, 1)
        for r in range(4, 5):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 3):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0_1_0_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"RHCP", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_1_0_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_1_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_1_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_1_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_1_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_1_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_1_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_1_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_waterfall_sink_x_0_1_0_0_win, 4, 4, 2, 4)
        for r in range(4, 6):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_1_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
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
        self.main_tab_grid_layout_4.addWidget(self._qtgui_waterfall_sink_x_0_1_0_win, 4, 0, 2, 4)
        for r in range(4, 6):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_1 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/5, #bw
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
        self.qtgui_waterfall_sink_x_0_0_0_0_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"LHCP", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0_0_0_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_0_0_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_0_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0_0_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0_0_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_waterfall_sink_x_0_0_0_0_0_win, 6, 4, 2, 4)
        for r in range(6, 8):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_0_0_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
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
        self.main_tab_grid_layout_4.addWidget(self._qtgui_waterfall_sink_x_0_0_0_0_win, 6, 0, 2, 4)
        for r in range(6, 8):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_0_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/5, #bw
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
        	samp_rate, #bw
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
        	samp_rate, #bw
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
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            nfft,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

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
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_vector_sink_f_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
        	2048, #size
        	samp_rate, #samp_rate
        	"Freq Offset PLL", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(True)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_2.disable_legend()

        labels = ['RHCP', 'LHCP', 'R-L', '', '',
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

        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_time_sink_x_2_win, 0, 8, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(8, 12):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_c(
        	1024*8, #size
        	samp_rate, #samp_rate
        	"Original", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(True)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0.disable_legend()

        labels = ['re{NS}', 'im{NS}', 're{EW}', 'im{EW}', '',
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
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_1_0_win, 0, 0, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
        	1024*8, #size
        	samp_rate, #samp_rate
        	"Shifted", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

        labels = ['re{NS}', 'im{NS}', 're{EW}', 'im{EW}', '',
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
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_1_win, 0, 4, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	1024*8, #size
        	samp_rate, #samp_rate
        	"Shifted", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.010)
        self.qtgui_time_sink_x_0_1.set_y_axis(-360, 360)

        self.qtgui_time_sink_x_0_1.set_y_label('Phase', "")

        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()

        labels = ['NS', 'EW', 'NS-EW', '', '',
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

        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_1_win, 2, 4, 2, 4)
        for r in range(2, 4):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024*8, #size
        	samp_rate, #samp_rate
        	"Original", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0.set_y_axis(-360, 360)

        self.qtgui_time_sink_x_0.set_y_label('Phase', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['NS', 'EW', 'NS-EW', '', '',
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

        for i in xrange(3):
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
        self.main_tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_win, 2, 0, 2, 4)
        for r in range(2, 4):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            2
        )
        self.qtgui_number_sink_0.set_update_time(0.010)
        self.qtgui_number_sink_0.set_title("")

        labels = ['Delay', 'Phase', 'Range Delta', '', '',
                  '', '', '', '', '']
        units = ['[samp]', '[deg]', '[km]', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(2):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(True)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_number_sink_0_win, 4, 4, 1, 4)
        for r in range(4, 5):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_1_0 = qtgui.histogram_sink_f(
        	1000,
        	20000,
                -360,
                360,
        	"Phase",
        	1
        )

        self.qtgui_histogram_sink_x_1_0.set_update_time(0.10)
        self.qtgui_histogram_sink_x_1_0.enable_autoscale(False)
        self.qtgui_histogram_sink_x_1_0.enable_accumulate(True)
        self.qtgui_histogram_sink_x_1_0.enable_grid(False)
        self.qtgui_histogram_sink_x_1_0.enable_axis_labels(True)

        if not True:
          self.qtgui_histogram_sink_x_1_0.disable_legend()

        labels = ['RHCP', 'LHCP', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_1_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_histogram_sink_x_1_0_win, 6, 8, 2, 4)
        for r in range(6, 8):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(8, 12):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_1 = qtgui.histogram_sink_f(
        	1000,
        	20000,
                -100,
                100,
        	"FREQ PLL",
        	2
        )

        self.qtgui_histogram_sink_x_1.set_update_time(0.10)
        self.qtgui_histogram_sink_x_1.enable_autoscale(False)
        self.qtgui_histogram_sink_x_1.enable_accumulate(True)
        self.qtgui_histogram_sink_x_1.enable_grid(False)
        self.qtgui_histogram_sink_x_1.enable_axis_labels(True)

        if not True:
          self.qtgui_histogram_sink_x_1.disable_legend()

        labels = ['RHCP', 'LHCP', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_1_win = sip.wrapinstance(self.qtgui_histogram_sink_x_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_histogram_sink_x_1_win, 4, 8, 2, 4)
        for r in range(4, 6):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(8, 12):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_0_0 = qtgui.histogram_sink_f(
        	1,
        	720,
                -180,
                180,
        	"phase",
        	1
        )

        self.qtgui_histogram_sink_x_0_0.set_update_time(0.010)
        self.qtgui_histogram_sink_x_0_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0_0.enable_accumulate(True)
        self.qtgui_histogram_sink_x_0_0.enable_grid(False)
        self.qtgui_histogram_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_histogram_sink_x_0_0.disable_legend()

        labels = ['phase [deg]', 'Corr Mag', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_0_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_histogram_sink_x_0_0_win, 2, 4, 2, 4)
        for r in range(2, 4):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_0 = qtgui.histogram_sink_f(
        	1,
        	nfft,
                -500,
                500,
        	"sample offset",
        	1
        )

        self.qtgui_histogram_sink_x_0.set_update_time(0.010)
        self.qtgui_histogram_sink_x_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0.enable_accumulate(True)
        self.qtgui_histogram_sink_x_0.enable_grid(False)
        self.qtgui_histogram_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_histogram_sink_x_0.disable_legend()

        labels = ['samp offset', 'Corr Mag', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_histogram_sink_x_0_win, 0, 4, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Freq Corrected", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_freq_sink_x_0_0_0_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Orig", #name
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
        self.main_tab_grid_layout_4.addWidget(self._qtgui_freq_sink_x_0_0_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/5, #bw
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
        	samp_rate, #bw
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
        self._ppm_tool_bar = Qt.QToolBar(self)
        self._ppm_tool_bar.addWidget(Qt.QLabel('PPM'+": "))
        self._ppm_line_edit = Qt.QLineEdit(str(self.ppm))
        self._ppm_tool_bar.addWidget(self._ppm_line_edit)
        self._ppm_line_edit.returnPressed.connect(
        	lambda: self.set_ppm(eng_notation.str_to_num(str(self._ppm_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._ppm_tool_bar, 4, 3, 1, 1)
        for r in range(4, 5):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(3, 4):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)

        def _phase_rad_probe():
            while True:
                val = self.phase_probe.level()
                try:
                    self.set_phase_rad(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _phase_rad_thread = threading.Thread(target=_phase_rad_probe)
        _phase_rad_thread.daemon = True
        _phase_rad_thread.start()

        self._phase_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._phase_label_formatter = None
        else:
          self._phase_label_formatter = lambda x: eng_notation.num_to_str(x)

        self._phase_label_tool_bar.addWidget(Qt.QLabel("phase_label"+": "))
        self._phase_label_label = Qt.QLabel(str(self._phase_label_formatter(self.phase_label)))
        self._phase_label_tool_bar.addWidget(self._phase_label_label)
        self.main_tab_grid_layout_3.addWidget(self._phase_label_tool_bar, 4, 0, 1, 1)
        for r in range(4, 5):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self._phase_deg_tool_bar = Qt.QToolBar(self)
        self._phase_deg_tool_bar.addWidget(Qt.QLabel("phase_deg"+": "))
        self._phase_deg_line_edit = Qt.QLineEdit(str(self.phase_deg))
        self._phase_deg_tool_bar.addWidget(self._phase_deg_line_edit)
        self._phase_deg_line_edit.returnPressed.connect(
        	lambda: self.set_phase_deg(eng_notation.str_to_num(str(self._phase_deg_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_3.addWidget(self._phase_deg_tool_bar, 4, 4, 1, 1)
        for r in range(4, 5):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(4, 5):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self.low_pass_filter_1 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, lpf_cut, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, lpf_cut, 1e3, firdes.WIN_HAMMING, 6.76))
        self._idx_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._idx_label_formatter = None
        else:
          self._idx_label_formatter = lambda x: eng_notation.num_to_str(x)

        self._idx_label_tool_bar.addWidget(Qt.QLabel("idx_label"+": "))
        self._idx_label_label = Qt.QLabel(str(self._idx_label_formatter(self.idx_label)))
        self._idx_label_tool_bar.addWidget(self._idx_label_label)
        self.main_tab_grid_layout_2.addWidget(self._idx_label_tool_bar, 4, 3, 1, 1)
        for r in range(4, 5):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.fft_vxx_2 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 4)
        self.fft_vxx_1 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 4)
        self.fft_vxx_0 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 4)
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, nfft)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_sub_xx_1_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_1 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_gr_complex*1, 95)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_multiply_const_vxx_2_0 = blocks.multiply_const_vff((samp_rate/(2*math.pi), ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vff((samp_rate/(2*math.pi), ))
        self.blocks_multiply_const_vxx_1_1_0 = blocks.multiply_const_vff((180.0/math.pi, ))
        self.blocks_multiply_const_vxx_1_1 = blocks.multiply_const_vff((180.0/math.pi, ))
        self.blocks_multiply_const_vxx_1_0_2_0 = blocks.multiply_const_vff((180.0/math.pi, ))
        self.blocks_multiply_const_vxx_1_0_2 = blocks.multiply_const_vff((180.0/math.pi, ))
        self.blocks_multiply_const_vxx_1_0_1 = blocks.multiply_const_vcc((complex(0,1), ))
        self.blocks_multiply_const_vxx_1_0_0_2_0 = blocks.multiply_const_vff((180.0/math.pi, ))
        self.blocks_multiply_const_vxx_1_0_0_2 = blocks.multiply_const_vff((180.0/math.pi, ))
        self.blocks_multiply_const_vxx_1_0_0_1 = blocks.multiply_const_vcc((complex(math.cos(-1*phase_rad2),math.sin(-1*phase_rad2)), ))
        self.blocks_multiply_const_vxx_1_0_0_0 = blocks.multiply_const_vcc((complex(0,-1), ))
        self.blocks_multiply_const_vxx_1_0_0 = blocks.multiply_const_vff((180.0/math.pi, ))
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_vff((180.0/math.pi, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((180.0/math.pi, ))
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(nfft)
        self.blocks_moving_average_xx_0_1 = blocks.moving_average_ff(int(avg_len), 1.0/avg_len, 4000, 1)
        self.blocks_moving_average_xx_0_0_0 = blocks.moving_average_ff(int(avg_len), 1.0/avg_len, 4000, 1)
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_ff(int(avg_len), 1.0/avg_len, 4000, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(int(avg_len), 1.0/avg_len, 4000, 1)
        self.blocks_keep_m_in_n_0_0_0 = blocks.keep_m_in_n(gr.sizeof_float, 1, nfft, int(idx_max))
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, int(ew_delay))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, int(ns_delay))
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(nfft)
        self.blocks_complex_to_arg_0_0_0_2 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0_0_0_1 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0_0_0_0_1 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0_0_0_0_0 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0_0_0_0 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0_0_0 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.blocks_argmax_xx_0 = blocks.argmax_fs(nfft)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-nfft/2.0, ))
        self.analog_pll_freqdet_cf_0_0 = analog.pll_freqdet_cf(math.pi/pll_lbw, math.pi/pll_freq, -1*math.pi/pll_freq)
        self.analog_pll_freqdet_cf_0 = analog.pll_freqdet_cf(math.pi/pll_lbw, math.pi/pll_freq, -1*math.pi/pll_freq)
        self.analog_pll_carriertracking_cc_0_0 = analog.pll_carriertracking_cc(math.pi/pll_lbw, math.pi/pll_freq, -math.pi/pll_freq)
        self.analog_pll_carriertracking_cc_0 = analog.pll_carriertracking_cc(math.pi/pll_lbw, math.pi/pll_freq, -math.pi/pll_freq)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pll_carriertracking_cc_0, 0), (self.qtgui_freq_sink_x_0_0_0_0, 1))
        self.connect((self.analog_pll_carriertracking_cc_0, 0), (self.qtgui_waterfall_sink_x_0_0_0_0_0, 0))
        self.connect((self.analog_pll_carriertracking_cc_0_0, 0), (self.qtgui_freq_sink_x_0_0_0_0, 0))
        self.connect((self.analog_pll_carriertracking_cc_0_0, 0), (self.qtgui_waterfall_sink_x_0_1_0_0, 0))
        self.connect((self.analog_pll_freqdet_cf_0, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.analog_pll_freqdet_cf_0_0, 0), (self.blocks_multiply_const_vxx_2_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.max_idx_probe1, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.qtgui_histogram_sink_x_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.analog_pll_carriertracking_cc_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.analog_pll_freqdet_cf_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_complex_to_arg_0_0_0_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_waterfall_sink_x_0_1_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.analog_pll_carriertracking_cc_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.analog_pll_freqdet_cf_0_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_complex_to_arg_0_0_0_0_1, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_freq_sink_x_0_0_0, 1))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_waterfall_sink_x_0_0_0_0, 0))
        self.connect((self.blocks_argmax_xx_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_argmax_xx_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_keep_m_in_n_0_0_0, 0))
        self.connect((self.blocks_complex_to_arg_0_0_0, 0), (self.blocks_multiply_const_vxx_1_1, 0))
        self.connect((self.blocks_complex_to_arg_0_0_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_complex_to_arg_0_0_0_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.blocks_complex_to_arg_0_0_0_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_complex_to_arg_0_0_0_0_0, 0), (self.blocks_multiply_const_vxx_1_0_0, 0))
        self.connect((self.blocks_complex_to_arg_0_0_0_0_0, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.blocks_complex_to_arg_0_0_0_0_1, 0), (self.blocks_multiply_const_vxx_1_0_0_2_0, 0))
        self.connect((self.blocks_complex_to_arg_0_0_0_1, 0), (self.blocks_multiply_const_vxx_1_1_0, 0))
        self.connect((self.blocks_complex_to_arg_0_0_0_1, 0), (self.blocks_sub_xx_0_0, 0))
        self.connect((self.blocks_complex_to_arg_0_0_0_2, 0), (self.blocks_multiply_const_vxx_1_0_0_2, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_argmax_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.blocks_keep_m_in_n_0_0_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_sub_xx_1, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_histogram_sink_x_1, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.blocks_sub_xx_1, 1))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.qtgui_histogram_sink_x_1, 1))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.qtgui_time_sink_x_2, 1))
        self.connect((self.blocks_moving_average_xx_0_0_0, 0), (self.blocks_sub_xx_1_0, 1))
        self.connect((self.blocks_moving_average_xx_0_1, 0), (self.blocks_sub_xx_1_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.fft_vxx_2, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_histogram_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_number_sink_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_0, 0), (self.qtgui_time_sink_x_0_1, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_0_1, 0), (self.blocks_complex_to_arg_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0_0_1, 0), (self.blocks_multiply_const_vxx_1_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0_0_1, 0), (self.blocks_multiply_const_vxx_1_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0_0_1, 0), (self.qtgui_time_sink_x_1, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_0_2, 0), (self.blocks_moving_average_xx_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0_0_2_0, 0), (self.blocks_moving_average_xx_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_2, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_multiply_const_vxx_1_0_2_0, 0), (self.qtgui_time_sink_x_0_1, 2))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_1_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2_0, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_1, 0), (self.fft_vxx_1, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_multiply_const_vxx_1_0_2, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.phase_probe, 0))
        self.connect((self.blocks_sub_xx_0_0, 0), (self.blocks_multiply_const_vxx_1_0_2_0, 0))
        self.connect((self.blocks_sub_xx_1, 0), (self.qtgui_time_sink_x_2, 2))
        self.connect((self.blocks_sub_xx_1_0, 0), (self.qtgui_histogram_sink_x_1_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.fft_vxx_1, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.fft_vxx_2, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.fft_vxx_2, 0), (self.blocks_vector_to_stream_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_arg_0_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_arg_0_0_0_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_time_sink_x_1_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_complex_to_arg_0_0_0_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_multiply_const_vxx_1_0_0_1, 0))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_stream_to_vector_1, 0))
        self.connect((self.low_pass_filter_1, 0), (self.qtgui_time_sink_x_1_0, 1))
        self.connect((self.low_pass_filter_1, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_waterfall_sink_x_0_1, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_freq_sink_x_0_0, 1))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_waterfall_sink_x_0_0_0, 0))
        self.connect((self.sigmf_source_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.sigmf_source_1, 0), (self.blocks_throttle_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rtlsdr_v3_dual_WWV_1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
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

    def get_interp_1(self):
        return self.interp_1

    def set_interp_1(self, interp_1):
        self.interp_1 = interp_1
        self.set_samp_rate(2048000/self.decim_1*self.interp_1)

    def get_decim_1(self):
        return self.decim_1

    def set_decim_1(self, decim_1):
        self.decim_1 = decim_1
        self.set_samp_rate(2048000/self.decim_1*self.interp_1)

    def get_antenna_1(self):
        return self.antenna_1

    def set_antenna_1(self, antenna_1):
        self.antenna_1 = antenna_1

    def get_antenna_0(self):
        return self.antenna_0

    def set_antenna_0(self, antenna_0):
        self.antenna_0 = antenna_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0_1_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(0, self.samp_rate/5)
        self.qtgui_waterfall_sink_x_0_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(0, self.samp_rate/5)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate)
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/5)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate)
        self.set_offset(self.samp_rate/4)
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cut, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cut, 1e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.blocks_multiply_const_vxx_2_0.set_k((self.samp_rate/(2*math.pi), ))
        self.blocks_multiply_const_vxx_2.set_k((self.samp_rate/(2*math.pi), ))

    def get_pol(self):
        return self.pol

    def set_pol(self, pol):
        self.pol = pol

    def get_phase_rad(self):
        return self.phase_rad

    def set_phase_rad(self, phase_rad):
        self.phase_rad = phase_rad
        self.set_phase_label(self._phase_label_formatter(self.phase_rad*180.0/math.pi))

    def get_phase_deg(self):
        return self.phase_deg

    def set_phase_deg(self, phase_deg):
        self.phase_deg = phase_deg
        self.set_phase_rad2(self.phase_deg*math.pi/180.0)
        Qt.QMetaObject.invokeMethod(self._phase_deg_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.phase_deg)))

    def get_idx_max(self):
        return self.idx_max

    def set_idx_max(self, idx_max):
        self.idx_max = idx_max
        self.set_idx_label(self._idx_label_formatter(self.idx_max))
        self.blocks_keep_m_in_n_0_0_0.set_offset(int(self.idx_max))

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

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate)

    def get_ppm(self):
        return self.ppm

    def set_ppm(self, ppm):
        self.ppm = ppm
        Qt.QMetaObject.invokeMethod(self._ppm_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ppm)))

    def get_pll_lbw(self):
        return self.pll_lbw

    def set_pll_lbw(self, pll_lbw):
        self.pll_lbw = pll_lbw
        Qt.QMetaObject.invokeMethod(self._pll_lbw_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.pll_lbw)))
        self.analog_pll_freqdet_cf_0_0.set_loop_bandwidth(math.pi/self.pll_lbw)
        self.analog_pll_freqdet_cf_0.set_loop_bandwidth(math.pi/self.pll_lbw)
        self.analog_pll_carriertracking_cc_0_0.set_loop_bandwidth(math.pi/self.pll_lbw)
        self.analog_pll_carriertracking_cc_0.set_loop_bandwidth(math.pi/self.pll_lbw)

    def get_pll_freq(self):
        return self.pll_freq

    def set_pll_freq(self, pll_freq):
        self.pll_freq = pll_freq
        Qt.QMetaObject.invokeMethod(self._pll_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.pll_freq)))
        self.analog_pll_freqdet_cf_0_0.set_max_freq(math.pi/self.pll_freq)
        self.analog_pll_freqdet_cf_0_0.set_min_freq(-1*math.pi/self.pll_freq)
        self.analog_pll_freqdet_cf_0.set_max_freq(math.pi/self.pll_freq)
        self.analog_pll_freqdet_cf_0.set_min_freq(-1*math.pi/self.pll_freq)
        self.analog_pll_carriertracking_cc_0_0.set_max_freq(math.pi/self.pll_freq)
        self.analog_pll_carriertracking_cc_0_0.set_min_freq(-math.pi/self.pll_freq)
        self.analog_pll_carriertracking_cc_0.set_max_freq(math.pi/self.pll_freq)
        self.analog_pll_carriertracking_cc_0.set_min_freq(-math.pi/self.pll_freq)

    def get_phase_rad2(self):
        return self.phase_rad2

    def set_phase_rad2(self, phase_rad2):
        self.phase_rad2 = phase_rad2
        self.blocks_multiply_const_vxx_1_0_0_1.set_k((complex(math.cos(-1*self.phase_rad2),math.sin(-1*self.phase_rad2)), ))

    def get_phase_label(self):
        return self.phase_label

    def set_phase_label(self, phase_label):
        self.phase_label = phase_label
        Qt.QMetaObject.invokeMethod(self._phase_label_label, "setText", Qt.Q_ARG("QString", self.phase_label))

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset

    def get_ns_delay(self):
        return self.ns_delay

    def set_ns_delay(self, ns_delay):
        self.ns_delay = ns_delay
        Qt.QMetaObject.invokeMethod(self._ns_delay_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ns_delay)))
        self.blocks_delay_0.set_dly(int(self.ns_delay))

    def get_nfft(self):
        return self.nfft

    def set_nfft(self, nfft):
        self.nfft = nfft
        self.qtgui_histogram_sink_x_0.set_bins(self.nfft)
        self.qtgui_histogram_sink_x_0.set_bins(self.nfft)
        self.blocks_keep_m_in_n_0_0_0.set_n(self.nfft)
        self.blocks_add_const_vxx_0.set_k((-self.nfft/2.0, ))

    def get_lpf_cut(self):
        return self.lpf_cut

    def set_lpf_cut(self, lpf_cut):
        self.lpf_cut = lpf_cut
        Qt.QMetaObject.invokeMethod(self._lpf_cut_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.lpf_cut)))
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cut, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cut, 1e3, firdes.WIN_HAMMING, 6.76))

    def get_idx_label(self):
        return self.idx_label

    def set_idx_label(self, idx_label):
        self.idx_label = idx_label
        Qt.QMetaObject.invokeMethod(self._idx_label_label, "setText", Qt.Q_ARG("QString", self.idx_label))

    def get_fp_1(self):
        return self.fp_1

    def set_fp_1(self, fp_1):
        self.fp_1 = fp_1

    def get_fp_0(self):
        return self.fp_0

    def set_fp_0(self, fp_0):
        self.fp_0 = fp_0

    def get_fn_wav(self):
        return self.fn_wav

    def set_fn_wav(self, fn_wav):
        self.fn_wav = fn_wav

    def get_ew_delay(self):
        return self.ew_delay

    def set_ew_delay(self, ew_delay):
        self.ew_delay = ew_delay
        Qt.QMetaObject.invokeMethod(self._ew_delay_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ew_delay)))
        self.blocks_delay_0_0.set_dly(int(self.ew_delay))

    def get_avg_len(self):
        return self.avg_len

    def set_avg_len(self, avg_len):
        self.avg_len = avg_len
        Qt.QMetaObject.invokeMethod(self._avg_len_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.avg_len)))
        self.blocks_moving_average_xx_0_1.set_length_and_scale(int(self.avg_len), 1.0/self.avg_len)
        self.blocks_moving_average_xx_0_0_0.set_length_and_scale(int(self.avg_len), 1.0/self.avg_len)
        self.blocks_moving_average_xx_0_0.set_length_and_scale(int(self.avg_len), 1.0/self.avg_len)
        self.blocks_moving_average_xx_0.set_length_and_scale(int(self.avg_len), 1.0/self.avg_len)


def argument_parser():
    description = 'Analyze power, doppler, polarization of WWV emissions'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "", "--path", dest="path", type="string", default="/captures/radio_jove",
        help="Set path [default=%default]")
    parser.add_option(
        "", "--signal-type", dest="signal_type", type="string", default='WWV',
        help="Set signal_type [default=%default]")
    return parser


def main(top_block_cls=rtlsdr_v3_dual_WWV_1, options=None):
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
