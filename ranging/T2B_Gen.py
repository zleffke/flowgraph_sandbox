#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: T2B Gen
# Generated: Mon Mar  5 23:52:18 2018
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
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import pmt,struct,numpy,math ; from datetime import datetime as dt; import string
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
        self.samp_per_symb = samp_per_symb = 4
        self.fft_size = fft_size = 8192
        self.chan_delay_ms = chan_delay_ms = 0
        self.beta = beta = 1
        self.alpha = alpha = 0.5

        self.rrc_filter_taps = rrc_filter_taps = firdes.root_raised_cosine(32, 1.0, 1.0/(samp_per_symb*32), alpha, samp_per_symb*32)

        self.noise_amp = noise_amp = 0.01
        self.mv_avg_len = mv_avg_len = 1
        self.fft_window = fft_window = window.kaiser(fft_size, beta)
        self.chan_delay_samp = chan_delay_samp = samp_rate *chan_delay_ms/1000
        self.chan_delay_lbl = chan_delay_lbl = samp_rate *chan_delay_ms/1000
        self.c6 = c6 = (1,1,1,1,1,-1,1,-1,1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,-1,-1,-1)
        self.c5 = c5 = (1,1,1,1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1)
        self.c4 = c4 = (1,1,1,1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1)
        self.c3 = c3 = (1,1,1,-1,-1,-1,1,-1,1,1,-1)
        self.c2 = c2 = (1,1,1,-1,-1,1,-1)
        self.c1 = c1 = (1,-1)
        self.baud = baud = samp_rate/samp_per_symb

        ##################################################
        # Blocks
        ##################################################
        self._noise_amp_range = Range(0, 50, 0.001, 0.01, 200)
        self._noise_amp_win = RangeWidget(self._noise_amp_range, self.set_noise_amp, "noise_amp", "counter_slider", float)
        self.top_layout.addWidget(self._noise_amp_win)
        self.root_raised_cosine_filter_0_0 = filter.interp_fir_filter_ccf(samp_per_symb, firdes.root_raised_cosine(
        	1, samp_rate, baud, alpha, 30))
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	fft_size*4, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)

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
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024*4, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate , #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.0010)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
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

        labels = ['pre-d', 'post', '', '', '',
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 0,0,4,4)
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 0,4,4,4)
        self._mv_avg_len_range = Range(0, 500, 1, 1, 200)
        self._mv_avg_len_win = RangeWidget(self._mv_avg_len_range, self.set_mv_avg_len, "mv_avg_len", "counter_slider", int)
        self.top_layout.addWidget(self._mv_avg_len_win)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, (baud *(1+alpha) )/2, 1000, firdes.WIN_HAMMING, 6.76))
        self.fft_vxx_0_0_0 = fft.fft_vcc(fft_size, True, (fft_window), False, 1)
        self.fft_vxx_0_0 = fft.fft_vcc(fft_size, True, (fft_window), True, 1)
        self.fft_vxx_0 = fft.fft_vcc(fft_size, True, (fft_window), True, 1)
        self.digital_pfb_clock_sync_xxx_0_0 = digital.pfb_clock_sync_ccf(samp_per_symb, math.pi*2/100, (rrc_filter_taps), 32, 16, 1.5, 1)
        self.digital_map_bb_0 = digital.map_bb(([-1,1]))
        self.digital_costas_loop_cc_0_0 = digital.costas_loop_cc(math.pi*2/100, 2, False)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(math.pi*2/100, 2, False)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self._chan_delay_ms_tool_bar = Qt.QToolBar(self)
        self._chan_delay_ms_tool_bar.addWidget(Qt.QLabel("chan_delay_ms"+": "))
        self._chan_delay_ms_line_edit = Qt.QLineEdit(str(self.chan_delay_ms))
        self._chan_delay_ms_tool_bar.addWidget(self._chan_delay_ms_line_edit)
        self._chan_delay_ms_line_edit.returnPressed.connect(
        	lambda: self.set_chan_delay_ms(eng_notation.str_to_num(str(self._chan_delay_ms_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._chan_delay_ms_tool_bar)
        self._chan_delay_lbl_tool_bar = Qt.QToolBar(self)

        if None:
          self._chan_delay_lbl_formatter = None
        else:
          self._chan_delay_lbl_formatter = lambda x: eng_notation.num_to_str(x)

        self._chan_delay_lbl_tool_bar.addWidget(Qt.QLabel('Channel Delay [samp]'+": "))
        self._chan_delay_lbl_label = Qt.QLabel(str(self._chan_delay_lbl_formatter(self.chan_delay_lbl)))
        self._chan_delay_lbl_tool_bar.addWidget(self._chan_delay_lbl_label)
        self.top_layout.addWidget(self._chan_delay_lbl_tool_bar)

        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_vector_source_x_0_0_0_0_0_0 = blocks.vector_source_s(c6, True, 1, [])
        self.blocks_vector_source_x_0_0_0_0_0 = blocks.vector_source_s(c5, True, 1, [])
        self.blocks_vector_source_x_0_0_0_0 = blocks.vector_source_s(c4, True, 1, [])
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_s(c3, True, 1, [])
        self.blocks_vector_source_x_0_0 = blocks.vector_source_s(c2, True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_s(c1, True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_short*1, samp_rate,True)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_size)
        self.blocks_short_to_float_1 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((1.0/(samp_rate), ))
        self.blocks_multiply_const_vxx_0_1_0_0_0 = blocks.multiply_const_vss((-1, ))
        self.blocks_multiply_const_vxx_0_1_0_0 = blocks.multiply_const_vss((1, ))
        self.blocks_multiply_const_vxx_0_1_0 = blocks.multiply_const_vss((-1, ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vss((-1, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vss((1, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vss((2, ))
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(fft_size)
        self.blocks_moving_average_xx_0 = blocks.moving_average_cc(100, 1, 4000, fft_size)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, int(chan_delay_samp))
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(fft_size)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_argmax_xx_0 = blocks.argmax_fs(fft_size)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vss(1)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, noise_amp, 0, 8192)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_agc2_xx_0_0 = analog.agc2_cc(1e-3, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0_0, 0), (self.digital_costas_loop_cc_0_0, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_argmax_xx_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_argmax_xx_0, 0), (self.blocks_short_to_float_1, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_argmax_xx_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.analog_agc2_xx_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.root_raised_cosine_filter_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_vector_to_stream_0_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.fft_vxx_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0_1_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0_1_0_0, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_multiply_const_vxx_0_1_0_0_0, 0), (self.blocks_add_xx_0, 5))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.blocks_short_to_float_1, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.blocks_vector_source_x_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_0, 0))
        self.connect((self.blocks_vector_source_x_0_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_0_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_1_0_0_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.fft_vxx_0_0_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.digital_pfb_clock_sync_xxx_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_0_0, 1))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.blocks_stream_to_vector_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "T2B_Gen")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_chan_delay_samp(self.samp_rate *self.chan_delay_ms/1000)
        self.set_baud(self.samp_rate/self.samp_per_symb)
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.baud, self.alpha, 30))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate )
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, (self.baud *(1+self.alpha) )/2, 1000, firdes.WIN_HAMMING, 6.76))
        self.set_chan_delay_lbl(self._chan_delay_lbl_formatter(self.samp_rate *self.chan_delay_ms/1000))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.blocks_multiply_const_vxx_1.set_k((1.0/(self.samp_rate), ))

    def get_samp_per_symb(self):
        return self.samp_per_symb

    def set_samp_per_symb(self, samp_per_symb):
        self.samp_per_symb = samp_per_symb
        self.set_baud(self.samp_rate/self.samp_per_symb)

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size
        self.set_fft_window(window.kaiser(self.fft_size, self.beta))

    def get_chan_delay_ms(self):
        return self.chan_delay_ms

    def set_chan_delay_ms(self, chan_delay_ms):
        self.chan_delay_ms = chan_delay_ms
        self.set_chan_delay_samp(self.samp_rate *self.chan_delay_ms/1000)
        Qt.QMetaObject.invokeMethod(self._chan_delay_ms_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.chan_delay_ms)))
        self.set_chan_delay_lbl(self._chan_delay_lbl_formatter(self.samp_rate *self.chan_delay_ms/1000))

    def get_beta(self):
        return self.beta

    def set_beta(self, beta):
        self.beta = beta
        self.set_fft_window(window.kaiser(self.fft_size, self.beta))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.baud, self.alpha, 30))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, (self.baud *(1+self.alpha) )/2, 1000, firdes.WIN_HAMMING, 6.76))

    def get_rrc_filter_taps(self):
        return self.rrc_filter_taps

    def set_rrc_filter_taps(self, rrc_filter_taps):
        self.rrc_filter_taps = rrc_filter_taps
        self.digital_pfb_clock_sync_xxx_0_0.update_taps((self.rrc_filter_taps))

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.analog_fastnoise_source_x_0.set_amplitude(self.noise_amp)

    def get_mv_avg_len(self):
        return self.mv_avg_len

    def set_mv_avg_len(self, mv_avg_len):
        self.mv_avg_len = mv_avg_len

    def get_fft_window(self):
        return self.fft_window

    def set_fft_window(self, fft_window):
        self.fft_window = fft_window

    def get_chan_delay_samp(self):
        return self.chan_delay_samp

    def set_chan_delay_samp(self, chan_delay_samp):
        self.chan_delay_samp = chan_delay_samp
        self.blocks_delay_0.set_dly(int(self.chan_delay_samp))

    def get_chan_delay_lbl(self):
        return self.chan_delay_lbl

    def set_chan_delay_lbl(self, chan_delay_lbl):
        self.chan_delay_lbl = chan_delay_lbl
        Qt.QMetaObject.invokeMethod(self._chan_delay_lbl_label, "setText", Qt.Q_ARG("QString", self.chan_delay_lbl))

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

    def get_baud(self):
        return self.baud

    def set_baud(self, baud):
        self.baud = baud
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, self.baud, self.alpha, 30))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, (self.baud *(1+self.alpha) )/2, 1000, firdes.WIN_HAMMING, 6.76))


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
