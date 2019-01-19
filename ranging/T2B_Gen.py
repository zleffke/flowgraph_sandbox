#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: T2B Gen
# Generated: Sat Nov  3 14:21:34 2018
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
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
from gnuradio import qtgui


class T2B_Gen(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "T2B Gen")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("T2B Gen")
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

        self.settings = Qt.QSettings("GNU Radio", "T2B_Gen")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250e3
        self.noise_amp = noise_amp = 0.01
        self.c6 = c6 = (1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1)
        self.c5 = c5 = (1,1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1)
        self.c4 = c4 = (1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1)
        self.c3 = c3 = (1,1,1,-1,-1,-1,1,-1,1,1,-1)
        self.c2 = c2 = (1,1,1,-1,-1,1,-1)
        self.c1 = c1 = (1,-1)

        ##################################################
        # Blocks
        ##################################################
        self._noise_amp_range = Range(0, 100, 0.001, 0.01, 200)
        self._noise_amp_win = RangeWidget(self._noise_amp_range, self.set_noise_amp, "noise_amp", "counter_slider", float)
        self.top_grid_layout.addWidget(self._noise_amp_win)
        self.root_raised_cosine_filter_0_0 = filter.fir_filter_ccf(5, firdes.root_raised_cosine(
        	5, samp_rate, samp_rate/5, 0.5, 30))
        self.root_raised_cosine_filter_0 = filter.interp_fir_filter_ccf(5, firdes.root_raised_cosine(
        	1, samp_rate, samp_rate/5, 0.5, 30))
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

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
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate*5, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-80, -20)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [0, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [9, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.digital_map_bb_0 = digital.map_bb(([-1,1]))
        self.digital_corr_est_cc_0_1 = digital.corr_est_cc((c3), 5, 0, 0.9)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_cc(5*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_1_0_0_0 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_vector_source_x_0_0_0_0_0_0 = blocks.vector_source_s(c6, True, 1, [])
        self.blocks_vector_source_x_0_0_0_0_0 = blocks.vector_source_s(c5, True, 1, [])
        self.blocks_vector_source_x_0_0_0_0 = blocks.vector_source_s(c4, True, 1, [])
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_s(c3, True, 1, [])
        self.blocks_vector_source_x_0_0 = blocks.vector_source_s(c2, True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_s(c1, True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_short*1, 1e6,True)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_null_sink_0_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_const_vxx_0_1_0_0_0 = blocks.multiply_const_vss((-1, ))
        self.blocks_multiply_const_vxx_0_1_0_0 = blocks.multiply_const_vss((1, ))
        self.blocks_multiply_const_vxx_0_1_0 = blocks.multiply_const_vss((-1, ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vss((-1, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vss((1, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vss((2, ))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.blocks_complex_to_real_0_1 = blocks.complex_to_real(1)
        self.blocks_char_to_float_1_0_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vss(1)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, noise_amp, 0, 8192)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_char_to_float_1_0_0_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_complex_to_real_0_1, 0), (self.digital_binary_slicer_fb_1_0_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0_1_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0_1_0_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_multiply_const_vxx_0_1_0_0_0, 0), (self.blocks_add_xx_0, 5))
        self.connect((self.blocks_short_to_float_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.blocks_vector_source_x_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_0, 0))
        self.connect((self.blocks_vector_source_x_0_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_0_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_0_0_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_binary_slicer_fb_1_0_0_0, 0), (self.blocks_char_to_float_1_0_0_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_corr_est_cc_0_1, 1), (self.blocks_complex_to_real_0_1, 0))
        self.connect((self.digital_corr_est_cc_0_1, 0), (self.blocks_null_sink_0_1, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.digital_corr_est_cc_0_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "T2B_Gen")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(5, self.samp_rate, self.samp_rate/5, 0.5, 30))
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.samp_rate/5, 0.5, 30))
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate*5)

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_fastnoise_source_x_0.set_amplitude(self.noise_amp)

    def get_c6(self):
        return self.c6

    def set_c6(self, c6):
        self.c6 = c6
        self.blocks_vector_source_x_0_0_0_0_0_0.set_data(self.c6, [])

    def get_c5(self):
        return self.c5

    def set_c5(self, c5):
        self.c5 = c5
        self.blocks_vector_source_x_0_0_0_0_0.set_data(self.c5, [])

    def get_c4(self):
        return self.c4

    def set_c4(self, c4):
        self.c4 = c4
        self.blocks_vector_source_x_0_0_0_0.set_data(self.c4, [])

    def get_c3(self):
        return self.c3

    def set_c3(self, c3):
        self.c3 = c3
        self.blocks_vector_source_x_0_0_0.set_data(self.c3, [])

    def get_c2(self):
        return self.c2

    def set_c2(self, c2):
        self.c2 = c2
        self.blocks_vector_source_x_0_0.set_data(self.c2, [])

    def get_c1(self):
        return self.c1

    def set_c1(self, c1):
        self.c1 = c1
        self.blocks_vector_source_x_0.set_data(self.c1, [])


def main(top_block_cls=T2B_Gen, options=None):

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
