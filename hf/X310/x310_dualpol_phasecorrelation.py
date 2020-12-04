#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Dual Polarization Phase Correlation, Start Time [UTC]: 2020-09-09T03:36:04.637873Z
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
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
import time
from gnuradio import qtgui


class x310_dualpol_phasecorrelation(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Dual Polarization Phase Correlation, Start Time [UTC]: 2020-09-09T03:36:04.637873Z")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Dual Polarization Phase Correlation, Start Time [UTC]: 2020-09-09T03:36:04.637873Z")
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

        self.settings = Qt.QSettings("GNU Radio", "x310_dualpol_phasecorrelation")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.rx_freq = rx_freq = 10e6
        self.offset_tune = offset_tune = -10e3
        self.usrp_tune_freq = usrp_tune_freq = rx_freq+ offset_tune
        self.usrp_clk_rate = usrp_clk_rate = 200e6
        self.usrp_ddc_freq = usrp_ddc_freq = np.round(usrp_tune_freq/usrp_clk_rate* 2**32)/2**32*usrp_clk_rate
        self.coarse_tune = coarse_tune = 0
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.phase_shift = phase_shift = 90
        self.phase_deg = phase_deg = 0
        self.lo_freq = lo_freq = usrp_ddc_freq +coarse_tune - offset_tune
        self.title_str = title_str = "Dual Polarization Phase Correlation, Start Time [UTC]: {:s}".format(ts_str)
        self.samp_rate = samp_rate = 2e6
        self.pll_lpf_cut = pll_lpf_cut = 5000
        self.pll_lbw = pll_lbw = 200
        self.pll_freq = pll_freq = 100
        self.pll_avg = pll_avg = 100000
        self.phase_rad2 = phase_rad2 = phase_shift * math.pi/180.0
        self.phase_rad = phase_rad = phase_deg * math.pi/180.0
        self.phase_delta_avg = phase_delta_avg = 1000
        self.lpf_cutoff = lpf_cutoff = 100e3
        self.lo_freq_label = lo_freq_label = "{:9f}".format(lo_freq)
        self.filter_taps = filter_taps = firdes.low_pass(1.0, 2.5,0.1,0.02,firdes.WIN_HAMMING)
        self.decim2 = decim2 = 10
        self.decim = decim = 10
        self.c_ms = c_ms = 299792458

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
        self.main_tab.addTab(self.main_tab_widget_1, 'Phase Align')
        self.main_tab_widget_2 = Qt.QWidget()
        self.main_tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_2)
        self.main_tab_grid_layout_2 = Qt.QGridLayout()
        self.main_tab_layout_2.addLayout(self.main_tab_grid_layout_2)
        self.main_tab.addTab(self.main_tab_widget_2, 'RHCP_LHCP')
        self.main_tab_widget_3 = Qt.QWidget()
        self.main_tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_3)
        self.main_tab_grid_layout_3 = Qt.QGridLayout()
        self.main_tab_layout_3.addLayout(self.main_tab_grid_layout_3)
        self.main_tab.addTab(self.main_tab_widget_3, 'Correlation')
        self.main_tab_widget_4 = Qt.QWidget()
        self.main_tab_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_4)
        self.main_tab_grid_layout_4 = Qt.QGridLayout()
        self.main_tab_layout_4.addLayout(self.main_tab_grid_layout_4)
        self.main_tab.addTab(self.main_tab_widget_4, 'PLL')
        self.main_tab_widget_5 = Qt.QWidget()
        self.main_tab_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_5)
        self.main_tab_grid_layout_5 = Qt.QGridLayout()
        self.main_tab_layout_5.addLayout(self.main_tab_grid_layout_5)
        self.main_tab.addTab(self.main_tab_widget_5, 'Phase Compare')
        self.top_grid_layout.addWidget(self.main_tab, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel('SAMP_RATE'+": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._samp_rate_tool_bar, 8, 0, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('FREQ'+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._rx_freq_tool_bar, 8, 1, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self._pll_lpf_cut_tool_bar = Qt.QToolBar(self)
        self._pll_lpf_cut_tool_bar.addWidget(Qt.QLabel("pll_lpf_cut"+": "))
        self._pll_lpf_cut_line_edit = Qt.QLineEdit(str(self.pll_lpf_cut))
        self._pll_lpf_cut_tool_bar.addWidget(self._pll_lpf_cut_line_edit)
        self._pll_lpf_cut_line_edit.returnPressed.connect(
        	lambda: self.set_pll_lpf_cut(eng_notation.str_to_num(str(self._pll_lpf_cut_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_4.addWidget(self._pll_lpf_cut_tool_bar, 8, 3, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(3, 4):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
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
        self._pll_avg_tool_bar = Qt.QToolBar(self)
        self._pll_avg_tool_bar.addWidget(Qt.QLabel("pll_avg"+": "))
        self._pll_avg_line_edit = Qt.QLineEdit(str(self.pll_avg))
        self._pll_avg_tool_bar.addWidget(self._pll_avg_line_edit)
        self._pll_avg_line_edit.returnPressed.connect(
        	lambda: self.set_pll_avg(eng_notation.str_to_num(str(self._pll_avg_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_4.addWidget(self._pll_avg_tool_bar, 8, 2, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(2, 3):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self._phase_delta_avg_tool_bar = Qt.QToolBar(self)
        self._phase_delta_avg_tool_bar.addWidget(Qt.QLabel("phase_delta_avg"+": "))
        self._phase_delta_avg_line_edit = Qt.QLineEdit(str(self.phase_delta_avg))
        self._phase_delta_avg_tool_bar.addWidget(self._phase_delta_avg_line_edit)
        self._phase_delta_avg_line_edit.returnPressed.connect(
        	lambda: self.set_phase_delta_avg(eng_notation.str_to_num(str(self._phase_delta_avg_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_1.addWidget(self._phase_delta_avg_tool_bar, 4, 1, 1, 1)
        for r in range(4, 5):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self._lpf_cutoff_tool_bar = Qt.QToolBar(self)
        self._lpf_cutoff_tool_bar.addWidget(Qt.QLabel('LPF Cutoff'+": "))
        self._lpf_cutoff_line_edit = Qt.QLineEdit(str(self.lpf_cutoff))
        self._lpf_cutoff_tool_bar.addWidget(self._lpf_cutoff_line_edit)
        self._lpf_cutoff_line_edit.returnPressed.connect(
        	lambda: self.set_lpf_cutoff(eng_notation.str_to_num(str(self._lpf_cutoff_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._lpf_cutoff_tool_bar, 8, 2, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 3):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.uhd_usrp_source_1 = uhd.usrp_source(
        	",".join(("addr=192.168.10.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_1.set_clock_source('gpsdo', 0)
        self.uhd_usrp_source_1.set_time_source('gpsdo', 0)
        self.uhd_usrp_source_1.set_subdev_spec('A:AB B:AB', 0)
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(usrp_tune_freq), 0)
        self.uhd_usrp_source_1.set_gain(0, 0)
        self.uhd_usrp_source_1.set_antenna('A', 0)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(usrp_tune_freq), 1)
        self.uhd_usrp_source_1.set_gain(0, 1)
        self.uhd_usrp_source_1.set_antenna('A', 1)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 1)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 1)
        self.qtgui_waterfall_sink_x_0_1 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate / decim, #bw
        	"", #name
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

        self.qtgui_waterfall_sink_x_0_1.set_intensity_range(-140, -40)

        self._qtgui_waterfall_sink_x_0_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_waterfall_sink_x_0_1_win, 4, 0, 4, 4)
        for r in range(4, 8):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_0_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate / decim, #bw
        	"", #name
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

        self.qtgui_waterfall_sink_x_0_0_0.set_intensity_range(-140, -40)

        self._qtgui_waterfall_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_waterfall_sink_x_0_0_0_win, 4, 4, 4, 4)
        for r in range(4, 8):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate / decim, #bw
        	"", #name
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

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-140, -40)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 4, 4, 4, 4)
        for r in range(4, 8):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
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

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, -40)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win, 4, 0, 4, 4)
        for r in range(4, 8):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate / decim, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.010)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1.set_y_label('PLL Freq Offset [Hz]', "")

        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1.enable_grid(True)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()

        labels = ['RHCP', 'LHCP', 'Range Delta [km]', '', '',
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
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_time_sink_x_0_1_win, 0, 4, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	8192, #size
        	samp_rate / decim, #samp_rate
        	"90 degree shift", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()

        labels = ['N/S', 'E/W', 'Delta', '', '',
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
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_0_0_win, 2, 0, 2, 4)
        for r in range(2, 4):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	8192*2, #size
        	samp_rate / decim, #samp_rate
        	"Calibration", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['N/S', 'E/W', 'Delta', '', '',
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
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_0_win, 0, 0, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            2
        )
        self.qtgui_number_sink_0_0.set_update_time(0.010)
        self.qtgui_number_sink_0_0.set_title("PLL Freq Offset [Hz]")

        labels = ['RHCP', 'LHCP', 'Range Delta', '', '',
                  '', '', '', '', '']
        units = ['', '', '[km]', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(2):
            self.qtgui_number_sink_0_0.set_min(i, -1000)
            self.qtgui_number_sink_0_0.set_max(i, 1000)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_number_sink_0_0_win, 4, 6, 1, 2)
        for r in range(4, 5):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(6, 8):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate / decim / decim2, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_1_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_freq_sink_x_1_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq*0, #fc
        	samp_rate / decim, #bw
        	"RHCP", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_1.set_y_axis(-140, 0)
        self.qtgui_freq_sink_x_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1.enable_grid(True)
        self.qtgui_freq_sink_x_0_1.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_freq_sink_x_0_1_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq*0, #fc
        	samp_rate / decim, #bw
        	"LHCP", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-140, 0)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_freq_sink_x_0_0_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq*0, #fc
        	samp_rate / decim, #bw
        	"East/West", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 0)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq*0, #fc
        	samp_rate / decim, #bw
        	"North/South", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 0)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
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
        self.main_tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self._phase_shift_range = Range(0, 359, 1, 90, 200)
        self._phase_shift_win = RangeWidget(self._phase_shift_range, self.set_phase_shift, 'Phase Shift [deg]', "counter_slider", float)
        self.main_tab_grid_layout_2.addWidget(self._phase_shift_win, 8, 0, 1, 2)
        for r in range(8, 9):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self._phase_deg_range = Range(0, 359, 1, 0, 200)
        self._phase_deg_win = RangeWidget(self._phase_deg_range, self.set_phase_deg, 'Phase Shift [deg]', "counter_slider", float)
        self.main_tab_grid_layout_1.addWidget(self._phase_deg_win, 4, 0, 1, 1)
        for r in range(4, 5):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.low_pass_filter_0_1_0 = filter.fir_filter_ccf(decim2, firdes.low_pass(
        	1, samp_rate / decim, pll_lpf_cut, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1 = filter.fir_filter_ccf(decim2, firdes.low_pass(
        	1, samp_rate / decim, pll_lpf_cut, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate / decim, lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate / decim, lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self._lo_freq_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._lo_freq_label_formatter = None
        else:
          self._lo_freq_label_formatter = lambda x: str(x)

        self._lo_freq_label_tool_bar.addWidget(Qt.QLabel('LO Freq [Hz]'+": "))
        self._lo_freq_label_label = Qt.QLabel(str(self._lo_freq_label_formatter(self.lo_freq_label)))
        self._lo_freq_label_tool_bar.addWidget(self._lo_freq_label_label)
        self.main_tab_grid_layout_4.addWidget(self._lo_freq_label_tool_bar, 4, 4, 1, 2)
        for r in range(4, 5):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(4, 6):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(decim, (filter_taps), lo_freq - usrp_ddc_freq, samp_rate)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(decim, (filter_taps), lo_freq - usrp_ddc_freq, samp_rate)
        self._coarse_tune_tool_bar = Qt.QToolBar(self)
        self._coarse_tune_tool_bar.addWidget(Qt.QLabel("coarse_tune"+": "))
        self._coarse_tune_line_edit = Qt.QLineEdit(str(self.coarse_tune))
        self._coarse_tune_tool_bar.addWidget(self._coarse_tune_line_edit)
        self._coarse_tune_line_edit.returnPressed.connect(
        	lambda: self.set_coarse_tune(eng_notation.str_to_num(str(self._coarse_tune_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._coarse_tune_tool_bar)
        self.blocks_sub_xx_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_multiply_const_vxx_1_1 = blocks.multiply_const_vff((samp_rate/decim/decim2/(2*math.pi), ))
        self.blocks_multiply_const_vxx_1_0_1 = blocks.multiply_const_vff((samp_rate/decim/decim2/(2*math.pi), ))
        self.blocks_multiply_const_vxx_1_0_0 = blocks.multiply_const_vcc((complex(math.cos(phase_rad2),math.sin(phase_rad2)), ))
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_vcc((complex(math.cos(phase_rad2),math.sin(phase_rad2)), ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((complex(math.cos(phase_rad),math.sin(phase_rad)), ))
        self.blocks_moving_average_xx_1 = blocks.moving_average_ff(int(pll_avg), 1.0/pll_avg, 4000, 1)
        self.blocks_moving_average_xx_0_0_0 = blocks.moving_average_ff(int(pll_avg), 1.0/pll_avg, 4000, 1)
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_ff(int(phase_delta_avg), 1.0/phase_delta_avg, 4000, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(int(phase_delta_avg), 1.0/phase_delta_avg, 4000, 1)
        self.blocks_complex_to_real_0_1 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_abs_xx_0_0 = blocks.abs_ff(1)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.analog_pll_freqdet_cf_0_0 = analog.pll_freqdet_cf(math.pi/pll_lbw, math.pi/pll_freq, -math.pi/pll_freq)
        self.analog_pll_freqdet_cf_0 = analog.pll_freqdet_cf(math.pi/pll_lbw, math.pi/pll_freq, -math.pi/pll_freq)
        self.analog_agc2_xx_1 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_1.set_max_gain(65536)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.analog_agc2_xx_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_pll_freqdet_cf_0, 0), (self.blocks_moving_average_xx_0_0_0, 0))
        self.connect((self.analog_pll_freqdet_cf_0_0, 0), (self.blocks_moving_average_xx_1, 0))
        self.connect((self.blocks_abs_xx_0, 0), (self.qtgui_time_sink_x_0_0, 2))
        self.connect((self.blocks_abs_xx_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 2))
        self.connect((self.blocks_add_xx_0, 0), (self.low_pass_filter_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_waterfall_sink_x_0_1, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.low_pass_filter_0_1_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_waterfall_sink_x_0_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.blocks_complex_to_real_0_0_0, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.blocks_complex_to_real_0_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 1))
        self.connect((self.blocks_complex_to_real_0_1, 0), (self.blocks_sub_xx_0_0, 0))
        self.connect((self.blocks_complex_to_real_0_1, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.blocks_abs_xx_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0_0, 0), (self.blocks_multiply_const_vxx_1_1, 0))
        self.connect((self.blocks_moving_average_xx_1, 0), (self.blocks_multiply_const_vxx_1_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.analog_agc2_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_complex_to_real_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_1, 0), (self.qtgui_number_sink_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_1, 0), (self.qtgui_time_sink_x_0_1, 1))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_sub_xx_0_0, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_real_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_real_0_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_const_vxx_1_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.analog_pll_freqdet_cf_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.qtgui_freq_sink_x_1_0, 0))
        self.connect((self.low_pass_filter_0_1_0, 0), (self.analog_pll_freqdet_cf_0_0, 0))
        self.connect((self.low_pass_filter_0_1_0, 0), (self.qtgui_freq_sink_x_1_0, 1))
        self.connect((self.uhd_usrp_source_1, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.uhd_usrp_source_1, 1), (self.freq_xlating_fir_filter_xxx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "x310_dualpol_phasecorrelation")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self.set_usrp_tune_freq(self.rx_freq+ self.offset_tune)
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)

    def get_offset_tune(self):
        return self.offset_tune

    def set_offset_tune(self, offset_tune):
        self.offset_tune = offset_tune
        self.set_usrp_tune_freq(self.rx_freq+ self.offset_tune)
        self.set_lo_freq(self.usrp_ddc_freq +self.coarse_tune - self.offset_tune)

    def get_usrp_tune_freq(self):
        return self.usrp_tune_freq

    def set_usrp_tune_freq(self, usrp_tune_freq):
        self.usrp_tune_freq = usrp_tune_freq
        self.set_usrp_ddc_freq(np.round(self.usrp_tune_freq/self.usrp_clk_rate* 2**32)/2**32*self.usrp_clk_rate)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.usrp_tune_freq), 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.usrp_tune_freq), 1)

    def get_usrp_clk_rate(self):
        return self.usrp_clk_rate

    def set_usrp_clk_rate(self, usrp_clk_rate):
        self.usrp_clk_rate = usrp_clk_rate
        self.set_usrp_ddc_freq(np.round(self.usrp_tune_freq/self.usrp_clk_rate* 2**32)/2**32*self.usrp_clk_rate)

    def get_usrp_ddc_freq(self):
        return self.usrp_ddc_freq

    def set_usrp_ddc_freq(self, usrp_ddc_freq):
        self.usrp_ddc_freq = usrp_ddc_freq
        self.set_lo_freq(self.usrp_ddc_freq +self.coarse_tune - self.offset_tune)
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.lo_freq - self.usrp_ddc_freq)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.lo_freq - self.usrp_ddc_freq)

    def get_coarse_tune(self):
        return self.coarse_tune

    def set_coarse_tune(self, coarse_tune):
        self.coarse_tune = coarse_tune
        self.set_lo_freq(self.usrp_ddc_freq +self.coarse_tune - self.offset_tune)
        Qt.QMetaObject.invokeMethod(self._coarse_tune_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.coarse_tune)))

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_title_str("Dual Polarization Phase Correlation, Start Time [UTC]: {:s}".format(self.ts_str))

    def get_phase_shift(self):
        return self.phase_shift

    def set_phase_shift(self, phase_shift):
        self.phase_shift = phase_shift
        self.set_phase_rad2(self.phase_shift * math.pi/180.0)

    def get_phase_deg(self):
        return self.phase_deg

    def set_phase_deg(self, phase_deg):
        self.phase_deg = phase_deg
        self.set_phase_rad(self.phase_deg * math.pi/180.0)

    def get_lo_freq(self):
        return self.lo_freq

    def set_lo_freq(self, lo_freq):
        self.lo_freq = lo_freq
        self.set_lo_freq_label(self._lo_freq_label_formatter("{:9f}".format(self.lo_freq)))
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.lo_freq - self.usrp_ddc_freq)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.lo_freq - self.usrp_ddc_freq)

    def get_title_str(self):
        return self.title_str

    def set_title_str(self, title_str):
        self.title_str = title_str

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim / self.decim2)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.low_pass_filter_0_1_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_1_1.set_k((self.samp_rate/self.decim/self.decim2/(2*math.pi), ))
        self.blocks_multiply_const_vxx_1_0_1.set_k((self.samp_rate/self.decim/self.decim2/(2*math.pi), ))

    def get_pll_lpf_cut(self):
        return self.pll_lpf_cut

    def set_pll_lpf_cut(self, pll_lpf_cut):
        self.pll_lpf_cut = pll_lpf_cut
        Qt.QMetaObject.invokeMethod(self._pll_lpf_cut_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.pll_lpf_cut)))
        self.low_pass_filter_0_1_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 1e3, firdes.WIN_HAMMING, 6.76))

    def get_pll_lbw(self):
        return self.pll_lbw

    def set_pll_lbw(self, pll_lbw):
        self.pll_lbw = pll_lbw
        Qt.QMetaObject.invokeMethod(self._pll_lbw_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.pll_lbw)))
        self.analog_pll_freqdet_cf_0_0.set_loop_bandwidth(math.pi/self.pll_lbw)
        self.analog_pll_freqdet_cf_0.set_loop_bandwidth(math.pi/self.pll_lbw)

    def get_pll_freq(self):
        return self.pll_freq

    def set_pll_freq(self, pll_freq):
        self.pll_freq = pll_freq
        Qt.QMetaObject.invokeMethod(self._pll_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.pll_freq)))
        self.analog_pll_freqdet_cf_0_0.set_max_freq(math.pi/self.pll_freq)
        self.analog_pll_freqdet_cf_0_0.set_min_freq(-math.pi/self.pll_freq)
        self.analog_pll_freqdet_cf_0.set_max_freq(math.pi/self.pll_freq)
        self.analog_pll_freqdet_cf_0.set_min_freq(-math.pi/self.pll_freq)

    def get_pll_avg(self):
        return self.pll_avg

    def set_pll_avg(self, pll_avg):
        self.pll_avg = pll_avg
        Qt.QMetaObject.invokeMethod(self._pll_avg_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.pll_avg)))
        self.blocks_moving_average_xx_1.set_length_and_scale(int(self.pll_avg), 1.0/self.pll_avg)
        self.blocks_moving_average_xx_0_0_0.set_length_and_scale(int(self.pll_avg), 1.0/self.pll_avg)

    def get_phase_rad2(self):
        return self.phase_rad2

    def set_phase_rad2(self, phase_rad2):
        self.phase_rad2 = phase_rad2
        self.blocks_multiply_const_vxx_1_0_0.set_k((complex(math.cos(self.phase_rad2),math.sin(self.phase_rad2)), ))
        self.blocks_multiply_const_vxx_1_0.set_k((complex(math.cos(self.phase_rad2),math.sin(self.phase_rad2)), ))

    def get_phase_rad(self):
        return self.phase_rad

    def set_phase_rad(self, phase_rad):
        self.phase_rad = phase_rad
        self.blocks_multiply_const_vxx_1.set_k((complex(math.cos(self.phase_rad),math.sin(self.phase_rad)), ))

    def get_phase_delta_avg(self):
        return self.phase_delta_avg

    def set_phase_delta_avg(self, phase_delta_avg):
        self.phase_delta_avg = phase_delta_avg
        Qt.QMetaObject.invokeMethod(self._phase_delta_avg_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.phase_delta_avg)))
        self.blocks_moving_average_xx_0_0.set_length_and_scale(int(self.phase_delta_avg), 1.0/self.phase_delta_avg)
        self.blocks_moving_average_xx_0.set_length_and_scale(int(self.phase_delta_avg), 1.0/self.phase_delta_avg)

    def get_lpf_cutoff(self):
        return self.lpf_cutoff

    def set_lpf_cutoff(self, lpf_cutoff):
        self.lpf_cutoff = lpf_cutoff
        Qt.QMetaObject.invokeMethod(self._lpf_cutoff_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.lpf_cutoff)))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))

    def get_lo_freq_label(self):
        return self.lo_freq_label

    def set_lo_freq_label(self, lo_freq_label):
        self.lo_freq_label = lo_freq_label
        Qt.QMetaObject.invokeMethod(self._lo_freq_label_label, "setText", Qt.Q_ARG("QString", self.lo_freq_label))

    def get_filter_taps(self):
        return self.filter_taps

    def set_filter_taps(self, filter_taps):
        self.filter_taps = filter_taps
        self.freq_xlating_fir_filter_xxx_0_0.set_taps((self.filter_taps))
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.filter_taps))

    def get_decim2(self):
        return self.decim2

    def set_decim2(self, decim2):
        self.decim2 = decim2
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim / self.decim2)
        self.blocks_multiply_const_vxx_1_1.set_k((self.samp_rate/self.decim/self.decim2/(2*math.pi), ))
        self.blocks_multiply_const_vxx_1_0_1.set_k((self.samp_rate/self.decim/self.decim2/(2*math.pi), ))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim / self.decim2)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.low_pass_filter_0_1_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_1_1.set_k((self.samp_rate/self.decim/self.decim2/(2*math.pi), ))
        self.blocks_multiply_const_vxx_1_0_1.set_k((self.samp_rate/self.decim/self.decim2/(2*math.pi), ))

    def get_c_ms(self):
        return self.c_ms

    def set_c_ms(self, c_ms):
        self.c_ms = c_ms


def main(top_block_cls=x310_dualpol_phasecorrelation, options=None):

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
