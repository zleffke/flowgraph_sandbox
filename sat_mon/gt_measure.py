#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Gt Measure
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
from gnuradio import blocks
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


class gt_measure(gr.top_block, Qt.QWidget):

    def __init__(self, decim=2, nfft=2048):
        gr.top_block.__init__(self, "Gt Measure")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Gt Measure")
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

        self.settings = Qt.QSettings("GNU Radio", "gt_measure")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.decim = decim
        self.nfft = nfft

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 4e6
        self.rx_gain = rx_gain = 10
        self.rx_freq = rx_freq = 2271.2e6
        self.keep_n = keep_n = 1
        self.fft_min = fft_min = -120
        self.fft_max = fft_max = -80
        self.avg_length = avg_length = 1000.0
        self.alpha = alpha = 100e-9

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel('SAMP_RATE'+": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._samp_rate_tool_bar, 9, 0, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel('GAIN'+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_gain_tool_bar, 9, 2, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('FREQ'+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_freq_tool_bar, 9, 1, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._keep_n_tool_bar = Qt.QToolBar(self)
        self._keep_n_tool_bar.addWidget(Qt.QLabel('keep_n'+": "))
        self._keep_n_line_edit = Qt.QLineEdit(str(self.keep_n))
        self._keep_n_tool_bar.addWidget(self._keep_n_line_edit)
        self._keep_n_line_edit.returnPressed.connect(
        	lambda: self.set_keep_n(eng_notation.str_to_num(str(self._keep_n_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._keep_n_tool_bar, 10, 3, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._fft_min_tool_bar = Qt.QToolBar(self)
        self._fft_min_tool_bar.addWidget(Qt.QLabel('fft_min'+": "))
        self._fft_min_line_edit = Qt.QLineEdit(str(self.fft_min))
        self._fft_min_tool_bar.addWidget(self._fft_min_line_edit)
        self._fft_min_line_edit.returnPressed.connect(
        	lambda: self.set_fft_min(eng_notation.str_to_num(str(self._fft_min_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._fft_min_tool_bar, 10, 1, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._fft_max_tool_bar = Qt.QToolBar(self)
        self._fft_max_tool_bar.addWidget(Qt.QLabel('fft_max'+": "))
        self._fft_max_line_edit = Qt.QLineEdit(str(self.fft_max))
        self._fft_max_tool_bar.addWidget(self._fft_max_line_edit)
        self._fft_max_line_edit.returnPressed.connect(
        	lambda: self.set_fft_max(eng_notation.str_to_num(str(self._fft_max_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._fft_max_tool_bar, 10, 0, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._alpha_tool_bar = Qt.QToolBar(self)
        self._alpha_tool_bar.addWidget(Qt.QLabel('alpha'+": "))
        self._alpha_line_edit = Qt.QLineEdit(str(self.alpha))
        self._alpha_tool_bar.addWidget(self._alpha_line_edit)
        self._alpha_line_edit.returnPressed.connect(
        	lambda: self.set_alpha(eng_notation.str_to_num(str(self._alpha_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._alpha_tool_bar, 10, 2, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_1 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(rx_freq, samp_rate/2.0), 0)
        self.uhd_usrp_source_1.set_gain(rx_gain, 0)
        self.uhd_usrp_source_1.set_antenna('RX2', 0)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(rx_freq, samp_rate/2.0), 1)
        self.uhd_usrp_source_1.set_gain(rx_gain, 1)
        self.uhd_usrp_source_1.set_antenna('RX2', 1)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 1)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 1)
        self.single_pole_iir_filter_xx_0_0 = filter.single_pole_iir_filter_ff(alpha, 1)
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(alpha, 1)
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	nfft, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
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

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(fft_min, fft_max)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 4, 4, 4, 4)
        for r in range(4, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	nfft, #size
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

        self.qtgui_waterfall_sink_x_0.set_intensity_range(fft_min, fft_max)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 4, 0, 4, 4)
        for r in range(4, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            2
        )
        self.qtgui_number_sink_0.set_update_time(0.01)
        self.qtgui_number_sink_0.set_title("")

        labels = ['', '', '', '', '',
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
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 9, 4, 2, 2)
        for r in range(9, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	nfft, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"LHCP", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0.set_y_axis(fft_min, fft_max)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not True:
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
        	nfft, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate / decim, #bw
        	"RHCP", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(fft_min, fft_max)
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
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, 1, -10*math.log10(nfft))
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, -10*math.log10(nfft))
        self.blocks_keep_one_in_n_0_0 = blocks.keep_one_in_n(gr.sizeof_float*1, int(samp_rate/keep_n))
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_float*1, int(samp_rate/keep_n))
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self._avg_length_tool_bar = Qt.QToolBar(self)
        self._avg_length_tool_bar.addWidget(Qt.QLabel('avg_length'+": "))
        self._avg_length_line_edit = Qt.QLineEdit(str(self.avg_length))
        self._avg_length_tool_bar.addWidget(self._avg_length_line_edit)
        self._avg_length_line_edit.returnPressed.connect(
        	lambda: self.set_avg_length(eng_notation.str_to_num(str(self._avg_length_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._avg_length_tool_bar, 9, 3, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.single_pole_iir_filter_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.single_pole_iir_filter_xx_0_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_keep_one_in_n_0_0, 0), (self.qtgui_number_sink_0, 1))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.blocks_keep_one_in_n_0_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0_0, 0), (self.blocks_nlog10_ff_0_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.uhd_usrp_source_1, 1), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_1, 1), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_1, 1), (self.qtgui_waterfall_sink_x_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "gt_measure")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate / self.decim)

    def get_nfft(self):
        return self.nfft

    def set_nfft(self, nfft):
        self.nfft = nfft

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq, self.samp_rate/2.0), 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq, self.samp_rate/2.0), 1)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate / self.decim)
        self.blocks_keep_one_in_n_0_0.set_n(int(self.samp_rate/self.keep_n))
        self.blocks_keep_one_in_n_0.set_n(int(self.samp_rate/self.keep_n))

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))
        self.uhd_usrp_source_1.set_gain(self.rx_gain, 0)

        self.uhd_usrp_source_1.set_gain(self.rx_gain, 1)


    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq, self.samp_rate/2.0), 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq, self.samp_rate/2.0), 1)

    def get_keep_n(self):
        return self.keep_n

    def set_keep_n(self, keep_n):
        self.keep_n = keep_n
        Qt.QMetaObject.invokeMethod(self._keep_n_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.keep_n)))
        self.blocks_keep_one_in_n_0_0.set_n(int(self.samp_rate/self.keep_n))
        self.blocks_keep_one_in_n_0.set_n(int(self.samp_rate/self.keep_n))

    def get_fft_min(self):
        return self.fft_min

    def set_fft_min(self, fft_min):
        self.fft_min = fft_min
        Qt.QMetaObject.invokeMethod(self._fft_min_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.fft_min)))
        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(self.fft_min, self.fft_max)
        self.qtgui_waterfall_sink_x_0.set_intensity_range(self.fft_min, self.fft_max)
        self.qtgui_freq_sink_x_0_0.set_y_axis(self.fft_min, self.fft_max)
        self.qtgui_freq_sink_x_0.set_y_axis(self.fft_min, self.fft_max)

    def get_fft_max(self):
        return self.fft_max

    def set_fft_max(self, fft_max):
        self.fft_max = fft_max
        Qt.QMetaObject.invokeMethod(self._fft_max_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.fft_max)))
        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(self.fft_min, self.fft_max)
        self.qtgui_waterfall_sink_x_0.set_intensity_range(self.fft_min, self.fft_max)
        self.qtgui_freq_sink_x_0_0.set_y_axis(self.fft_min, self.fft_max)
        self.qtgui_freq_sink_x_0.set_y_axis(self.fft_min, self.fft_max)

    def get_avg_length(self):
        return self.avg_length

    def set_avg_length(self, avg_length):
        self.avg_length = avg_length
        Qt.QMetaObject.invokeMethod(self._avg_length_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.avg_length)))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        Qt.QMetaObject.invokeMethod(self._alpha_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.alpha)))
        self.single_pole_iir_filter_xx_0_0.set_taps(self.alpha)
        self.single_pole_iir_filter_xx_0.set_taps(self.alpha)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--decim", dest="decim", type="intx", default=2,
        help="Set decim [default=%default]")
    parser.add_option(
        "", "--nfft", dest="nfft", type="intx", default=2048,
        help="Set nfft [default=%default]")
    return parser


def main(top_block_cls=gt_measure, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(decim=options.decim, nfft=options.nfft)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
