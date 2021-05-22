#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: rothr_playback_sigmf
# Author: Zach Leffke
# Description: Generic SigMF Playback
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import fosphor
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import gr_sigmf
import sip
import sys
from gnuradio import qtgui


class rothr_playback_sigmf(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "rothr_playback_sigmf")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("rothr_playback_sigmf")
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

        self.settings = Qt.QSettings("GNU Radio", "rothr_playback_sigmf")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.target_freq = target_freq = 4.575e6
        self.rec_center = rec_center = 9.25e6
        self.tune_offset = tune_offset = target_freq - rec_center
        self.trig_lvl = trig_lvl = 0
        self.throttle_rate = throttle_rate = 1.0
        self.samp_rate = samp_rate = 12.5e6
        self.decim = decim = 10
        self.cutoff = cutoff = 25e3

        ##################################################
        # Blocks
        ##################################################
        self._trig_lvl_tool_bar = Qt.QToolBar(self)
        self._trig_lvl_tool_bar.addWidget(Qt.QLabel("trig_lvl"+": "))
        self._trig_lvl_line_edit = Qt.QLineEdit(str(self.trig_lvl))
        self._trig_lvl_tool_bar.addWidget(self._trig_lvl_line_edit)
        self._trig_lvl_line_edit.returnPressed.connect(
        	lambda: self.set_trig_lvl(eng_notation.str_to_num(str(self._trig_lvl_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._trig_lvl_tool_bar, 7, 6, 1, 2)
        for r in range(7, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._throttle_rate_tool_bar = Qt.QToolBar(self)
        self._throttle_rate_tool_bar.addWidget(Qt.QLabel("throttle_rate"+": "))
        self._throttle_rate_line_edit = Qt.QLineEdit(str(self.throttle_rate))
        self._throttle_rate_tool_bar.addWidget(self._throttle_rate_line_edit)
        self._throttle_rate_line_edit.returnPressed.connect(
        	lambda: self.set_throttle_rate(eng_notation.str_to_num(str(self._throttle_rate_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._throttle_rate_tool_bar, 4, 6, 1, 2)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._target_freq_tool_bar = Qt.QToolBar(self)
        self._target_freq_tool_bar.addWidget(Qt.QLabel("target_freq"+": "))
        self._target_freq_line_edit = Qt.QLineEdit(str(self.target_freq))
        self._target_freq_tool_bar.addWidget(self._target_freq_line_edit)
        self._target_freq_line_edit.returnPressed.connect(
        	lambda: self.set_target_freq(eng_notation.str_to_num(str(self._target_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._target_freq_tool_bar, 5, 4, 1, 2)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel("samp_rate"+": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._samp_rate_tool_bar, 4, 4, 1, 2)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._cutoff_tool_bar = Qt.QToolBar(self)
        self._cutoff_tool_bar.addWidget(Qt.QLabel("cutoff"+": "))
        self._cutoff_line_edit = Qt.QLineEdit(str(self.cutoff))
        self._cutoff_tool_bar.addWidget(self._cutoff_line_edit)
        self._cutoff_line_edit.returnPressed.connect(
        	lambda: self.set_cutoff(eng_notation.str_to_num(str(self._cutoff_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._cutoff_tool_bar, 6, 4, 1, 2)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.sigmf_source_0 = gr_sigmf.source('/captures/20210516/HF-FULL_2021-05-17T00:43:31Z.sigmf-data', "ci16" + ("_le" if sys.byteorder == "little" else "_be"), True)
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
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
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

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 8, 0, 4, 4)
        for r in range(8, 12):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate/decim/decim, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0.set_y_axis(-30, 20)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, trig_lvl, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not False:
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 2, 4, 2, 4)
        for r in range(2, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-80, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 4, 0, 4, 4)
        for r in range(4, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/decim, cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.fosphor_qt_sink_c_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0.set_frequency_range(target_freq, samp_rate / decim)
        self._fosphor_qt_sink_c_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._fosphor_qt_sink_c_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate*throttle_rate,True)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_cc(1.0 / 65536.0)
        self.blocks_interleaved_short_to_complex_0 = blocks.interleaved_short_to_complex(True, False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1*tune_offset, 1, 0)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-1, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.blocks_multiply_const_xx_0, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.fosphor_qt_sink_c_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.sigmf_source_0, 0), (self.blocks_interleaved_short_to_complex_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rothr_playback_sigmf")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_target_freq(self):
        return self.target_freq

    def set_target_freq(self, target_freq):
        self.target_freq = target_freq
        self.set_tune_offset(self.target_freq - self.rec_center)
        Qt.QMetaObject.invokeMethod(self._target_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.target_freq)))
        self.fosphor_qt_sink_c_0.set_frequency_range(self.target_freq, self.samp_rate / self.decim)

    def get_rec_center(self):
        return self.rec_center

    def set_rec_center(self, rec_center):
        self.rec_center = rec_center
        self.set_tune_offset(self.target_freq - self.rec_center)

    def get_tune_offset(self):
        return self.tune_offset

    def set_tune_offset(self, tune_offset):
        self.tune_offset = tune_offset
        self.analog_sig_source_x_0.set_frequency(-1*self.tune_offset)

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

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate/self.decim/self.decim)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.fosphor_qt_sink_c_0.set_frequency_range(self.target_freq, self.samp_rate / self.decim)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.throttle_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate / self.decim)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate/self.decim/self.decim)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.fosphor_qt_sink_c_0.set_frequency_range(self.target_freq, self.samp_rate / self.decim)

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        Qt.QMetaObject.invokeMethod(self._cutoff_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.cutoff)))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.cutoff, 1e3, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=rothr_playback_sigmf, options=None):

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
