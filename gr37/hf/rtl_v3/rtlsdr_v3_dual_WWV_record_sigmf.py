#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Dual RTL-SDR, WWV Receiver / Analyzer
# Author: Zach Leffke, KJ4QLP
# Description: Analyze power, doppler, polarization of WWV emissions
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
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import gr_sigmf
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class rtlsdr_v3_dual_WWV_record_sigmf(gr.top_block, Qt.QWidget):

    def __init__(self, path="/captures/wwv", signal_type='WWV'):
        gr.top_block.__init__(self, "Dual RTL-SDR, WWV Receiver / Analyzer")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Dual RTL-SDR, WWV Receiver / Analyzer")
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

        self.settings = Qt.QSettings("GNU Radio", "rtlsdr_v3_dual_WWV_record_sigmf")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.path = path
        self.signal_type = signal_type

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y-%m-%dT%H:%M:%SZ")
        self.antenna_1 = antenna_1 = "EW"
        self.antenna_0 = antenna_0 = "NS"
        self.samp_rate = samp_rate = 2048000
        self.fn_1 = fn_1 = "{:s}_{:s}_{:s}".format(signal_type.upper(), antenna_1.upper(),ts_str)
        self.fn_0 = fn_0 = "{:s}_{:s}_{:s}".format(signal_type.upper(), antenna_0.upper(),ts_str)
        self.rx_gain = rx_gain = 10
        self.rx_freq = rx_freq = 15e6
        self.ppm = ppm = 0
        self.offset = offset = samp_rate/4
        self.noise_cal = noise_cal = True
        self.interp_1 = interp_1 = 100
        self.fp_1 = fp_1 = "{:s}/{:s}".format(path, fn_1)
        self.fp_0 = fp_0 = "{:s}/{:s}".format(path, fn_0)
        self.decim_1 = decim_1 = 2048*2

        ##################################################
        # Blocks
        ##################################################
        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel('Gain'+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_gain_tool_bar, 4, 2, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('Freq [Hz]'+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_freq_tool_bar, 4, 0, 1, 2)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._ppm_tool_bar = Qt.QToolBar(self)
        self._ppm_tool_bar.addWidget(Qt.QLabel('PPM'+": "))
        self._ppm_line_edit = Qt.QLineEdit(str(self.ppm))
        self._ppm_tool_bar.addWidget(self._ppm_line_edit)
        self._ppm_line_edit.returnPressed.connect(
        	lambda: self.set_ppm(eng_notation.str_to_num(str(self._ppm_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._ppm_tool_bar, 4, 3, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.sigmf_sink_0_1 = gr_sigmf.sink("cf32", fp_1, gr_sigmf.sigmf_time_mode_absolute, False)
        self.sigmf_sink_0_1.set_global_meta("core:sample_rate", samp_rate / decim_1*interp_1)
        self.sigmf_sink_0_1.set_global_meta("core:description", 'WWV Recorder - EW Antenna')
        self.sigmf_sink_0_1.set_global_meta("core:author", 'Zach Leffke, KJ4QLP')
        self.sigmf_sink_0_1.set_global_meta("core:license", 'MIT')
        self.sigmf_sink_0_1.set_global_meta("core:hw", 'Dual RTLSDR V3, shared clock, KJ4QLP AHFDB')
        self.sigmf_sink_0_1.set_global_meta('misc:analog_filter', 'QRP Labs 20.1 MHz BPF')
        self.sigmf_sink_0_1.set_global_meta('antenna:id', 'EW')
        self.sigmf_sink_0_1.set_global_meta('antenna:description', 'Active HF Dipole, LWA type, 45 deg arm')
        self.sigmf_sink_0_1.set_global_meta('rtlsdr:device_index', 1)
        self.sigmf_sink_0_1.set_global_meta('rtlsdr:serial', '00000102')
        self.sigmf_sink_0_1.set_global_meta('antenna:orientation', 'East/West')
        self.sigmf_sink_0_1.set_global_meta('core:frequency', 15000000.0)
        self.sigmf_sink_0_1.set_global_meta('rtlsdr:noise_cal', True)

        self.sigmf_sink_0 = gr_sigmf.sink("cf32", fp_0, gr_sigmf.sigmf_time_mode_absolute, False)
        self.sigmf_sink_0.set_global_meta("core:sample_rate", samp_rate / decim_1*interp_1)
        self.sigmf_sink_0.set_global_meta("core:description", 'WWV Recorder - NS Antenna')
        self.sigmf_sink_0.set_global_meta("core:author", 'Zach Leffke, KJ4QLP')
        self.sigmf_sink_0.set_global_meta("core:license", 'MIT')
        self.sigmf_sink_0.set_global_meta("core:hw", 'Dual RTLSDR V3, shared clock, KJ4QLP AHFDB')
        self.sigmf_sink_0.set_global_meta('misc:analog_filter', 'QRP Labs 20.1 MHz BPF')
        self.sigmf_sink_0.set_global_meta('antenna:id', 'NS')
        self.sigmf_sink_0.set_global_meta('antenna:description', 'Active HF Dipole, LWA type, 45 deg arm')
        self.sigmf_sink_0.set_global_meta('rtlsdr:device_index', 0)
        self.sigmf_sink_0.set_global_meta('rtlsdr:serial', '00000101')
        self.sigmf_sink_0.set_global_meta('antenna:orientation', 'North/South')
        self.sigmf_sink_0.set_global_meta('core:frequency', 15000000.0)
        self.sigmf_sink_0.set_global_meta('rtlsdr:noise_cal', True)

        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=interp_1,
                decimation=decim_1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=interp_1,
                decimation=decim_1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate/decim_1*interp_1, #bw
        	"E/W", #name
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

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 2, 4, 2, 4)
        for r in range(2, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate/decim_1*interp_1, #bw
        	"N/S", #name
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

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win, 0, 4, 2, 4)
        for r in range(0, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq*0, #fc
        	samp_rate / decim_1 *interp_1, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['N/S', 'E/W', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.osmosdr_source_1 = osmosdr.source( args="numchan=" + str(1) + " " + "rtl=1,direct_samp=2" )
        self.osmosdr_source_1.set_sample_rate(samp_rate)
        self.osmosdr_source_1.set_center_freq(rx_freq-offset, 0)
        self.osmosdr_source_1.set_freq_corr(ppm, 0)
        self.osmosdr_source_1.set_dc_offset_mode(0, 0)
        self.osmosdr_source_1.set_iq_balance_mode(0, 0)
        self.osmosdr_source_1.set_gain_mode(False, 0)
        self.osmosdr_source_1.set_gain(rx_gain, 0)
        self.osmosdr_source_1.set_if_gain(20, 0)
        self.osmosdr_source_1.set_bb_gain(20, 0)
        self.osmosdr_source_1.set_antenna('', 0)
        self.osmosdr_source_1.set_bandwidth(0, 0)

        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "rtl=0,direct_samp=2" )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(rx_freq - offset, 0)
        self.osmosdr_source_0.set_freq_corr(ppm, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(rx_gain, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1 * (offset), 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_2, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.osmosdr_source_1, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.sigmf_sink_0, 0))
        self.connect((self.rational_resampler_xxx_2, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.rational_resampler_xxx_2, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.rational_resampler_xxx_2, 0), (self.sigmf_sink_0_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rtlsdr_v3_dual_WWV_record_sigmf")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        self.set_fp_1("{:s}/{:s}".format(self.path, self.fn_1))
        self.set_fp_0("{:s}/{:s}".format(self.path, self.fn_0))

    def get_signal_type(self):
        return self.signal_type

    def set_signal_type(self, signal_type):
        self.signal_type = signal_type

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_fn_1("{:s}_{:s}_{:s}".format(signal_type.upper(), antenna_1.upper(),self.ts_str))
        self.set_fn_0("{:s}_{:s}_{:s}".format(signal_type.upper(), antenna_0.upper(),self.ts_str))

    def get_antenna_1(self):
        return self.antenna_1

    def set_antenna_1(self, antenna_1):
        self.antenna_1 = antenna_1

    def get_antenna_0(self):
        return self.antenna_0

    def set_antenna_0(self, antenna_0):
        self.antenna_0 = antenna_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_offset(self.samp_rate/4)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim_1 *self.interp_1)
        self.osmosdr_source_1.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_fn_1(self):
        return self.fn_1

    def set_fn_1(self, fn_1):
        self.fn_1 = fn_1
        self.set_fp_1("{:s}/{:s}".format(self.path, self.fn_1))

    def get_fn_0(self):
        return self.fn_0

    def set_fn_0(self, fn_0):
        self.fn_0 = fn_0
        self.set_fp_0("{:s}/{:s}".format(self.path, self.fn_0))

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))
        self.osmosdr_source_1.set_gain(self.rx_gain, 0)
        self.osmosdr_source_0.set_gain(self.rx_gain, 0)

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim_1 *self.interp_1)
        self.osmosdr_source_1.set_center_freq(self.rx_freq-self.offset, 0)
        self.osmosdr_source_0.set_center_freq(self.rx_freq - self.offset, 0)

    def get_ppm(self):
        return self.ppm

    def set_ppm(self, ppm):
        self.ppm = ppm
        Qt.QMetaObject.invokeMethod(self._ppm_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ppm)))
        self.osmosdr_source_1.set_freq_corr(self.ppm, 0)
        self.osmosdr_source_0.set_freq_corr(self.ppm, 0)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self.osmosdr_source_1.set_center_freq(self.rx_freq-self.offset, 0)
        self.osmosdr_source_0.set_center_freq(self.rx_freq - self.offset, 0)
        self.analog_sig_source_x_0.set_frequency(-1 * (self.offset))

    def get_noise_cal(self):
        return self.noise_cal

    def set_noise_cal(self, noise_cal):
        self.noise_cal = noise_cal

    def get_interp_1(self):
        return self.interp_1

    def set_interp_1(self, interp_1):
        self.interp_1 = interp_1
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim_1 *self.interp_1)

    def get_fp_1(self):
        return self.fp_1

    def set_fp_1(self, fp_1):
        self.fp_1 = fp_1

    def get_fp_0(self):
        return self.fp_0

    def set_fp_0(self, fp_0):
        self.fp_0 = fp_0

    def get_decim_1(self):
        return self.decim_1

    def set_decim_1(self, decim_1):
        self.decim_1 = decim_1
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate/self.decim_1*self.interp_1)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim_1 *self.interp_1)


def argument_parser():
    description = 'Analyze power, doppler, polarization of WWV emissions'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "", "--path", dest="path", type="string", default="/captures/wwv",
        help="Set path [default=%default]")
    parser.add_option(
        "", "--signal-type", dest="signal_type", type="string", default='WWV',
        help="Set signal_type [default=%default]")
    return parser


def main(top_block_cls=rtlsdr_v3_dual_WWV_record_sigmf, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(path=options.path, signal_type=options.signal_type)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
