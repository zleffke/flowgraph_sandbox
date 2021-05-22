#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Lms6 Experiment
# Generated: Sun Apr 15 01:39:46 2018
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
from datetime import datetime as dt; import string
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import kiss
import math
import pmt
import sip
import sys
from gnuradio import qtgui


class lms6_experiment(gr.top_block, Qt.QWidget):

    def __init__(self, meta_rate=1):
        gr.top_block.__init__(self, "Lms6 Experiment")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Lms6 Experiment")
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

        self.settings = Qt.QSettings("GNU Radio", "lms6_experiment")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.meta_rate = meta_rate

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 50e3
        self.decim = decim = 1
        self.baud = baud = 4800

        self.xlate_taps = xlate_taps = firdes.low_pass(1.0, samp_rate, samp_rate/2, 1000, firdes.WIN_HAMMING, 6.76)

        self.variable_tag_object_0 = variable_tag_object_0 = gr.tag_utils.python_to_tag((0, pmt.intern("key"), pmt.intern("value"), pmt.intern("src")))
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y%m%d_%H%M%S.%f" )+'_UTC'
        self.sync3 = sync3 = "001110110010000000000000000000000000000000000000"
        self.sync2 = sync2 = "00111011001000000000000000000000"
        self.samps_per_symb = samps_per_symb = samp_rate/decim*24/25 / baud
        self.offset = offset = 0

        ##################################################
        # Blocks
        ##################################################
        self._offset_tool_bar = Qt.QToolBar(self)
        self._offset_tool_bar.addWidget(Qt.QLabel('OFFSET'+": "))
        self._offset_line_edit = Qt.QLineEdit(str(self.offset))
        self._offset_tool_bar.addWidget(self._offset_line_edit)
        self._offset_line_edit.returnPressed.connect(
        	lambda: self.set_offset(eng_notation.str_to_num(str(self._offset_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._offset_tool_bar, 3,3,1,3)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=24,
                decimation=25,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024*4, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 2)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "hit")
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
        markers = [0, -1, -1, -1, -1,
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
        self.qtgui_number_sink_0_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0_0_0.set_title("")

        labels = ['SNR', '', '', '', '',
                  '', '', '', '', '']
        units = ['dB', '', '', '', '',
                 '', '', '', '', '']
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_0_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0_0_0_0.set_max(i, 30)
            self.qtgui_number_sink_0_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_0_0_win, 4,4,1,1)
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
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_0_win, 4,3,1,1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"Filtered", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-70, -10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.2)
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
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 0,3,3,3)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"Freq compensated", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-70, -10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,0,3,3)
        self.low_pass_filter_0 = filter.fir_filter_ccf(decim, firdes.low_pass(
        	1, samp_rate, 7.5e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.kiss_nrzi_decode_0 = kiss.nrzi_decode()
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, (xlate_taps), offset, samp_rate)
        self.digital_fll_band_edge_cc_0 = digital.fll_band_edge_cc(samps_per_symb, .5, 1024, math.pi/500)
        self.digital_correlate_access_code_tag_xx_0 = digital.correlate_access_code_tag_bb(sync3, 0, 'hit')
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(samps_per_symb*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_tagged_stream_to_pdu_1 = blocks.tagged_stream_to_pdu(blocks.byte_t, 'packet_len')
        self.blocks_tagged_stream_to_pdu_0_0 = blocks.tagged_stream_to_pdu(blocks.float_t, 'snr')
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.float_t, 'rfo')
        self.blocks_tagged_stream_multiply_length_0 = blocks.tagged_stream_multiply_length(gr.sizeof_char*1, 'packet_len', 1/8.0)
        self.blocks_tagged_stream_align_0 = blocks.tagged_stream_align(gr.sizeof_char*1, 'hit')
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_char*1, '', ""); self.blocks_tag_debug_0.set_display(True)
        self.blocks_stream_to_tagged_stream_1 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 576, "packet_len")
        self.blocks_stream_to_tagged_stream_0_0 = blocks.stream_to_tagged_stream(gr.sizeof_float, 1, 1, "snr")
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_float, 1, 1, "rfo")
        self.blocks_socket_pdu_0_0 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '52002', 10000, False)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("TCP_SERVER", '0.0.0.0', '52001', 10000, False)
        self.blocks_pdu_filter_0 = blocks.pdu_filter(pmt.intern("hit"), pmt.from_long(0), False)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_nlog10_ff_0_1 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((-1*samp_rate/(2*math.pi), ))
        self.blocks_moving_average_xx_0_0_1 = blocks.moving_average_ff(10000, 0.0001, 4000, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(10000, 0.0001, 4000, 1)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_keep_one_in_n_0_0 = blocks.keep_one_in_n(gr.sizeof_float*1, int(samp_rate*meta_rate))
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_float*1, int(samp_rate/4*meta_rate))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/zleffke/captures/radiosonde/BBNWS_LMS6_RTLSDR_20171202_235806.395054_UTC_50k.fc32', False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.audio_sink_1 = audio.sink(48000, '', True)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, samp_rate/2, 1, 0)
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
        self.msg_connect((self.blocks_pdu_filter_0, 'pdus'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.blocks_socket_pdu_0, 'pdus'))
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0_0, 'pdus'), (self.blocks_socket_pdu_0_0, 'pdus'))
        self.msg_connect((self.blocks_tagged_stream_to_pdu_1, 'pdus'), (self.blocks_pdu_filter_0, 'pdus'))
        self.connect((self.analog_agc2_xx_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.analog_nbfm_rx_0, 0), (self.audio_sink_1, 0))
        self.connect((self.analog_nbfm_rx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_divide_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_divide_xx_0, 1))
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_nlog10_ff_0_1, 0))
        self.connect((self.blocks_file_source_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.blocks_stream_to_tagged_stream_0_0, 0))
        self.connect((self.blocks_keep_one_in_n_0_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_keep_one_in_n_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_number_sink_0_0_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0_1, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0_1, 0), (self.qtgui_number_sink_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_nlog10_ff_0_1, 0), (self.blocks_moving_average_xx_0_0_1, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_tagged_stream_multiply_length_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_tagged_stream_to_pdu_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0_0, 0), (self.blocks_tagged_stream_to_pdu_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_1, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_tagged_stream_align_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_tagged_stream_align_0, 0), (self.blocks_stream_to_tagged_stream_1, 0))
        self.connect((self.blocks_tagged_stream_align_0, 0), (self.blocks_tag_debug_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.blocks_tagged_stream_to_pdu_1, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.kiss_nrzi_decode_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0, 0), (self.blocks_tagged_stream_align_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 1), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 2), (self.blocks_null_sink_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 3), (self.blocks_null_sink_0_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.digital_fll_band_edge_cc_0, 0))
        self.connect((self.kiss_nrzi_decode_0, 0), (self.digital_correlate_access_code_tag_xx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_complex_to_mag_squared_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lms6_experiment")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_meta_rate(self):
        return self.meta_rate

    def set_meta_rate(self, meta_rate):
        self.meta_rate = meta_rate
        self.blocks_keep_one_in_n_0_0.set_n(int(self.samp_rate*self.meta_rate))
        self.blocks_keep_one_in_n_0.set_n(int(self.samp_rate/4*self.meta_rate))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samps_per_symb(self.samp_rate/self.decim*24/25 / self.baud)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 7.5e3, 1e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_1.set_k((-1*self.samp_rate/(2*math.pi), ))
        self.blocks_keep_one_in_n_0_0.set_n(int(self.samp_rate*self.meta_rate))
        self.blocks_keep_one_in_n_0.set_n(int(self.samp_rate/4*self.meta_rate))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_frequency(self.samp_rate/2)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_samps_per_symb(self.samp_rate/self.decim*24/25 / self.baud)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)

    def get_baud(self):
        return self.baud

    def set_baud(self, baud):
        self.baud = baud
        self.set_samps_per_symb(self.samp_rate/self.decim*24/25 / self.baud)

    def get_xlate_taps(self):
        return self.xlate_taps

    def set_xlate_taps(self, xlate_taps):
        self.xlate_taps = xlate_taps
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.xlate_taps))

    def get_variable_tag_object_0(self):
        return self.variable_tag_object_0

    def set_variable_tag_object_0(self, variable_tag_object_0):
        self.variable_tag_object_0 = variable_tag_object_0

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str

    def get_sync3(self):
        return self.sync3

    def set_sync3(self, sync3):
        self.sync3 = sync3
        self.digital_correlate_access_code_tag_xx_0.set_access_code(self.sync3)

    def get_sync2(self):
        return self.sync2

    def set_sync2(self, sync2):
        self.sync2 = sync2

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
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.offset)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--meta-rate", dest="meta_rate", type="eng_float", default=eng_notation.num_to_str(1),
        help="Set meta_rate [default=%default]")
    return parser


def main(top_block_cls=lms6_experiment, options=None):
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
