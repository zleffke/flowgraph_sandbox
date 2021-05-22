#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Channel 1
# Generated: Mon Apr  9 22:58:28 2018
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
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import math
import sip
import sys
from gnuradio import qtgui


class channel_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Channel 1")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Channel 1")
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

        self.settings = Qt.QSettings("GNU Radio", "channel_1")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48000
        self.rx_loss = rx_loss = 60
        self.offset = offset = 0
        self.noise_amp = noise_amp = 0.1
        self.loss = loss = 30

        ##################################################
        # Blocks
        ##################################################
        self._rx_loss_tool_bar = Qt.QToolBar(self)
        self._rx_loss_tool_bar.addWidget(Qt.QLabel('RX Level Adjust [dB]'+": "))
        self._rx_loss_line_edit = Qt.QLineEdit(str(self.rx_loss))
        self._rx_loss_tool_bar.addWidget(self._rx_loss_line_edit)
        self._rx_loss_line_edit.returnPressed.connect(
        	lambda: self.set_rx_loss(eng_notation.str_to_num(str(self._rx_loss_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._rx_loss_tool_bar)
        self._offset_range = Range(-samp_rate/2, samp_rate/2, 100, 0, 200)
        self._offset_win = RangeWidget(self._offset_range, self.set_offset, 'offset', "counter_slider", float)
        self.top_grid_layout.addWidget(self._offset_win, 8,0,1,4)
        self._noise_amp_tool_bar = Qt.QToolBar(self)
        self._noise_amp_tool_bar.addWidget(Qt.QLabel('Noise'+": "))
        self._noise_amp_line_edit = Qt.QLineEdit(str(self.noise_amp))
        self._noise_amp_tool_bar.addWidget(self._noise_amp_line_edit)
        self._noise_amp_line_edit.returnPressed.connect(
        	lambda: self.set_noise_amp(eng_notation.str_to_num(str(self._noise_amp_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._noise_amp_tool_bar)
        self._loss_tool_bar = Qt.QToolBar(self)
        self._loss_tool_bar.addWidget(Qt.QLabel('Signal Loss [dB]'+": "))
        self._loss_line_edit = Qt.QLineEdit(str(self.loss))
        self._loss_tool_bar.addWidget(self._loss_line_edit)
        self._loss_line_edit.returnPressed.connect(
        	lambda: self.set_loss(eng_notation.str_to_num(str(self._loss_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._loss_tool_bar)
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
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Channel Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.010)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(True)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)

        if not False:
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win, 2,0,4,4)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_gr_complex*1, '0.0.0.0', 9000, 1472, True)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, '0.0.0.0', 9001, 1472, True)
        self.blocks_tag_gate_1_0 = blocks.tag_gate(gr.sizeof_gr_complex * 1, False)
        self.blocks_tag_gate_1_0.set_single_key("")
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((1/pow(10,rx_loss/20.0), ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1/pow(10,loss/20.0), ))
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, offset, 1, 0)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, noise_amp, 0, 8192)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_tag_gate_1_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_tag_gate_1_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.blocks_tag_gate_1_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.blocks_tag_gate_1_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_multiply_xx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "channel_1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_rx_loss(self):
        return self.rx_loss

    def set_rx_loss(self, rx_loss):
        self.rx_loss = rx_loss
        Qt.QMetaObject.invokeMethod(self._rx_loss_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_loss)))
        self.blocks_multiply_const_vxx_0_0.set_k((1/pow(10,self.rx_loss/20.0), ))

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self.analog_sig_source_x_0.set_frequency(self.offset)

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        Qt.QMetaObject.invokeMethod(self._noise_amp_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.noise_amp)))
        self.analog_fastnoise_source_x_0.set_amplitude(self.noise_amp)

    def get_loss(self):
        return self.loss

    def set_loss(self, loss):
        self.loss = loss
        Qt.QMetaObject.invokeMethod(self._loss_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.loss)))
        self.blocks_multiply_const_vxx_0.set_k((1/pow(10,self.loss/20.0), ))


def main(top_block_cls=channel_1, options=None):

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
