#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Wwv X310 Corr 1
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


class wwv_x310_corr_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Wwv X310 Corr 1")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Wwv X310 Corr 1")
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

        self.settings = Qt.QSettings("GNU Radio", "wwv_x310_corr_1")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.y_min = y_min = -60
        self.y_max = y_max = 0
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = ts_str
        self.samp_rate = samp_rate = 500e3
        self.rx_freq = rx_freq = 4.51e6
        self.nfft = nfft = 1024*32
        self.lpf_cutoff = lpf_cutoff = 50e3
        self.delay = delay = 0
        self.decim = decim = 1
        self.decay_rate = decay_rate = 20e-3
        self.c_ms = c_ms = 299792458

        ##################################################
        # Blocks
        ##################################################
        self.main_tab = Qt.QTabWidget()
        self.main_tab_widget_0 = Qt.QWidget()
        self.main_tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_0)
        self.main_tab_grid_layout_0 = Qt.QGridLayout()
        self.main_tab_layout_0.addLayout(self.main_tab_grid_layout_0)
        self.main_tab.addTab(self.main_tab_widget_0, 'Main')
        self.main_tab_widget_1 = Qt.QWidget()
        self.main_tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_1)
        self.main_tab_grid_layout_1 = Qt.QGridLayout()
        self.main_tab_layout_1.addLayout(self.main_tab_grid_layout_1)
        self.main_tab.addTab(self.main_tab_widget_1, 'Corr')
        self.top_grid_layout.addWidget(self.main_tab, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._y_min_tool_bar = Qt.QToolBar(self)
        self._y_min_tool_bar.addWidget(Qt.QLabel('FREQ'+": "))
        self._y_min_line_edit = Qt.QLineEdit(str(self.y_min))
        self._y_min_tool_bar.addWidget(self._y_min_line_edit)
        self._y_min_line_edit.returnPressed.connect(
        	lambda: self.set_y_min(eng_notation.str_to_num(str(self._y_min_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._y_min_tool_bar, 8, 4, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(4, 5):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self._y_max_tool_bar = Qt.QToolBar(self)
        self._y_max_tool_bar.addWidget(Qt.QLabel('FREQ'+": "))
        self._y_max_line_edit = Qt.QLineEdit(str(self.y_max))
        self._y_max_tool_bar.addWidget(self._y_max_line_edit)
        self._y_max_line_edit.returnPressed.connect(
        	lambda: self.set_y_max(eng_notation.str_to_num(str(self._y_max_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._y_max_tool_bar, 8, 5, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(5, 6):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
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
        self._lpf_cutoff_tool_bar = Qt.QToolBar(self)
        self._lpf_cutoff_tool_bar.addWidget(Qt.QLabel("lpf_cutoff"+": "))
        self._lpf_cutoff_line_edit = Qt.QLineEdit(str(self.lpf_cutoff))
        self._lpf_cutoff_tool_bar.addWidget(self._lpf_cutoff_line_edit)
        self._lpf_cutoff_line_edit.returnPressed.connect(
        	lambda: self.set_lpf_cutoff(eng_notation.str_to_num(str(self._lpf_cutoff_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_0.addWidget(self._lpf_cutoff_tool_bar, 8, 3, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(3, 4):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self._delay_tool_bar = Qt.QToolBar(self)
        self._delay_tool_bar.addWidget(Qt.QLabel('corr_delay'+": "))
        self._delay_line_edit = Qt.QLineEdit(str(self.delay))
        self._delay_tool_bar.addWidget(self._delay_line_edit)
        self._delay_line_edit.returnPressed.connect(
        	lambda: self.set_delay(eng_notation.str_to_num(str(self._delay_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_1.addWidget(self._delay_tool_bar, 8, 0, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
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
        self.main_tab_grid_layout_0.addWidget(self._decay_rate_group_box, 8, 2, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 3):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Start Time [UTC]'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.main_tab_grid_layout_0.addWidget(self._variable_qtgui_label_0_tool_bar, 8, 6, 1, 2)
        for r in range(8, 9):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(6, 8):
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
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	10, #size
        	samp_rate/decim, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0_0.set_y_axis(-20, 20)

        self.qtgui_time_sink_x_0_0.set_y_label('Range Delta [km]', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

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
        self.main_tab_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_0_win, 4, 0, 2, 4)
        for r in range(4, 6):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	nfft, #size
        	samp_rate/decim, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Correlation', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
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
        self.main_tab_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            3
        )
        self.qtgui_number_sink_0.set_update_time(0.010)
        self.qtgui_number_sink_0.set_title("")

        labels = ['Delay', '', 'Range Delta', '', '',
                  '', '', '', '', '']
        units = ['[usec]', '', '[km]', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(3):
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
        self.main_tab_grid_layout_1.addWidget(self._qtgui_number_sink_0_win, 6, 0, 1, 2)
        for r in range(6, 7):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_0_0 = qtgui.histogram_sink_f(
        	20,
        	1000,
                0,
                100e4,
        	"",
        	1
        )

        self.qtgui_histogram_sink_x_0_0.set_update_time(0.010)
        self.qtgui_histogram_sink_x_0_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0_0.enable_accumulate(True)
        self.qtgui_histogram_sink_x_0_0.enable_grid(False)
        self.qtgui_histogram_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_histogram_sink_x_0_0.disable_legend()

        labels = ['Correlation Magnitude', 'Corr Mag', '', '', '',
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
        self.main_tab_grid_layout_1.addWidget(self._qtgui_histogram_sink_x_0_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_0 = qtgui.histogram_sink_f(
        	20,
        	2000,
                -25*1/(samp_rate/decim) *c_ms / 1000.0,
                25*1/(samp_rate/decim) *c_ms / 1000.0,
        	"",
        	1
        )

        self.qtgui_histogram_sink_x_0.set_update_time(0.010)
        self.qtgui_histogram_sink_x_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0.enable_accumulate(True)
        self.qtgui_histogram_sink_x_0.enable_grid(False)
        self.qtgui_histogram_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_histogram_sink_x_0.disable_legend()

        labels = ['Range Delta [km]', 'Corr Mag', '', '', '',
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
        self.main_tab_grid_layout_1.addWidget(self._qtgui_histogram_sink_x_0_win, 4, 4, 2, 4)
        for r in range(4, 6):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate /decim, #bw
        	"E/W Dipole", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0.set_y_axis(y_min, y_max)
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
        for i in xrange(2):
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
        	rx_freq, #fc
        	samp_rate / decim, #bw
        	"N/S Dipole", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(y_min, y_max)
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
        self.low_pass_filter_1 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/decim, lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/decim, lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.fft_vxx_2 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 4)
        self.fft_vxx_1 = fft.fft_vcc(nfft, False, (window.blackmanharris(nfft)), False, 4)
        self.fft_vxx_0 = fft.fft_vcc(nfft, False, (window.blackmanharris(nfft)), False, 4)
        self.blocks_vector_to_stream_1 = blocks.vector_to_stream(gr.sizeof_float*1, nfft)
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((1/(samp_rate/decim) *c_ms / 1000.0, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((1/(samp_rate/decim) * 1e6, ))
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(nfft)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(10, .1, 4000, 1)
        self.blocks_max_xx_0 = blocks.max_ff(nfft,1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, int(delay))
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(nfft)
        self.blocks_argmax_xx_0 = blocks.argmax_fs(nfft)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-nfft/2.0, ))
        self.analog_agc2_xx_0_0 = analog.agc2_cc(decay_rate, decay_rate, 1.0, .5)
        self.analog_agc2_xx_0_0.set_max_gain(65536)
        self.analog_agc2_xx_0 = analog.agc2_cc(decay_rate, decay_rate, 1.0, .5)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.analog_agc2_xx_0_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_argmax_xx_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_argmax_xx_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_argmax_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_max_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_vector_to_stream_1, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_stream_to_vector_1, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.qtgui_histogram_sink_x_0_0, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.qtgui_number_sink_0, 1))
        self.connect((self.blocks_max_xx_0, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_histogram_sink_x_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_number_sink_0, 2))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.fft_vxx_2, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_1, 0), (self.fft_vxx_1, 0))
        self.connect((self.blocks_vector_to_stream_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.fft_vxx_1, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.fft_vxx_2, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.low_pass_filter_1, 0), (self.qtgui_freq_sink_x_0_0, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.uhd_usrp_source_1, 1), (self.analog_agc2_xx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "wwv_x310_corr_1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.ts_str))

    def get_y_min(self):
        return self.y_min

    def set_y_min(self, y_min):
        self.y_min = y_min
        Qt.QMetaObject.invokeMethod(self._y_min_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.y_min)))
        self.qtgui_freq_sink_x_0_0.set_y_axis(self.y_min, self.y_max)
        self.qtgui_freq_sink_x_0.set_y_axis(self.y_min, self.y_max)

    def get_y_max(self):
        return self.y_max

    def set_y_max(self, y_max):
        self.y_max = y_max
        Qt.QMetaObject.invokeMethod(self._y_max_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.y_max)))
        self.qtgui_freq_sink_x_0_0.set_y_axis(self.y_min, self.y_max)
        self.qtgui_freq_sink_x_0.set_y_axis(self.y_min, self.y_max)

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate/self.decim)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate/self.decim)
        self.qtgui_histogram_sink_x_0.set_x_axis(-25*1/(self.samp_rate/self.decim) *self.c_ms / 1000.0, 25*1/(self.samp_rate/self.decim) *self.c_ms / 1000.0)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate /self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_0_0.set_k((1/(self.samp_rate/self.decim) *self.c_ms / 1000.0, ))
        self.blocks_multiply_const_vxx_0.set_k((1/(self.samp_rate/self.decim) * 1e6, ))

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq), 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq), 1)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate /self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)

    def get_nfft(self):
        return self.nfft

    def set_nfft(self, nfft):
        self.nfft = nfft
        self.blocks_add_const_vxx_0.set_k((-self.nfft/2.0, ))

    def get_lpf_cutoff(self):
        return self.lpf_cutoff

    def set_lpf_cutoff(self, lpf_cutoff):
        self.lpf_cutoff = lpf_cutoff
        Qt.QMetaObject.invokeMethod(self._lpf_cutoff_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.lpf_cutoff)))
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))

    def get_delay(self):
        return self.delay

    def set_delay(self, delay):
        self.delay = delay
        Qt.QMetaObject.invokeMethod(self._delay_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.delay)))
        self.blocks_delay_0.set_dly(int(self.delay))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate/self.decim)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate/self.decim)
        self.qtgui_histogram_sink_x_0.set_x_axis(-25*1/(self.samp_rate/self.decim) *self.c_ms / 1000.0, 25*1/(self.samp_rate/self.decim) *self.c_ms / 1000.0)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate /self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_0_0.set_k((1/(self.samp_rate/self.decim) *self.c_ms / 1000.0, ))
        self.blocks_multiply_const_vxx_0.set_k((1/(self.samp_rate/self.decim) * 1e6, ))

    def get_decay_rate(self):
        return self.decay_rate

    def set_decay_rate(self, decay_rate):
        self.decay_rate = decay_rate
        self._decay_rate_callback(self.decay_rate)
        self.analog_agc2_xx_0_0.set_attack_rate(self.decay_rate)
        self.analog_agc2_xx_0_0.set_decay_rate(self.decay_rate)
        self.analog_agc2_xx_0.set_attack_rate(self.decay_rate)
        self.analog_agc2_xx_0.set_decay_rate(self.decay_rate)

    def get_c_ms(self):
        return self.c_ms

    def set_c_ms(self, c_ms):
        self.c_ms = c_ms
        self.qtgui_histogram_sink_x_0.set_x_axis(-25*1/(self.samp_rate/self.decim) *self.c_ms / 1000.0, 25*1/(self.samp_rate/self.decim) *self.c_ms / 1000.0)
        self.blocks_multiply_const_vxx_0_0.set_k((1/(self.samp_rate/self.decim) *self.c_ms / 1000.0, ))


def main(top_block_cls=wwv_x310_corr_1, options=None):

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
