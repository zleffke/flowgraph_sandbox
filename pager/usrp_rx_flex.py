#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: USRP FLEX Pager Receiver (Single Channel)
# Generated: Tue Apr 10 22:04:23 2018
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
from gnuradio import filter
from gnuradio import fosphor
from gnuradio import gr
from gnuradio import pager
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import math
import os, math
import sip
import sys
import time
from gnuradio import qtgui


class usrp_rx_flex(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "USRP FLEX Pager Receiver (Single Channel)")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("USRP FLEX Pager Receiver (Single Channel)")
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

        self.settings = Qt.QSettings("GNU Radio", "usrp_rx_flex")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.symbol_rate = symbol_rate = 3200
        self.deviation = deviation = 4800
        self.decim = decim = 20
        self.adc_rate = adc_rate = 64e6
        self.sample_rate = sample_rate = adc_rate/decim
        self.passband = passband = 2*(deviation+symbol_rate)
        self.channel_rate = channel_rate = 8*3200
        self.channel_taps = channel_taps = firdes.low_pass(10, sample_rate, passband/2.0, (channel_rate-passband)/2.0)
        self.rx_gain = rx_gain = 40
        self.rx_freq = rx_freq = 931e6
        self.offset = offset = 0
        self.nchan_taps = nchan_taps = len(channel_taps)
        self.ma_ntaps = ma_ntaps = int(channel_rate/symbol_rate)
        self.demod_k = demod_k = 3*channel_rate/(2*math.pi*deviation)
        self.config_filename = config_filename = os.environ["HOME"]+"/.gnuradio/config.conf"
        self.channel_decim = channel_decim = int(sample_rate/channel_rate)
        self.bb_interp = bb_interp = 5
        self.bb_decim = bb_decim = 8
        self.baseband_rate = baseband_rate = 16000

        ##################################################
        # Blocks
        ##################################################
        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel('GAIN'+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_gain_tool_bar, 0,2,1,1)
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('FREQ'+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_freq_tool_bar, 0,1,1,1)
        self._offset_tool_bar = Qt.QToolBar(self)
        self._offset_tool_bar.addWidget(Qt.QLabel("offset"+": "))
        self._offset_line_edit = Qt.QLineEdit(str(self.offset))
        self._offset_tool_bar.addWidget(self._offset_line_edit)
        self._offset_line_edit.returnPressed.connect(
        	lambda: self.set_offset(eng_notation.str_to_num(str(self._offset_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._offset_tool_bar, 0,0,1,1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		otw_format='sc16',
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(sample_rate)
        self.uhd_usrp_source_0.set_center_freq(rx_freq, 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=bb_decim,
                decimation=bb_interp,
                taps=([1.0/ma_ntaps,]*ma_ntaps*bb_interp),
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	sample_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
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
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.pager_slicer_fb_0 = pager.slicer_fb(1e-6)
        self.pager_flex_sync_0 = pager.flex_sync()
        self.pager_flex_deinterleave_0_1_0 = pager.flex_deinterleave()
        self.pager_flex_deinterleave_0_1 = pager.flex_deinterleave()
        self.pager_flex_deinterleave_0_0 = pager.flex_deinterleave()
        self.pager_flex_deinterleave_0 = pager.flex_deinterleave()
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(channel_decim, (channel_taps), offset, sample_rate)
        self.fosphor_glfw_sink_c_0 = fosphor.glfw_sink_c()
        self.fosphor_glfw_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_glfw_sink_c_0.set_frequency_range(0, sample_rate)
        self.fm_demod = analog.quadrature_demod_cf(demod_k)
        self.blocks_null_sink_0_2 = blocks.null_sink(gr.sizeof_int*1)
        self.blocks_null_sink_0_1 = blocks.null_sink(gr.sizeof_int*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_int*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_int*1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.fm_demod, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.fm_demod, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.pager_flex_deinterleave_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.pager_flex_deinterleave_0_0, 0), (self.blocks_null_sink_0_2, 0))
        self.connect((self.pager_flex_deinterleave_0_1, 0), (self.blocks_null_sink_0_1, 0))
        self.connect((self.pager_flex_deinterleave_0_1_0, 0), (self.blocks_null_sink_0_0, 0))
        self.connect((self.pager_flex_sync_0, 0), (self.pager_flex_deinterleave_0, 0))
        self.connect((self.pager_flex_sync_0, 3), (self.pager_flex_deinterleave_0_0, 0))
        self.connect((self.pager_flex_sync_0, 2), (self.pager_flex_deinterleave_0_1, 0))
        self.connect((self.pager_flex_sync_0, 1), (self.pager_flex_deinterleave_0_1_0, 0))
        self.connect((self.pager_slicer_fb_0, 0), (self.pager_flex_sync_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.pager_slicer_fb_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.fosphor_glfw_sink_c_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "usrp_rx_flex")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.set_ma_ntaps(int(self.channel_rate/self.symbol_rate))
        self.set_passband(2*(self.deviation+self.symbol_rate))

    def get_deviation(self):
        return self.deviation

    def set_deviation(self, deviation):
        self.deviation = deviation
        self.set_demod_k(3*self.channel_rate/(2*math.pi*self.deviation))
        self.set_passband(2*(self.deviation+self.symbol_rate))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_sample_rate(self.adc_rate/self.decim)

    def get_adc_rate(self):
        return self.adc_rate

    def set_adc_rate(self, adc_rate):
        self.adc_rate = adc_rate
        self.set_sample_rate(self.adc_rate/self.decim)

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.set_channel_taps(firdes.low_pass(10, self.sample_rate, self.passband/2.0, (self.channel_rate-self.passband)/2.0))
        self.set_channel_decim(int(self.sample_rate/self.channel_rate))
        self.uhd_usrp_source_0.set_samp_rate(self.sample_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.sample_rate)
        self.fosphor_glfw_sink_c_0.set_frequency_range(0, self.sample_rate)

    def get_passband(self):
        return self.passband

    def set_passband(self, passband):
        self.passband = passband
        self.set_channel_taps(firdes.low_pass(10, self.sample_rate, self.passband/2.0, (self.channel_rate-self.passband)/2.0))

    def get_channel_rate(self):
        return self.channel_rate

    def set_channel_rate(self, channel_rate):
        self.channel_rate = channel_rate
        self.set_ma_ntaps(int(self.channel_rate/self.symbol_rate))
        self.set_demod_k(3*self.channel_rate/(2*math.pi*self.deviation))
        self.set_channel_taps(firdes.low_pass(10, self.sample_rate, self.passband/2.0, (self.channel_rate-self.passband)/2.0))
        self.set_channel_decim(int(self.sample_rate/self.channel_rate))

    def get_channel_taps(self):
        return self.channel_taps

    def set_channel_taps(self, channel_taps):
        self.channel_taps = channel_taps
        self.set_nchan_taps(len(self.channel_taps))
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.channel_taps))

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)


    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))
        self.uhd_usrp_source_0.set_center_freq(self.rx_freq, 0)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        Qt.QMetaObject.invokeMethod(self._offset_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.offset)))
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.offset)

    def get_nchan_taps(self):
        return self.nchan_taps

    def set_nchan_taps(self, nchan_taps):
        self.nchan_taps = nchan_taps

    def get_ma_ntaps(self):
        return self.ma_ntaps

    def set_ma_ntaps(self, ma_ntaps):
        self.ma_ntaps = ma_ntaps
        self.rational_resampler_xxx_0.set_taps(([1.0/self.ma_ntaps,]*self.ma_ntaps*self.bb_interp))

    def get_demod_k(self):
        return self.demod_k

    def set_demod_k(self, demod_k):
        self.demod_k = demod_k
        self.fm_demod.set_gain(self.demod_k)

    def get_config_filename(self):
        return self.config_filename

    def set_config_filename(self, config_filename):
        self.config_filename = config_filename

    def get_channel_decim(self):
        return self.channel_decim

    def set_channel_decim(self, channel_decim):
        self.channel_decim = channel_decim

    def get_bb_interp(self):
        return self.bb_interp

    def set_bb_interp(self, bb_interp):
        self.bb_interp = bb_interp
        self.rational_resampler_xxx_0.set_taps(([1.0/self.ma_ntaps,]*self.ma_ntaps*self.bb_interp))

    def get_bb_decim(self):
        return self.bb_decim

    def set_bb_decim(self, bb_decim):
        self.bb_decim = bb_decim

    def get_baseband_rate(self):
        return self.baseband_rate

    def set_baseband_rate(self, baseband_rate):
        self.baseband_rate = baseband_rate


def main(top_block_cls=usrp_rx_flex, options=None):

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
