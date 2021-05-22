#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Inmarsat Cband Playback
# Generated: Mon Sep  3 00:59:00 2018
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fosphor
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import pmt
import sip
import sys
from gnuradio import qtgui


class inmarsat_cband_playback(gr.top_block, Qt.QWidget):

    def __init__(self, samp_rate=80e6):
        gr.top_block.__init__(self, "Inmarsat Cband Playback")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Inmarsat Cband Playback")
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

        self.settings = Qt.QSettings("GNU Radio", "inmarsat_cband_playback")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.rf_freq = rf_freq = 3627.5e6
        self.hs_lo = hs_lo = 5150e6
        self.xpndr_4_offset = xpndr_4_offset = 23e6
        self.xpndr_3_offset = xpndr_3_offset = 7.5e6
        self.xpndr_2_offset = xpndr_2_offset = -7.5e6
        self.xpndr_1_offset = xpndr_1_offset = -23e6
        self.if_freq = if_freq = hs_lo-rf_freq
        self.xpndr4_lbl = xpndr4_lbl = xpndr_4_offset
        self.xpndr3_lbl = xpndr3_lbl = xpndr_3_offset
        self.xpndr2_lbl = xpndr2_lbl = xpndr_2_offset
        self.xpndr1_lbl = xpndr1_lbl = xpndr_1_offset
        self.rf_freq_lbl = rf_freq_lbl = rf_freq
        self.resamp_rate = resamp_rate = 0.175
        self.if_freq_lbl = if_freq_lbl = if_freq

        ##################################################
        # Blocks
        ##################################################
        self._xpndr4_lbl_tool_bar = Qt.QToolBar(self)

        if None:
          self._xpndr4_lbl_formatter = None
        else:
          self._xpndr4_lbl_formatter = lambda x: eng_notation.num_to_str(x)

        self._xpndr4_lbl_tool_bar.addWidget(Qt.QLabel('Transponder 4'+": "))
        self._xpndr4_lbl_label = Qt.QLabel(str(self._xpndr4_lbl_formatter(self.xpndr4_lbl)))
        self._xpndr4_lbl_tool_bar.addWidget(self._xpndr4_lbl_label)
        self.top_grid_layout.addWidget(self._xpndr4_lbl_tool_bar, 9, 6, 1, 2)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._xpndr3_lbl_tool_bar = Qt.QToolBar(self)

        if None:
          self._xpndr3_lbl_formatter = None
        else:
          self._xpndr3_lbl_formatter = lambda x: eng_notation.num_to_str(x)

        self._xpndr3_lbl_tool_bar.addWidget(Qt.QLabel('Transponder 3'+": "))
        self._xpndr3_lbl_label = Qt.QLabel(str(self._xpndr3_lbl_formatter(self.xpndr3_lbl)))
        self._xpndr3_lbl_tool_bar.addWidget(self._xpndr3_lbl_label)
        self.top_grid_layout.addWidget(self._xpndr3_lbl_tool_bar, 9, 2, 1, 2)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._xpndr2_lbl_tool_bar = Qt.QToolBar(self)

        if None:
          self._xpndr2_lbl_formatter = None
        else:
          self._xpndr2_lbl_formatter = lambda x: eng_notation.num_to_str(x)

        self._xpndr2_lbl_tool_bar.addWidget(Qt.QLabel('Transponder 2'+": "))
        self._xpndr2_lbl_label = Qt.QLabel(str(self._xpndr2_lbl_formatter(self.xpndr2_lbl)))
        self._xpndr2_lbl_tool_bar.addWidget(self._xpndr2_lbl_label)
        self.top_grid_layout.addWidget(self._xpndr2_lbl_tool_bar, 4, 6, 1, 2)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._xpndr1_lbl_tool_bar = Qt.QToolBar(self)

        if None:
          self._xpndr1_lbl_formatter = None
        else:
          self._xpndr1_lbl_formatter = lambda x: eng_notation.num_to_str(x)

        self._xpndr1_lbl_tool_bar.addWidget(Qt.QLabel('Transponder 1'+": "))
        self._xpndr1_lbl_label = Qt.QLabel(str(self._xpndr1_lbl_formatter(self.xpndr1_lbl)))
        self._xpndr1_lbl_tool_bar.addWidget(self._xpndr1_lbl_label)
        self.top_grid_layout.addWidget(self._xpndr1_lbl_tool_bar, 4, 2, 1, 2)
        for r in range(4, 5):
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
        self.top_grid_layout.addWidget(self._rf_freq_lbl_tool_bar, 10, 0, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.pfb_arb_resampler_xxx_0_1 = pfb.arb_resampler_ccf(
        	  resamp_rate,
                  taps=None,
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0_1.declare_sample_delay(0)

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
        self.top_grid_layout.addWidget(self._if_freq_lbl_tool_bar, 10, 1, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0_1 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0_1.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0_1.set_frequency_range(rf_freq + xpndr_3_offset, samp_rate*resamp_rate)
        self._fosphor_qt_sink_c_0_1_win = sip.wrapinstance(self.fosphor_qt_sink_c_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._fosphor_qt_sink_c_0_1_win, 5, 0, 4, 4)
        for r in range(5, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0_0_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0_0_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0_0_0.set_frequency_range(rf_freq + xpndr_4_offset, samp_rate*resamp_rate)
        self._fosphor_qt_sink_c_0_0_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._fosphor_qt_sink_c_0_0_0_win, 5, 4, 4, 4)
        for r in range(5, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0_0.set_frequency_range(rf_freq + xpndr_2_offset, samp_rate*resamp_rate)
        self._fosphor_qt_sink_c_0_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._fosphor_qt_sink_c_0_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0.set_frequency_range(rf_freq + xpndr_1_offset, samp_rate*resamp_rate)
        self._fosphor_qt_sink_c_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._fosphor_qt_sink_c_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_glfw_sink_c_0 = fosphor.glfw_sink_c()
        self.fosphor_glfw_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_glfw_sink_c_0.set_frequency_range(rf_freq, samp_rate)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
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
        self.analog_sig_source_x_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1*xpndr_4_offset, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1*xpndr_2_offset, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1*xpndr_1_offset, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_file_source_1, 0), (self.blocks_interleaved_short_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.fosphor_glfw_sink_c_0, 0))
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.pfb_arb_resampler_xxx_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.pfb_arb_resampler_xxx_0_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.pfb_arb_resampler_xxx_0_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.fosphor_qt_sink_c_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0, 0), (self.fosphor_qt_sink_c_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_0_0, 0), (self.fosphor_qt_sink_c_0_0_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0_1, 0), (self.fosphor_qt_sink_c_0_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "inmarsat_cband_playback")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.fosphor_qt_sink_c_0_1.set_frequency_range(self.rf_freq + self.xpndr_3_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0_0_0.set_frequency_range(self.rf_freq + self.xpndr_4_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0_0.set_frequency_range(self.rf_freq + self.xpndr_2_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rf_freq + self.xpndr_1_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_glfw_sink_c_0.set_frequency_range(self.rf_freq, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_rf_freq(self):
        return self.rf_freq

    def set_rf_freq(self, rf_freq):
        self.rf_freq = rf_freq
        self.set_rf_freq_lbl(self._rf_freq_lbl_formatter(self.rf_freq))
        self.set_if_freq(self.hs_lo-self.rf_freq)
        self.fosphor_qt_sink_c_0_1.set_frequency_range(self.rf_freq + self.xpndr_3_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0_0_0.set_frequency_range(self.rf_freq + self.xpndr_4_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0_0.set_frequency_range(self.rf_freq + self.xpndr_2_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rf_freq + self.xpndr_1_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_glfw_sink_c_0.set_frequency_range(self.rf_freq, self.samp_rate)

    def get_hs_lo(self):
        return self.hs_lo

    def set_hs_lo(self, hs_lo):
        self.hs_lo = hs_lo
        self.set_if_freq(self.hs_lo-self.rf_freq)

    def get_xpndr_4_offset(self):
        return self.xpndr_4_offset

    def set_xpndr_4_offset(self, xpndr_4_offset):
        self.xpndr_4_offset = xpndr_4_offset
        self.set_xpndr4_lbl(self._xpndr4_lbl_formatter(self.xpndr_4_offset))
        self.fosphor_qt_sink_c_0_0_0.set_frequency_range(self.rf_freq + self.xpndr_4_offset, self.samp_rate*self.resamp_rate)
        self.analog_sig_source_x_0_0_0.set_frequency(-1*self.xpndr_4_offset)

    def get_xpndr_3_offset(self):
        return self.xpndr_3_offset

    def set_xpndr_3_offset(self, xpndr_3_offset):
        self.xpndr_3_offset = xpndr_3_offset
        self.set_xpndr3_lbl(self._xpndr3_lbl_formatter(self.xpndr_3_offset))
        self.fosphor_qt_sink_c_0_1.set_frequency_range(self.rf_freq + self.xpndr_3_offset, self.samp_rate*self.resamp_rate)
        self.analog_sig_source_x_0_1.set_frequency(-1*self.xpndr_3_offset)

    def get_xpndr_2_offset(self):
        return self.xpndr_2_offset

    def set_xpndr_2_offset(self, xpndr_2_offset):
        self.xpndr_2_offset = xpndr_2_offset
        self.set_xpndr2_lbl(self._xpndr2_lbl_formatter(self.xpndr_2_offset))
        self.fosphor_qt_sink_c_0_0.set_frequency_range(self.rf_freq + self.xpndr_2_offset, self.samp_rate*self.resamp_rate)
        self.analog_sig_source_x_0_0.set_frequency(-1*self.xpndr_2_offset)

    def get_xpndr_1_offset(self):
        return self.xpndr_1_offset

    def set_xpndr_1_offset(self, xpndr_1_offset):
        self.xpndr_1_offset = xpndr_1_offset
        self.set_xpndr1_lbl(self._xpndr1_lbl_formatter(self.xpndr_1_offset))
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rf_freq + self.xpndr_1_offset, self.samp_rate*self.resamp_rate)
        self.analog_sig_source_x_0.set_frequency(-1*self.xpndr_1_offset)

    def get_if_freq(self):
        return self.if_freq

    def set_if_freq(self, if_freq):
        self.if_freq = if_freq
        self.set_if_freq_lbl(self._if_freq_lbl_formatter(self.if_freq))

    def get_xpndr4_lbl(self):
        return self.xpndr4_lbl

    def set_xpndr4_lbl(self, xpndr4_lbl):
        self.xpndr4_lbl = xpndr4_lbl
        Qt.QMetaObject.invokeMethod(self._xpndr4_lbl_label, "setText", Qt.Q_ARG("QString", self.xpndr4_lbl))

    def get_xpndr3_lbl(self):
        return self.xpndr3_lbl

    def set_xpndr3_lbl(self, xpndr3_lbl):
        self.xpndr3_lbl = xpndr3_lbl
        Qt.QMetaObject.invokeMethod(self._xpndr3_lbl_label, "setText", Qt.Q_ARG("QString", self.xpndr3_lbl))

    def get_xpndr2_lbl(self):
        return self.xpndr2_lbl

    def set_xpndr2_lbl(self, xpndr2_lbl):
        self.xpndr2_lbl = xpndr2_lbl
        Qt.QMetaObject.invokeMethod(self._xpndr2_lbl_label, "setText", Qt.Q_ARG("QString", self.xpndr2_lbl))

    def get_xpndr1_lbl(self):
        return self.xpndr1_lbl

    def set_xpndr1_lbl(self, xpndr1_lbl):
        self.xpndr1_lbl = xpndr1_lbl
        Qt.QMetaObject.invokeMethod(self._xpndr1_lbl_label, "setText", Qt.Q_ARG("QString", self.xpndr1_lbl))

    def get_rf_freq_lbl(self):
        return self.rf_freq_lbl

    def set_rf_freq_lbl(self, rf_freq_lbl):
        self.rf_freq_lbl = rf_freq_lbl
        Qt.QMetaObject.invokeMethod(self._rf_freq_lbl_label, "setText", Qt.Q_ARG("QString", self.rf_freq_lbl))

    def get_resamp_rate(self):
        return self.resamp_rate

    def set_resamp_rate(self, resamp_rate):
        self.resamp_rate = resamp_rate
        self.pfb_arb_resampler_xxx_0_1.set_rate(self.resamp_rate)
        self.pfb_arb_resampler_xxx_0_0_0.set_rate(self.resamp_rate)
        self.pfb_arb_resampler_xxx_0_0.set_rate(self.resamp_rate)
        self.pfb_arb_resampler_xxx_0.set_rate(self.resamp_rate)
        self.fosphor_qt_sink_c_0_1.set_frequency_range(self.rf_freq + self.xpndr_3_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0_0_0.set_frequency_range(self.rf_freq + self.xpndr_4_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0_0.set_frequency_range(self.rf_freq + self.xpndr_2_offset, self.samp_rate*self.resamp_rate)
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rf_freq + self.xpndr_1_offset, self.samp_rate*self.resamp_rate)

    def get_if_freq_lbl(self):
        return self.if_freq_lbl

    def set_if_freq_lbl(self, if_freq_lbl):
        self.if_freq_lbl = if_freq_lbl
        Qt.QMetaObject.invokeMethod(self._if_freq_lbl_label, "setText", Qt.Q_ARG("QString", self.if_freq_lbl))


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(80e6),
        help="Set samp_rate [default=%default]")
    return parser


def main(top_block_cls=inmarsat_cband_playback, options=None):
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
