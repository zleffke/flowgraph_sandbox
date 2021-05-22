#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Uhd Hf Ssb
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
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import fosphor
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import math
import sip
import sys
import time
from gnuradio import qtgui


class uhd_hf_ssb(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Uhd Hf Ssb")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Uhd Hf Ssb")
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

        self.settings = Qt.QSettings("GNU Radio", "uhd_hf_ssb")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2.5e6
        self.rx_freq = rx_freq = 3.9e6
        self.fine_freq = fine_freq = 0
        self.coarse_freq = coarse_freq = 0
        self.volume = volume = 1
        self.usb_lsb = usb_lsb = -1
        self.lpf_cutoff = lpf_cutoff = 1.4e3
        self.interp = interp = 48
        self.freq_label = freq_label = rx_freq+fine_freq+coarse_freq
        self.decim = decim = samp_rate/1e3
        self.decay_rate = decay_rate = 100e-6
        self.audio_ref = audio_ref = 1
        self.audio_max_gain = audio_max_gain = 1
        self.audio_gain = audio_gain = 1
        self.audio_decay = audio_decay = 100
        self.audio_attack = audio_attack = 1000

        ##################################################
        # Blocks
        ##################################################
        self._volume_range = Range(0, 100, .1, 1, 200)
        self._volume_win = RangeWidget(self._volume_range, self.set_volume, "volume", "counter_slider", float)
        self.top_grid_layout.addWidget(self._volume_win, 7, 0, 1, 4)
        for r in range(7, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._usb_lsb_options = (-1, 1, )
        self._usb_lsb_labels = ('USB', 'LSB', )
        self._usb_lsb_group_box = Qt.QGroupBox("usb_lsb")
        self._usb_lsb_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._usb_lsb_button_group = variable_chooser_button_group()
        self._usb_lsb_group_box.setLayout(self._usb_lsb_box)
        for i, label in enumerate(self._usb_lsb_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._usb_lsb_box.addWidget(radio_button)
        	self._usb_lsb_button_group.addButton(radio_button, i)
        self._usb_lsb_callback = lambda i: Qt.QMetaObject.invokeMethod(self._usb_lsb_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._usb_lsb_options.index(i)))
        self._usb_lsb_callback(self.usb_lsb)
        self._usb_lsb_button_group.buttonClicked[int].connect(
        	lambda i: self.set_usb_lsb(self._usb_lsb_options[i]))
        self.top_grid_layout.addWidget(self._usb_lsb_group_box, 5, 5, 1, 1)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_freq_range = Range(1e6, 100e6, 100e3, 3.9e6, 200)
        self._rx_freq_win = RangeWidget(self._rx_freq_range, self.set_rx_freq, "rx_freq", "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_freq_win, 4, 0, 1, 4)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._lpf_cutoff_tool_bar = Qt.QToolBar(self)
        self._lpf_cutoff_tool_bar.addWidget(Qt.QLabel("lpf_cutoff"+": "))
        self._lpf_cutoff_line_edit = Qt.QLineEdit(str(self.lpf_cutoff))
        self._lpf_cutoff_tool_bar.addWidget(self._lpf_cutoff_line_edit)
        self._lpf_cutoff_line_edit.returnPressed.connect(
        	lambda: self.set_lpf_cutoff(eng_notation.str_to_num(str(self._lpf_cutoff_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._lpf_cutoff_tool_bar, 4, 5, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._fine_freq_range = Range(-1e3, 1e3, 1, 0, 200)
        self._fine_freq_win = RangeWidget(self._fine_freq_range, self.set_fine_freq, "fine_freq", "counter_slider", float)
        self.top_grid_layout.addWidget(self._fine_freq_win, 6, 0, 1, 4)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._decay_rate_options = (100e-6, 65e-3, 20e-3, )
        self._decay_rate_labels = ('Fast', 'Medium', 'Slow', )
        self._decay_rate_group_box = Qt.QGroupBox("decay_rate")
        self._decay_rate_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._decay_rate_button_group = variable_chooser_button_group()
        self._decay_rate_group_box.setLayout(self._decay_rate_box)
        for i, label in enumerate(self._decay_rate_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._decay_rate_box.addWidget(radio_button)
        	self._decay_rate_button_group.addButton(radio_button, i)
        self._decay_rate_callback = lambda i: Qt.QMetaObject.invokeMethod(self._decay_rate_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._decay_rate_options.index(i)))
        self._decay_rate_callback(self.decay_rate)
        self._decay_rate_button_group.buttonClicked[int].connect(
        	lambda i: self.set_decay_rate(self._decay_rate_options[i]))
        self.top_grid_layout.addWidget(self._decay_rate_group_box, 4, 6, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 7):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._coarse_freq_range = Range(-100e3, 100e3, 1, 0, 200)
        self._coarse_freq_win = RangeWidget(self._coarse_freq_range, self.set_coarse_freq, "coarse_freq", "counter_slider", float)
        self.top_grid_layout.addWidget(self._coarse_freq_win, 5, 0, 1, 4)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._audio_ref_tool_bar = Qt.QToolBar(self)
        self._audio_ref_tool_bar.addWidget(Qt.QLabel("audio_ref"+": "))
        self._audio_ref_line_edit = Qt.QLineEdit(str(self.audio_ref))
        self._audio_ref_tool_bar.addWidget(self._audio_ref_line_edit)
        self._audio_ref_line_edit.returnPressed.connect(
        	lambda: self.set_audio_ref(eng_notation.str_to_num(str(self._audio_ref_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._audio_ref_tool_bar, 9, 3, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._audio_max_gain_tool_bar = Qt.QToolBar(self)
        self._audio_max_gain_tool_bar.addWidget(Qt.QLabel("audio_max_gain"+": "))
        self._audio_max_gain_line_edit = Qt.QLineEdit(str(self.audio_max_gain))
        self._audio_max_gain_tool_bar.addWidget(self._audio_max_gain_line_edit)
        self._audio_max_gain_line_edit.returnPressed.connect(
        	lambda: self.set_audio_max_gain(eng_notation.str_to_num(str(self._audio_max_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._audio_max_gain_tool_bar, 9, 5, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(5, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._audio_gain_tool_bar = Qt.QToolBar(self)
        self._audio_gain_tool_bar.addWidget(Qt.QLabel("audio_gain"+": "))
        self._audio_gain_line_edit = Qt.QLineEdit(str(self.audio_gain))
        self._audio_gain_tool_bar.addWidget(self._audio_gain_line_edit)
        self._audio_gain_line_edit.returnPressed.connect(
        	lambda: self.set_audio_gain(eng_notation.str_to_num(str(self._audio_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._audio_gain_tool_bar, 9, 4, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._audio_decay_tool_bar = Qt.QToolBar(self)
        self._audio_decay_tool_bar.addWidget(Qt.QLabel("audio_decay"+": "))
        self._audio_decay_line_edit = Qt.QLineEdit(str(self.audio_decay))
        self._audio_decay_tool_bar.addWidget(self._audio_decay_line_edit)
        self._audio_decay_line_edit.returnPressed.connect(
        	lambda: self.set_audio_decay(eng_notation.str_to_num(str(self._audio_decay_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._audio_decay_tool_bar, 9, 2, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._audio_attack_tool_bar = Qt.QToolBar(self)
        self._audio_attack_tool_bar.addWidget(Qt.QLabel("audio_attack"+": "))
        self._audio_attack_line_edit = Qt.QLineEdit(str(self.audio_attack))
        self._audio_attack_tool_bar.addWidget(self._audio_attack_line_edit)
        self._audio_attack_line_edit.returnPressed.connect(
        	lambda: self.set_audio_attack(eng_notation.str_to_num(str(self._audio_attack_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._audio_attack_tool_bar, 9, 1, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_1 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_1.set_clock_source('gpsdo', 0)
        self.uhd_usrp_source_1.set_time_source('gpsdo', 0)
        self.uhd_usrp_source_1.set_subdev_spec('A:AB', 0)
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(rx_freq), 0)
        self.uhd_usrp_source_1.set_gain(0, 0)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 0)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=200,
                decimation=int(samp_rate/1e3),
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=interp,
                decimation=int(decim),
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate/decim*interp/3/4, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 100)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 6, 6, 3, 2)
        for r in range(6, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate/decim*interp/3, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 8, 0, 1, 4)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.010)
        self.qtgui_number_sink_0.set_title('')

        labels = ["RSSI", '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("blue", "red"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, 50)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 5, 6, 1, 1)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(6, 7):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim * interp/3, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.0010)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['', 'processed', '', '', '',
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_0_win, 6, 4, 3, 2)
        for r in range(6, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim * interp, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-120, -10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['pre-d', 'processed', '', '', '',
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.low_pass_filter_0_1 = filter.interp_fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate/decim*interp/3, 1.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(3, firdes.low_pass(
        	1, samp_rate/decim*interp, lpf_cutoff, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate/decim*interp/3, 1.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self._freq_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._freq_label_formatter = None
        else:
          self._freq_label_formatter = lambda x: eng_notation.num_to_str(x)

        self._freq_label_tool_bar.addWidget(Qt.QLabel('Tuned Freq'+": "))
        self._freq_label_label = Qt.QLabel(str(self._freq_label_formatter(self.freq_label)))
        self._freq_label_tool_bar.addWidget(self._freq_label_label)
        self.top_grid_layout.addWidget(self._freq_label_tool_bar, 5, 4, 1, 1)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0.set_frequency_range(rx_freq, samp_rate/int(samp_rate/1e3)*200)
        self._fosphor_qt_sink_c_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._fosphor_qt_sink_c_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_glfw_sink_c_0 = fosphor.glfw_sink_c()
        self.fosphor_glfw_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_glfw_sink_c_0.set_frequency_range(rx_freq, samp_rate)
        self.blocks_multiply_xx_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_vff((100000, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((usb_lsb, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(1000, 1/1000.0, 4000, 1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_sink_0 = audio.sink(16000, '', True)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate/decim*interp/3, analog.GR_SIN_WAVE, 1.5e3, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate/decim*interp/3, analog.GR_COS_WAVE, 1.5e3, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1 * (fine_freq+coarse_freq), 1, 0)
        self.analog_agc2_xx_0_0 = analog.agc2_ff(audio_attack, audio_decay, audio_ref, audio_gain)
        self.analog_agc2_xx_0_0.set_max_gain(audio_max_gain)
        self.analog_agc2_xx_0 = analog.agc2_cc(0.1, decay_rate, .3, 1000)
        self.analog_agc2_xx_0.set_max_gain(65000)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.fosphor_glfw_sink_c_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.analog_agc2_xx_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_1_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.analog_agc2_xx_0_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.low_pass_filter_0_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_1_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.blocks_multiply_xx_1_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.fosphor_qt_sink_c_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.analog_agc2_xx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "uhd_hf_ssb")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_decim(self.samp_rate/1e3)
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate/self.decim*self.interp/3/4)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate/self.decim*self.interp/3)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim * self.interp/3)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim * self.interp)
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate/self.decim*self.interp/3, 1.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim*self.interp, self.lpf_cutoff, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim*self.interp/3, 1.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rx_freq, self.samp_rate/int(self.samp_rate/1e3)*200)
        self.fosphor_glfw_sink_c_0.set_frequency_range(self.rx_freq, self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate/self.decim*self.interp/3)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate/self.decim*self.interp/3)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq), 0)
        self.set_freq_label(self._freq_label_formatter(self.rx_freq+self.fine_freq+self.coarse_freq))
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rx_freq, self.samp_rate/int(self.samp_rate/1e3)*200)
        self.fosphor_glfw_sink_c_0.set_frequency_range(self.rx_freq, self.samp_rate)

    def get_fine_freq(self):
        return self.fine_freq

    def set_fine_freq(self, fine_freq):
        self.fine_freq = fine_freq
        self.set_freq_label(self._freq_label_formatter(self.rx_freq+self.fine_freq+self.coarse_freq))
        self.analog_sig_source_x_0.set_frequency(-1 * (self.fine_freq+self.coarse_freq))

    def get_coarse_freq(self):
        return self.coarse_freq

    def set_coarse_freq(self, coarse_freq):
        self.coarse_freq = coarse_freq
        self.set_freq_label(self._freq_label_formatter(self.rx_freq+self.fine_freq+self.coarse_freq))
        self.analog_sig_source_x_0.set_frequency(-1 * (self.fine_freq+self.coarse_freq))

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k((self.volume, ))

    def get_usb_lsb(self):
        return self.usb_lsb

    def set_usb_lsb(self, usb_lsb):
        self.usb_lsb = usb_lsb
        self._usb_lsb_callback(self.usb_lsb)
        self.blocks_multiply_const_vxx_1.set_k((self.usb_lsb, ))

    def get_lpf_cutoff(self):
        return self.lpf_cutoff

    def set_lpf_cutoff(self, lpf_cutoff):
        self.lpf_cutoff = lpf_cutoff
        Qt.QMetaObject.invokeMethod(self._lpf_cutoff_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.lpf_cutoff)))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim*self.interp, self.lpf_cutoff, 100, firdes.WIN_HAMMING, 6.76))

    def get_interp(self):
        return self.interp

    def set_interp(self, interp):
        self.interp = interp
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate/self.decim*self.interp/3/4)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate/self.decim*self.interp/3)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim * self.interp/3)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim * self.interp)
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate/self.decim*self.interp/3, 1.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim*self.interp, self.lpf_cutoff, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim*self.interp/3, 1.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate/self.decim*self.interp/3)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate/self.decim*self.interp/3)

    def get_freq_label(self):
        return self.freq_label

    def set_freq_label(self, freq_label):
        self.freq_label = freq_label
        Qt.QMetaObject.invokeMethod(self._freq_label_label, "setText", Qt.Q_ARG("QString", self.freq_label))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate/self.decim*self.interp/3/4)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate/self.decim*self.interp/3)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate/self.decim * self.interp/3)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim * self.interp)
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate/self.decim*self.interp/3, 1.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim*self.interp, self.lpf_cutoff, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim*self.interp/3, 1.5e3, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate/self.decim*self.interp/3)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate/self.decim*self.interp/3)

    def get_decay_rate(self):
        return self.decay_rate

    def set_decay_rate(self, decay_rate):
        self.decay_rate = decay_rate
        self._decay_rate_callback(self.decay_rate)
        self.analog_agc2_xx_0.set_decay_rate(self.decay_rate)

    def get_audio_ref(self):
        return self.audio_ref

    def set_audio_ref(self, audio_ref):
        self.audio_ref = audio_ref
        Qt.QMetaObject.invokeMethod(self._audio_ref_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.audio_ref)))
        self.analog_agc2_xx_0_0.set_reference(self.audio_ref)

    def get_audio_max_gain(self):
        return self.audio_max_gain

    def set_audio_max_gain(self, audio_max_gain):
        self.audio_max_gain = audio_max_gain
        Qt.QMetaObject.invokeMethod(self._audio_max_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.audio_max_gain)))
        self.analog_agc2_xx_0_0.set_max_gain(self.audio_max_gain)

    def get_audio_gain(self):
        return self.audio_gain

    def set_audio_gain(self, audio_gain):
        self.audio_gain = audio_gain
        Qt.QMetaObject.invokeMethod(self._audio_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.audio_gain)))
        self.analog_agc2_xx_0_0.set_gain(self.audio_gain)

    def get_audio_decay(self):
        return self.audio_decay

    def set_audio_decay(self, audio_decay):
        self.audio_decay = audio_decay
        Qt.QMetaObject.invokeMethod(self._audio_decay_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.audio_decay)))
        self.analog_agc2_xx_0_0.set_decay_rate(self.audio_decay)

    def get_audio_attack(self):
        return self.audio_attack

    def set_audio_attack(self, audio_attack):
        self.audio_attack = audio_attack
        Qt.QMetaObject.invokeMethod(self._audio_attack_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.audio_attack)))
        self.analog_agc2_xx_0_0.set_attack_rate(self.audio_attack)


def main(top_block_cls=uhd_hf_ssb, options=None):

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
