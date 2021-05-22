#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: /data2/captures/20200329/LRO_RHCP_2020-04-01T22:40:27Z
# GNU Radio version: 3.7.13.5
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
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import threading
import time
from gnuradio import qtgui


class lro_track_2(gr.top_block, Qt.QWidget):

    def __init__(self, avg_len=256, nfft=2048, path="/data2/captures/20200329", record_hz=10, rx_alt=542, rx_lat=37.148745, rx_lon=-80.578557, signal_type='LRO', usrp_type='B210'):
        gr.top_block.__init__(self, "/data2/captures/20200329/LRO_RHCP_2020-04-01T22:40:27Z")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("/data2/captures/20200329/LRO_RHCP_2020-04-01T22:40:27Z")
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

        self.settings = Qt.QSettings("GNU Radio", "lro_track_2")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.avg_len = avg_len
        self.nfft = nfft
        self.path = path
        self.record_hz = record_hz
        self.rx_alt = rx_alt
        self.rx_lat = rx_lat
        self.rx_lon = rx_lon
        self.signal_type = signal_type
        self.usrp_type = usrp_type

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y-%m-%dT%H:%M:%SZ")
        self.rhcp_probe_snr_func = rhcp_probe_snr_func = 0
        self.rhcp_probe_signal_func = rhcp_probe_signal_func = 0
        self.rhcp_probe_offset_func = rhcp_probe_offset_func = 0
        self.rhcp_probe_noise_func = rhcp_probe_noise_func = 0
        self.lhcp_probe_snr_func = lhcp_probe_snr_func = 0
        self.lhcp_probe_signal_func = lhcp_probe_signal_func = 0
        self.lhcp_probe_offset_func = lhcp_probe_offset_func = 0
        self.lhcp_probe_noise_func = lhcp_probe_noise_func = 0
        self.samp_rate = samp_rate = 4e6
        self.rhcp_snr_var = rhcp_snr_var = "{:3.3f}".format(rhcp_probe_snr_func)
        self.rhcp_signal_var = rhcp_signal_var = "{:3.3f}".format(rhcp_probe_signal_func)
        self.rhcp_offset_var = rhcp_offset_var = "{:3.1f}".format(rhcp_probe_offset_func)
        self.rhcp_noise_var = rhcp_noise_var = "{:3.3f}".format(rhcp_probe_noise_func)
        self.lhcp_snr_var = lhcp_snr_var = "{:3.3f}".format(lhcp_probe_snr_func)
        self.lhcp_signal_var = lhcp_signal_var = "{:3.3f}".format(lhcp_probe_signal_func)
        self.lhcp_offset_var = lhcp_offset_var = "{:3.1f}".format(lhcp_probe_offset_func)
        self.lhcp_noise_var = lhcp_noise_var = "{:3.3f}".format(lhcp_probe_noise_func)
        self.fn_rhcp = fn_rhcp = "{:s}_RHCP_{:s}".format(signal_type.upper(), ts_str)
        self.fn_lhcp = fn_lhcp = "{:s}_LHCP_{:s}".format(signal_type.upper(), ts_str)
        self.rx_gain = rx_gain = 20
        self.rx_freq = rx_freq = 2271.2e6
        self.rhcp_snr_label = rhcp_snr_label = rhcp_snr_var
        self.rhcp_signal_label = rhcp_signal_label = rhcp_signal_var
        self.rhcp_offset_label = rhcp_offset_label = rhcp_offset_var
        self.rhcp_noise_label = rhcp_noise_label = rhcp_noise_var
        self.lhcp_signal_label = lhcp_signal_label = lhcp_signal_var
        self.lhcp_offset_label = lhcp_offset_label = lhcp_offset_var
        self.lhcp_noise_label = lhcp_noise_label = lhcp_noise_var
        self.lchp_snr_label = lchp_snr_label = lhcp_snr_var
        self.keep_n = keep_n = samp_rate/record_hz
        self.fp_rhcp = fp_rhcp = "{:s}/{:s}".format(path, fn_rhcp)
        self.fp_lhcp = fp_lhcp = "{:s}/{:s}".format(path, fn_lhcp)
        self.fft_min = fft_min = -115
        self.fft_max = fft_max = -75
        self.decim_0 = decim_0 = 8
        self.decim = decim = 8
        self.alpha = alpha = 1.0/(samp_rate/record_hz)

        ##################################################
        # Blocks
        ##################################################
        self.rhcp_probe_offset = blocks.probe_signal_f()
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel('SAMP_RATE'+": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._samp_rate_tool_bar, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel('GAIN'+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_gain_tool_bar, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('FREQ'+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_freq_tool_bar, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.rhcp_probe_snr = blocks.probe_signal_f()
        self.rhcp_probe_signal = blocks.probe_signal_f()

        def _rhcp_probe_offset_func_probe():
            while True:
                val = self.rhcp_probe_offset.level()
                try:
                    self.set_rhcp_probe_offset_func(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _rhcp_probe_offset_func_thread = threading.Thread(target=_rhcp_probe_offset_func_probe)
        _rhcp_probe_offset_func_thread.daemon = True
        _rhcp_probe_offset_func_thread.start()

        self.rhcp_probe_noise = blocks.probe_signal_f()
        self.lhcp_probe_snr = blocks.probe_signal_f()
        self.lhcp_probe_signal = blocks.probe_signal_f()
        self.lhcp_probe_offset = blocks.probe_signal_f()
        self.lhcp_probe_noise = blocks.probe_signal_f()
        self._fft_min_tool_bar = Qt.QToolBar(self)
        self._fft_min_tool_bar.addWidget(Qt.QLabel('fft_min'+": "))
        self._fft_min_line_edit = Qt.QLineEdit(str(self.fft_min))
        self._fft_min_tool_bar.addWidget(self._fft_min_line_edit)
        self._fft_min_line_edit.returnPressed.connect(
        	lambda: self.set_fft_min(eng_notation.str_to_num(str(self._fft_min_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._fft_min_tool_bar, 0, 3, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._fft_max_tool_bar = Qt.QToolBar(self)
        self._fft_max_tool_bar.addWidget(Qt.QLabel('fft_max'+": "))
        self._fft_max_line_edit = Qt.QLineEdit(str(self.fft_max))
        self._fft_max_tool_bar.addWidget(self._fft_max_line_edit)
        self._fft_max_line_edit.returnPressed.connect(
        	lambda: self.set_fft_max(eng_notation.str_to_num(str(self._fft_max_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._fft_max_tool_bar, 0, 4, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_1 = uhd.usrp_source(
        	",".join(("serial=30CF9D2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_1.set_clock_source('external', 0)
        self.uhd_usrp_source_1.set_time_source('external', 0)
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(rx_freq, samp_rate/2), 0)
        self.uhd_usrp_source_1.set_gain(rx_gain, 0)
        self.uhd_usrp_source_1.set_antenna('RX2', 0)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(rx_freq, samp_rate/2), 1)
        self.uhd_usrp_source_1.set_gain(rx_gain, 1)
        self.uhd_usrp_source_1.set_antenna('RX2', 1)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 1)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 1)
        self._rhcp_snr_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._rhcp_snr_label_formatter = None
        else:
          self._rhcp_snr_label_formatter = lambda x: str(x)

        self._rhcp_snr_label_tool_bar.addWidget(Qt.QLabel('SNR [dB]'+": "))
        self._rhcp_snr_label_label = Qt.QLabel(str(self._rhcp_snr_label_formatter(self.rhcp_snr_label)))
        self._rhcp_snr_label_tool_bar.addWidget(self._rhcp_snr_label_label)
        self.top_grid_layout.addWidget(self._rhcp_snr_label_tool_bar, 9, 3, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rhcp_signal_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._rhcp_signal_label_formatter = None
        else:
          self._rhcp_signal_label_formatter = lambda x: str(x)

        self._rhcp_signal_label_tool_bar.addWidget(Qt.QLabel('Signal [dBFS]'+": "))
        self._rhcp_signal_label_label = Qt.QLabel(str(self._rhcp_signal_label_formatter(self.rhcp_signal_label)))
        self._rhcp_signal_label_tool_bar.addWidget(self._rhcp_signal_label_label)
        self.top_grid_layout.addWidget(self._rhcp_signal_label_tool_bar, 9, 1, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)

        def _rhcp_probe_snr_func_probe():
            while True:
                val = self.rhcp_probe_snr.level()
                try:
                    self.set_rhcp_probe_snr_func(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _rhcp_probe_snr_func_thread = threading.Thread(target=_rhcp_probe_snr_func_probe)
        _rhcp_probe_snr_func_thread.daemon = True
        _rhcp_probe_snr_func_thread.start()


        def _rhcp_probe_signal_func_probe():
            while True:
                val = self.rhcp_probe_signal.level()
                try:
                    self.set_rhcp_probe_signal_func(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _rhcp_probe_signal_func_thread = threading.Thread(target=_rhcp_probe_signal_func_probe)
        _rhcp_probe_signal_func_thread.daemon = True
        _rhcp_probe_signal_func_thread.start()


        def _rhcp_probe_noise_func_probe():
            while True:
                val = self.rhcp_probe_noise.level()
                try:
                    self.set_rhcp_probe_noise_func(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _rhcp_probe_noise_func_thread = threading.Thread(target=_rhcp_probe_noise_func_probe)
        _rhcp_probe_noise_func_thread.daemon = True
        _rhcp_probe_noise_func_thread.start()

        self._rhcp_offset_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._rhcp_offset_label_formatter = None
        else:
          self._rhcp_offset_label_formatter = lambda x: str(x)

        self._rhcp_offset_label_tool_bar.addWidget(Qt.QLabel('Offset [Hz]'+": "))
        self._rhcp_offset_label_label = Qt.QLabel(str(self._rhcp_offset_label_formatter(self.rhcp_offset_label)))
        self._rhcp_offset_label_tool_bar.addWidget(self._rhcp_offset_label_label)
        self.top_grid_layout.addWidget(self._rhcp_offset_label_tool_bar, 9, 0, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rhcp_noise_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._rhcp_noise_label_formatter = None
        else:
          self._rhcp_noise_label_formatter = lambda x: str(x)

        self._rhcp_noise_label_tool_bar.addWidget(Qt.QLabel('Noise [dBFS]'+": "))
        self._rhcp_noise_label_label = Qt.QLabel(str(self._rhcp_noise_label_formatter(self.rhcp_noise_label)))
        self._rhcp_noise_label_tool_bar.addWidget(self._rhcp_noise_label_label)
        self.top_grid_layout.addWidget(self._rhcp_noise_label_tool_bar, 9, 2, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(fft_min, fft_max)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 5, 4, 4, 4)
        for r in range(5, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 5, 0, 4, 4)
        for r in range(5, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"LHCP", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0.set_y_axis(fft_min, fft_max)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.05)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 1, 4, 4, 4)
        for r in range(1, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 1, 0, 4, 4)
        for r in range(1, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._lhcp_signal_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._lhcp_signal_label_formatter = None
        else:
          self._lhcp_signal_label_formatter = lambda x: str(x)

        self._lhcp_signal_label_tool_bar.addWidget(Qt.QLabel('Signal [dBFS]'+": "))
        self._lhcp_signal_label_label = Qt.QLabel(str(self._lhcp_signal_label_formatter(self.lhcp_signal_label)))
        self._lhcp_signal_label_tool_bar.addWidget(self._lhcp_signal_label_label)
        self.top_grid_layout.addWidget(self._lhcp_signal_label_tool_bar, 9, 5, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 6):
            self.top_grid_layout.setColumnStretch(c, 1)

        def _lhcp_probe_snr_func_probe():
            while True:
                val = self.lhcp_probe_snr.level()
                try:
                    self.set_lhcp_probe_snr_func(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _lhcp_probe_snr_func_thread = threading.Thread(target=_lhcp_probe_snr_func_probe)
        _lhcp_probe_snr_func_thread.daemon = True
        _lhcp_probe_snr_func_thread.start()


        def _lhcp_probe_signal_func_probe():
            while True:
                val = self.lhcp_probe_signal.level()
                try:
                    self.set_lhcp_probe_signal_func(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _lhcp_probe_signal_func_thread = threading.Thread(target=_lhcp_probe_signal_func_probe)
        _lhcp_probe_signal_func_thread.daemon = True
        _lhcp_probe_signal_func_thread.start()


        def _lhcp_probe_offset_func_probe():
            while True:
                val = self.lhcp_probe_offset.level()
                try:
                    self.set_lhcp_probe_offset_func(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _lhcp_probe_offset_func_thread = threading.Thread(target=_lhcp_probe_offset_func_probe)
        _lhcp_probe_offset_func_thread.daemon = True
        _lhcp_probe_offset_func_thread.start()


        def _lhcp_probe_noise_func_probe():
            while True:
                val = self.lhcp_probe_noise.level()
                try:
                    self.set_lhcp_probe_noise_func(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _lhcp_probe_noise_func_thread = threading.Thread(target=_lhcp_probe_noise_func_probe)
        _lhcp_probe_noise_func_thread.daemon = True
        _lhcp_probe_noise_func_thread.start()

        self._lhcp_offset_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._lhcp_offset_label_formatter = None
        else:
          self._lhcp_offset_label_formatter = lambda x: str(x)

        self._lhcp_offset_label_tool_bar.addWidget(Qt.QLabel('Offset [Hz]'+": "))
        self._lhcp_offset_label_label = Qt.QLabel(str(self._lhcp_offset_label_formatter(self.lhcp_offset_label)))
        self._lhcp_offset_label_tool_bar.addWidget(self._lhcp_offset_label_label)
        self.top_grid_layout.addWidget(self._lhcp_offset_label_tool_bar, 9, 4, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._lhcp_noise_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._lhcp_noise_label_formatter = None
        else:
          self._lhcp_noise_label_formatter = lambda x: str(x)

        self._lhcp_noise_label_tool_bar.addWidget(Qt.QLabel('Noise [dBFS]'+": "))
        self._lhcp_noise_label_label = Qt.QLabel(str(self._lhcp_noise_label_formatter(self.lhcp_noise_label)))
        self._lhcp_noise_label_tool_bar.addWidget(self._lhcp_noise_label_label)
        self.top_grid_layout.addWidget(self._lhcp_noise_label_tool_bar, 9, 6, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 7):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._lchp_snr_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._lchp_snr_label_formatter = None
        else:
          self._lchp_snr_label_formatter = lambda x: str(x)

        self._lchp_snr_label_tool_bar.addWidget(Qt.QLabel('SNR [dB]'+": "))
        self._lchp_snr_label_label = Qt.QLabel(str(self._lchp_snr_label_formatter(self.lchp_snr_label)))
        self._lchp_snr_label_tool_bar.addWidget(self._lchp_snr_label_label)
        self.top_grid_layout.addWidget(self._lchp_snr_label_tool_bar, 9, 7, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(7, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._keep_n_tool_bar = Qt.QToolBar(self)
        self._keep_n_tool_bar.addWidget(Qt.QLabel('keep_n'+": "))
        self._keep_n_line_edit = Qt.QLineEdit(str(self.keep_n))
        self._keep_n_tool_bar.addWidget(self._keep_n_line_edit)
        self._keep_n_line_edit.returnPressed.connect(
        	lambda: self.set_keep_n(eng_notation.str_to_num(str(self._keep_n_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._keep_n_tool_bar, 0, 6, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 7):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fft_vxx_0_1 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 4)
        self.fft_vxx_0_0_0 = fft.fft_vcc(nfft/decim, True, (window.blackmanharris(nfft/decim)), True, 4)
        self.fft_vxx_0_0 = fft.fft_vcc(nfft/decim, True, (window.blackmanharris(nfft/decim)), True, 4)
        self.fft_vxx_0 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 4)
        self.blocks_sub_xx_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft/decim)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft/decim)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_nlog10_ff_0_0_1 = blocks.nlog10_ff(10, nfft, -10*math.log10(nfft))
        self.blocks_nlog10_ff_0_0_0_0 = blocks.nlog10_ff(10, nfft/decim, -10*math.log10(nfft/decim))
        self.blocks_nlog10_ff_0_0_0 = blocks.nlog10_ff(10, nfft/decim, -10*math.log10(nfft/decim))
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, nfft, -10*math.log10(nfft))
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff((samp_rate/(2*math.pi), ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((samp_rate/(2*math.pi), ))
        self.blocks_moving_average_xx_0_2 = blocks.moving_average_ff(int(avg_len), 1.0/(avg_len)/nfft, 4000, nfft)
        self.blocks_moving_average_xx_0_1_0 = blocks.moving_average_ff(int(samp_rate/record_hz), 1.0/(samp_rate/record_hz), 4000, 1)
        self.blocks_moving_average_xx_0_1 = blocks.moving_average_ff(int(samp_rate/record_hz), 1.0/(samp_rate/record_hz), 4000, 1)
        self.blocks_moving_average_xx_0_0_0 = blocks.moving_average_ff(int(avg_len), 1.0/(avg_len)/(nfft/decim*2), 4000, nfft/decim)
        self.blocks_moving_average_xx_0_0 = blocks.moving_average_ff(int(avg_len), 1.0/(avg_len)/(nfft/decim*2), 4000, nfft/decim)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(int(avg_len), 1.0/(avg_len)/nfft, 4000, nfft)
        self.blocks_max_xx_0_1 = blocks.max_ff(nfft,1)
        self.blocks_max_xx_0_0_0 = blocks.max_ff(nfft/decim,1)
        self.blocks_max_xx_0_0 = blocks.max_ff(nfft/decim,1)
        self.blocks_max_xx_0 = blocks.max_ff(nfft,1)
        self.blocks_keep_one_in_n_0_0_1 = blocks.keep_one_in_n(gr.sizeof_float*1, int(samp_rate/record_hz))
        self.blocks_keep_one_in_n_0_0 = blocks.keep_one_in_n(gr.sizeof_float*1, int(samp_rate/record_hz))
        self.blocks_complex_to_mag_squared_0_0_1 = blocks.complex_to_mag_squared(nfft)
        self.blocks_complex_to_mag_squared_0_0_0_0 = blocks.complex_to_mag_squared(nfft/decim)
        self.blocks_complex_to_mag_squared_0_0_0 = blocks.complex_to_mag_squared(nfft/decim)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(nfft)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, rhcp_probe_offset_func+samp_rate/4, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, rhcp_probe_offset_func+samp_rate/4, 1, 0)
        self.analog_pll_freqdet_cf_0_0 = analog.pll_freqdet_cf(math.pi/200, math.pi/2.0, -math.pi/2.0)
        self.analog_pll_freqdet_cf_0 = analog.pll_freqdet_cf(math.pi/200, math.pi/2.0, -math.pi/2.0)
        self._alpha_tool_bar = Qt.QToolBar(self)
        self._alpha_tool_bar.addWidget(Qt.QLabel('alpha'+": "))
        self._alpha_line_edit = Qt.QLineEdit(str(self.alpha))
        self._alpha_tool_bar.addWidget(self._alpha_line_edit)
        self._alpha_line_edit.returnPressed.connect(
        	lambda: self.set_alpha(eng_notation.str_to_num(str(self._alpha_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._alpha_tool_bar, 0, 5, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 6):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pll_freqdet_cf_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.analog_pll_freqdet_cf_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0_0, 0), (self.blocks_moving_average_xx_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0_0_0, 0), (self.blocks_moving_average_xx_0_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0_1, 0), (self.blocks_moving_average_xx_0_2, 0))
        self.connect((self.blocks_keep_one_in_n_0_0, 0), (self.rhcp_probe_offset, 0))
        self.connect((self.blocks_keep_one_in_n_0_0_1, 0), (self.lhcp_probe_offset, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_max_xx_0, 0), (self.rhcp_probe_signal, 0))
        self.connect((self.blocks_max_xx_0_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_max_xx_0_0, 0), (self.rhcp_probe_noise, 0))
        self.connect((self.blocks_max_xx_0_0_0, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.blocks_max_xx_0_0_0, 0), (self.lhcp_probe_noise, 0))
        self.connect((self.blocks_max_xx_0_1, 0), (self.blocks_sub_xx_0_0, 0))
        self.connect((self.blocks_max_xx_0_1, 0), (self.lhcp_probe_signal, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_nlog10_ff_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0, 0), (self.blocks_nlog10_ff_0_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0_0, 0), (self.blocks_nlog10_ff_0_0_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_1, 0), (self.blocks_keep_one_in_n_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_1_0, 0), (self.blocks_keep_one_in_n_0_0_1, 0))
        self.connect((self.blocks_moving_average_xx_0_2, 0), (self.blocks_nlog10_ff_0_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_moving_average_xx_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_moving_average_xx_0_1_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.blocks_max_xx_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0_0, 0), (self.blocks_max_xx_0_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0_0_0, 0), (self.blocks_max_xx_0_0_0, 0))
        self.connect((self.blocks_nlog10_ff_0_0_1, 0), (self.blocks_max_xx_0_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.fft_vxx_0_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.fft_vxx_0_1, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.rhcp_probe_snr, 0))
        self.connect((self.blocks_sub_xx_0_0, 0), (self.lhcp_probe_snr, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_complex_to_mag_squared_0_0_0, 0))
        self.connect((self.fft_vxx_0_0_0, 0), (self.blocks_complex_to_mag_squared_0_0_0_0, 0))
        self.connect((self.fft_vxx_0_1, 0), (self.blocks_complex_to_mag_squared_0_0_1, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_stream_to_vector_0_0_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.analog_pll_freqdet_cf_0, 0))
        self.connect((self.uhd_usrp_source_1, 1), (self.analog_pll_freqdet_cf_0_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.uhd_usrp_source_1, 1), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.uhd_usrp_source_1, 1), (self.blocks_stream_to_vector_0_1, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_1, 1), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_1, 1), (self.qtgui_waterfall_sink_x_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lro_track_2")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_avg_len(self):
        return self.avg_len

    def set_avg_len(self, avg_len):
        self.avg_len = avg_len
        self.blocks_moving_average_xx_0_2.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/self.nfft)
        self.blocks_moving_average_xx_0_0_0.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/(self.nfft/self.decim*2))
        self.blocks_moving_average_xx_0_0.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/(self.nfft/self.decim*2))
        self.blocks_moving_average_xx_0.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/self.nfft)

    def get_nfft(self):
        return self.nfft

    def set_nfft(self, nfft):
        self.nfft = nfft
        self.blocks_moving_average_xx_0_2.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/self.nfft)
        self.blocks_moving_average_xx_0_0_0.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/(self.nfft/self.decim*2))
        self.blocks_moving_average_xx_0_0.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/(self.nfft/self.decim*2))
        self.blocks_moving_average_xx_0.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/self.nfft)

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        self.set_fp_rhcp("{:s}/{:s}".format(self.path, self.fn_rhcp))
        self.set_fp_lhcp("{:s}/{:s}".format(self.path, self.fn_lhcp))

    def get_record_hz(self):
        return self.record_hz

    def set_record_hz(self, record_hz):
        self.record_hz = record_hz
        self.set_keep_n(self.samp_rate/self.record_hz)
        self.blocks_moving_average_xx_0_1_0.set_length_and_scale(int(self.samp_rate/self.record_hz), 1.0/(self.samp_rate/self.record_hz))
        self.blocks_moving_average_xx_0_1.set_length_and_scale(int(self.samp_rate/self.record_hz), 1.0/(self.samp_rate/self.record_hz))
        self.blocks_keep_one_in_n_0_0_1.set_n(int(self.samp_rate/self.record_hz))
        self.blocks_keep_one_in_n_0_0.set_n(int(self.samp_rate/self.record_hz))
        self.set_alpha(1.0/(self.samp_rate/self.record_hz))

    def get_rx_alt(self):
        return self.rx_alt

    def set_rx_alt(self, rx_alt):
        self.rx_alt = rx_alt

    def get_rx_lat(self):
        return self.rx_lat

    def set_rx_lat(self, rx_lat):
        self.rx_lat = rx_lat

    def get_rx_lon(self):
        return self.rx_lon

    def set_rx_lon(self, rx_lon):
        self.rx_lon = rx_lon

    def get_signal_type(self):
        return self.signal_type

    def set_signal_type(self, signal_type):
        self.signal_type = signal_type

    def get_usrp_type(self):
        return self.usrp_type

    def set_usrp_type(self, usrp_type):
        self.usrp_type = usrp_type

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_fn_rhcp("{:s}_RHCP_{:s}".format(signal_type.upper(), self.ts_str))
        self.set_fn_lhcp("{:s}_LHCP_{:s}".format(signal_type.upper(), self.ts_str))

    def get_rhcp_probe_snr_func(self):
        return self.rhcp_probe_snr_func

    def set_rhcp_probe_snr_func(self, rhcp_probe_snr_func):
        self.rhcp_probe_snr_func = rhcp_probe_snr_func
        self.set_rhcp_snr_var("{:3.3f}".format(self.rhcp_probe_snr_func))

    def get_rhcp_probe_signal_func(self):
        return self.rhcp_probe_signal_func

    def set_rhcp_probe_signal_func(self, rhcp_probe_signal_func):
        self.rhcp_probe_signal_func = rhcp_probe_signal_func
        self.set_rhcp_signal_var("{:3.3f}".format(self.rhcp_probe_signal_func))

    def get_rhcp_probe_offset_func(self):
        return self.rhcp_probe_offset_func

    def set_rhcp_probe_offset_func(self, rhcp_probe_offset_func):
        self.rhcp_probe_offset_func = rhcp_probe_offset_func
        self.set_rhcp_offset_var("{:3.1f}".format(self.rhcp_probe_offset_func))
        self.analog_sig_source_x_0_0.set_frequency(self.rhcp_probe_offset_func+self.samp_rate/4)
        self.analog_sig_source_x_0.set_frequency(self.rhcp_probe_offset_func+self.samp_rate/4)

    def get_rhcp_probe_noise_func(self):
        return self.rhcp_probe_noise_func

    def set_rhcp_probe_noise_func(self, rhcp_probe_noise_func):
        self.rhcp_probe_noise_func = rhcp_probe_noise_func
        self.set_rhcp_noise_var("{:3.3f}".format(self.rhcp_probe_noise_func))

    def get_lhcp_probe_snr_func(self):
        return self.lhcp_probe_snr_func

    def set_lhcp_probe_snr_func(self, lhcp_probe_snr_func):
        self.lhcp_probe_snr_func = lhcp_probe_snr_func
        self.set_lhcp_snr_var("{:3.3f}".format(self.lhcp_probe_snr_func))

    def get_lhcp_probe_signal_func(self):
        return self.lhcp_probe_signal_func

    def set_lhcp_probe_signal_func(self, lhcp_probe_signal_func):
        self.lhcp_probe_signal_func = lhcp_probe_signal_func
        self.set_lhcp_signal_var("{:3.3f}".format(self.lhcp_probe_signal_func))

    def get_lhcp_probe_offset_func(self):
        return self.lhcp_probe_offset_func

    def set_lhcp_probe_offset_func(self, lhcp_probe_offset_func):
        self.lhcp_probe_offset_func = lhcp_probe_offset_func
        self.set_lhcp_offset_var("{:3.1f}".format(self.lhcp_probe_offset_func))

    def get_lhcp_probe_noise_func(self):
        return self.lhcp_probe_noise_func

    def set_lhcp_probe_noise_func(self, lhcp_probe_noise_func):
        self.lhcp_probe_noise_func = lhcp_probe_noise_func
        self.set_lhcp_noise_var("{:3.3f}".format(self.lhcp_probe_noise_func))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq, self.samp_rate/2), 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq, self.samp_rate/2), 1)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.set_keep_n(self.samp_rate/self.record_hz)
        self.blocks_multiply_const_vxx_0_0_0.set_k((self.samp_rate/(2*math.pi), ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.samp_rate/(2*math.pi), ))
        self.blocks_moving_average_xx_0_1_0.set_length_and_scale(int(self.samp_rate/self.record_hz), 1.0/(self.samp_rate/self.record_hz))
        self.blocks_moving_average_xx_0_1.set_length_and_scale(int(self.samp_rate/self.record_hz), 1.0/(self.samp_rate/self.record_hz))
        self.blocks_keep_one_in_n_0_0_1.set_n(int(self.samp_rate/self.record_hz))
        self.blocks_keep_one_in_n_0_0.set_n(int(self.samp_rate/self.record_hz))
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_frequency(self.rhcp_probe_offset_func+self.samp_rate/4)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_frequency(self.rhcp_probe_offset_func+self.samp_rate/4)
        self.set_alpha(1.0/(self.samp_rate/self.record_hz))

    def get_rhcp_snr_var(self):
        return self.rhcp_snr_var

    def set_rhcp_snr_var(self, rhcp_snr_var):
        self.rhcp_snr_var = rhcp_snr_var
        self.set_rhcp_snr_label(self._rhcp_snr_label_formatter(self.rhcp_snr_var))

    def get_rhcp_signal_var(self):
        return self.rhcp_signal_var

    def set_rhcp_signal_var(self, rhcp_signal_var):
        self.rhcp_signal_var = rhcp_signal_var
        self.set_rhcp_signal_label(self._rhcp_signal_label_formatter(self.rhcp_signal_var))

    def get_rhcp_offset_var(self):
        return self.rhcp_offset_var

    def set_rhcp_offset_var(self, rhcp_offset_var):
        self.rhcp_offset_var = rhcp_offset_var
        self.set_rhcp_offset_label(self._rhcp_offset_label_formatter(self.rhcp_offset_var))

    def get_rhcp_noise_var(self):
        return self.rhcp_noise_var

    def set_rhcp_noise_var(self, rhcp_noise_var):
        self.rhcp_noise_var = rhcp_noise_var
        self.set_rhcp_noise_label(self._rhcp_noise_label_formatter(self.rhcp_noise_var))

    def get_lhcp_snr_var(self):
        return self.lhcp_snr_var

    def set_lhcp_snr_var(self, lhcp_snr_var):
        self.lhcp_snr_var = lhcp_snr_var
        self.set_lchp_snr_label(self._lchp_snr_label_formatter(self.lhcp_snr_var))

    def get_lhcp_signal_var(self):
        return self.lhcp_signal_var

    def set_lhcp_signal_var(self, lhcp_signal_var):
        self.lhcp_signal_var = lhcp_signal_var
        self.set_lhcp_signal_label(self._lhcp_signal_label_formatter(self.lhcp_signal_var))

    def get_lhcp_offset_var(self):
        return self.lhcp_offset_var

    def set_lhcp_offset_var(self, lhcp_offset_var):
        self.lhcp_offset_var = lhcp_offset_var
        self.set_lhcp_offset_label(self._lhcp_offset_label_formatter(self.lhcp_offset_var))

    def get_lhcp_noise_var(self):
        return self.lhcp_noise_var

    def set_lhcp_noise_var(self, lhcp_noise_var):
        self.lhcp_noise_var = lhcp_noise_var
        self.set_lhcp_noise_label(self._lhcp_noise_label_formatter(self.lhcp_noise_var))

    def get_fn_rhcp(self):
        return self.fn_rhcp

    def set_fn_rhcp(self, fn_rhcp):
        self.fn_rhcp = fn_rhcp
        self.set_fp_rhcp("{:s}/{:s}".format(self.path, self.fn_rhcp))

    def get_fn_lhcp(self):
        return self.fn_lhcp

    def set_fn_lhcp(self, fn_lhcp):
        self.fn_lhcp = fn_lhcp
        self.set_fp_lhcp("{:s}/{:s}".format(self.path, self.fn_lhcp))

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))
        self.uhd_usrp_source_1.set_gain(self.rx_gain, 0)

        self.uhd_usrp_source_1.set_gain(self.rx_gain, 1)


    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq, self.samp_rate/2), 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq, self.samp_rate/2), 1)

    def get_rhcp_snr_label(self):
        return self.rhcp_snr_label

    def set_rhcp_snr_label(self, rhcp_snr_label):
        self.rhcp_snr_label = rhcp_snr_label
        Qt.QMetaObject.invokeMethod(self._rhcp_snr_label_label, "setText", Qt.Q_ARG("QString", self.rhcp_snr_label))

    def get_rhcp_signal_label(self):
        return self.rhcp_signal_label

    def set_rhcp_signal_label(self, rhcp_signal_label):
        self.rhcp_signal_label = rhcp_signal_label
        Qt.QMetaObject.invokeMethod(self._rhcp_signal_label_label, "setText", Qt.Q_ARG("QString", self.rhcp_signal_label))

    def get_rhcp_offset_label(self):
        return self.rhcp_offset_label

    def set_rhcp_offset_label(self, rhcp_offset_label):
        self.rhcp_offset_label = rhcp_offset_label
        Qt.QMetaObject.invokeMethod(self._rhcp_offset_label_label, "setText", Qt.Q_ARG("QString", self.rhcp_offset_label))

    def get_rhcp_noise_label(self):
        return self.rhcp_noise_label

    def set_rhcp_noise_label(self, rhcp_noise_label):
        self.rhcp_noise_label = rhcp_noise_label
        Qt.QMetaObject.invokeMethod(self._rhcp_noise_label_label, "setText", Qt.Q_ARG("QString", self.rhcp_noise_label))

    def get_lhcp_signal_label(self):
        return self.lhcp_signal_label

    def set_lhcp_signal_label(self, lhcp_signal_label):
        self.lhcp_signal_label = lhcp_signal_label
        Qt.QMetaObject.invokeMethod(self._lhcp_signal_label_label, "setText", Qt.Q_ARG("QString", self.lhcp_signal_label))

    def get_lhcp_offset_label(self):
        return self.lhcp_offset_label

    def set_lhcp_offset_label(self, lhcp_offset_label):
        self.lhcp_offset_label = lhcp_offset_label
        Qt.QMetaObject.invokeMethod(self._lhcp_offset_label_label, "setText", Qt.Q_ARG("QString", self.lhcp_offset_label))

    def get_lhcp_noise_label(self):
        return self.lhcp_noise_label

    def set_lhcp_noise_label(self, lhcp_noise_label):
        self.lhcp_noise_label = lhcp_noise_label
        Qt.QMetaObject.invokeMethod(self._lhcp_noise_label_label, "setText", Qt.Q_ARG("QString", self.lhcp_noise_label))

    def get_lchp_snr_label(self):
        return self.lchp_snr_label

    def set_lchp_snr_label(self, lchp_snr_label):
        self.lchp_snr_label = lchp_snr_label
        Qt.QMetaObject.invokeMethod(self._lchp_snr_label_label, "setText", Qt.Q_ARG("QString", self.lchp_snr_label))

    def get_keep_n(self):
        return self.keep_n

    def set_keep_n(self, keep_n):
        self.keep_n = keep_n
        Qt.QMetaObject.invokeMethod(self._keep_n_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.keep_n)))

    def get_fp_rhcp(self):
        return self.fp_rhcp

    def set_fp_rhcp(self, fp_rhcp):
        self.fp_rhcp = fp_rhcp

    def get_fp_lhcp(self):
        return self.fp_lhcp

    def set_fp_lhcp(self, fp_lhcp):
        self.fp_lhcp = fp_lhcp

    def get_fft_min(self):
        return self.fft_min

    def set_fft_min(self, fft_min):
        self.fft_min = fft_min
        Qt.QMetaObject.invokeMethod(self._fft_min_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.fft_min)))
        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(self.fft_min, self.fft_max)
        self.qtgui_waterfall_sink_x_0.set_intensity_range(self.fft_min, self.fft_max)
        self.qtgui_freq_sink_x_0_0.set_y_axis(self.fft_min, self.fft_max)
        self.qtgui_freq_sink_x_0.set_y_axis(self.fft_min, self.fft_max)

    def get_fft_max(self):
        return self.fft_max

    def set_fft_max(self, fft_max):
        self.fft_max = fft_max
        Qt.QMetaObject.invokeMethod(self._fft_max_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.fft_max)))
        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(self.fft_min, self.fft_max)
        self.qtgui_waterfall_sink_x_0.set_intensity_range(self.fft_min, self.fft_max)
        self.qtgui_freq_sink_x_0_0.set_y_axis(self.fft_min, self.fft_max)
        self.qtgui_freq_sink_x_0.set_y_axis(self.fft_min, self.fft_max)

    def get_decim_0(self):
        return self.decim_0

    def set_decim_0(self, decim_0):
        self.decim_0 = decim_0

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.blocks_moving_average_xx_0_0_0.set_length_and_scale(int(self.avg_len), 1.0/(self.avg_len)/(self.nfft/self.decim*2))
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
        "", "--path", dest="path", type="string", default="/data2/captures/20200329",
        help="Set path [default=%default]")
    parser.add_option(
        "", "--record-hz", dest="record_hz", type="intx", default=10,
        help="Set record_hz [default=%default]")
    parser.add_option(
        "", "--rx-alt", dest="rx_alt", type="eng_float", default=eng_notation.num_to_str(542),
        help="Set rx_alt [default=%default]")
    parser.add_option(
        "", "--rx-lat", dest="rx_lat", type="eng_float", default=eng_notation.num_to_str(37.148745),
        help="Set rx_lat [default=%default]")
    parser.add_option(
        "", "--rx-lon", dest="rx_lon", type="eng_float", default=eng_notation.num_to_str(-80.578557),
        help="Set rx_lon [default=%default]")
    parser.add_option(
        "", "--signal-type", dest="signal_type", type="string", default='LRO',
        help="Set signal_type [default=%default]")
    parser.add_option(
        "", "--usrp-type", dest="usrp_type", type="string", default='B210',
        help="Set usrp_type [default=%default]")
    return parser


def main(top_block_cls=lro_track_2, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(avg_len=options.avg_len, nfft=options.nfft, path=options.path, record_hz=options.record_hz, rx_alt=options.rx_alt, rx_lat=options.rx_lat, rx_lon=options.rx_lon, signal_type=options.signal_type, usrp_type=options.usrp_type)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
