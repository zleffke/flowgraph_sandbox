#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Hf Spectrum Simple
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
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import time
from gnuradio import qtgui


class hf_spectrum_simple(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Hf Spectrum Simple")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Hf Spectrum Simple")
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

        self.settings = Qt.QSettings("GNU Radio", "hf_spectrum_simple")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.y_min = y_min = -140
        self.y_max = y_max = -60
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = ts_str
        self.samp_rate = samp_rate = .5e6
        self.rx_freq = rx_freq = 5e6
        self.decim = decim = 10
        self.decay_rate = decay_rate = 20e-3
        self.ahfd_ant = ahfd_ant = 'A'

        ##################################################
        # Blocks
        ##################################################
        self._y_min_tool_bar = Qt.QToolBar(self)
        self._y_min_tool_bar.addWidget(Qt.QLabel('FREQ'+": "))
        self._y_min_line_edit = Qt.QLineEdit(str(self.y_min))
        self._y_min_tool_bar.addWidget(self._y_min_line_edit)
        self._y_min_line_edit.returnPressed.connect(
        	lambda: self.set_y_min(eng_notation.str_to_num(str(self._y_min_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._y_min_tool_bar, 8, 4, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._y_max_tool_bar = Qt.QToolBar(self)
        self._y_max_tool_bar.addWidget(Qt.QLabel('FREQ'+": "))
        self._y_max_line_edit = Qt.QLineEdit(str(self.y_max))
        self._y_max_tool_bar.addWidget(self._y_max_line_edit)
        self._y_max_line_edit.returnPressed.connect(
        	lambda: self.set_y_max(eng_notation.str_to_num(str(self._y_max_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._y_max_tool_bar, 8, 5, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel('SAMP_RATE'+": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._samp_rate_tool_bar, 8, 0, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('FREQ'+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_freq_tool_bar, 8, 1, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._ahfd_ant_options = ('A', 'B', )
        self._ahfd_ant_labels = ('N/S', 'E/W', )
        self._ahfd_ant_tool_bar = Qt.QToolBar(self)
        self._ahfd_ant_tool_bar.addWidget(Qt.QLabel('AHFD Ant'+": "))
        self._ahfd_ant_combo_box = Qt.QComboBox()
        self._ahfd_ant_tool_bar.addWidget(self._ahfd_ant_combo_box)
        for label in self._ahfd_ant_labels: self._ahfd_ant_combo_box.addItem(label)
        self._ahfd_ant_callback = lambda i: Qt.QMetaObject.invokeMethod(self._ahfd_ant_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._ahfd_ant_options.index(i)))
        self._ahfd_ant_callback(self.ahfd_ant)
        self._ahfd_ant_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_ahfd_ant(self._ahfd_ant_options[i]))
        self.top_grid_layout.addWidget(self._ahfd_ant_tool_bar, 8, 3, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Start Time [UTC]'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_tool_bar, 8, 6, 1, 2)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self.uhd_usrp_source_1.set_antenna(ahfd_ant, 1)
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
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 4, 4, 4, 4)
        for r in range(4, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 4, 0, 4, 4)
        for r in range(4, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate /decim, #bw
        	"E/W Dipole", #name
        	1 #number of inputs
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
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate / decim, #bw
        	"N/S Dipole", #name
        	1 #number of inputs
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
        self.top_grid_layout.addWidget(self._decay_rate_group_box, 8, 2, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_1, 1), (self.rational_resampler_xxx_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.rational_resampler_xxx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "hf_spectrum_simple")
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
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate /self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)

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

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate /self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)

    def get_decay_rate(self):
        return self.decay_rate

    def set_decay_rate(self, decay_rate):
        self.decay_rate = decay_rate
        self._decay_rate_callback(self.decay_rate)

    def get_ahfd_ant(self):
        return self.ahfd_ant

    def set_ahfd_ant(self, ahfd_ant):
        self.ahfd_ant = ahfd_ant
        self._ahfd_ant_callback(self.ahfd_ant)
        self.uhd_usrp_source_1.set_antenna(self.ahfd_ant, 1)


def main(top_block_cls=hf_spectrum_simple, options=None):

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
