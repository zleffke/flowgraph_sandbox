#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Nexrad Playback Sigmf
# GNU Radio version: 3.8.2.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import fosphor
from gnuradio.fft import window
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
import gr_sigmf

from gnuradio import qtgui

class nexrad_playback_sigmf(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Nexrad Playback Sigmf")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Nexrad Playback Sigmf")
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

        self.settings = Qt.QSettings("GNU Radio", "nexrad_playback_sigmf")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.tune = tune = 1e6
        self.trig_lvl = trig_lvl = 30
        self.throttle_rate = throttle_rate = 0.5
        self.thresh_lo = thresh_lo = 10000
        self.thresh_hi = thresh_hi = 10000
        self.samp_rate = samp_rate = 15e6
        self.lpf_trans = lpf_trans = 500e3
        self.lpf_cutoff = lpf_cutoff = .45e6
        self.look_ahead = look_ahead = 10
        self.decim = decim = 1
        self.alpha_0 = alpha_0 = 1
        self.alpha = alpha = 0.01

        ##################################################
        # Blocks
        ##################################################
        self._tune_tool_bar = Qt.QToolBar(self)
        self._tune_tool_bar.addWidget(Qt.QLabel('tune' + ": "))
        self._tune_line_edit = Qt.QLineEdit(str(self.tune))
        self._tune_tool_bar.addWidget(self._tune_line_edit)
        self._tune_line_edit.returnPressed.connect(
            lambda: self.set_tune(eng_notation.str_to_num(str(self._tune_line_edit.text()))))
        self.top_grid_layout.addWidget(self._tune_tool_bar, 1, 4, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._trig_lvl_tool_bar = Qt.QToolBar(self)
        self._trig_lvl_tool_bar.addWidget(Qt.QLabel('trig_lvl' + ": "))
        self._trig_lvl_line_edit = Qt.QLineEdit(str(self.trig_lvl))
        self._trig_lvl_tool_bar.addWidget(self._trig_lvl_line_edit)
        self._trig_lvl_line_edit.returnPressed.connect(
            lambda: self.set_trig_lvl(eng_notation.str_to_num(str(self._trig_lvl_line_edit.text()))))
        self.top_grid_layout.addWidget(self._trig_lvl_tool_bar, 3, 4, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._throttle_rate_tool_bar = Qt.QToolBar(self)
        self._throttle_rate_tool_bar.addWidget(Qt.QLabel('throttle_rate' + ": "))
        self._throttle_rate_line_edit = Qt.QLineEdit(str(self.throttle_rate))
        self._throttle_rate_tool_bar.addWidget(self._throttle_rate_line_edit)
        self._throttle_rate_line_edit.returnPressed.connect(
            lambda: self.set_throttle_rate(eng_notation.str_to_num(str(self._throttle_rate_line_edit.text()))))
        self.top_grid_layout.addWidget(self._throttle_rate_tool_bar, 3, 5, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._thresh_lo_tool_bar = Qt.QToolBar(self)
        self._thresh_lo_tool_bar.addWidget(Qt.QLabel('thresh_lo' + ": "))
        self._thresh_lo_line_edit = Qt.QLineEdit(str(self.thresh_lo))
        self._thresh_lo_tool_bar.addWidget(self._thresh_lo_line_edit)
        self._thresh_lo_line_edit.returnPressed.connect(
            lambda: self.set_thresh_lo(eng_notation.str_to_num(str(self._thresh_lo_line_edit.text()))))
        self.top_grid_layout.addWidget(self._thresh_lo_tool_bar, 0, 7, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(7, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._thresh_hi_tool_bar = Qt.QToolBar(self)
        self._thresh_hi_tool_bar.addWidget(Qt.QLabel('thresh_hi' + ": "))
        self._thresh_hi_line_edit = Qt.QLineEdit(str(self.thresh_hi))
        self._thresh_hi_tool_bar.addWidget(self._thresh_hi_line_edit)
        self._thresh_hi_line_edit.returnPressed.connect(
            lambda: self.set_thresh_hi(eng_notation.str_to_num(str(self._thresh_hi_line_edit.text()))))
        self.top_grid_layout.addWidget(self._thresh_hi_tool_bar, 0, 6, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 7):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel('samp_rate' + ": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
            lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text()))))
        self.top_grid_layout.addWidget(self._samp_rate_tool_bar, 0, 4, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._lpf_trans_tool_bar = Qt.QToolBar(self)
        self._lpf_trans_tool_bar.addWidget(Qt.QLabel('lpf_trans' + ": "))
        self._lpf_trans_line_edit = Qt.QLineEdit(str(self.lpf_trans))
        self._lpf_trans_tool_bar.addWidget(self._lpf_trans_line_edit)
        self._lpf_trans_line_edit.returnPressed.connect(
            lambda: self.set_lpf_trans(eng_notation.str_to_num(str(self._lpf_trans_line_edit.text()))))
        self.top_grid_layout.addWidget(self._lpf_trans_tool_bar, 2, 5, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._lpf_cutoff_tool_bar = Qt.QToolBar(self)
        self._lpf_cutoff_tool_bar.addWidget(Qt.QLabel('lpf_cutoff' + ": "))
        self._lpf_cutoff_line_edit = Qt.QLineEdit(str(self.lpf_cutoff))
        self._lpf_cutoff_tool_bar.addWidget(self._lpf_cutoff_line_edit)
        self._lpf_cutoff_line_edit.returnPressed.connect(
            lambda: self.set_lpf_cutoff(eng_notation.str_to_num(str(self._lpf_cutoff_line_edit.text()))))
        self.top_grid_layout.addWidget(self._lpf_cutoff_tool_bar, 2, 4, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._alpha_0_tool_bar = Qt.QToolBar(self)
        self._alpha_0_tool_bar.addWidget(Qt.QLabel('alpha_0' + ": "))
        self._alpha_0_line_edit = Qt.QLineEdit(str(self.alpha_0))
        self._alpha_0_tool_bar.addWidget(self._alpha_0_line_edit)
        self._alpha_0_line_edit.returnPressed.connect(
            lambda: self.set_alpha_0(eng_notation.str_to_num(str(self._alpha_0_line_edit.text()))))
        self.top_grid_layout.addWidget(self._alpha_0_tool_bar, 2, 6, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 7):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(alpha_0, 1)
        self.sigmf_source_0 = gr_sigmf.source('/captures/20191214/NEXRAD_2019-12-14T23:24:46Z.sigmf-data', "ci16" + ("_le" if sys.byteorder == "little" else "_be"), True)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
            1024*16*100, #size
            samp_rate / decim, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(0, 2)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, .5, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 7, 4, 1, 4)
        for r in range(7, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024*16*100, #size
            samp_rate / decim, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(0, 50)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, trig_lvl, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 4, 4, 3, 4)
        for r in range(4, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            decim,
            firdes.low_pass(
                1,
                samp_rate,
                lpf_cutoff,
                lpf_trans,
                firdes.WIN_HAMMING,
                6.76))
        self._look_ahead_tool_bar = Qt.QToolBar(self)
        self._look_ahead_tool_bar.addWidget(Qt.QLabel('look_ahead' + ": "))
        self._look_ahead_line_edit = Qt.QLineEdit(str(self.look_ahead))
        self._look_ahead_tool_bar.addWidget(self._look_ahead_line_edit)
        self._look_ahead_line_edit.returnPressed.connect(
            lambda: self.set_look_ahead(int(str(self._look_ahead_line_edit.text()))))
        self.top_grid_layout.addWidget(self._look_ahead_tool_bar, 1, 6, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 7):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0.set_frequency_range(0, samp_rate /decim)
        self._fosphor_qt_sink_c_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._fosphor_qt_sink_c_0_win, 0, 0, 8, 4)
        for r in range(0, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_short*2, samp_rate*throttle_rate,True)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(thresh_hi, thresh_lo, 0)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_cc(1.0 / 65536.0, 1)
        self.blocks_interleaved_short_to_complex_0 = blocks.interleaved_short_to_complex(True, False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, tune, 1, 0, 0)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)
        self._alpha_tool_bar = Qt.QToolBar(self)
        self._alpha_tool_bar.addWidget(Qt.QLabel('alpha' + ": "))
        self._alpha_line_edit = Qt.QLineEdit(str(self.alpha))
        self._alpha_tool_bar.addWidget(self._alpha_line_edit)
        self._alpha_line_edit.returnPressed.connect(
            lambda: self.set_alpha(eng_notation.str_to_num(str(self._alpha_line_edit.text()))))
        self.top_grid_layout.addWidget(self._alpha_tool_bar, 1, 7, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(7, 8):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.single_pole_iir_filter_xx_0, 0))
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.blocks_multiply_const_xx_0, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_interleaved_short_to_complex_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.fosphor_qt_sink_c_0, 0))
        self.connect((self.sigmf_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_threshold_ff_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "nexrad_playback_sigmf")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_tune(self):
        return self.tune

    def set_tune(self, tune):
        self.tune = tune
        Qt.QMetaObject.invokeMethod(self._tune_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.tune)))
        self.analog_sig_source_x_0.set_frequency(self.tune)

    def get_trig_lvl(self):
        return self.trig_lvl

    def set_trig_lvl(self, trig_lvl):
        self.trig_lvl = trig_lvl
        Qt.QMetaObject.invokeMethod(self._trig_lvl_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.trig_lvl)))
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, self.trig_lvl, 0, 0, "")

    def get_throttle_rate(self):
        return self.throttle_rate

    def set_throttle_rate(self, throttle_rate):
        self.throttle_rate = throttle_rate
        Qt.QMetaObject.invokeMethod(self._throttle_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.throttle_rate)))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.throttle_rate)

    def get_thresh_lo(self):
        return self.thresh_lo

    def set_thresh_lo(self, thresh_lo):
        self.thresh_lo = thresh_lo
        Qt.QMetaObject.invokeMethod(self._thresh_lo_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.thresh_lo)))
        self.blocks_threshold_ff_0.set_hi(self.thresh_lo)

    def get_thresh_hi(self):
        return self.thresh_hi

    def set_thresh_hi(self, thresh_hi):
        self.thresh_hi = thresh_hi
        Qt.QMetaObject.invokeMethod(self._thresh_hi_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.thresh_hi)))
        self.blocks_threshold_ff_0.set_lo(self.thresh_hi)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.throttle_rate)
        self.fosphor_qt_sink_c_0.set_frequency_range(0, self.samp_rate /self.decim)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cutoff, self.lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate / self.decim)

    def get_lpf_trans(self):
        return self.lpf_trans

    def set_lpf_trans(self, lpf_trans):
        self.lpf_trans = lpf_trans
        Qt.QMetaObject.invokeMethod(self._lpf_trans_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.lpf_trans)))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cutoff, self.lpf_trans, firdes.WIN_HAMMING, 6.76))

    def get_lpf_cutoff(self):
        return self.lpf_cutoff

    def set_lpf_cutoff(self, lpf_cutoff):
        self.lpf_cutoff = lpf_cutoff
        Qt.QMetaObject.invokeMethod(self._lpf_cutoff_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.lpf_cutoff)))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cutoff, self.lpf_trans, firdes.WIN_HAMMING, 6.76))

    def get_look_ahead(self):
        return self.look_ahead

    def set_look_ahead(self, look_ahead):
        self.look_ahead = look_ahead
        Qt.QMetaObject.invokeMethod(self._look_ahead_line_edit, "setText", Qt.Q_ARG("QString", str(self.look_ahead)))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.fosphor_qt_sink_c_0.set_frequency_range(0, self.samp_rate /self.decim)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate / self.decim)

    def get_alpha_0(self):
        return self.alpha_0

    def set_alpha_0(self, alpha_0):
        self.alpha_0 = alpha_0
        Qt.QMetaObject.invokeMethod(self._alpha_0_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.alpha_0)))
        self.single_pole_iir_filter_xx_0.set_taps(self.alpha_0)

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        Qt.QMetaObject.invokeMethod(self._alpha_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.alpha)))





def main(top_block_cls=nexrad_playback_sigmf, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
