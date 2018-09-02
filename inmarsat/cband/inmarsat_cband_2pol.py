#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: 4F3_30CF9D2_20180812_025235.358998_UTC_1M.fc32
# Generated: Sat Aug 11 22:52:40 2018
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
from datetime import datetime as dt; import string
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
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


class inmarsat_cband_2pol(gr.top_block, Qt.QWidget):

    def __init__(self, radio_id='30CF9D2', sat_name='4F3'):
        gr.top_block.__init__(self, "4F3_30CF9D2_20180812_025235.358998_UTC_1M.fc32")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("4F3_30CF9D2_20180812_025235.358998_UTC_1M.fc32")
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

        self.settings = Qt.QSettings("GNU Radio", "inmarsat_cband_2pol")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.radio_id = radio_id
        self.sat_name = sat_name

        ##################################################
        # Variables
        ##################################################
        self.rx_freq = rx_freq = 3618e6
        self.hs_lo = hs_lo = 5150e6
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y%m%d_%H%M%S.%f" )+'_UTC'
        self.samp_rate = samp_rate = 1e6
        self.offset = offset = 0
        self.if_freq_rhcp = if_freq_rhcp = hs_lo-rx_freq
        self.if_freq_lhcp = if_freq_lhcp = hs_lo-rx_freq
        self.rx_gain_rhcp = rx_gain_rhcp = 25
        self.rx_gain_lhcp = rx_gain_lhcp = 25
        self.if_freq_rhcp_lbl = if_freq_rhcp_lbl = if_freq_rhcp-offset
        self.if_freq_lhcp_lbl = if_freq_lhcp_lbl = if_freq_lhcp
        self.fn = fn = "{:s}_{:s}_{:s}_{:s}M.fc32".format(sat_name, radio_id, ts_str, str(int(samp_rate/1e6)))
        self.exponent = exponent = 2

        ##################################################
        # Blocks
        ##################################################
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
        self._rx_gain_rhcp_tool_bar = Qt.QToolBar(self)
        self._rx_gain_rhcp_tool_bar.addWidget(Qt.QLabel('RHCP Gain'+": "))
        self._rx_gain_rhcp_line_edit = Qt.QLineEdit(str(self.rx_gain_rhcp))
        self._rx_gain_rhcp_tool_bar.addWidget(self._rx_gain_rhcp_line_edit)
        self._rx_gain_rhcp_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain_rhcp(eng_notation.str_to_num(str(self._rx_gain_rhcp_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_gain_rhcp_tool_bar, 8, 4, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_gain_lhcp_tool_bar = Qt.QToolBar(self)
        self._rx_gain_lhcp_tool_bar.addWidget(Qt.QLabel('LHCP Gain'+": "))
        self._rx_gain_lhcp_line_edit = Qt.QLineEdit(str(self.rx_gain_lhcp))
        self._rx_gain_lhcp_tool_bar.addWidget(self._rx_gain_lhcp_line_edit)
        self._rx_gain_lhcp_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain_lhcp(eng_notation.str_to_num(str(self._rx_gain_lhcp_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_gain_lhcp_tool_bar, 8, 5, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._offset_tool_bar = Qt.QToolBar(self)
        self._offset_tool_bar.addWidget(Qt.QLabel('rhcp_offset'+": "))
        self._offset_line_edit = Qt.QLineEdit(str(self.offset))
        self._offset_tool_bar.addWidget(self._offset_line_edit)
        self._offset_line_edit.returnPressed.connect(
        	lambda: self.set_offset(eng_notation.str_to_num(str(self._offset_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._offset_tool_bar, 8, 2, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._exponent_range = Range(0, 100, 1, 2, 200)
        self._exponent_win = RangeWidget(self._exponent_range, self.set_exponent, "exponent", "counter_slider", int)
        self.top_grid_layout.addWidget(self._exponent_win, 11, 0, 1, 1)
        for r in range(11, 12):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(if_freq_rhcp), 0)
        self.uhd_usrp_source_0_0.set_gain(rx_gain_rhcp, 0)
        self.uhd_usrp_source_0_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(if_freq_lhcp), 1)
        self.uhd_usrp_source_0_0.set_gain(rx_gain_lhcp, 1)
        self.uhd_usrp_source_0_0.set_antenna('RX2', 1)
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel("rx_freq"+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_freq_tool_bar, 8, 1, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
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
        colors = [1, 0, 0, 0, 0,
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

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-90, -40)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 4, 4, 4, 4)
        for r in range(4, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
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
        colors = [1, 0, 0, 0, 0,
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

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-90, -40)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 4, 0, 4, 4)
        for r in range(4, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(True)
        self.qtgui_freq_sink_x_1.enable_grid(True)
        self.qtgui_freq_sink_x_1.set_fft_average(0.2)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)

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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win, 9, 0, 2, 8)
        for r in range(9, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"LHCP", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-90, -40)
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
        	0, #fc
        	samp_rate, #bw
        	"RHCP", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-90, -40)
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
        self._if_freq_rhcp_lbl_tool_bar = Qt.QToolBar(self)

        if None:
          self._if_freq_rhcp_lbl_formatter = None
        else:
          self._if_freq_rhcp_lbl_formatter = lambda x: eng_notation.num_to_str(x)

        self._if_freq_rhcp_lbl_tool_bar.addWidget(Qt.QLabel('RHCP IF [MHz]'+": "))
        self._if_freq_rhcp_lbl_label = Qt.QLabel(str(self._if_freq_rhcp_lbl_formatter(self.if_freq_rhcp_lbl)))
        self._if_freq_rhcp_lbl_tool_bar.addWidget(self._if_freq_rhcp_lbl_label)
        self.top_grid_layout.addWidget(self._if_freq_rhcp_lbl_tool_bar, 8, 3, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._if_freq_lhcp_lbl_tool_bar = Qt.QToolBar(self)

        if None:
          self._if_freq_lhcp_lbl_formatter = None
        else:
          self._if_freq_lhcp_lbl_formatter = lambda x: eng_notation.num_to_str(x)

        self._if_freq_lhcp_lbl_tool_bar.addWidget(Qt.QLabel('LHCP IF [MHz]'+": "))
        self._if_freq_lhcp_lbl_label = Qt.QLabel(str(self._if_freq_lhcp_lbl_formatter(self.if_freq_lhcp_lbl)))
        self._if_freq_lhcp_lbl_tool_bar.addWidget(self._if_freq_lhcp_lbl_label)
        self.top_grid_layout.addWidget(self._if_freq_lhcp_lbl_tool_bar)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((-1, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((-1, ))
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_exponentiate_const_cci_0 = blocks.exponentiate_const_cci(exponent, 1)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1*offset, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_exponentiate_const_cci_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_exponentiate_const_cci_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 1), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.blocks_multiply_xx_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "inmarsat_cband_2pol")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_radio_id(self):
        return self.radio_id

    def set_radio_id(self, radio_id):
        self.radio_id = radio_id
        self.set_fn("{:s}_{:s}_{:s}_{:s}M.fc32".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate/1e6))))

    def get_sat_name(self):
        return self.sat_name

    def set_sat_name(self, sat_name):
        self.sat_name = sat_name
        self.set_fn("{:s}_{:s}_{:s}_{:s}M.fc32".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate/1e6))))

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self.set_if_freq_rhcp(self.hs_lo-self.rx_freq)
        self.set_if_freq_lhcp(self.hs_lo-self.rx_freq)
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))

    def get_hs_lo(self):
        return self.hs_lo

    def set_hs_lo(self, hs_lo):
        self.hs_lo = hs_lo
        self.set_if_freq_rhcp(self.hs_lo-self.rx_freq)
        self.set_if_freq_lhcp(self.hs_lo-self.rx_freq)

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_fn("{:s}_{:s}_{:s}_{:s}M.fc32".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate/1e6))))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.set_fn("{:s}_{:s}_{:s}_{:s}M.fc32".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate/1e6))))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        Qt.QMetaObject.invokeMethod(self._offset_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.offset)))
        self.set_if_freq_rhcp_lbl(self._if_freq_rhcp_lbl_formatter(self.if_freq_rhcp-self.offset))
        self.analog_sig_source_x_0.set_frequency(-1*self.offset)

    def get_if_freq_rhcp(self):
        return self.if_freq_rhcp

    def set_if_freq_rhcp(self, if_freq_rhcp):
        self.if_freq_rhcp = if_freq_rhcp
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(self.if_freq_rhcp), 0)
        self.set_if_freq_rhcp_lbl(self._if_freq_rhcp_lbl_formatter(self.if_freq_rhcp-self.offset))

    def get_if_freq_lhcp(self):
        return self.if_freq_lhcp

    def set_if_freq_lhcp(self, if_freq_lhcp):
        self.if_freq_lhcp = if_freq_lhcp
        self.uhd_usrp_source_0_0.set_center_freq(uhd.tune_request(self.if_freq_lhcp), 1)
        self.set_if_freq_lhcp_lbl(self._if_freq_lhcp_lbl_formatter(self.if_freq_lhcp))

    def get_rx_gain_rhcp(self):
        return self.rx_gain_rhcp

    def set_rx_gain_rhcp(self, rx_gain_rhcp):
        self.rx_gain_rhcp = rx_gain_rhcp
        Qt.QMetaObject.invokeMethod(self._rx_gain_rhcp_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain_rhcp)))
        self.uhd_usrp_source_0_0.set_gain(self.rx_gain_rhcp, 0)


    def get_rx_gain_lhcp(self):
        return self.rx_gain_lhcp

    def set_rx_gain_lhcp(self, rx_gain_lhcp):
        self.rx_gain_lhcp = rx_gain_lhcp
        Qt.QMetaObject.invokeMethod(self._rx_gain_lhcp_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain_lhcp)))
        self.uhd_usrp_source_0_0.set_gain(self.rx_gain_lhcp, 1)


    def get_if_freq_rhcp_lbl(self):
        return self.if_freq_rhcp_lbl

    def set_if_freq_rhcp_lbl(self, if_freq_rhcp_lbl):
        self.if_freq_rhcp_lbl = if_freq_rhcp_lbl
        Qt.QMetaObject.invokeMethod(self._if_freq_rhcp_lbl_label, "setText", Qt.Q_ARG("QString", self.if_freq_rhcp_lbl))

    def get_if_freq_lhcp_lbl(self):
        return self.if_freq_lhcp_lbl

    def set_if_freq_lhcp_lbl(self, if_freq_lhcp_lbl):
        self.if_freq_lhcp_lbl = if_freq_lhcp_lbl
        Qt.QMetaObject.invokeMethod(self._if_freq_lhcp_lbl_label, "setText", Qt.Q_ARG("QString", self.if_freq_lhcp_lbl))

    def get_fn(self):
        return self.fn

    def set_fn(self, fn):
        self.fn = fn

    def get_exponent(self):
        return self.exponent

    def set_exponent(self, exponent):
        self.exponent = exponent
        self.blocks_exponentiate_const_cci_0.set_exponent(self.exponent)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--radio-id", dest="radio_id", type="string", default='30CF9D2',
        help="Set radio_id [default=%default]")
    parser.add_option(
        "", "--sat-name", dest="sat_name", type="string", default='4F3',
        help="Set sat_name [default=%default]")
    return parser


def main(top_block_cls=inmarsat_cband_2pol, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(radio_id=options.radio_id, sat_name=options.sat_name)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
