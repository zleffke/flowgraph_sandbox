#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: INMARSAT BGAN Service, C-Band Return, Transponder 2
# Generated: Mon Sep  3 02:02:44 2018
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
from datetime import datetime as dt; import string
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fosphor
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import pmt
import sip
import sys
from gnuradio import qtgui


class inmarsat_cband_playback_3(gr.top_block, Qt.QWidget):

    def __init__(self, samp_rate=80e6):
        gr.top_block.__init__(self, "INMARSAT BGAN Service, C-Band Return, Transponder 2")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("INMARSAT BGAN Service, C-Band Return, Transponder 2")
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

        self.settings = Qt.QSettings("GNU Radio", "inmarsat_cband_playback_3")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.xpndr_offset = xpndr_offset = [-23e6,-7.5e6,8e6,23e6]
        self.xpndr_id = xpndr_id = 1
        self.rf_freq = rf_freq = 3627.5e6
        self.offset = offset = 0
        self.rf_center = rf_center = (rf_freq+xpndr_offset[xpndr_id]+offset)
        self.hs_lo = hs_lo = 5150e6
        self.xpndr_lbl = xpndr_lbl = "{:s}, Center [MHz]: {:4.3f}, BW [MHz]: 1.0".format(str(xpndr_id+1), rf_center/1e6)
        self.if_freq = if_freq = hs_lo-rf_freq
        self.xpndr_lbll = xpndr_lbll = xpndr_lbl
        self.xpndr_4_offset = xpndr_4_offset = xpndr_offset[3]
        self.xpndr_3_offset = xpndr_3_offset = xpndr_offset[2]
        self.xpndr_2_offset = xpndr_2_offset = xpndr_offset[1]
        self.xpndr_1_offset = xpndr_1_offset = xpndr_offset[0]
        self.rf_freq_lbl = rf_freq_lbl = rf_freq
        self.resamp_rate = resamp_rate = 0.175
        self.if_freq_lbl = if_freq_lbl = if_freq
        self.fg_title = fg_title = "INMARSAT BGAN Service, C-Band Return, Transponder {:s}".format(str(xpndr_id+1))

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, 'Transponder 1')
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, 'Transponder 2')
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, 'Transponder 3')
        self.tab_widget_3 = Qt.QWidget()
        self.tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_3)
        self.tab_grid_layout_3 = Qt.QGridLayout()
        self.tab_layout_3.addLayout(self.tab_grid_layout_3)
        self.tab.addTab(self.tab_widget_3, 'Transponder 4')
        self.top_grid_layout.addWidget(self.tab, 2, 0, 4, 2)
        for r in range(2, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._offset_tool_bar = Qt.QToolBar(self)
        self._offset_tool_bar.addWidget(Qt.QLabel("offset"+": "))
        self._offset_line_edit = Qt.QLineEdit(str(self.offset))
        self._offset_tool_bar.addWidget(self._offset_line_edit)
        self._offset_line_edit.returnPressed.connect(
        	lambda: self.set_offset(eng_notation.str_to_num(str(self._offset_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._offset_tool_bar, 8, 2, 1, 2)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._xpndr_lbll_tool_bar = Qt.QToolBar(self)

        if None:
          self._xpndr_lbll_formatter = None
        else:
          self._xpndr_lbll_formatter = lambda x: str(x)

        self._xpndr_lbll_tool_bar.addWidget(Qt.QLabel('Transponder'+": "))
        self._xpndr_lbll_label = Qt.QLabel(str(self._xpndr_lbll_formatter(self.xpndr_lbll)))
        self._xpndr_lbll_tool_bar.addWidget(self._xpndr_lbll_label)
        self.top_grid_layout.addWidget(self._xpndr_lbll_tool_bar, 9, 2, 1, 2)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rf_freq_lbl_tool_bar = Qt.QToolBar(self)

        if None:
          self._rf_freq_lbl_formatter = None
        else:
          self._rf_freq_lbl_formatter = lambda x: eng_notation.num_to_str(x)

        self._rf_freq_lbl_tool_bar.addWidget(Qt.QLabel('RF'+": "))
        self._rf_freq_lbl_label = Qt.QLabel(str(self._rf_freq_lbl_formatter(self.rf_freq_lbl)))
        self._rf_freq_lbl_tool_bar.addWidget(self._rf_freq_lbl_label)
        self.top_grid_layout.addWidget(self._rf_freq_lbl_tool_bar, 8, 0, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate*resamp_rate*0.071428571, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(False)

        if not False:
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

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-100, -20)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 3, 2, 3, 2)
        for r in range(3, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rf_freq + xpndr_offset[xpndr_id]+offset, #fc
        	samp_rate*resamp_rate*0.071428571, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.0010)
        self.qtgui_freq_sink_x_0.set_y_axis(-100, -20)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(False)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 2, 2, 1, 2)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.pfb_arb_resampler_xxx_0_1 = pfb.arb_resampler_ccf(
        	  resamp_rate,
                  taps=None,
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0_1.declare_sample_delay(0)

        self.pfb_arb_resampler_xxx_0_0_0_0 = pfb.arb_resampler_ccf(
        	  0.071428571,
                  taps=None,
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0_0_0_0.declare_sample_delay(0)

        self.pfb_arb_resampler_xxx_0_0_0 = pfb.arb_resampler_ccf(
        	  resamp_rate,
                  taps=None,
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0_0_0.declare_sample_delay(0)

        self.pfb_arb_resampler_xxx_0_0 = pfb.arb_resampler_ccf(
        	  resamp_rate,
                  taps=None,
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0_0.declare_sample_delay(0)

        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  resamp_rate,
                  taps=None,
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)

        self._if_freq_lbl_tool_bar = Qt.QToolBar(self)

        if None:
          self._if_freq_lbl_formatter = None
        else:
          self._if_freq_lbl_formatter = lambda x: eng_notation.num_to_str(x)

        self._if_freq_lbl_tool_bar.addWidget(Qt.QLabel('IF'+": "))
        self._if_freq_lbl_label = Qt.QLabel(str(self._if_freq_lbl_formatter(self.if_freq_lbl)))
        self._if_freq_lbl_tool_bar.addWidget(self._if_freq_lbl_label)
        self.top_grid_layout.addWidget(self._if_freq_lbl_tool_bar, 8, 1, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0_2 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0_2.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0_2.set_frequency_range(rf_freq, samp_rate)
        self._fosphor_qt_sink_c_0_2_win = sip.wrapinstance(self.fosphor_qt_sink_c_0_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._fosphor_qt_sink_c_0_2_win, 0, 0, 2, 4)
        for r in range(0, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0_1 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0_1.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0_1.set_frequency_range(rf_freq + xpndr_3_offset, samp_rate*resamp_rate)
        self._fosphor_qt_sink_c_0_1_win = sip.wrapinstance(self.fosphor_qt_sink_c_0_1.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_2.addWidget(self._fosphor_qt_sink_c_0_1_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tab_grid_layout_2.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0_0_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0_0_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0_0_0.set_frequency_range(rf_freq + xpndr_4_offset, samp_rate*resamp_rate)
        self._fosphor_qt_sink_c_0_0_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_3.addWidget(self._fosphor_qt_sink_c_0_0_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tab_grid_layout_3.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0_0.set_frequency_range(rf_freq + xpndr_2_offset, samp_rate*resamp_rate)
        self._fosphor_qt_sink_c_0_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_1.addWidget(self._fosphor_qt_sink_c_0_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tab_grid_layout_1.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0.set_frequency_range(rf_freq + xpndr_1_offset, samp_rate*resamp_rate)
        self._fosphor_qt_sink_c_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0.pyqwidget(), Qt.QWidget)
        self.tab_grid_layout_0.addWidget(self._fosphor_qt_sink_c_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 4):
            self.tab_grid_layout_0.setColumnStretch(c, 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((-1, ))
        self.blocks_interleaved_short_to_complex_0 = blocks.interleaved_short_to_complex(False, False)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_1 = blocks.file_source(gr.sizeof_short*1, '/data1/captures/inmarsat_c/4F3_F5BE35_20180903_043333.872099_UTC_80M.short', True)
        self.blocks_file_source_1.set_begin_tag(pmt.PMT_NIL)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.analog_sig_source_x_0_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1*xpndr_3_offset, 1, 0)
        self.analog_sig_source_x_0_0_1 = analog.sig_source_c(samp_rate*resamp_rate, analog.GR_COS_WAVE, -1*(offset), 1, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1*xpndr_4_offset, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1*xpndr_2_offset, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1*xpndr_1_offset, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0_1, 0), (self.blocks_multiply_xx_0_0_1, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_file_source_1, 0), (self.blocks_interleaved_short_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.fosphor_qt_sink_c_0_2, 0))
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.pfb_arb_resampler_xxx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.pfb_arb_resampler_xxx_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_1, 0), (self.pfb_arb_resampler_xxx_0_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.pfb_arb_resampler_xxx_0_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.fosphor_qt_sink_c_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.blocks_multiply_xx_0_0_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.fosphor_qt_sink_c_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0, 0), (self.fosphor_qt_sink_c_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_1, 0), (self.fosphor_qt_sink_c_0_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "inmarsat_cband_playback_3")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate*self.resamp_rate*0.071428571)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rf_freq + self.xpndr_offset[self.xpndr_id]+self.offset, self.samp_rate*self.resamp_rate*0.071428571)
        self.fosphor_qt_sink_c_0_2.set_frequency_range(self.rf_freq, self.samp_rate)
        self.fosphor_qt_sink_c_0_1.set_frequency_range(self.rf_freq + self.xpndr_3_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0_0_0.set_frequency_range(self.rf_freq + self.xpndr_4_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0_0.set_frequency_range(self.rf_freq + self.xpndr_2_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rf_freq + self.xpndr_1_offset, self.samp_rate*self.resamp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_1.set_sampling_freq(self.samp_rate*self.resamp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_xpndr_offset(self):
        return self.xpndr_offset

    def set_xpndr_offset(self, xpndr_offset):
        self.xpndr_offset = xpndr_offset
        self.set_xpndr_4_offset(self.xpndr_offset[3])
        self.set_xpndr_3_offset(self.xpndr_offset[2])
        self.set_xpndr_2_offset(self.xpndr_offset[1])
        self.set_xpndr_1_offset(self.xpndr_offset[0])
        self.set_rf_center((self.rf_freq+self.xpndr_offset[self.xpndr_id]+self.offset))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rf_freq + self.xpndr_offset[self.xpndr_id]+self.offset, self.samp_rate*self.resamp_rate*0.071428571)

    def get_xpndr_id(self):
        return self.xpndr_id

    def set_xpndr_id(self, xpndr_id):
        self.xpndr_id = xpndr_id
        self.set_xpndr_lbl("{:s}, Center [MHz]: {:4.3f}, BW [MHz]: 1.0".format(str(self.xpndr_id+1), self.rf_center/1e6))
        self.set_rf_center((self.rf_freq+self.xpndr_offset[self.xpndr_id]+self.offset))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rf_freq + self.xpndr_offset[self.xpndr_id]+self.offset, self.samp_rate*self.resamp_rate*0.071428571)
        self.set_fg_title("INMARSAT BGAN Service, C-Band Return, Transponder {:s}".format(str(self.xpndr_id+1)))

    def get_rf_freq(self):
        return self.rf_freq

    def set_rf_freq(self, rf_freq):
        self.rf_freq = rf_freq
        self.set_rf_freq_lbl(self._rf_freq_lbl_formatter(self.rf_freq))
        self.set_rf_center((self.rf_freq+self.xpndr_offset[self.xpndr_id]+self.offset))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rf_freq + self.xpndr_offset[self.xpndr_id]+self.offset, self.samp_rate*self.resamp_rate*0.071428571)
        self.set_if_freq(self.hs_lo-self.rf_freq)
        self.fosphor_qt_sink_c_0_2.set_frequency_range(self.rf_freq, self.samp_rate)
        self.fosphor_qt_sink_c_0_1.set_frequency_range(self.rf_freq + self.xpndr_3_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0_0_0.set_frequency_range(self.rf_freq + self.xpndr_4_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0_0.set_frequency_range(self.rf_freq + self.xpndr_2_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rf_freq + self.xpndr_1_offset, self.samp_rate*self.resamp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        Qt.QMetaObject.invokeMethod(self._offset_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.offset)))
        self.set_rf_center((self.rf_freq+self.xpndr_offset[self.xpndr_id]+self.offset))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rf_freq + self.xpndr_offset[self.xpndr_id]+self.offset, self.samp_rate*self.resamp_rate*0.071428571)
        self.analog_sig_source_x_0_0_1.set_frequency(-1*(self.offset))

    def get_rf_center(self):
        return self.rf_center

    def set_rf_center(self, rf_center):
        self.rf_center = rf_center
        self.set_xpndr_lbl("{:s}, Center [MHz]: {:4.3f}, BW [MHz]: 1.0".format(str(self.xpndr_id+1), self.rf_center/1e6))

    def get_hs_lo(self):
        return self.hs_lo

    def set_hs_lo(self, hs_lo):
        self.hs_lo = hs_lo
        self.set_if_freq(self.hs_lo-self.rf_freq)

    def get_xpndr_lbl(self):
        return self.xpndr_lbl

    def set_xpndr_lbl(self, xpndr_lbl):
        self.xpndr_lbl = xpndr_lbl
        self.set_xpndr_lbll(self._xpndr_lbll_formatter(self.xpndr_lbl))

    def get_if_freq(self):
        return self.if_freq

    def set_if_freq(self, if_freq):
        self.if_freq = if_freq
        self.set_if_freq_lbl(self._if_freq_lbl_formatter(self.if_freq))

    def get_xpndr_lbll(self):
        return self.xpndr_lbll

    def set_xpndr_lbll(self, xpndr_lbll):
        self.xpndr_lbll = xpndr_lbll
        Qt.QMetaObject.invokeMethod(self._xpndr_lbll_label, "setText", Qt.Q_ARG("QString", self.xpndr_lbll))

    def get_xpndr_4_offset(self):
        return self.xpndr_4_offset

    def set_xpndr_4_offset(self, xpndr_4_offset):
        self.xpndr_4_offset = xpndr_4_offset
        self.fosphor_qt_sink_c_0_0_0.set_frequency_range(self.rf_freq + self.xpndr_4_offset, self.samp_rate*self.resamp_rate)
        self.analog_sig_source_x_0_0_0.set_frequency(-1*self.xpndr_4_offset)

    def get_xpndr_3_offset(self):
        return self.xpndr_3_offset

    def set_xpndr_3_offset(self, xpndr_3_offset):
        self.xpndr_3_offset = xpndr_3_offset
        self.fosphor_qt_sink_c_0_1.set_frequency_range(self.rf_freq + self.xpndr_3_offset, self.samp_rate*self.resamp_rate)
        self.analog_sig_source_x_0_1.set_frequency(-1*self.xpndr_3_offset)

    def get_xpndr_2_offset(self):
        return self.xpndr_2_offset

    def set_xpndr_2_offset(self, xpndr_2_offset):
        self.xpndr_2_offset = xpndr_2_offset
        self.fosphor_qt_sink_c_0_0.set_frequency_range(self.rf_freq + self.xpndr_2_offset, self.samp_rate*self.resamp_rate)
        self.analog_sig_source_x_0_0.set_frequency(-1*self.xpndr_2_offset)

    def get_xpndr_1_offset(self):
        return self.xpndr_1_offset

    def set_xpndr_1_offset(self, xpndr_1_offset):
        self.xpndr_1_offset = xpndr_1_offset
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rf_freq + self.xpndr_1_offset, self.samp_rate*self.resamp_rate)
        self.analog_sig_source_x_0.set_frequency(-1*self.xpndr_1_offset)

    def get_rf_freq_lbl(self):
        return self.rf_freq_lbl

    def set_rf_freq_lbl(self, rf_freq_lbl):
        self.rf_freq_lbl = rf_freq_lbl
        Qt.QMetaObject.invokeMethod(self._rf_freq_lbl_label, "setText", Qt.Q_ARG("QString", self.rf_freq_lbl))

    def get_resamp_rate(self):
        return self.resamp_rate

    def set_resamp_rate(self, resamp_rate):
        self.resamp_rate = resamp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate*self.resamp_rate*0.071428571)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rf_freq + self.xpndr_offset[self.xpndr_id]+self.offset, self.samp_rate*self.resamp_rate*0.071428571)
        self.pfb_arb_resampler_xxx_0_1.set_rate(self.resamp_rate)
        self.pfb_arb_resampler_xxx_0_0_0.set_rate(self.resamp_rate)
        self.pfb_arb_resampler_xxx_0_0.set_rate(self.resamp_rate)
        self.pfb_arb_resampler_xxx_0.set_rate(self.resamp_rate)
        self.fosphor_qt_sink_c_0_1.set_frequency_range(self.rf_freq + self.xpndr_3_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0_0_0.set_frequency_range(self.rf_freq + self.xpndr_4_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0_0.set_frequency_range(self.rf_freq + self.xpndr_2_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rf_freq + self.xpndr_1_offset, self.samp_rate*self.resamp_rate)
        self.analog_sig_source_x_0_0_1.set_sampling_freq(self.samp_rate*self.resamp_rate)

    def get_if_freq_lbl(self):
        return self.if_freq_lbl

    def set_if_freq_lbl(self, if_freq_lbl):
        self.if_freq_lbl = if_freq_lbl
        Qt.QMetaObject.invokeMethod(self._if_freq_lbl_label, "setText", Qt.Q_ARG("QString", self.if_freq_lbl))

    def get_fg_title(self):
        return self.fg_title

    def set_fg_title(self, fg_title):
        self.fg_title = fg_title


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(80e6),
        help="Set samp_rate [default=%default]")
    return parser


def main(top_block_cls=inmarsat_cband_playback_3, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(samp_rate=options.samp_rate)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
