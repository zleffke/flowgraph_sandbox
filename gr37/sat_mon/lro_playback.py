#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: /captures/20200329/LRO_RHCP_2020-03-29T20:34:45Z.sigmf-data
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
from datetime import datetime as dt; import string; import math
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import gr_sigmf
import pmt
import sip
import sys
import threading
import time
from gnuradio import qtgui


class lro_playback(gr.top_block, Qt.QWidget):

    def __init__(self, avg_len=256, nfft=2048, path="/captures/20200329", record_hz=10):
        gr.top_block.__init__(self, "/captures/20200329/LRO_RHCP_2020-03-29T20:34:45Z.sigmf-data")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("/captures/20200329/LRO_RHCP_2020-03-29T20:34:45Z.sigmf-data")
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

        self.settings = Qt.QSettings("GNU Radio", "lro_playback")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.avg_len = avg_len
        self.nfft = nfft
        self.path = path
        self.record_hz = record_hz

        ##################################################
        # Variables
        ##################################################
        self.probe_snr_func = probe_snr_func = 0
        self.probe_signal_func = probe_signal_func = 0
        self.probe_offset_func = probe_offset_func = 0
        self.probe_noise_func = probe_noise_func = 0
        self.filename = filename = "LRO_RHCP_2020-03-29T20:34:45Z.sigmf-data"
        self.snr_var = snr_var = "{:3.3f}".format(probe_snr_func)
        self.signal_var = signal_var = "{:3.3f}".format(probe_signal_func)
        self.samp_rate = samp_rate = 250e3
        self.offset_var = offset_var = "{:3.3f}".format(probe_offset_func)
        self.offset_file = offset_file = "{:s}_{:s}".format(filename.split(".")[0], "offset")
        self.noise_var = noise_var = "{:3.3f}".format(probe_noise_func)
        self.variable_tag_object_0 = variable_tag_object_0 = gr.tag_utils.python_to_tag((0, pmt.intern("key"), pmt.intern("value"), pmt.intern("src")))
        self.throttle_factor = throttle_factor = 10
        self.snr_label = snr_label = snr_var
        self.signal_label = signal_label = signal_var
        self.rx_freq = rx_freq = 2271.2e6
        self.offset_label = offset_label = offset_var
        self.offset_fp = offset_fp = "/".join([path,offset_file])
        self.noise_label = noise_label = noise_var
        self.keep_n = keep_n = samp_rate/record_hz
        self.fp = fp = "/".join([path,filename])
        self.file_l = file_l = filename.split(".")[0].split("_")
        self.fft_min = fft_min = -120
        self.fft_max = fft_max = -80
        self.decim = decim = 8
        self.alpha = alpha = 1.0/(samp_rate/record_hz)

        ##################################################
        # Blocks
        ##################################################
        self.probe_offset = blocks.probe_signal_f()
        self._throttle_factor_tool_bar = Qt.QToolBar(self)
        self._throttle_factor_tool_bar.addWidget(Qt.QLabel('Throttle'+": "))
        self._throttle_factor_line_edit = Qt.QLineEdit(str(self.throttle_factor))
        self._throttle_factor_tool_bar.addWidget(self._throttle_factor_line_edit)
        self._throttle_factor_line_edit.returnPressed.connect(
        	lambda: self.set_throttle_factor(eng_notation.str_to_num(str(self._throttle_factor_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._throttle_factor_tool_bar, 10, 2, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel('SAMP_RATE'+": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._samp_rate_tool_bar, 9, 0, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.probe_snr = blocks.probe_signal_f()
        self.probe_signal = blocks.probe_signal_f()

        def _probe_offset_func_probe():
            while True:
                val = self.probe_offset.level()
                try:
                    self.set_probe_offset_func(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _probe_offset_func_thread = threading.Thread(target=_probe_offset_func_probe)
        _probe_offset_func_thread.daemon = True
        _probe_offset_func_thread.start()

        self.probe_noise = blocks.probe_signal_f()
        self._fft_min_tool_bar = Qt.QToolBar(self)
        self._fft_min_tool_bar.addWidget(Qt.QLabel('fft_min'+": "))
        self._fft_min_line_edit = Qt.QLineEdit(str(self.fft_min))
        self._fft_min_tool_bar.addWidget(self._fft_min_line_edit)
        self._fft_min_line_edit.returnPressed.connect(
        	lambda: self.set_fft_min(eng_notation.str_to_num(str(self._fft_min_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._fft_min_tool_bar, 9, 2, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._fft_max_tool_bar = Qt.QToolBar(self)
        self._fft_max_tool_bar.addWidget(Qt.QLabel('fft_max'+": "))
        self._fft_max_line_edit = Qt.QLineEdit(str(self.fft_max))
        self._fft_max_tool_bar.addWidget(self._fft_max_line_edit)
        self._fft_max_line_edit.returnPressed.connect(
        	lambda: self.set_fft_max(eng_notation.str_to_num(str(self._fft_max_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._fft_max_tool_bar, 9, 3, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._snr_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._snr_label_formatter = None
        else:
          self._snr_label_formatter = lambda x: str(x)

        self._snr_label_tool_bar.addWidget(Qt.QLabel('SNR [dB]'+": "))
        self._snr_label_label = Qt.QLabel(str(self._snr_label_formatter(self.snr_label)))
        self._snr_label_tool_bar.addWidget(self._snr_label_label)
        self.top_grid_layout.addWidget(self._snr_label_tool_bar, 3, 4, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._signal_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._signal_label_formatter = None
        else:
          self._signal_label_formatter = lambda x: str(x)

        self._signal_label_tool_bar.addWidget(Qt.QLabel('Signal [dBFS]'+": "))
        self._signal_label_label = Qt.QLabel(str(self._signal_label_formatter(self.signal_label)))
        self._signal_label_tool_bar.addWidget(self._signal_label_label)
        self.top_grid_layout.addWidget(self._signal_label_tool_bar, 1, 4, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.sigmf_source_0 = gr_sigmf.source(fp, "cf32" + ("_le" if sys.byteorder == "little" else "_be"), False)
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('FREQ'+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_freq_tool_bar, 9, 1, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
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

        self.qtgui_waterfall_sink_x_0.set_intensity_range(fft_min, fft_max)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 4, 0, 4, 4)
        for r in range(4, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"RHCP", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(fft_min, fft_max)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)

        def _probe_snr_func_probe():
            while True:
                val = self.probe_snr.level()
                try:
                    self.set_probe_snr_func(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _probe_snr_func_thread = threading.Thread(target=_probe_snr_func_probe)
        _probe_snr_func_thread.daemon = True
        _probe_snr_func_thread.start()


        def _probe_signal_func_probe():
            while True:
                val = self.probe_signal.level()
                try:
                    self.set_probe_signal_func(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _probe_signal_func_thread = threading.Thread(target=_probe_signal_func_probe)
        _probe_signal_func_thread.daemon = True
        _probe_signal_func_thread.start()


        def _probe_noise_func_probe():
            while True:
                val = self.probe_noise.level()
                try:
                    self.set_probe_noise_func(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _probe_noise_func_thread = threading.Thread(target=_probe_noise_func_probe)
        _probe_noise_func_thread.daemon = True
        _probe_noise_func_thread.start()

        self._offset_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._offset_label_formatter = None
        else:
          self._offset_label_formatter = lambda x: str(x)

        self._offset_label_tool_bar.addWidget(Qt.QLabel('Offset [Hz]'+": "))
        self._offset_label_label = Qt.QLabel(str(self._offset_label_formatter(self.offset_label)))
        self._offset_label_tool_bar.addWidget(self._offset_label_label)
        self.top_grid_layout.addWidget(self._offset_label_tool_bar, 0, 4, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._noise_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._noise_label_formatter = None
        else:
          self._noise_label_formatter = lambda x: str(x)

        self._noise_label_tool_bar.addWidget(Qt.QLabel('Noise [dBFS]'+": "))
        self._noise_label_label = Qt.QLabel(str(self._noise_label_formatter(self.noise_label)))
        self._noise_label_tool_bar.addWidget(self._noise_label_label)
        self.top_grid_layout.addWidget(self._noise_label_tool_bar, 2, 4, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._keep_n_tool_bar = Qt.QToolBar(self)
        self._keep_n_tool_bar.addWidget(Qt.QLabel('keep_n'+": "))
        self._keep_n_line_edit = Qt.QLineEdit(str(self.keep_n))
        self._keep_n_tool_bar.addWidget(self._keep_n_line_edit)
        self._keep_n_line_edit.returnPressed.connect(
        	lambda: self.set_keep_n(eng_notation.str_to_num(str(self._keep_n_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._keep_n_tool_bar, 10, 1, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fft_vxx_0_0 = fft.fft_vcc(nfft/decim, True, (window.blackmanharris(nfft/decim)), True, 4)
        self.fft_vxx_0 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 4)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate*throttle_factor,True)
        self.blocks_tag_share_0 = blocks.tag_share(gr.sizeof_float, gr.sizeof_gr_complex, 1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft/decim)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_nlog10_ff_0_0_0 = blocks.nlog10_ff(10, nfft/decim, -10*math.log10(nfft/decim))
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, nfft, -10*math.log10(nfft))
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((samp_rate/(2*math.pi), ))
        self.blocks_moving_average_xx_0_1 = blocks.moving_average_ff(int(samp_rate/record_hz), 1.0/(samp_rate/record_hz), 4000, 1)
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_ff(int(avg_len), 1.0/(avg_len)/(nfft/decim*2), 4000, nfft/decim)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(int(avg_len), 1.0/(avg_len)/nfft, 4000, nfft)
        self.blocks_max_xx_0_0 = blocks.max_ff(nfft/decim,1)
        self.blocks_max_xx_0 = blocks.max_ff(nfft,1)
        self.blocks_keep_one_in_n_0_0 = blocks.keep_one_in_n(gr.sizeof_float*1, int(samp_rate/record_hz))
        self.blocks_complex_to_mag_squared_0_0_0 = blocks.complex_to_mag_squared(nfft/decim)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(nfft)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, probe_offset_func+samp_rate/4, 1, 0)
        self.analog_pll_freqdet_cf_0 = analog.pll_freqdet_cf(math.pi/200, math.pi/10, -math.pi/10)
        self._alpha_tool_bar = Qt.QToolBar(self)
        self._alpha_tool_bar.addWidget(Qt.QLabel('alpha'+": "))
        self._alpha_line_edit = Qt.QLineEdit(str(self.alpha))
        self._alpha_tool_bar.addWidget(self._alpha_line_edit)
        self._alpha_line_edit.returnPressed.connect(
        	lambda: self.set_alpha(eng_notation.str_to_num(str(self._alpha_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._alpha_tool_bar, 10, 0, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pll_freqdet_cf_0, 0), (self.blocks_tag_share_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0_0, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.blocks_keep_one_in_n_0_0, 0), (self.probe_offset, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.probe_signal, 0))
        self.connect((self.blocks_max_xx_0_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_max_xx_0_0, 0), (self.probe_noise, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_nlog10_ff_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.blocks_nlog10_ff_0_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_1, 0), (self.blocks_keep_one_in_n_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_moving_average_xx_0_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.blocks_max_xx_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0_0, 0), (self.blocks_max_xx_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_0_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.probe_snr, 0))
        self.connect((self.blocks_tag_share_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_pll_freqdet_cf_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_tag_share_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_complex_to_mag_squared_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.sigmf_source_0, 0), (self.blocks_throttle_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lro_playback")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_avg_len(self):
        return self.avg_len

    def set_avg_len(self, avg_len):
        self.avg_len = avg_len
        self.blocks_moving_average_xx_0_0.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/(self.nfft/self.decim*2))
        self.blocks_moving_average_xx_0.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/self.nfft)

    def get_nfft(self):
        return self.nfft

    def set_nfft(self, nfft):
        self.nfft = nfft
        self.blocks_moving_average_xx_0_0.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/(self.nfft/self.decim*2))
        self.blocks_moving_average_xx_0.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/self.nfft)

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        self.set_fp("/".join([self.path,self.filename]))
        self.set_offset_fp("/".join([self.path,self.offset_file]))

    def get_record_hz(self):
        return self.record_hz

    def set_record_hz(self, record_hz):
        self.record_hz = record_hz
        self.set_keep_n(self.samp_rate/self.record_hz)
        self.blocks_moving_average_xx_0_1.set_length_and_scale(int(self.samp_rate/self.record_hz), 1.0/(self.samp_rate/self.record_hz))
        self.blocks_keep_one_in_n_0_0.set_n(int(self.samp_rate/self.record_hz))
        self.set_alpha(1.0/(self.samp_rate/self.record_hz))

    def get_probe_snr_func(self):
        return self.probe_snr_func

    def set_probe_snr_func(self, probe_snr_func):
        self.probe_snr_func = probe_snr_func
        self.set_snr_var("{:3.3f}".format(self.probe_snr_func))

    def get_probe_signal_func(self):
        return self.probe_signal_func

    def set_probe_signal_func(self, probe_signal_func):
        self.probe_signal_func = probe_signal_func
        self.set_signal_var("{:3.3f}".format(self.probe_signal_func))

    def get_probe_offset_func(self):
        return self.probe_offset_func

    def set_probe_offset_func(self, probe_offset_func):
        self.probe_offset_func = probe_offset_func
        self.set_offset_var("{:3.3f}".format(self.probe_offset_func))
        self.analog_sig_source_x_0.set_frequency(self.probe_offset_func+self.samp_rate/4)

    def get_probe_noise_func(self):
        return self.probe_noise_func

    def set_probe_noise_func(self, probe_noise_func):
        self.probe_noise_func = probe_noise_func
        self.set_noise_var("{:3.3f}".format(self.probe_noise_func))

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
        self.set_fp("/".join([self.path,self.filename]))

    def get_snr_var(self):
        return self.snr_var

    def set_snr_var(self, snr_var):
        self.snr_var = snr_var
        self.set_snr_label(self._snr_label_formatter(self.snr_var))

    def get_signal_var(self):
        return self.signal_var

    def set_signal_var(self, signal_var):
        self.signal_var = signal_var
        self.set_signal_label(self._signal_label_formatter(self.signal_var))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.set_keep_n(self.samp_rate/self.record_hz)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.throttle_factor)
        self.blocks_multiply_const_vxx_0_0.set_k((self.samp_rate/(2*math.pi), ))
        self.blocks_moving_average_xx_0_1.set_length_and_scale(int(self.samp_rate/self.record_hz), 1.0/(self.samp_rate/self.record_hz))
        self.blocks_keep_one_in_n_0_0.set_n(int(self.samp_rate/self.record_hz))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_frequency(self.probe_offset_func+self.samp_rate/4)
        self.set_alpha(1.0/(self.samp_rate/self.record_hz))

    def get_offset_var(self):
        return self.offset_var

    def set_offset_var(self, offset_var):
        self.offset_var = offset_var
        self.set_offset_label(self._offset_label_formatter(self.offset_var))

    def get_offset_file(self):
        return self.offset_file

    def set_offset_file(self, offset_file):
        self.offset_file = offset_file
        self.set_offset_fp("/".join([self.path,self.offset_file]))

    def get_noise_var(self):
        return self.noise_var

    def set_noise_var(self, noise_var):
        self.noise_var = noise_var
        self.set_noise_label(self._noise_label_formatter(self.noise_var))

    def get_variable_tag_object_0(self):
        return self.variable_tag_object_0

    def set_variable_tag_object_0(self, variable_tag_object_0):
        self.variable_tag_object_0 = variable_tag_object_0

    def get_throttle_factor(self):
        return self.throttle_factor

    def set_throttle_factor(self, throttle_factor):
        self.throttle_factor = throttle_factor
        Qt.QMetaObject.invokeMethod(self._throttle_factor_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.throttle_factor)))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.throttle_factor)

    def get_snr_label(self):
        return self.snr_label

    def set_snr_label(self, snr_label):
        self.snr_label = snr_label
        Qt.QMetaObject.invokeMethod(self._snr_label_label, "setText", Qt.Q_ARG("QString", self.snr_label))

    def get_signal_label(self):
        return self.signal_label

    def set_signal_label(self, signal_label):
        self.signal_label = signal_label
        Qt.QMetaObject.invokeMethod(self._signal_label_label, "setText", Qt.Q_ARG("QString", self.signal_label))

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))

    def get_offset_label(self):
        return self.offset_label

    def set_offset_label(self, offset_label):
        self.offset_label = offset_label
        Qt.QMetaObject.invokeMethod(self._offset_label_label, "setText", Qt.Q_ARG("QString", self.offset_label))

    def get_offset_fp(self):
        return self.offset_fp

    def set_offset_fp(self, offset_fp):
        self.offset_fp = offset_fp

    def get_noise_label(self):
        return self.noise_label

    def set_noise_label(self, noise_label):
        self.noise_label = noise_label
        Qt.QMetaObject.invokeMethod(self._noise_label_label, "setText", Qt.Q_ARG("QString", self.noise_label))

    def get_keep_n(self):
        return self.keep_n

    def set_keep_n(self, keep_n):
        self.keep_n = keep_n
        Qt.QMetaObject.invokeMethod(self._keep_n_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.keep_n)))

    def get_fp(self):
        return self.fp

    def set_fp(self, fp):
        self.fp = fp

    def get_file_l(self):
        return self.file_l

    def set_file_l(self, file_l):
        self.file_l = file_l

    def get_fft_min(self):
        return self.fft_min

    def set_fft_min(self, fft_min):
        self.fft_min = fft_min
        Qt.QMetaObject.invokeMethod(self._fft_min_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.fft_min)))
        self.qtgui_waterfall_sink_x_0.set_intensity_range(self.fft_min, self.fft_max)
        self.qtgui_freq_sink_x_0.set_y_axis(self.fft_min, self.fft_max)

    def get_fft_max(self):
        return self.fft_max

    def set_fft_max(self, fft_max):
        self.fft_max = fft_max
        Qt.QMetaObject.invokeMethod(self._fft_max_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.fft_max)))
        self.qtgui_waterfall_sink_x_0.set_intensity_range(self.fft_min, self.fft_max)
        self.qtgui_freq_sink_x_0.set_y_axis(self.fft_min, self.fft_max)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.blocks_moving_average_xx_0_0.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/(self.nfft/self.decim*2))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        Qt.QMetaObject.invokeMethod(self._alpha_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.alpha)))


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--avg-len", dest="avg_len", type="eng_float", default=eng_notation.num_to_str(256),
        help="Set avg_len [default=%default]")
    parser.add_option(
        "", "--nfft", dest="nfft", type="intx", default=2048,
        help="Set nfft [default=%default]")
    parser.add_option(
        "", "--path", dest="path", type="string", default="/captures/20200329",
        help="Set path [default=%default]")
    parser.add_option(
        "", "--record-hz", dest="record_hz", type="intx", default=10,
        help="Set record_hz [default=%default]")
    return parser


def main(top_block_cls=lro_playback, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(avg_len=options.avg_len, nfft=options.nfft, path=options.path, record_hz=options.record_hz)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
