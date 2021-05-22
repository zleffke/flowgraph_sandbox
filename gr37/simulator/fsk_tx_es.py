#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fsk Tx Es
# Generated: Thu Apr  5 16:33:37 2018
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
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import es
import kiss
import pyqt
import sip
import sys
from gnuradio import qtgui


class fsk_tx_es(gr.top_block, Qt.QWidget):

    def __init__(self, fsk_dev=10000, lpf_cutoff=12.5e3, lpf_trans=1e3):
        gr.top_block.__init__(self, "Fsk Tx Es")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fsk Tx Es")
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

        self.settings = Qt.QSettings("GNU Radio", "fsk_tx_es")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.fsk_dev = fsk_dev
        self.lpf_cutoff = lpf_cutoff
        self.lpf_trans = lpf_trans

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48e3
        self.baud = baud = 9600
        self.samps_per_symb = samps_per_symb = int(samp_rate/baud)
        self.mult = mult = (samp_rate)/2/3.141593
        self.bb_gain = bb_gain = 10
        self.alpha = alpha = 0.5

        ##################################################
        # Blocks
        ##################################################
        self._bb_gain_range = Range(0, 10, .01, 10, 200)
        self._bb_gain_win = RangeWidget(self._bb_gain_range, self.set_bb_gain, 'bb_gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._bb_gain_win, 6,0,1,4)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"TX Spectrum", #name
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
        self.pyqt_text_output_0_0 = pyqt.text_output()
        self._pyqt_text_output_0_0_win = self.pyqt_text_output_0_0;
        self.top_grid_layout.addWidget(self._pyqt_text_output_0_0_win, 0,0,2,4)
        self.kiss_kiss_to_pdu_0 = kiss.kiss_to_pdu(True)
        self.kiss_hdlc_framer_0 = kiss.hdlc_framer(preamble_bytes=32, postamble_bytes=16)
        self.es_source_0 = es.source(1*[gr.sizeof_gr_complex], 1, 2, 0)
        self.digital_scrambler_bb_0 = digital.scrambler_bb(0x21, 0x0, 16)
        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=samps_per_symb,
        	bt=alpha,
        	verbose=False,
        	log=False,
        )
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, '0.0.0.0', 9000, 1472, True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.complex_t, 'packet_len')
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_gr_complex * 1, False)
        self.blocks_tag_gate_0.set_single_key("packet_len")
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_gr_complex, 1, 4096*3, "packet_len")
        (self.blocks_stream_to_tagged_stream_0).set_min_output_buffer(17000)
        self.blocks_socket_pdu_0_2 = blocks.socket_pdu("TCP_CLIENT", '0.0.0.0', '8000', 1024, False)
        self.blocks_pdu_to_tagged_stream_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((bb_gain, ))



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_socket_pdu_0_2, 'pdus'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.es_source_0, 'schedule_event'))
        self.msg_connect((self.kiss_hdlc_framer_0, 'out'), (self.blocks_pdu_to_tagged_stream_0_0, 'pdus'))
        self.msg_connect((self.kiss_kiss_to_pdu_0, 'out'), (self.kiss_hdlc_framer_0, 'in'))
        self.msg_connect((self.kiss_kiss_to_pdu_0, 'out'), (self.pyqt_text_output_0_0, 'pdus'))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.digital_gmsk_mod_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0, 0), (self.digital_scrambler_bb_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.kiss_kiss_to_pdu_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_tagged_stream_to_pdu_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.digital_scrambler_bb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.es_source_0, 0), (self.blocks_throttle_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fsk_tx_es")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_fsk_dev(self):
        return self.fsk_dev

    def set_fsk_dev(self, fsk_dev):
        self.fsk_dev = fsk_dev

    def get_lpf_cutoff(self):
        return self.lpf_cutoff

    def set_lpf_cutoff(self, lpf_cutoff):
        self.lpf_cutoff = lpf_cutoff

    def get_lpf_trans(self):
        return self.lpf_trans

    def set_lpf_trans(self, lpf_trans):
        self.lpf_trans = lpf_trans

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samps_per_symb(int(self.samp_rate/self.baud))
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.set_mult((self.samp_rate)/2/3.141593)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)

    def get_baud(self):
        return self.baud

    def set_baud(self, baud):
        self.baud = baud
        self.set_samps_per_symb(int(self.samp_rate/self.baud))

    def get_samps_per_symb(self):
        return self.samps_per_symb

    def set_samps_per_symb(self, samps_per_symb):
        self.samps_per_symb = samps_per_symb

    def get_mult(self):
        return self.mult

    def set_mult(self, mult):
        self.mult = mult

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        self.blocks_multiply_const_vxx_0_0.set_k((self.bb_gain, ))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--fsk-dev", dest="fsk_dev", type="eng_float", default=eng_notation.num_to_str(10000),
        help="Set FSK Deviation [default=%default]")
    parser.add_option(
        "", "--lpf-cutoff", dest="lpf_cutoff", type="eng_float", default=eng_notation.num_to_str(12.5e3),
        help="Set LPF Cutoff [default=%default]")
    parser.add_option(
        "", "--lpf-trans", dest="lpf_trans", type="eng_float", default=eng_notation.num_to_str(1e3),
        help="Set LPF Trans Width [default=%default]")
    return parser


def main(top_block_cls=fsk_tx_es, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(fsk_dev=options.fsk_dev, lpf_cutoff=options.lpf_cutoff, lpf_trans=options.lpf_trans)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
