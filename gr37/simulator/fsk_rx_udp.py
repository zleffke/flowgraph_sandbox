#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Fsk Rx Udp
# Generated: Mon Apr  9 22:58:14 2018
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
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import es
import kiss
import math
import pmt
import pyqt
import sip
import sys
from gnuradio import qtgui


class fsk_rx_udp(gr.top_block, Qt.QWidget):

    def __init__(self, fsk_dev=10000, lpf_cutoff=12.5e3, lpf_trans=1e3):
        gr.top_block.__init__(self, "Fsk Rx Udp")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Fsk Rx Udp")
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

        self.settings = Qt.QSettings("GNU Radio", "fsk_rx_udp")
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
        self.thresh = thresh = -4
        self.smooth_len = smooth_len = 25
        self.samps_per_symb = samps_per_symb = int(samp_rate/baud)
        self.offset = offset = 0
        self.num_items = num_items = 1024
        self.mult = mult = (samp_rate)/2/3.141593
        self.decay = decay = 100e-6
        self.bw_factor = bw_factor = 1000
        self.attack = attack = 0.001
        self.alpha = alpha = 0.5

        ##################################################
        # Blocks
        ##################################################
        self._thresh_tool_bar = Qt.QToolBar(self)
        self._thresh_tool_bar.addWidget(Qt.QLabel('Threshold'+": "))
        self._thresh_line_edit = Qt.QLineEdit(str(self.thresh))
        self._thresh_tool_bar.addWidget(self._thresh_line_edit)
        self._thresh_line_edit.returnPressed.connect(
        	lambda: self.set_thresh(eng_notation.str_to_num(str(self._thresh_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._thresh_tool_bar, 0,4,1,2)
        self._offset_range = Range(-10000, 10000, 1, 0, 200)
        self._offset_win = RangeWidget(self._offset_range, self.set_offset, "offset", "counter_slider", float)
        self.top_grid_layout.addWidget(self._offset_win, 3,4,1,4)
        self._decay_tool_bar = Qt.QToolBar(self)
        self._decay_tool_bar.addWidget(Qt.QLabel("decay"+": "))
        self._decay_line_edit = Qt.QLineEdit(str(self.decay))
        self._decay_tool_bar.addWidget(self._decay_line_edit)
        self._decay_line_edit.returnPressed.connect(
        	lambda: self.set_decay(eng_notation.str_to_num(str(self._decay_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._decay_tool_bar, 1,6,1,2)
        self._bw_factor_tool_bar = Qt.QToolBar(self)
        self._bw_factor_tool_bar.addWidget(Qt.QLabel("bw_factor"+": "))
        self._bw_factor_line_edit = Qt.QLineEdit(str(self.bw_factor))
        self._bw_factor_tool_bar.addWidget(self._bw_factor_line_edit)
        self._bw_factor_line_edit.returnPressed.connect(
        	lambda: self.set_bw_factor(eng_notation.str_to_num(str(self._bw_factor_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._bw_factor_tool_bar, 2,6,1,2)
        self._attack_tool_bar = Qt.QToolBar(self)
        self._attack_tool_bar.addWidget(Qt.QLabel("attack"+": "))
        self._attack_line_edit = Qt.QLineEdit(str(self.attack))
        self._attack_tool_bar.addWidget(self._attack_line_edit)
        self._attack_line_edit.returnPressed.connect(
        	lambda: self.set_attack(eng_notation.str_to_num(str(self._attack_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._attack_tool_bar, 1,4,1,2)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
        	50, #size
        	samp_rate, #samp_rate
        	"trigger", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_2.disable_legend()

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
                self.qtgui_time_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_2_win, 8,0,2,4)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	4096, #size
        	samp_rate, #samp_rate
        	"Freq Error", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.010)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(True)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)

        if not False:
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win, 4,0,2,4)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	2048, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "packet_len")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_0.disable_legend()

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
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 4,4,2,4)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	4096, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "packet_len")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 8,4,2,4)
        self.qtgui_number_sink_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_1.set_update_time(0.10)
        self.qtgui_number_sink_1.set_title("Doppler")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_1.set_min(i, -1)
            self.qtgui_number_sink_1.set_max(i, 1)
            self.qtgui_number_sink_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_1.set_label(i, labels[i])
            self.qtgui_number_sink_1.set_unit(i, units[i])
            self.qtgui_number_sink_1.set_factor(i, factor[i])

        self.qtgui_number_sink_1.enable_autoscale(False)
        self._qtgui_number_sink_1_win = sip.wrapinstance(self.qtgui_number_sink_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_1_win, 2,4,1,2)
        self.qtgui_number_sink_0_0_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            1
        )
        self.qtgui_number_sink_0_0_1.set_update_time(0.010)
        self.qtgui_number_sink_0_0_1.set_title("SNR")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_1.set_min(i, 0)
            self.qtgui_number_sink_0_0_1.set_max(i, 100)
            self.qtgui_number_sink_0_0_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_1.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_1.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_1.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_1.enable_autoscale(False)
        self._qtgui_number_sink_0_0_1_win = sip.wrapinstance(self.qtgui_number_sink_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_1_win, 2,5,1,1)
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"RX Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0.enable_grid(True)
        self.qtgui_freq_sink_x_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_1_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_win, 0,0,4,4)
        self.pyqt_time_plot_0 = pyqt.time_plot('')
        self._pyqt_time_plot_0_win = self.pyqt_time_plot_0;
        self.top_grid_layout.addWidget(self._pyqt_time_plot_0_win, 6,0,2,4)
        self.pyqt_time_plot_0.line_off()
        self.pyqt_text_output_0 = pyqt.text_output()
        self._pyqt_text_output_0_win = self.pyqt_text_output_0;
        self.top_grid_layout.addWidget(self._pyqt_text_output_0_win, 6,4,2,4)
        self.kiss_hdlc_deframer_0 = kiss.hdlc_deframer(check_fcs=True, max_length=300)
        self.es_trigger_edge_f_0 = es.trigger_edge_f(thresh,3500,500,gr.sizeof_float,100)
        self.es_sink_0 = es.sink(1*[gr.sizeof_float],8,64,0,2,0)
        self.es_handler_pdu_0 = es.es_make_handler_pdu(es.es_handler_print.TYPE_F32)
        self.digital_fll_band_edge_cc_0 = digital.fll_band_edge_cc(samps_per_symb, .5, 512, math.pi/bw_factor)
        self.digital_descrambler_bb_0 = digital.descrambler_bb(0x21, 0, 16)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(samps_per_symb*(1+0.0), 0.25*0.175*0.175, 0.25, 0.175, 0.005)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_gr_complex*1, '0.0.0.0', 9001, 1472, True)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(-100, -100, 0)
        self.blocks_sub_xx_1_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_1 = blocks.sub_ff(1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, num_items)
        self.blocks_skiphead_1 = blocks.skiphead(gr.sizeof_gr_complex*1, 500)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_float*1, 1)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_pdu_to_tagged_stream_2 = blocks.pdu_to_tagged_stream(blocks.complex_t, 'packet_len')
        self.blocks_pdu_remove_0_0 = blocks.pdu_remove(pmt.intern("es::event_buffer"))
        self.blocks_pdu_remove_0 = blocks.pdu_remove(pmt.intern("es::event_buffer"))
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_nlog10_ff_0_0_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vff((mult, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((mult*-1, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((-1, ))
        self.blocks_moving_average_xx_2 = blocks.moving_average_ff(num_items, 1.0/num_items, 4000, 1)
        self.blocks_moving_average_xx_0_1_0_0 = blocks.moving_average_ff(500, 1.0/500, 4000, 1)
        self.blocks_moving_average_xx_0_1_0 = blocks.moving_average_ff(2000, 1.0/2000, 4000, 1)
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_ff(smooth_len, 1.0/smooth_len, 4000, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(smooth_len, 1.0/smooth_len, 4000, 1)
        self.blocks_keep_m_in_n_1 = blocks.keep_m_in_n(gr.sizeof_float, 1, num_items, 0)
        self.blocks_keep_m_in_n_0_1 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 2000, 3500, 10)
        self.blocks_keep_m_in_n_0_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 500, 3500, 10)
        self.blocks_complex_to_mag_squared_0_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_argmax_xx_0 = blocks.argmax_fs(num_items)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, offset)
        self.analog_quadrature_demod_cf_1 = analog.quadrature_demod_cf((samp_rate)/(2*math.pi*fsk_dev/8.0))
        self.analog_agc3_xx_0 = analog.agc3_cc(attack, decay, 1.0, 1.0, 1)
        self.analog_agc3_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_pdu_remove_0, 'pdus'), (self.blocks_pdu_remove_0_0, 'pdus'))
        self.msg_connect((self.blocks_pdu_remove_0, 'pdus'), (self.pyqt_time_plot_0, 'pdus'))
        self.msg_connect((self.blocks_pdu_remove_0_0, 'pdus'), (self.blocks_pdu_to_tagged_stream_2, 'pdus'))
        self.msg_connect((self.es_handler_pdu_0, 'pdus_out'), (self.blocks_pdu_remove_0, 'pdus'))
        self.msg_connect((self.es_trigger_edge_f_0, 'edge_event'), (self.es_handler_pdu_0, 'handle_event'))
        self.msg_connect((self.es_trigger_edge_f_0, 'which_stream'), (self.es_sink_0, 'schedule_event'))
        self.msg_connect((self.kiss_hdlc_deframer_0, 'out'), (self.pyqt_text_output_0, 'pdus'))
        self.connect((self.analog_agc3_xx_0, 0), (self.digital_fll_band_edge_cc_0, 0))
        self.connect((self.analog_quadrature_demod_cf_1, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_argmax_xx_0, 0), (self.blocks_null_sink_1, 0))
        self.connect((self.blocks_argmax_xx_0, 1), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_moving_average_xx_0_1_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0_0, 0), (self.blocks_moving_average_xx_0_1_0_0, 0))
        self.connect((self.blocks_keep_m_in_n_0_0, 0), (self.blocks_complex_to_mag_squared_0_0_0, 0))
        self.connect((self.blocks_keep_m_in_n_0_1, 0), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.blocks_keep_m_in_n_1, 0), (self.blocks_sub_xx_1, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.qtgui_number_sink_1, 0))
        self.connect((self.blocks_moving_average_xx_0_1_0, 0), (self.blocks_nlog10_ff_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_1_0_0, 0), (self.blocks_nlog10_ff_0_0_0, 0))
        self.connect((self.blocks_moving_average_xx_2, 0), (self.blocks_keep_m_in_n_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.es_trigger_edge_f_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.analog_agc3_xx_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_moving_average_xx_2, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.blocks_sub_xx_1_0, 1))
        self.connect((self.blocks_nlog10_ff_0_0_0, 0), (self.blocks_sub_xx_1_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_2, 0), (self.blocks_keep_m_in_n_0_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_2, 0), (self.blocks_skiphead_1, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_sub_xx_1, 1))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_skiphead_1, 0), (self.blocks_keep_m_in_n_0_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_argmax_xx_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.blocks_sub_xx_1, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_sub_xx_1_0, 0), (self.qtgui_number_sink_0_0_1, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_descrambler_bb_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.es_trigger_edge_f_0, 1))
        self.connect((self.digital_descrambler_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_descrambler_bb_0, 0), (self.kiss_hdlc_deframer_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.analog_quadrature_demod_cf_1, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 1), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 3), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 2), (self.blocks_null_sink_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.qtgui_freq_sink_x_1_0, 0))
        self.connect((self.es_trigger_edge_f_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.es_trigger_edge_f_0, 0), (self.es_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fsk_rx_udp")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_fsk_dev(self):
        return self.fsk_dev

    def set_fsk_dev(self, fsk_dev):
        self.fsk_dev = fsk_dev
        self.analog_quadrature_demod_cf_1.set_gain((self.samp_rate)/(2*math.pi*self.fsk_dev/8.0))

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
        self.set_mult((self.samp_rate)/2/3.141593)
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_quadrature_demod_cf_1.set_gain((self.samp_rate)/(2*math.pi*self.fsk_dev/8.0))

    def get_baud(self):
        return self.baud

    def set_baud(self, baud):
        self.baud = baud
        self.set_samps_per_symb(int(self.samp_rate/self.baud))

    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh
        Qt.QMetaObject.invokeMethod(self._thresh_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.thresh)))
        self.es_trigger_edge_f_0.set_thresh(self.thresh)

    def get_smooth_len(self):
        return self.smooth_len

    def set_smooth_len(self, smooth_len):
        self.smooth_len = smooth_len
        self.blocks_moving_average_xx_0_0.set_length_and_scale(self.smooth_len, 1.0/self.smooth_len)
        self.blocks_moving_average_xx_0.set_length_and_scale(self.smooth_len, 1.0/self.smooth_len)

    def get_samps_per_symb(self):
        return self.samps_per_symb

    def set_samps_per_symb(self, samps_per_symb):
        self.samps_per_symb = samps_per_symb
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samps_per_symb*(1+0.0))

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self.analog_sig_source_x_0.set_offset(self.offset)

    def get_num_items(self):
        return self.num_items

    def set_num_items(self, num_items):
        self.num_items = num_items
        self.blocks_moving_average_xx_2.set_length_and_scale(self.num_items, 1.0/self.num_items)
        self.blocks_keep_m_in_n_1.set_n(self.num_items)

    def get_mult(self):
        return self.mult

    def set_mult(self, mult):
        self.mult = mult
        self.blocks_multiply_const_vxx_2.set_k((self.mult, ))
        self.blocks_multiply_const_vxx_1.set_k((self.mult*-1, ))

    def get_decay(self):
        return self.decay

    def set_decay(self, decay):
        self.decay = decay
        Qt.QMetaObject.invokeMethod(self._decay_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.decay)))
        self.analog_agc3_xx_0.set_decay_rate(self.decay)

    def get_bw_factor(self):
        return self.bw_factor

    def set_bw_factor(self, bw_factor):
        self.bw_factor = bw_factor
        Qt.QMetaObject.invokeMethod(self._bw_factor_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.bw_factor)))
        self.digital_fll_band_edge_cc_0.set_loop_bandwidth(math.pi/self.bw_factor)

    def get_attack(self):
        return self.attack

    def set_attack(self, attack):
        self.attack = attack
        Qt.QMetaObject.invokeMethod(self._attack_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.attack)))
        self.analog_agc3_xx_0.set_attack_rate(self.attack)

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


def main(top_block_cls=fsk_rx_udp, options=None):
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
