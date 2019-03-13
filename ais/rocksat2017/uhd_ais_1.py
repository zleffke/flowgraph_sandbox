#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Uhd Ais 1
# Generated: Sat Dec 17 00:02:37 2016
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
from optparse import OptionParser
import ais
import math
import sip
import sys
from gnuradio import qtgui


class uhd_ais_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Uhd Ais 1")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Uhd Ais 1")
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

        self.settings = Qt.QSettings("GNU Radio", "uhd_ais_1")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250e3
        self.decim = decim = 5
        self.baud = baud = 9600
        self.samp_per_sym = samp_per_sym = (samp_rate/decim/50*48)/baud
        self.rx_gain = rx_gain = 45
        self.fsk_deviation = fsk_deviation = 10e3
        self.freq = freq = 162e6
        self.filter_taps = filter_taps = firdes.low_pass(1,samp_rate, samp_rate/2, 50000, firdes.WIN_FLATTOP, 6.76)

        ##################################################
        # Blocks
        ##################################################
        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel("rx_gain"+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_gain_tool_bar, 8,0,1,2)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=50,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=50,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"", #name
                2 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.01)
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
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-120, -40)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 0,0,4,4)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.01)
        self.qtgui_freq_sink_x_0.set_y_axis(-120, -40)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
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
        colors = ["green", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 4,0,4,4)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/decim, 12.5e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/decim, 12.5e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fft_filter_ccc_0_0 = filter.freq_xlating_fft_filter_ccc(decim, (filter_taps), -25e3, samp_rate)
        self.freq_xlating_fft_filter_ccc_0_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0_0.declare_sample_delay(0)
        self.freq_xlating_fft_filter_ccc_0 = filter.freq_xlating_fft_filter_ccc(decim, (filter_taps), 25e3, samp_rate)
        self.freq_xlating_fft_filter_ccc_0.set_nthreads(1)
        self.freq_xlating_fft_filter_ccc_0.declare_sample_delay(0)
        self.digital_hdlc_deframer_bp_0_0 = digital.hdlc_deframer_bp(11, 1000)
        self.digital_hdlc_deframer_bp_0 = digital.hdlc_deframer_bp(11, 1000)
        self.digital_diff_decoder_bb_0_0 = digital.diff_decoder_bb(2)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2)
        self.digital_clock_recovery_mm_xx_0_0 = digital.clock_recovery_mm_ff(samp_per_sym*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(samp_per_sym*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_0_0 = digital.binary_slicer_fb()
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_message_debug_0_1 = blocks.message_debug()
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/leffke/sandbox/ais/captures/ais_20161216_250k_6.32fc', False)
        self.analog_quadrature_demod_cf_0_0 = analog.quadrature_demod_cf((samp_rate/decim)/(2*math.pi*fsk_deviation/8.0))
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf((samp_rate/decim)/(2*math.pi*fsk_deviation/8.0))
        self.ais_pdu_to_nmea_0 = ais.pdu_to_nmea('A')
        self.ais_invert_0_0 = ais.invert()
        self.ais_invert_0 = ais.invert()

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.ais_pdu_to_nmea_0, 'out'), (self.blocks_message_debug_0_1, 'print'))
        self.msg_connect((self.digital_hdlc_deframer_bp_0, 'out'), (self.ais_pdu_to_nmea_0, 'to_nmea'))
        self.msg_connect((self.digital_hdlc_deframer_bp_0_0, 'out'), (self.ais_pdu_to_nmea_0, 'to_nmea'))
        self.connect((self.ais_invert_0, 0), (self.digital_hdlc_deframer_bp_0, 0))
        self.connect((self.ais_invert_0_0, 0), (self.digital_hdlc_deframer_bp_0_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fft_filter_ccc_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.freq_xlating_fft_filter_ccc_0_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0, 0), (self.digital_diff_decoder_bb_0_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0_0, 0), (self.digital_binary_slicer_fb_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.ais_invert_0, 0))
        self.connect((self.digital_diff_decoder_bb_0_0, 0), (self.ais_invert_0_0, 0))
        self.connect((self.freq_xlating_fft_filter_ccc_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.freq_xlating_fft_filter_ccc_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.analog_quadrature_demod_cf_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_waterfall_sink_x_0, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.digital_clock_recovery_mm_xx_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "uhd_ais_1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_per_sym((self.samp_rate/self.decim/50*48)/self.baud)
        self.set_filter_taps(firdes.low_pass(1,self.samp_rate, self.samp_rate/2, 50000, firdes.WIN_FLATTOP, 6.76))
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, 12.5e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, 12.5e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_quadrature_demod_cf_0_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_samp_per_sym((self.samp_rate/self.decim/50*48)/self.baud)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, 12.5e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, 12.5e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.analog_quadrature_demod_cf_0_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))

    def get_baud(self):
        return self.baud

    def set_baud(self, baud):
        self.baud = baud
        self.set_samp_per_sym((self.samp_rate/self.decim/50*48)/self.baud)

    def get_samp_per_sym(self):
        return self.samp_per_sym

    def set_samp_per_sym(self, samp_per_sym):
        self.samp_per_sym = samp_per_sym
        self.digital_clock_recovery_mm_xx_0_0.set_omega(self.samp_per_sym*(1+0.0))
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samp_per_sym*(1+0.0))

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))

    def get_fsk_deviation(self):
        return self.fsk_deviation

    def set_fsk_deviation(self, fsk_deviation):
        self.fsk_deviation = fsk_deviation
        self.analog_quadrature_demod_cf_0_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))
        self.analog_quadrature_demod_cf_0.set_gain((self.samp_rate/self.decim)/(2*math.pi*self.fsk_deviation/8.0))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_filter_taps(self):
        return self.filter_taps

    def set_filter_taps(self, filter_taps):
        self.filter_taps = filter_taps
        self.freq_xlating_fft_filter_ccc_0_0.set_taps((self.filter_taps))
        self.freq_xlating_fft_filter_ccc_0.set_taps((self.filter_taps))


def main(top_block_cls=uhd_ais_1, options=None):

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
