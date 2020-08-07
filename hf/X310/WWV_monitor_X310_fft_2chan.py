#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: WWV Monitor X310, Start Time [UTC]: 2020-07-15T03:27:25.430442Z
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
from PyQt4.QtCore import QObject, pyqtSlot
from datetime import datetime as dt; import string; import math; import numpy as np
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import time
from gnuradio import qtgui


class WWV_monitor_X310_fft_2chan(gr.top_block, Qt.QWidget):

    def __init__(self, avg_len=1, nfft=2048*8):
        gr.top_block.__init__(self, "WWV Monitor X310, Start Time [UTC]: 2020-07-15T03:27:25.430442Z")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("WWV Monitor X310, Start Time [UTC]: 2020-07-15T03:27:25.430442Z")
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

        self.settings = Qt.QSettings("GNU Radio", "WWV_monitor_X310_fft_2chan")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.avg_len = avg_len
        self.nfft = nfft

        ##################################################
        # Variables
        ##################################################
        self.wwv_freq = wwv_freq = 10e6
        self.offset_tune = offset_tune = -10e3
        self.usrp_tune_freq = usrp_tune_freq = wwv_freq + offset_tune
        self.usrp_clk_rate = usrp_clk_rate = 200e6
        self.usrp_ddc_freq = usrp_ddc_freq = np.round(usrp_tune_freq/usrp_clk_rate* 2**32)/2**32*usrp_clk_rate
        self.coarse_tune = coarse_tune = 0
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.samp_rate = samp_rate = 250e3
        self.lo_freq = lo_freq = usrp_ddc_freq +coarse_tune - offset_tune
        self.decim_2 = decim_2 = 10
        self.decim = decim = 10
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = ts_str
        self.title_str = title_str = "WWV Monitor X310, Start Time [UTC]: {:s}".format(ts_str)
        self.lo_freq_label = lo_freq_label = "{:9f}".format(lo_freq)
        self.hz_per_bin = hz_per_bin = (samp_rate / decim / decim_2) / nfft
        self.filter_taps = filter_taps = firdes.low_pass(1.0, 2.5,0.1,0.02,firdes.WIN_HAMMING)
        self.decay_rate = decay_rate = 100e-6

        ##################################################
        # Blocks
        ##################################################
        self.main_tab = Qt.QTabWidget()
        self.main_tab_widget_0 = Qt.QWidget()
        self.main_tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_0)
        self.main_tab_grid_layout_0 = Qt.QGridLayout()
        self.main_tab_layout_0.addLayout(self.main_tab_grid_layout_0)
        self.main_tab.addTab(self.main_tab_widget_0, 'Controls')
        self.main_tab_widget_1 = Qt.QWidget()
        self.main_tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_1)
        self.main_tab_grid_layout_1 = Qt.QGridLayout()
        self.main_tab_layout_1.addLayout(self.main_tab_grid_layout_1)
        self.main_tab.addTab(self.main_tab_widget_1, 'NS_EW')
        self.main_tab_widget_2 = Qt.QWidget()
        self.main_tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_2)
        self.main_tab_grid_layout_2 = Qt.QGridLayout()
        self.main_tab_layout_2.addLayout(self.main_tab_grid_layout_2)
        self.main_tab.addTab(self.main_tab_widget_2, 'RHCP_LHCP')
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
        self.main_tab_grid_layout_0.addWidget(self._samp_rate_tool_bar, 2, 0, 1, 1)
        for r in range(2, 3):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self._decay_rate_options = (100e-6, 65e-3, 20e-3, )
        self._decay_rate_labels = ('Fast', 'Medium', 'Slow', )
        self._decay_rate_tool_bar = Qt.QToolBar(self)
        self._decay_rate_tool_bar.addWidget(Qt.QLabel("decay_rate"+": "))
        self._decay_rate_combo_box = Qt.QComboBox()
        self._decay_rate_tool_bar.addWidget(self._decay_rate_combo_box)
        for label in self._decay_rate_labels: self._decay_rate_combo_box.addItem(label)
        self._decay_rate_callback = lambda i: Qt.QMetaObject.invokeMethod(self._decay_rate_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._decay_rate_options.index(i)))
        self._decay_rate_callback(self.decay_rate)
        self._decay_rate_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_decay_rate(self._decay_rate_options[i]))
        self.main_tab_grid_layout_0.addWidget(self._decay_rate_tool_bar, 3, 0, 1, 1)
        for r in range(3, 4):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self._wwv_freq_options = (5e6, 10e6, 15e6, 20e6, 25e6, )
        self._wwv_freq_labels = ('5 MHz', '10 MHz', '15 MHz', '20 MHz', '25 MHz', )
        self._wwv_freq_tool_bar = Qt.QToolBar(self)
        self._wwv_freq_tool_bar.addWidget(Qt.QLabel('WWV Freq'+": "))
        self._wwv_freq_combo_box = Qt.QComboBox()
        self._wwv_freq_tool_bar.addWidget(self._wwv_freq_combo_box)
        for label in self._wwv_freq_labels: self._wwv_freq_combo_box.addItem(label)
        self._wwv_freq_callback = lambda i: Qt.QMetaObject.invokeMethod(self._wwv_freq_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._wwv_freq_options.index(i)))
        self._wwv_freq_callback(self.wwv_freq)
        self._wwv_freq_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_wwv_freq(self._wwv_freq_options[i]))
        self.main_tab_grid_layout_0.addWidget(self._wwv_freq_tool_bar, 1, 0, 1, 1)
        for r in range(1, 2):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Start Time [UTC]'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.main_tab_grid_layout_0.addWidget(self._variable_qtgui_label_0_tool_bar, 0, 0, 1, 1)
        for r in range(0, 1):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("addr=192.168.10.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_0.set_clock_rate(usrp_clk_rate, uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_clock_source('gpsdo', 0)
        self.uhd_usrp_source_0.set_time_source('gpsdo', 0)
        self.uhd_usrp_source_0.set_subdev_spec('A:AB B:AB', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_source_0.set_center_freq(usrp_tune_freq, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_antenna('A', 0)
        self.uhd_usrp_source_0.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_0.set_auto_iq_balance(True, 0)
        self.uhd_usrp_source_0.set_center_freq(usrp_tune_freq, 1)
        self.uhd_usrp_source_0.set_gain(0, 1)
        self.uhd_usrp_source_0.set_antenna('A', 1)
        self.uhd_usrp_source_0.set_auto_dc_offset(True, 1)
        self.uhd_usrp_source_0.set_auto_iq_balance(True, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	2, #size
        	samp_rate / decim/decim_2/nfft, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.0010)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Offset Freq [Hz[', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['N/S', 'E/W', '', '', '',
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
        self.main_tab_grid_layout_2.addWidget(self._qtgui_time_sink_x_0_win, 0, 0, 1, 2)
        for r in range(0, 1):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            2
        )
        self.qtgui_number_sink_0.set_update_time(0.00010)
        self.qtgui_number_sink_0.set_title("")

        labels = ['N/S Freq', 'E/W Freq', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
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

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_number_sink_0_win, 8, 0, 1, 2)
        for r in range(8, 9):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 2):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate / decim / decim_2, #bw
        	"Narrow", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-100, -20)
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
        self.main_tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	usrp_ddc_freq, #fc
        	samp_rate, #bw
        	'Channel', #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-160, -20)
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
        self.main_tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.low_pass_filter_0_1 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 100e3, 20e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_1 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate / decim, 250, 100, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0_0_0_0 = filter.fir_filter_ccf(10, firdes.low_pass(
        	1, samp_rate / decim_2, 75, 50, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0_0_0 = filter.fir_filter_ccf(10, firdes.low_pass(
        	1, samp_rate / decim_2, 75, 50, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate / decim, 250, 100, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 100e3, 20e3, firdes.WIN_HAMMING, 6.76))
        self._lo_freq_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._lo_freq_label_formatter = None
        else:
          self._lo_freq_label_formatter = lambda x: str(x)

        self._lo_freq_label_tool_bar.addWidget(Qt.QLabel('LO Freq [Hz]'+": "))
        self._lo_freq_label_label = Qt.QLabel(str(self._lo_freq_label_formatter(self.lo_freq_label)))
        self._lo_freq_label_tool_bar.addWidget(self._lo_freq_label_label)
        self.main_tab_grid_layout_0.addWidget(self._lo_freq_label_tool_bar, 4, 0, 1, 1)
        for r in range(4, 5):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(decim, (filter_taps), lo_freq - usrp_ddc_freq, samp_rate)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(decim, (filter_taps), lo_freq - usrp_ddc_freq, samp_rate)
        self.fft_vxx_0_0 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 4)
        self.fft_vxx_0 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 4)
        self._coarse_tune_tool_bar = Qt.QToolBar(self)
        self._coarse_tune_tool_bar.addWidget(Qt.QLabel("coarse_tune"+": "))
        self._coarse_tune_line_edit = Qt.QLineEdit(str(self.coarse_tune))
        self._coarse_tune_tool_bar.addWidget(self._coarse_tune_line_edit)
        self._coarse_tune_line_edit.returnPressed.connect(
        	lambda: self.set_coarse_tune(eng_notation.str_to_num(str(self._coarse_tune_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._coarse_tune_tool_bar)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_short_to_float_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, nfft, -10*math.log10(nfft))
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, nfft, -10*math.log10(nfft))
        self.blocks_multiply_const_vxx_0_0_1 = blocks.multiply_const_vff((hz_per_bin, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((hz_per_bin, ))
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(nfft)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(nfft)
        self.blocks_argmax_xx_0_0 = blocks.argmax_fs(nfft)
        self.blocks_argmax_xx_0 = blocks.argmax_fs(nfft)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vff((-samp_rate/decim/decim_2/2, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-samp_rate/decim/decim_2/2, ))
        self.analog_agc2_xx_0_0 = analog.agc2_cc(0.01, decay_rate, .3, 1000)
        self.analog_agc2_xx_0_0.set_max_gain(65000)
        self.analog_agc2_xx_0 = analog.agc2_cc(0.01, decay_rate, .3, 1000)
        self.analog_agc2_xx_0.set_max_gain(65000)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.analog_agc2_xx_0_0, 0), (self.low_pass_filter_0_0_1, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.qtgui_number_sink_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_argmax_xx_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_argmax_xx_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_argmax_xx_0_0, 1), (self.blocks_null_sink_0_0, 0))
        self.connect((self.blocks_argmax_xx_0_0, 0), (self.blocks_short_to_float_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_nlog10_ff_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_1, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_argmax_xx_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.blocks_argmax_xx_0_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_short_to_float_0_0, 0), (self.blocks_multiply_const_vxx_0_0_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_0_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.analog_agc2_xx_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.low_pass_filter_0_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.low_pass_filter_0_0_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.low_pass_filter_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_0, 1))
        self.connect((self.low_pass_filter_0_0_1, 0), (self.low_pass_filter_0_0_0_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.uhd_usrp_source_0, 1), (self.low_pass_filter_0_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "WWV_monitor_X310_fft_2chan")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_avg_len(self):
        return self.avg_len

    def set_avg_len(self, avg_len):
        self.avg_len = avg_len

    def get_nfft(self):
        return self.nfft

    def set_nfft(self, nfft):
        self.nfft = nfft
        self.set_hz_per_bin((self.samp_rate / self.decim / self.decim_2) / self.nfft)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.decim/self.decim_2/self.nfft)

    def get_wwv_freq(self):
        return self.wwv_freq

    def set_wwv_freq(self, wwv_freq):
        self.wwv_freq = wwv_freq
        self.set_usrp_tune_freq(self.wwv_freq + self.offset_tune)
        self._wwv_freq_callback(self.wwv_freq)

    def get_offset_tune(self):
        return self.offset_tune

    def set_offset_tune(self, offset_tune):
        self.offset_tune = offset_tune
        self.set_usrp_tune_freq(self.wwv_freq + self.offset_tune)
        self.set_lo_freq(self.usrp_ddc_freq +self.coarse_tune - self.offset_tune)

    def get_usrp_tune_freq(self):
        return self.usrp_tune_freq

    def set_usrp_tune_freq(self, usrp_tune_freq):
        self.usrp_tune_freq = usrp_tune_freq
        self.set_usrp_ddc_freq(np.round(self.usrp_tune_freq/self.usrp_clk_rate* 2**32)/2**32*self.usrp_clk_rate)
        self.uhd_usrp_source_0.set_center_freq(self.usrp_tune_freq, 0)
        self.uhd_usrp_source_0.set_center_freq(self.usrp_tune_freq, 1)

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
        self.qtgui_freq_sink_x_0.set_frequency_range(self.usrp_ddc_freq, self.samp_rate)
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
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.ts_str))
        self.set_title_str("WWV Monitor X310, Start Time [UTC]: {:s}".format(self.ts_str))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.set_hz_per_bin((self.samp_rate / self.decim / self.decim_2) / self.nfft)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.decim/self.decim_2/self.nfft)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate / self.decim / self.decim_2)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.usrp_ddc_freq, self.samp_rate)
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate, 100e3, 20e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0_1.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, 250, 100, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim_2, 75, 50, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim_2, 75, 50, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, 250, 100, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 100e3, 20e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_add_const_vxx_0_0.set_k((-self.samp_rate/self.decim/self.decim_2/2, ))
        self.blocks_add_const_vxx_0.set_k((-self.samp_rate/self.decim/self.decim_2/2, ))

    def get_lo_freq(self):
        return self.lo_freq

    def set_lo_freq(self, lo_freq):
        self.lo_freq = lo_freq
        self.set_lo_freq_label(self._lo_freq_label_formatter("{:9f}".format(self.lo_freq)))
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.lo_freq - self.usrp_ddc_freq)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.lo_freq - self.usrp_ddc_freq)

    def get_decim_2(self):
        return self.decim_2

    def set_decim_2(self, decim_2):
        self.decim_2 = decim_2
        self.set_hz_per_bin((self.samp_rate / self.decim / self.decim_2) / self.nfft)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.decim/self.decim_2/self.nfft)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate / self.decim / self.decim_2)
        self.low_pass_filter_0_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim_2, 75, 50, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim_2, 75, 50, firdes.WIN_BLACKMAN, 6.76))
        self.blocks_add_const_vxx_0_0.set_k((-self.samp_rate/self.decim/self.decim_2/2, ))
        self.blocks_add_const_vxx_0.set_k((-self.samp_rate/self.decim/self.decim_2/2, ))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_hz_per_bin((self.samp_rate / self.decim / self.decim_2) / self.nfft)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.decim/self.decim_2/self.nfft)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate / self.decim / self.decim_2)
        self.low_pass_filter_0_0_1.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, 250, 100, firdes.WIN_BLACKMAN, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, 250, 100, firdes.WIN_BLACKMAN, 6.76))
        self.blocks_add_const_vxx_0_0.set_k((-self.samp_rate/self.decim/self.decim_2/2, ))
        self.blocks_add_const_vxx_0.set_k((-self.samp_rate/self.decim/self.decim_2/2, ))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_title_str(self):
        return self.title_str

    def set_title_str(self, title_str):
        self.title_str = title_str

    def get_lo_freq_label(self):
        return self.lo_freq_label

    def set_lo_freq_label(self, lo_freq_label):
        self.lo_freq_label = lo_freq_label
        Qt.QMetaObject.invokeMethod(self._lo_freq_label_label, "setText", Qt.Q_ARG("QString", self.lo_freq_label))

    def get_hz_per_bin(self):
        return self.hz_per_bin

    def set_hz_per_bin(self, hz_per_bin):
        self.hz_per_bin = hz_per_bin
        self.blocks_multiply_const_vxx_0_0_1.set_k((self.hz_per_bin, ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.hz_per_bin, ))

    def get_filter_taps(self):
        return self.filter_taps

    def set_filter_taps(self, filter_taps):
        self.filter_taps = filter_taps
        self.freq_xlating_fir_filter_xxx_0_0.set_taps((self.filter_taps))
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.filter_taps))

    def get_decay_rate(self):
        return self.decay_rate

    def set_decay_rate(self, decay_rate):
        self.decay_rate = decay_rate
        self._decay_rate_callback(self.decay_rate)
        self.analog_agc2_xx_0_0.set_decay_rate(self.decay_rate)
        self.analog_agc2_xx_0.set_decay_rate(self.decay_rate)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--avg-len", dest="avg_len", type="eng_float", default=eng_notation.num_to_str(1),
        help="Set avg_len [default=%default]")
    parser.add_option(
        "", "--nfft", dest="nfft", type="intx", default=2048*8,
        help="Set nfft [default=%default]")
    return parser


def main(top_block_cls=WWV_monitor_X310_fft_2chan, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(avg_len=options.avg_len, nfft=options.nfft)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
