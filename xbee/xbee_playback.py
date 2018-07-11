#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Xbee Playback
# Generated: Sat Apr 14 22:18:51 2018
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
from gnuradio import fosphor
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import math
import pmt
import sip
import sys
from gnuradio import qtgui


class xbee_playback(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Xbee Playback")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Xbee Playback")
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

        self.settings = Qt.QSettings("GNU Radio", "xbee_playback")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 12e6
        self.baud = baud = 95.2e3
        self.samps_per_symb = samps_per_symb = samp_rate/30/baud
        self.offset = offset = -1500

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel('SAMP_RATE'+": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._samp_rate_tool_bar, 9,0,1,1)
        self._offset_tool_bar = Qt.QToolBar(self)
        self._offset_tool_bar.addWidget(Qt.QLabel('offset'+": "))
        self._offset_line_edit = Qt.QLineEdit(str(self.offset))
        self._offset_tool_bar.addWidget(self._offset_line_edit)
        self._offset_line_edit.returnPressed.connect(
        	lambda: self.set_offset(eng_notation.str_to_num(str(self._offset_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._offset_tool_bar, 9,2,1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
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
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_time_raster_sink_x_0 = qtgui.time_raster_sink_b(
        	samp_rate,
        	20,
        	1000,
        	([]),
        	([]),
        	"",
        	1,
        	)

        self.qtgui_time_raster_sink_x_0.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_raster_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/30, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-80, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,4,4)
        self.pfb_channelizer_ccf_0 = pfb.channelizer_ccf(
        	  30,
        	  ([-0.0009440003777854145, -1.9967922852119293e-18, 0.0011775379534810781, -2.1018872363980166e-18, -0.001785947591997683, 1.104649332765264e-17, 0.0028464579954743385, -4.376348750402665e-18, -0.0044487821869552135, 6.047675863462489e-18, 0.006705658044666052, -7.96089705741242e-18, -0.009772991761565208, 1.0012871595263528e-17, 0.013889657333493233, -1.2092975237025114e-17, -0.019461529329419136, 1.4089067934233976e-17, 0.02725801058113575, -1.589354424254493e-17, -0.0389452800154686, 1.7409121104476838e-17, 0.058897972106933594, -1.855409458220539e-17, -0.10325390845537186, 1.9266737149699424e-17, 0.31760919094085693, 0.500455915927887, 0.31760919094085693, 1.9266737149699424e-17, -0.10325390845537186, -1.855409458220539e-17, 0.058897972106933594, 1.7409121104476838e-17, -0.0389452800154686, -1.589354424254493e-17, 0.02725801058113575, 1.4089067934233976e-17, -0.019461529329419136, -1.2092975237025114e-17, 0.013889657333493233, 1.0012871595263528e-17, -0.009772991761565208, -7.96089705741242e-18, 0.006705658044666052, 6.047675863462489e-18, -0.0044487821869552135, -4.376348750402665e-18, 0.0028464579954743385, 1.104649332765264e-17, -0.001785947591997683, -2.1018872363980166e-18, 0.0011775379534810781, -1.9967922852119293e-18, -0.0009440003777854145]),
        	  1.0,
        	  100)
        self.pfb_channelizer_ccf_0.set_channel_map(([]))
        self.pfb_channelizer_ccf_0.declare_sample_delay(0)

        self.fosphor_glfw_sink_c_0 = fosphor.glfw_sink_c()
        self.fosphor_glfw_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_glfw_sink_c_0.set_frequency_range(0, samp_rate)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(samps_per_symb*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/zleffke/captures/xbee/xbee_12MSPS.fc32', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1*offset, 1, 0)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.fosphor_glfw_sink_c_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.pfb_channelizer_ccf_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.qtgui_time_raster_sink_x_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 10), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 10), (self.blocks_delay_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 10), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 1), (self.blocks_null_sink_0, 1))
        self.connect((self.pfb_channelizer_ccf_0, 10), (self.blocks_null_sink_0, 10))
        self.connect((self.pfb_channelizer_ccf_0, 11), (self.blocks_null_sink_0, 11))
        self.connect((self.pfb_channelizer_ccf_0, 12), (self.blocks_null_sink_0, 12))
        self.connect((self.pfb_channelizer_ccf_0, 13), (self.blocks_null_sink_0, 13))
        self.connect((self.pfb_channelizer_ccf_0, 14), (self.blocks_null_sink_0, 14))
        self.connect((self.pfb_channelizer_ccf_0, 15), (self.blocks_null_sink_0, 15))
        self.connect((self.pfb_channelizer_ccf_0, 16), (self.blocks_null_sink_0, 16))
        self.connect((self.pfb_channelizer_ccf_0, 17), (self.blocks_null_sink_0, 17))
        self.connect((self.pfb_channelizer_ccf_0, 18), (self.blocks_null_sink_0, 18))
        self.connect((self.pfb_channelizer_ccf_0, 19), (self.blocks_null_sink_0, 19))
        self.connect((self.pfb_channelizer_ccf_0, 2), (self.blocks_null_sink_0, 2))
        self.connect((self.pfb_channelizer_ccf_0, 20), (self.blocks_null_sink_0, 20))
        self.connect((self.pfb_channelizer_ccf_0, 21), (self.blocks_null_sink_0, 21))
        self.connect((self.pfb_channelizer_ccf_0, 22), (self.blocks_null_sink_0, 22))
        self.connect((self.pfb_channelizer_ccf_0, 23), (self.blocks_null_sink_0, 23))
        self.connect((self.pfb_channelizer_ccf_0, 24), (self.blocks_null_sink_0, 24))
        self.connect((self.pfb_channelizer_ccf_0, 25), (self.blocks_null_sink_0, 25))
        self.connect((self.pfb_channelizer_ccf_0, 26), (self.blocks_null_sink_0, 26))
        self.connect((self.pfb_channelizer_ccf_0, 27), (self.blocks_null_sink_0, 27))
        self.connect((self.pfb_channelizer_ccf_0, 28), (self.blocks_null_sink_0, 28))
        self.connect((self.pfb_channelizer_ccf_0, 29), (self.blocks_null_sink_0, 29))
        self.connect((self.pfb_channelizer_ccf_0, 3), (self.blocks_null_sink_0, 3))
        self.connect((self.pfb_channelizer_ccf_0, 4), (self.blocks_null_sink_0, 4))
        self.connect((self.pfb_channelizer_ccf_0, 5), (self.blocks_null_sink_0, 5))
        self.connect((self.pfb_channelizer_ccf_0, 6), (self.blocks_null_sink_0, 6))
        self.connect((self.pfb_channelizer_ccf_0, 7), (self.blocks_null_sink_0, 7))
        self.connect((self.pfb_channelizer_ccf_0, 8), (self.blocks_null_sink_0, 8))
        self.connect((self.pfb_channelizer_ccf_0, 9), (self.blocks_null_sink_0, 9))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "xbee_playback")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samps_per_symb(self.samp_rate/30/self.baud)
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/30)
        self.fosphor_glfw_sink_c_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_baud(self):
        return self.baud

    def set_baud(self, baud):
        self.baud = baud
        self.set_samps_per_symb(self.samp_rate/30/self.baud)

    def get_samps_per_symb(self):
        return self.samps_per_symb

    def set_samps_per_symb(self, samps_per_symb):
        self.samps_per_symb = samps_per_symb
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samps_per_symb*(1+0.0))

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        Qt.QMetaObject.invokeMethod(self._offset_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.offset)))
        self.analog_sig_source_x_0.set_frequency(-1*self.offset)


def main(top_block_cls=xbee_playback, options=None):

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
