#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Modes Uf Rx Sigmf Stream
# GNU Radio version: 3.7.13.4
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
import gr_sigmf
import numpy
import sip
import sys
import time; import math
from gnuradio import qtgui


class modes_uf_rx_sigmf_stream(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Modes Uf Rx Sigmf Stream")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Modes Uf Rx Sigmf Stream")
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

        self.settings = Qt.QSettings("GNU Radio", "modes_uf_rx_sigmf_stream")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4000000
        self.samp_rate = samp_rate = 8000000

        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(1.0, 1, 0.5, 0.25, 32)

        self.rf_gain = rf_gain = 45
        self.qt_thresh = qt_thresh = 100
        self.det_mult = det_mult = 2
        self.det_avg_len = det_avg_len = 20
        self.cons_offset = cons_offset = 5
        self.burst_length = burst_length = 600
        self.avg_len = avg_len = 20

        ##################################################
        # Blocks
        ##################################################
        self._qt_thresh_tool_bar = Qt.QToolBar(self)
        self._qt_thresh_tool_bar.addWidget(Qt.QLabel("qt_thresh"+": "))
        self._qt_thresh_line_edit = Qt.QLineEdit(str(self.qt_thresh))
        self._qt_thresh_tool_bar.addWidget(self._qt_thresh_line_edit)
        self._qt_thresh_line_edit.returnPressed.connect(
        	lambda: self.set_qt_thresh(eng_notation.str_to_num(str(self._qt_thresh_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._qt_thresh_tool_bar, 0, 2, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._avg_len_tool_bar = Qt.QToolBar(self)
        self._avg_len_tool_bar.addWidget(Qt.QLabel("avg_len"+": "))
        self._avg_len_line_edit = Qt.QLineEdit(str(self.avg_len))
        self._avg_len_tool_bar.addWidget(self._avg_len_line_edit)
        self._avg_len_line_edit.returnPressed.connect(
        	lambda: self.set_avg_len(eng_notation.str_to_num(str(self._avg_len_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._avg_len_tool_bar, 0, 4, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.sigmf_source_0 = gr_sigmf.source('/captures/adsb/20210127/MODE-S_2021-01-27T23:43:24.sigmf-data', "ci16" + ("_le" if sys.byteorder == "little" else "_be"), False)
        self._rf_gain_tool_bar = Qt.QToolBar(self)
        self._rf_gain_tool_bar.addWidget(Qt.QLabel("rf_gain"+": "))
        self._rf_gain_line_edit = Qt.QLineEdit(str(self.rf_gain))
        self._rf_gain_tool_bar.addWidget(self._rf_gain_line_edit)
        self._rf_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rf_gain(eng_notation.str_to_num(str(self._rf_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rf_gain_tool_bar, 0, 0, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	burst_length, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.010)
        self.qtgui_time_sink_x_1.set_y_axis(-5, 20)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, qt_thresh, 1.0/samp_rate *100, 0, "")
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win, 1, 0, 2, 4)
        for r in range(1, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	burst_length/2/2*0 + 56, #size
        	samp_rate/2, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-3, 3)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0, 1.0/(samp_rate/2)*10, 0, "P1_P2")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['chips', 'bits', '', '', '',
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
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 3, 3, 2, 4)
        for r in range(3, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 7):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	burst_length/2, #size
        	samp_rate/2, #samp_rate
        	"soft chips", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0, 0, 0, "es::event_type")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not False:
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

        for i in xrange(2):
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 3, 0, 2, 3)
        for r in range(3, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	burst_length/2, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.010)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0.enable_grid(True)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 1, 8, 2, 2)
        for r in range(1, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(8, 10):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 3e6, 250e3, firdes.WIN_BLACKMAN, 6.76))
        self.fosphor_glfw_sink_c_0 = fosphor.glfw_sink_c()
        self.fosphor_glfw_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_glfw_sink_c_0.set_frequency_range(0, samp_rate)
        self.digital_diff_decoder_bb_1 = digital.diff_decoder_bb(2)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(math.pi / 50, 2, False)
        self.digital_correlate_access_code_tag_xx_0_0_1_2_2 = digital.correlate_access_code_tag_bb('10010000100100100001', 2, 'sync')
        self.digital_correlate_access_code_tag_xx_0_0_1_2 = digital.correlate_access_code_tag_bb('11100000111000', 1, 'P1_P2')
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_cc(2, 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_2 = digital.binary_slicer_fb()
        self._det_mult_tool_bar = Qt.QToolBar(self)
        self._det_mult_tool_bar.addWidget(Qt.QLabel("det_mult"+": "))
        self._det_mult_line_edit = Qt.QLineEdit(str(self.det_mult))
        self._det_mult_tool_bar.addWidget(self._det_mult_line_edit)
        self._det_mult_line_edit.returnPressed.connect(
        	lambda: self.set_det_mult(eng_notation.str_to_num(str(self._det_mult_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._det_mult_tool_bar, 0, 6, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._det_avg_len_tool_bar = Qt.QToolBar(self)
        self._det_avg_len_tool_bar.addWidget(Qt.QLabel("det_avg_len"+": "))
        self._det_avg_len_line_edit = Qt.QLineEdit(str(self.det_avg_len))
        self._det_avg_len_tool_bar.addWidget(self._det_avg_len_line_edit)
        self._det_avg_len_line_edit.returnPressed.connect(
        	lambda: self.set_det_avg_len(int(str(self._det_avg_len_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._det_avg_len_tool_bar, 0, 9, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(9, 10):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(4, True)
        self._cons_offset_tool_bar = Qt.QToolBar(self)
        self._cons_offset_tool_bar.addWidget(Qt.QLabel("cons_offset"+": "))
        self._cons_offset_line_edit = Qt.QLineEdit(str(self.cons_offset))
        self._cons_offset_tool_bar.addWidget(self._cons_offset_line_edit)
        self._cons_offset_line_edit.returnPressed.connect(
        	lambda: self.set_cons_offset(eng_notation.str_to_num(str(self._cons_offset_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._cons_offset_tool_bar, 0, 8, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(8, 9):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_cc(1.0 / 65536.0)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(int(avg_len), 1.0/avg_len, 4000, 1)
        self.blocks_interleaved_short_to_complex_0 = blocks.interleaved_short_to_complex(True, False)
        self.blocks_complex_to_real_1 = blocks.complex_to_real(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_add_const_vxx_1 = blocks.add_const_vff((1, ))
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.blocks_add_const_vxx_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_complex_to_real_1, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.blocks_complex_to_real_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.blocks_multiply_const_xx_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.digital_binary_slicer_fb_2, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.digital_binary_slicer_fb_2, 0), (self.digital_correlate_access_code_tag_xx_0_0_1_2, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0_0_1_2, 0), (self.digital_diff_decoder_bb_1, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0_0_1_2_2, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.blocks_complex_to_real_1, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_diff_decoder_bb_1, 0), (self.digital_correlate_access_code_tag_xx_0_0_1_2_2, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.fosphor_glfw_sink_c_0, 0))
        self.connect((self.sigmf_source_0, 0), (self.blocks_interleaved_short_to_complex_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "modes_uf_rx_sigmf_stream")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, self.qt_thresh, 1.0/self.samp_rate *100, 0, "")
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate/2)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0, 1.0/(self.samp_rate/2)*10, 0, "P1_P2")
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate/2)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 3e6, 250e3, firdes.WIN_BLACKMAN, 6.76))
        self.fosphor_glfw_sink_c_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        Qt.QMetaObject.invokeMethod(self._rf_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rf_gain)))

    def get_qt_thresh(self):
        return self.qt_thresh

    def set_qt_thresh(self, qt_thresh):
        self.qt_thresh = qt_thresh
        Qt.QMetaObject.invokeMethod(self._qt_thresh_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.qt_thresh)))
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, self.qt_thresh, 1.0/self.samp_rate *100, 0, "")

    def get_det_mult(self):
        return self.det_mult

    def set_det_mult(self, det_mult):
        self.det_mult = det_mult
        Qt.QMetaObject.invokeMethod(self._det_mult_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.det_mult)))

    def get_det_avg_len(self):
        return self.det_avg_len

    def set_det_avg_len(self, det_avg_len):
        self.det_avg_len = det_avg_len
        Qt.QMetaObject.invokeMethod(self._det_avg_len_line_edit, "setText", Qt.Q_ARG("QString", str(self.det_avg_len)))

    def get_cons_offset(self):
        return self.cons_offset

    def set_cons_offset(self, cons_offset):
        self.cons_offset = cons_offset
        Qt.QMetaObject.invokeMethod(self._cons_offset_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.cons_offset)))

    def get_burst_length(self):
        return self.burst_length

    def set_burst_length(self, burst_length):
        self.burst_length = burst_length

    def get_avg_len(self):
        return self.avg_len

    def set_avg_len(self, avg_len):
        self.avg_len = avg_len
        Qt.QMetaObject.invokeMethod(self._avg_len_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.avg_len)))
        self.blocks_moving_average_xx_0.set_length_and_scale(int(self.avg_len), 1.0/self.avg_len)


def main(top_block_cls=modes_uf_rx_sigmf_stream, options=None):

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
