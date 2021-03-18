#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Modes Uf Rx Sigmf V2
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
import ais
import epy_block_0_0
import epy_block_1
import es
import gr_sigmf
import numpy
import pmt
import pyqt
import sip
import sys
import time; import math
import vcc
from gnuradio import qtgui


class modes_uf_rx_sigmf_v2(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Modes Uf Rx Sigmf V2")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Modes Uf Rx Sigmf V2")
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

        self.settings = Qt.QSettings("GNU Radio", "modes_uf_rx_sigmf_v2")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 2
        self.samp_rate = samp_rate = 8000000

        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(1, 1, 0.5, 0.4, 32)

        self.rms_alpha = rms_alpha = 1e-6
        self.rf_gain = rf_gain = 45
        self.qt_thresh = qt_thresh = 110
        self.es_thresh = es_thresh = 110
        self.det_mult = det_mult = 2
        self.det_avg_len = det_avg_len = 20
        self.cons_offset = cons_offset = 5
        self.burst_length = burst_length = 600
        self.bit_thresh = bit_thresh = 5
        self.avg_len = avg_len = 20

        ##################################################
        # Blocks
        ##################################################
        self._rms_alpha_tool_bar = Qt.QToolBar(self)
        self._rms_alpha_tool_bar.addWidget(Qt.QLabel("rms_alpha"+": "))
        self._rms_alpha_line_edit = Qt.QLineEdit(str(self.rms_alpha))
        self._rms_alpha_tool_bar.addWidget(self._rms_alpha_line_edit)
        self._rms_alpha_line_edit.returnPressed.connect(
        	lambda: self.set_rms_alpha(eng_notation.str_to_num(str(self._rms_alpha_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rms_alpha_tool_bar, 6, 3, 1, 1)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self._es_thresh_tool_bar = Qt.QToolBar(self)
        self._es_thresh_tool_bar.addWidget(Qt.QLabel('ES Thresh'+": "))
        self._es_thresh_line_edit = Qt.QLineEdit(str(self.es_thresh))
        self._es_thresh_tool_bar.addWidget(self._es_thresh_line_edit)
        self._es_thresh_line_edit.returnPressed.connect(
        	lambda: self.set_es_thresh(eng_notation.str_to_num(str(self._es_thresh_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._es_thresh_tool_bar, 0, 5, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self.vcc_es_tag_to_utc_0 = vcc.es_tag_to_utc(samp_rate)
        self.vcc_burst_snr_0 = vcc.burst_snr(25, 2)
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
        	burst_length/2, #size
        	samp_rate, #samp_rate
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.010)
        self.qtgui_time_sink_x_1.set_y_axis(-5, 20)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, qt_thresh, 1.0/samp_rate *100, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(True)
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

        for i in xrange(3):
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
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	burst_length/2, #size
        	samp_rate/2, #samp_rate
        	"soft chips", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0, 0, 0, "es::event_type")
        self.qtgui_time_sink_x_0_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()

        labels = ['re', 'abs', 'mag', 'ph', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 2, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, -1, 0, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1, 0.25, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_1_win, 3, 0, 3, 5)
        for r in range(3, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_raster_sink_x_0 = qtgui.time_raster_sink_b(
        	samp_rate / 2,
        	20,
        	56,
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
        colors = [1, 0, 0, 0, 0,
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
        self.top_grid_layout.addWidget(self._qtgui_time_raster_sink_x_0_win, 3, 5, 3, 5)
        for r in range(3, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 10):
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
        self.pyqt_ctime_plot_0 = pyqt.ctime_plot('')
        self._pyqt_ctime_plot_0_win = self.pyqt_ctime_plot_0;
        self.top_grid_layout.addWidget(self._pyqt_ctime_plot_0_win, 1, 4, 2, 2)
        for r in range(1, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.pyqt_const_plot_0 = pyqt.const_plot(label='')
        self._pyqt_const_plot_0_win = self.pyqt_const_plot_0;
        self.top_grid_layout.addWidget(self._pyqt_const_plot_0_win, 1, 6, 2, 2)
        for r in range(1, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 8):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 4e6, 250e3, firdes.WIN_BLACKMAN, 6.76))
        self.fosphor_glfw_sink_c_0 = fosphor.glfw_sink_c()
        self.fosphor_glfw_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_glfw_sink_c_0.set_frequency_range(0, samp_rate)
        self.es_trigger_edge_f_0 = es.trigger_edge_f(es_thresh,burst_length,burst_length /3,gr.sizeof_gr_complex,300)
        self.es_sink_0 = es.sink(1*[gr.sizeof_gr_complex],4,64,0,2,0)
        self.es_handler_pdu_0 = es.es_make_handler_pdu(es.es_handler_print.TYPE_C32)
        self.epy_block_1 = epy_block_1.uf_frame_sync(tag_name='sync', msg_len=112, samp_rate=samp_rate, sps=2)
        self.epy_block_0_0 = epy_block_0_0.uf_decode(msg_filter='All Messages', verbose=True)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(2, math.pi/200, (rrc_taps), 32, 16, 1.1, 1)
        self.digital_diff_phasor_cc_0 = digital.diff_phasor_cc()
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(math.pi / 50, 2, False)
        self.digital_correlate_access_code_tag_xx_0_0_1_2_2_0_0_0 = digital.correlate_access_code_tag_bb('00011111000111000001', 3, 'sync')
        self.digital_binary_slicer_fb_0_0 = digital.binary_slicer_fb()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate*2,True)
        self.blocks_sub_xx_2_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_float*1, 1)
        self.blocks_rms_xx_1 = blocks.rms_cf(rms_alpha)
        self.blocks_pdu_to_tagged_stream_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.complex_t, 'est_len')
        (self.blocks_pdu_to_tagged_stream_0).set_min_output_buffer(600)
        self.blocks_pdu_remove_0 = blocks.pdu_remove(pmt.intern("es::event_buffer"))
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_cc(1.0 / 65536.0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((-1*det_mult, ))
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_ff(int(det_avg_len), 1.0/det_avg_len, 4000, 1)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(int(avg_len), 1.0/avg_len, 4000, 1)
        self.blocks_interleaved_short_to_complex_0 = blocks.interleaved_short_to_complex(True, False)
        self.blocks_complex_to_real_1_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.blocks_char_to_float_0_1 = blocks.char_to_float(1, 1/10.0)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((cons_offset, ))
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self._bit_thresh_tool_bar = Qt.QToolBar(self)
        self._bit_thresh_tool_bar.addWidget(Qt.QLabel("bit_thresh"+": "))
        self._bit_thresh_line_edit = Qt.QLineEdit(str(self.bit_thresh))
        self._bit_thresh_tool_bar.addWidget(self._bit_thresh_line_edit)
        self._bit_thresh_line_edit.returnPressed.connect(
        	lambda: self.set_bit_thresh(eng_notation.str_to_num(str(self._bit_thresh_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._bit_thresh_tool_bar, 6, 4, 1, 1)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)
        self.ais_invert_0 = ais.invert()



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_pdu_remove_0, 'pdus'), (self.vcc_burst_snr_0, 'in'))
        self.msg_connect((self.epy_block_0_0, 'out'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))
        self.msg_connect((self.epy_block_1, 'out'), (self.epy_block_0_0, 'in'))
        self.msg_connect((self.es_handler_pdu_0, 'pdus_out'), (self.blocks_pdu_remove_0, 'pdus'))
        self.msg_connect((self.es_trigger_edge_f_0, 'edge_event'), (self.es_handler_pdu_0, 'handle_event'))
        self.msg_connect((self.es_trigger_edge_f_0, 'which_stream'), (self.es_sink_0, 'schedule_event'))
        self.msg_connect((self.vcc_burst_snr_0, 'out'), (self.vcc_es_tag_to_utc_0, 'in'))
        self.msg_connect((self.vcc_es_tag_to_utc_0, 'out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.vcc_es_tag_to_utc_0, 'out'), (self.pyqt_const_plot_0, 'cpdus'))
        self.msg_connect((self.vcc_es_tag_to_utc_0, 'out'), (self.pyqt_ctime_plot_0, 'cpdus'))
        self.connect((self.ais_invert_0, 0), (self.digital_correlate_access_code_tag_xx_0_0_1_2_2_0_0_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.es_trigger_edge_f_0, 1))
        self.connect((self.analog_agc2_xx_0, 0), (self.fosphor_glfw_sink_c_0, 0))
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.qtgui_time_sink_x_1, 2))
        self.connect((self.blocks_char_to_float_0_1, 0), (self.qtgui_time_sink_x_0_1, 2))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.qtgui_time_sink_x_1, 1))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_complex_to_real_1_0_0, 0), (self.blocks_sub_xx_2_0, 0))
        self.connect((self.blocks_complex_to_real_1_0_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.blocks_multiply_const_xx_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.es_trigger_edge_f_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.qtgui_time_raster_sink_x_0, 0))
        self.connect((self.blocks_rms_xx_1, 0), (self.blocks_sub_xx_2_0, 1))
        self.connect((self.blocks_rms_xx_1, 0), (self.qtgui_time_sink_x_0_1, 1))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_sub_xx_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.blocks_sub_xx_2_0, 0), (self.digital_binary_slicer_fb_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.digital_binary_slicer_fb_0_0, 0), (self.ais_invert_0, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0_0_1_2_2_0_0_0, 0), (self.blocks_char_to_float_0_1, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0_0_1_2_2_0_0_0, 0), (self.epy_block_1, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.digital_diff_phasor_cc_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_diff_phasor_cc_0, 0), (self.blocks_complex_to_real_1_0_0, 0))
        self.connect((self.digital_diff_phasor_cc_0, 0), (self.blocks_rms_xx_1, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.es_trigger_edge_f_0, 0), (self.es_sink_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.sigmf_source_0, 0), (self.blocks_interleaved_short_to_complex_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "modes_uf_rx_sigmf_v2")
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
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate/2)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 4e6, 250e3, firdes.WIN_BLACKMAN, 6.76))
        self.fosphor_glfw_sink_c_0.set_frequency_range(0, self.samp_rate)
        self.epy_block_1.samp_rate = self.samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*2)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps))

    def get_rms_alpha(self):
        return self.rms_alpha

    def set_rms_alpha(self, rms_alpha):
        self.rms_alpha = rms_alpha
        Qt.QMetaObject.invokeMethod(self._rms_alpha_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rms_alpha)))
        self.blocks_rms_xx_1.set_alpha(self.rms_alpha)

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

    def get_es_thresh(self):
        return self.es_thresh

    def set_es_thresh(self, es_thresh):
        self.es_thresh = es_thresh
        Qt.QMetaObject.invokeMethod(self._es_thresh_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.es_thresh)))
        self.es_trigger_edge_f_0.set_thresh(self.es_thresh)

    def get_det_mult(self):
        return self.det_mult

    def set_det_mult(self, det_mult):
        self.det_mult = det_mult
        Qt.QMetaObject.invokeMethod(self._det_mult_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.det_mult)))
        self.blocks_multiply_const_vxx_0.set_k((-1*self.det_mult, ))

    def get_det_avg_len(self):
        return self.det_avg_len

    def set_det_avg_len(self, det_avg_len):
        self.det_avg_len = det_avg_len
        Qt.QMetaObject.invokeMethod(self._det_avg_len_line_edit, "setText", Qt.Q_ARG("QString", str(self.det_avg_len)))
        self.blocks_moving_average_xx_0_0.set_length_and_scale(int(self.det_avg_len), 1.0/self.det_avg_len)

    def get_cons_offset(self):
        return self.cons_offset

    def set_cons_offset(self, cons_offset):
        self.cons_offset = cons_offset
        Qt.QMetaObject.invokeMethod(self._cons_offset_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.cons_offset)))
        self.blocks_add_const_vxx_0.set_k((self.cons_offset, ))

    def get_burst_length(self):
        return self.burst_length

    def set_burst_length(self, burst_length):
        self.burst_length = burst_length

    def get_bit_thresh(self):
        return self.bit_thresh

    def set_bit_thresh(self, bit_thresh):
        self.bit_thresh = bit_thresh
        Qt.QMetaObject.invokeMethod(self._bit_thresh_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.bit_thresh)))

    def get_avg_len(self):
        return self.avg_len

    def set_avg_len(self, avg_len):
        self.avg_len = avg_len
        Qt.QMetaObject.invokeMethod(self._avg_len_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.avg_len)))
        self.blocks_moving_average_xx_0.set_length_and_scale(int(self.avg_len), 1.0/self.avg_len)


def main(top_block_cls=modes_uf_rx_sigmf_v2, options=None):

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
