#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: WWV Monitor X310, Start Time [UTC]: 2020-07-15T03:24:49.649869Z
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
from datetime import datetime as dt; import string; import math
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


class wwv_monitor_x310_2(gr.top_block, Qt.QWidget):

    def __init__(self, avg_len=128, nfft=2048):
        gr.top_block.__init__(self, "WWV Monitor X310, Start Time [UTC]: 2020-07-15T03:24:49.649869Z")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("WWV Monitor X310, Start Time [UTC]: 2020-07-15T03:24:49.649869Z")
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

        self.settings = Qt.QSettings("GNU Radio", "wwv_monitor_x310_2")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.avg_len = avg_len
        self.nfft = nfft

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.variable_qtgui_label_0_0 = variable_qtgui_label_0_0 = ts_str
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = ts_str
        self.title_str = title_str = "WWV Monitor X310, Start Time [UTC]: {:s}".format(ts_str)
        self.samp_rate = samp_rate = 250e3
        self.rx_freq = rx_freq = 15e6
        self.pll_lbw = pll_lbw = 200
        self.pll_freq = pll_freq = 100
        self.pll_avg = pll_avg = 100000
        self.decim_2 = decim_2 = 10
        self.decim = decim = 10
        self.decay_rate = decay_rate = 100e-6
        self.arg_avg = arg_avg = 100000

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
        self.main_tab.addTab(self.main_tab_widget_2, 'Freq')
        self.main_tab_widget_3 = Qt.QWidget()
        self.main_tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_3)
        self.main_tab_grid_layout_3 = Qt.QGridLayout()
        self.main_tab_layout_3.addLayout(self.main_tab_grid_layout_3)
        self.main_tab.addTab(self.main_tab_widget_3, 'Phase')
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
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('FREQ'+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._rx_freq_tool_bar, 1, 0, 1, 1)
        for r in range(1, 2):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self._pll_lbw_tool_bar = Qt.QToolBar(self)
        self._pll_lbw_tool_bar.addWidget(Qt.QLabel("pll_lbw"+": "))
        self._pll_lbw_line_edit = Qt.QLineEdit(str(self.pll_lbw))
        self._pll_lbw_tool_bar.addWidget(self._pll_lbw_line_edit)
        self._pll_lbw_line_edit.returnPressed.connect(
        	lambda: self.set_pll_lbw(eng_notation.str_to_num(str(self._pll_lbw_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_2.addWidget(self._pll_lbw_tool_bar, 5, 7, 1, 1)
        for r in range(5, 6):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(7, 8):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self._pll_freq_tool_bar = Qt.QToolBar(self)
        self._pll_freq_tool_bar.addWidget(Qt.QLabel("pll_freq"+": "))
        self._pll_freq_line_edit = Qt.QLineEdit(str(self.pll_freq))
        self._pll_freq_tool_bar.addWidget(self._pll_freq_line_edit)
        self._pll_freq_line_edit.returnPressed.connect(
        	lambda: self.set_pll_freq(eng_notation.str_to_num(str(self._pll_freq_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_2.addWidget(self._pll_freq_tool_bar, 5, 6, 1, 1)
        for r in range(5, 6):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(6, 7):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self._pll_avg_tool_bar = Qt.QToolBar(self)
        self._pll_avg_tool_bar.addWidget(Qt.QLabel("pll_avg"+": "))
        self._pll_avg_line_edit = Qt.QLineEdit(str(self.pll_avg))
        self._pll_avg_tool_bar.addWidget(self._pll_avg_line_edit)
        self._pll_avg_line_edit.returnPressed.connect(
        	lambda: self.set_pll_avg(eng_notation.str_to_num(str(self._pll_avg_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_2.addWidget(self._pll_avg_tool_bar, 6, 6, 1, 1)
        for r in range(6, 7):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(6, 7):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self._decay_rate_options = (100e-6, 65e-3, 20e-3, )
        self._decay_rate_labels = ('Fast', 'Medium', 'Slow', )
        self._decay_rate_group_box = Qt.QGroupBox("decay_rate")
        self._decay_rate_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._decay_rate_button_group = variable_chooser_button_group()
        self._decay_rate_group_box.setLayout(self._decay_rate_box)
        for i, label in enumerate(self._decay_rate_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._decay_rate_box.addWidget(radio_button)
        	self._decay_rate_button_group.addButton(radio_button, i)
        self._decay_rate_callback = lambda i: Qt.QMetaObject.invokeMethod(self._decay_rate_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._decay_rate_options.index(i)))
        self._decay_rate_callback(self.decay_rate)
        self._decay_rate_button_group.buttonClicked[int].connect(
        	lambda i: self.set_decay_rate(self._decay_rate_options[i]))
        self.main_tab_grid_layout_0.addWidget(self._decay_rate_group_box, 3, 0, 1, 1)
        for r in range(3, 4):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self._arg_avg_tool_bar = Qt.QToolBar(self)
        self._arg_avg_tool_bar.addWidget(Qt.QLabel("arg_avg"+": "))
        self._arg_avg_line_edit = Qt.QLineEdit(str(self.arg_avg))
        self._arg_avg_tool_bar.addWidget(self._arg_avg_line_edit)
        self._arg_avg_line_edit.returnPressed.connect(
        	lambda: self.set_arg_avg(eng_notation.str_to_num(str(self._arg_avg_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_3.addWidget(self._arg_avg_tool_bar, 6, 6, 1, 1)
        for r in range(6, 7):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(6, 7):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_0_formatter = None
        else:
          self._variable_qtgui_label_0_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_0_tool_bar.addWidget(Qt.QLabel('Start Time [UTC]'+": "))
        self._variable_qtgui_label_0_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_0_formatter(self.variable_qtgui_label_0_0)))
        self._variable_qtgui_label_0_0_tool_bar.addWidget(self._variable_qtgui_label_0_0_label)
        self.main_tab_grid_layout_0.addWidget(self._variable_qtgui_label_0_0_tool_bar, 4, 0, 10, 1)
        for r in range(4, 14):
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
        self.uhd_usrp_source_1 = uhd.usrp_source(
        	",".join(("addr=192.168.10.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_1.set_clock_rate(200e6, uhd.ALL_MBOARDS)
        self.uhd_usrp_source_1.set_clock_source('gpsdo', 0)
        self.uhd_usrp_source_1.set_time_source('gpsdo', 0)
        self.uhd_usrp_source_1.set_subdev_spec('A:AB B:AB', 0)
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(rx_freq), 0)
        self.uhd_usrp_source_1.set_gain(0, 0)
        self.uhd_usrp_source_1.set_antenna('A', 0)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(rx_freq), 1)
        self.uhd_usrp_source_1.set_gain(0, 1)
        self.uhd_usrp_source_1.set_antenna('A', 1)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 1)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 1)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	8192, #size
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

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-120, 0)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 4, 4, 4, 4)
        for r in range(4, 8):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	8192, #size
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

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-120, 0)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_waterfall_sink_x_0_win, 4, 0, 4, 4)
        for r in range(4, 8):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate / decim, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0_0.set_y_axis(-.2, .2)

        self.qtgui_time_sink_x_0_0.set_y_label('PLL Freq Offset [Hz]', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

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
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_0_win, 0, 0, 1, 6)
        for r in range(0, 1):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 6):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate / decim, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('PLL Freq Offset [Hz]', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
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
        self.main_tab_grid_layout_2.addWidget(self._qtgui_time_sink_x_0_win, 4, 0, 3, 6)
        for r in range(4, 7):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 6):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            2
        )
        self.qtgui_number_sink_0_0.set_update_time(0.010)
        self.qtgui_number_sink_0_0.set_title("PLL Freq Offset [Hz]")

        labels = ['North/South', 'East/West', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
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
        self.main_tab_grid_layout_2.addWidget(self._qtgui_number_sink_0_0_win, 4, 6, 1, 2)
        for r in range(4, 5):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(6, 8):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
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
        self.main_tab_grid_layout_2.addWidget(self._qtgui_number_sink_0_win, 8, 4, 1, 2)
        for r in range(8, 9):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 6):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq*0, #fc
        	samp_rate / decim / decim_2, #bw
        	"North/South", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_1.set_y_axis(-100, -20)
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
        	samp_rate /decim / decim_2, #bw
        	"East/West", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-100, -20)
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
        	samp_rate /decim, #bw
        	"East/West", #name
        	1 #number of inputs
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
        self.main_tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq*0, #fc
        	samp_rate / decim, #bw
        	"North/South", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-100, -20)
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
        self.main_tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	8192, #size
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.010)
        self.qtgui_const_sink_x_0.set_y_axis(-.2, .2)
        self.qtgui_const_sink_x_0.set_x_axis(-.2, .2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_3.addWidget(self._qtgui_const_sink_x_0_win, 1, 0, 3, 3)
        for r in range(1, 4):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 3):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self.low_pass_filter_1_0 = filter.fir_filter_ccf(decim_2, firdes.low_pass(
        	1, samp_rate / decim, 50, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_1 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate / decim, 50, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(decim_2, firdes.low_pass(
        	1, samp_rate / decim, 50, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate / decim, 50, 100, firdes.WIN_HAMMING, 6.76))
        self.fft_vxx_0 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), False, 4)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, nfft, -10*math.log10(nfft))
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_vff((samp_rate/decim/(2*math.pi), ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((samp_rate/decim/(2*math.pi), ))
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff(((samp_rate / decim / decim_2) / nfft, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff(((samp_rate / decim / decim_2) / nfft, ))
        self.blocks_moving_average_xx_1_0_0 = blocks.moving_average_ff(int(arg_avg), 1.0/arg_avg, 4000, 1)
        self.blocks_moving_average_xx_1_0 = blocks.moving_average_ff(int(arg_avg), 1.0/arg_avg, 4000, 1)
        self.blocks_moving_average_xx_1 = blocks.moving_average_ff(100000, 0.00001, 4000, 1)
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_ff(int(pll_avg), 1.0/pll_avg, 4000, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(int(avg_len), 1.0/(avg_len)/nfft, 4000, nfft)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(nfft)
        self.blocks_complex_to_arg_0_0 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.blocks_argmax_xx_0 = blocks.argmax_fs(nfft)
        self.analog_pll_freqdet_cf_0_0 = analog.pll_freqdet_cf(math.pi/pll_lbw, math.pi/pll_freq, -math.pi/pll_freq)
        self.analog_pll_freqdet_cf_0 = analog.pll_freqdet_cf(math.pi/pll_lbw, math.pi/pll_freq, -math.pi/pll_freq)
        self.analog_agc2_xx_0_0 = analog.agc2_cc(0.1, decay_rate, .3, 1000)
        self.analog_agc2_xx_0_0.set_max_gain(65000)
        self.analog_agc2_xx_0 = analog.agc2_cc(0.1, decay_rate, .3, 1000)
        self.analog_agc2_xx_0.set_max_gain(65000)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.analog_agc2_xx_0_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.analog_pll_freqdet_cf_0, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.analog_pll_freqdet_cf_0_0, 0), (self.blocks_moving_average_xx_1, 0))
        self.connect((self.blocks_argmax_xx_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_argmax_xx_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_moving_average_xx_1_0_0, 0))
        self.connect((self.blocks_complex_to_arg_0_0, 0), (self.blocks_moving_average_xx_1_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_moving_average_xx_1, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.blocks_moving_average_xx_1_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_moving_average_xx_1_0_0, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.qtgui_number_sink_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_argmax_xx_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_pll_freqdet_cf_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.analog_pll_freqdet_cf_0, 0))
        self.connect((self.low_pass_filter_1_0, 0), (self.qtgui_freq_sink_x_0_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_const_sink_x_0, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_complex_to_arg_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.low_pass_filter_1_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.uhd_usrp_source_1, 1), (self.analog_agc2_xx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "wwv_monitor_x310_2")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_avg_len(self):
        return self.avg_len

    def set_avg_len(self, avg_len):
        self.avg_len = avg_len
        self.blocks_moving_average_xx_0.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/self.nfft)

    def get_nfft(self):
        return self.nfft

    def set_nfft(self, nfft):
        self.nfft = nfft
        self.blocks_multiply_const_vxx_0_0_0.set_k(((self.samp_rate / self.decim / self.decim_2) / self.nfft, ))
        self.blocks_multiply_const_vxx_0_0.set_k(((self.samp_rate / self.decim / self.decim_2) / self.nfft, ))
        self.blocks_moving_average_xx_0.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/self.nfft)

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_variable_qtgui_label_0_0(self._variable_qtgui_label_0_0_formatter(self.ts_str))
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.ts_str))
        self.set_title_str("WWV Monitor X310, Start Time [UTC]: {:s}".format(self.ts_str))

    def get_variable_qtgui_label_0_0(self):
        return self.variable_qtgui_label_0_0

    def set_variable_qtgui_label_0_0(self, variable_qtgui_label_0_0):
        self.variable_qtgui_label_0_0 = variable_qtgui_label_0_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0_0))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

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
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim / self.decim_2)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate /self.decim / self.decim_2)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate /self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.low_pass_filter_1_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, 50, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, 50, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, 50, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, 50, 100, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_1_0.set_k((self.samp_rate/self.decim/(2*math.pi), ))
        self.blocks_multiply_const_vxx_1.set_k((self.samp_rate/self.decim/(2*math.pi), ))
        self.blocks_multiply_const_vxx_0_0_0.set_k(((self.samp_rate / self.decim / self.decim_2) / self.nfft, ))
        self.blocks_multiply_const_vxx_0_0.set_k(((self.samp_rate / self.decim / self.decim_2) / self.nfft, ))

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq), 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq), 1)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim / self.decim_2)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate /self.decim / self.decim_2)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate /self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)

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
        self.blocks_moving_average_xx_0_0.set_length_and_scale(int(self.pll_avg), 1.0/self.pll_avg)

    def get_decim_2(self):
        return self.decim_2

    def set_decim_2(self, decim_2):
        self.decim_2 = decim_2
        self.qtgui_freq_sink_x_0_1.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim / self.decim_2)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate /self.decim / self.decim_2)
        self.blocks_multiply_const_vxx_0_0_0.set_k(((self.samp_rate / self.decim / self.decim_2) / self.nfft, ))
        self.blocks_multiply_const_vxx_0_0.set_k(((self.samp_rate / self.decim / self.decim_2) / self.nfft, ))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim / self.decim_2)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate /self.decim / self.decim_2)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate /self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.low_pass_filter_1_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, 50, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, 50, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, 50, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, 50, 100, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_1_0.set_k((self.samp_rate/self.decim/(2*math.pi), ))
        self.blocks_multiply_const_vxx_1.set_k((self.samp_rate/self.decim/(2*math.pi), ))
        self.blocks_multiply_const_vxx_0_0_0.set_k(((self.samp_rate / self.decim / self.decim_2) / self.nfft, ))
        self.blocks_multiply_const_vxx_0_0.set_k(((self.samp_rate / self.decim / self.decim_2) / self.nfft, ))

    def get_decay_rate(self):
        return self.decay_rate

    def set_decay_rate(self, decay_rate):
        self.decay_rate = decay_rate
        self._decay_rate_callback(self.decay_rate)
        self.analog_agc2_xx_0_0.set_decay_rate(self.decay_rate)
        self.analog_agc2_xx_0.set_decay_rate(self.decay_rate)

    def get_arg_avg(self):
        return self.arg_avg

    def set_arg_avg(self, arg_avg):
        self.arg_avg = arg_avg
        Qt.QMetaObject.invokeMethod(self._arg_avg_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.arg_avg)))
        self.blocks_moving_average_xx_1_0_0.set_length_and_scale(int(self.arg_avg), 1.0/self.arg_avg)
        self.blocks_moving_average_xx_1_0.set_length_and_scale(int(self.arg_avg), 1.0/self.arg_avg)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--avg-len", dest="avg_len", type="eng_float", default=eng_notation.num_to_str(128),
        help="Set avg_len [default=%default]")
    parser.add_option(
        "", "--nfft", dest="nfft", type="intx", default=2048,
        help="Set nfft [default=%default]")
    return parser


def main(top_block_cls=wwv_monitor_x310_2, options=None):
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
