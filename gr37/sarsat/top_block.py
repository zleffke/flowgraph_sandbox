#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed May  2 22:47:47 2018
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
from gnuradio import fosphor
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import math
import pmt
import sarsat
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, meta_rate=1):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.meta_rate = meta_rate

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 500e3
        self.decim = decim = 10
        self.baud = baud = 4800
        self.samps_per_symb = samps_per_symb = (samp_rate/decim*(24.0/25.0))/ baud

        ##################################################
        # Blocks
        ##################################################
        self.sarsat_sarp_msg_extract_0 = sarsat.sarp_msg_extract()
        self.sarsat_pds_frame_sync_0 = sarsat.pds_frame_sync('pds_sync')
        self.sarsat_biphase_l_decode_bb_0 = sarsat.biphase_l_decode_bb()
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=24,
                decimation=25,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=10,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_number_sink_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0_0_0_0.set_update_time(0.010)
        self.qtgui_number_sink_0_0_0_0.set_title("")

        labels = ['Freq Offset', 'Phase', 'Error', '', '',
                  '', '', '', '', '']
        units = ['Hz', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_0_0.set_min(i, -32767)
            self.qtgui_number_sink_0_0_0_0.set_max(i, 32767)
            self.qtgui_number_sink_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_0_win, 3,4,1,4)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-80, 0)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,4,3,4)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate/decim, 5e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.fosphor_qt_sink_c_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0.set_frequency_range(0, samp_rate)
        self._fosphor_qt_sink_c_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._fosphor_qt_sink_c_0_win, 0,0,4,4)
        self.digital_correlate_access_code_tag_xx_0 = digital.correlate_access_code_tag_bb('010000101011101100011111', 0, 'pds_sync')
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(samps_per_symb*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate*10,True)
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.float_t, 'rfo')
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_float, 1, 1, "rfo")
        self.blocks_socket_pdu_0_0 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '8000', 10000, False)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '52001', 10000, False)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((samp_rate/(2*math.pi), ))
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(10000, 0.0001, 4000, 1)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_keep_one_in_n_0_0 = blocks.keep_one_in_n(gr.sizeof_float*1, int(samp_rate*meta_rate))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/zleffke/captures/sarsat/NOAA18_20161115_131537.305805540_UTC_500k.c32', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.analog_pll_freqdet_cf_0 = analog.pll_freqdet_cf(math.pi/200, math.pi/10, -math.pi/10)
        self.analog_pll_carriertracking_cc_0 = analog.pll_carriertracking_cc(math.pi/200, math.pi/10, -math.pi/10)
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=int(samp_rate / decim * 24 / 25),
        	quad_rate=int(samp_rate / decim * 24 / 25),
        	tau=75e-6,
        	max_dev=5e3,
          )
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.blocks_socket_pdu_0, 'pdus'))
        self.msg_connect((self.sarsat_pds_frame_sync_0, 'out'), (self.sarsat_sarp_msg_extract_0, 'in'))
        self.msg_connect((self.sarsat_sarp_msg_extract_0, 'valid'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.sarsat_sarp_msg_extract_0, 'valid'), (self.blocks_socket_pdu_0_0, 'pdus'))
        self.connect((self.analog_agc2_xx_0, 0), (self.analog_pll_carriertracking_cc_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.analog_pll_freqdet_cf_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.fosphor_qt_sink_c_0, 0))
        self.connect((self.analog_nbfm_rx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.analog_pll_carriertracking_cc_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.analog_pll_freqdet_cf_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_keep_one_in_n_0_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_keep_one_in_n_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_number_sink_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_tagged_stream_to_pdu_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.sarsat_biphase_l_decode_bb_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0, 0), (self.sarsat_pds_frame_sync_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.sarsat_biphase_l_decode_bb_0, 0), (self.digital_correlate_access_code_tag_xx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_meta_rate(self):
        return self.meta_rate

    def set_meta_rate(self, meta_rate):
        self.meta_rate = meta_rate
        self.blocks_keep_one_in_n_0_0.set_n(int(self.samp_rate*self.meta_rate))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samps_per_symb((self.samp_rate/self.decim*(24.0/25.0))/ self.baud)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, 5e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.fosphor_qt_sink_c_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*10)
        self.blocks_multiply_const_vxx_1.set_k((self.samp_rate/(2*math.pi), ))
        self.blocks_keep_one_in_n_0_0.set_n(int(self.samp_rate*self.meta_rate))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_samps_per_symb((self.samp_rate/self.decim*(24.0/25.0))/ self.baud)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, 5e3, 1e3, firdes.WIN_HAMMING, 6.76))

    def get_baud(self):
        return self.baud

    def set_baud(self, baud):
        self.baud = baud
        self.set_samps_per_symb((self.samp_rate/self.decim*(24.0/25.0))/ self.baud)

    def get_samps_per_symb(self):
        return self.samps_per_symb

    def set_samps_per_symb(self, samps_per_symb):
        self.samps_per_symb = samps_per_symb
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samps_per_symb*(1+0.0))


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--meta-rate", dest="meta_rate", type="eng_float", default=eng_notation.num_to_str(1),
        help="Set meta_rate [default=%default]")
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(meta_rate=options.meta_rate)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
