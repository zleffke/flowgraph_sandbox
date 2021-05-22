#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Dual Polarization Phase Correlation, Start Time [UTC]: 2020-09-08T04:06:16.766349Z
# GNU Radio version: 3.8.2.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from datetime import datetime as dt; import string; import math; import numpy as np
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import uhd
import time

from gnuradio import qtgui

class x310_cpol_simple_hf(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Dual Polarization Phase Correlation, Start Time [UTC]: 2020-09-08T04:06:16.766349Z")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Dual Polarization Phase Correlation, Start Time [UTC]: 2020-09-08T04:06:16.766349Z")
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

        self.settings = Qt.QSettings("GNU Radio", "x310_cpol_simple_hf")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.rx_freq = rx_freq = 10e6
        self.offset_tune = offset_tune = -10000
        self.usrp_tune_freq = usrp_tune_freq = rx_freq+ offset_tune
        self.usrp_clk_rate = usrp_clk_rate = 200e6
        self.usrp_ddc_freq = usrp_ddc_freq = np.round(usrp_tune_freq/usrp_clk_rate* 2**32)/2**32*usrp_clk_rate
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.samp_rate = samp_rate = 250e3
        self.phase_shift_deg = phase_shift_deg = 90
        self.title_str = title_str = "Dual Polarization Phase Correlation, Start Time [UTC]: {:s}".format(ts_str)
        self.selection = selection = ((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))
        self.pol_select = pol_select = 0
        self.pll_lpf_cut = pll_lpf_cut = 10
        self.pll_lbw = pll_lbw = 100
        self.pll_freq = pll_freq = 100
        self.pll_avg = pll_avg = 100000
        self.phase_rad = phase_rad = phase_shift_deg *math.pi / 180.0
        self.lpf_cutoff = lpf_cutoff = samp_rate/2.0
        self.lpf2_cut = lpf2_cut = 1e3
        self.lo_freq = lo_freq = usrp_ddc_freq - offset_tune
        self.filter_taps = filter_taps = firdes.low_pass(1.0, 2.5,0.1,0.02,firdes.WIN_HAMMING)
        self.decim2 = decim2 = 5
        self.decim = decim = 10
        self.c_ms = c_ms = 299792458

        ##################################################
        # Blocks
        ##################################################
        self.main_tab = Qt.QTabWidget()
        self.main_tab_widget_0 = Qt.QWidget()
        self.main_tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_0)
        self.main_tab_grid_layout_0 = Qt.QGridLayout()
        self.main_tab_layout_0.addLayout(self.main_tab_grid_layout_0)
        self.main_tab.addTab(self.main_tab_widget_0, 'NS_EW')
        self.main_tab_widget_1 = Qt.QWidget()
        self.main_tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_1)
        self.main_tab_grid_layout_1 = Qt.QGridLayout()
        self.main_tab_layout_1.addLayout(self.main_tab_grid_layout_1)
        self.main_tab.addTab(self.main_tab_widget_1, 'RHCP_LHCP')
        self.main_tab_widget_2 = Qt.QWidget()
        self.main_tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_2)
        self.main_tab_grid_layout_2 = Qt.QGridLayout()
        self.main_tab_layout_2.addLayout(self.main_tab_grid_layout_2)
        self.main_tab.addTab(self.main_tab_widget_2, 'CPol_FFT')
        self.main_tab_widget_3 = Qt.QWidget()
        self.main_tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_3)
        self.main_tab_grid_layout_3 = Qt.QGridLayout()
        self.main_tab_layout_3.addLayout(self.main_tab_grid_layout_3)
        self.main_tab.addTab(self.main_tab_widget_3, 'CPol_Spectrogram')
        self.main_tab_widget_4 = Qt.QWidget()
        self.main_tab_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_4)
        self.main_tab_grid_layout_4 = Qt.QGridLayout()
        self.main_tab_layout_4.addLayout(self.main_tab_grid_layout_4)
        self.main_tab.addTab(self.main_tab_widget_4, 'PLL')
        self.main_tab_widget_5 = Qt.QWidget()
        self.main_tab_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_5)
        self.main_tab_grid_layout_5 = Qt.QGridLayout()
        self.main_tab_layout_5.addLayout(self.main_tab_grid_layout_5)
        self.main_tab.addTab(self.main_tab_widget_5, 'Phase Compare 2')
        self.top_grid_layout.addWidget(self.main_tab, 0, 0, 8, 8)
        for r in range(0, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel('SAMP_RATE' + ": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
            lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text()))))
        self.top_grid_layout.addWidget(self._samp_rate_tool_bar, 8, 0, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('FREQ' + ": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
            lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text()))))
        self.top_grid_layout.addWidget(self._rx_freq_tool_bar, 8, 1, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        # Create the options list
        self._pol_select_options = (0, 1, 2, 3, )
        # Create the labels list
        self._pol_select_labels = ('NS', 'EW', 'RHCP', 'LHCP', )
        # Create the combo box
        # Create the radio buttons
        self._pol_select_group_box = Qt.QGroupBox('Polarization Selection' + ": ")
        self._pol_select_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._pol_select_button_group = variable_chooser_button_group()
        self._pol_select_group_box.setLayout(self._pol_select_box)
        for i, _label in enumerate(self._pol_select_labels):
            radio_button = Qt.QRadioButton(_label)
            self._pol_select_box.addWidget(radio_button)
            self._pol_select_button_group.addButton(radio_button, i)
        self._pol_select_callback = lambda i: Qt.QMetaObject.invokeMethod(self._pol_select_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._pol_select_options.index(i)))
        self._pol_select_callback(self.pol_select)
        self._pol_select_button_group.buttonClicked[int].connect(
            lambda i: self.set_pol_select(self._pol_select_options[i]))
        self.main_tab_grid_layout_2.addWidget(self._pol_select_group_box, 8, 0, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self._pll_lpf_cut_tool_bar = Qt.QToolBar(self)
        self._pll_lpf_cut_tool_bar.addWidget(Qt.QLabel('pll_lpf_cut' + ": "))
        self._pll_lpf_cut_line_edit = Qt.QLineEdit(str(self.pll_lpf_cut))
        self._pll_lpf_cut_tool_bar.addWidget(self._pll_lpf_cut_line_edit)
        self._pll_lpf_cut_line_edit.returnPressed.connect(
            lambda: self.set_pll_lpf_cut(eng_notation.str_to_num(str(self._pll_lpf_cut_line_edit.text()))))
        self.main_tab_grid_layout_3.addWidget(self._pll_lpf_cut_tool_bar, 8, 3, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(3, 4):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self._pll_lbw_tool_bar = Qt.QToolBar(self)
        self._pll_lbw_tool_bar.addWidget(Qt.QLabel('pll_lbw' + ": "))
        self._pll_lbw_line_edit = Qt.QLineEdit(str(self.pll_lbw))
        self._pll_lbw_tool_bar.addWidget(self._pll_lbw_line_edit)
        self._pll_lbw_line_edit.returnPressed.connect(
            lambda: self.set_pll_lbw(eng_notation.str_to_num(str(self._pll_lbw_line_edit.text()))))
        self.main_tab_grid_layout_4.addWidget(self._pll_lbw_tool_bar, 4, 6, 1, 2)
        for r in range(4, 5):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(6, 8):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self._pll_freq_tool_bar = Qt.QToolBar(self)
        self._pll_freq_tool_bar.addWidget(Qt.QLabel('pll_freq' + ": "))
        self._pll_freq_line_edit = Qt.QLineEdit(str(self.pll_freq))
        self._pll_freq_tool_bar.addWidget(self._pll_freq_line_edit)
        self._pll_freq_line_edit.returnPressed.connect(
            lambda: self.set_pll_freq(eng_notation.str_to_num(str(self._pll_freq_line_edit.text()))))
        self.main_tab_grid_layout_4.addWidget(self._pll_freq_tool_bar, 4, 4, 1, 2)
        for r in range(4, 5):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(4, 6):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self._pll_avg_tool_bar = Qt.QToolBar(self)
        self._pll_avg_tool_bar.addWidget(Qt.QLabel('pll_avg' + ": "))
        self._pll_avg_line_edit = Qt.QLineEdit(str(self.pll_avg))
        self._pll_avg_tool_bar.addWidget(self._pll_avg_line_edit)
        self._pll_avg_line_edit.returnPressed.connect(
            lambda: self.set_pll_avg(eng_notation.str_to_num(str(self._pll_avg_line_edit.text()))))
        self.main_tab_grid_layout_4.addWidget(self._pll_avg_tool_bar, 5, 4, 1, 2)
        for r in range(5, 6):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(4, 6):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self._lpf_cutoff_tool_bar = Qt.QToolBar(self)
        self._lpf_cutoff_tool_bar.addWidget(Qt.QLabel('LPF Cutoff' + ": "))
        self._lpf_cutoff_line_edit = Qt.QLineEdit(str(self.lpf_cutoff))
        self._lpf_cutoff_tool_bar.addWidget(self._lpf_cutoff_line_edit)
        self._lpf_cutoff_line_edit.returnPressed.connect(
            lambda: self.set_lpf_cutoff(eng_notation.str_to_num(str(self._lpf_cutoff_line_edit.text()))))
        self.top_grid_layout.addWidget(self._lpf_cutoff_tool_bar, 8, 2, 1, 1)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._lpf2_cut_tool_bar = Qt.QToolBar(self)
        self._lpf2_cut_tool_bar.addWidget(Qt.QLabel('LPF Cutoff' + ": "))
        self._lpf2_cut_line_edit = Qt.QLineEdit(str(self.lpf2_cut))
        self._lpf2_cut_tool_bar.addWidget(self._lpf2_cut_line_edit)
        self._lpf2_cut_line_edit.returnPressed.connect(
            lambda: self.set_lpf2_cut(eng_notation.str_to_num(str(self._lpf2_cut_line_edit.text()))))
        self.main_tab_grid_layout_2.addWidget(self._lpf2_cut_tool_bar, 8, 2, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.uhd_usrp_source_1 = uhd.usrp_source(
            ",".join(("addr=192.168.10.2", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,2)),
            ),
        )
        self.uhd_usrp_source_1.set_subdev_spec('A:AB B:AB', 0)
        self.uhd_usrp_source_1.set_time_source('gpsdo', 0)
        self.uhd_usrp_source_1.set_clock_source('gpsdo', 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(usrp_tune_freq), 0)
        self.uhd_usrp_source_1.set_gain(0, 0)
        self.uhd_usrp_source_1.set_antenna('A', 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(usrp_tune_freq), 1)
        self.uhd_usrp_source_1.set_gain(0, 1)
        self.uhd_usrp_source_1.set_antenna('A', 1)
        self.uhd_usrp_source_1.set_clock_rate(200e6, uhd.ALL_MBOARDS)
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1.set_time_unknown_pps(uhd.time_spec())
        self.qtgui_waterfall_sink_x_0_2_0 = qtgui.waterfall_sink_c(
            2048, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            rx_freq, #fc
            samp_rate / decim / decim2, #bw
            '', #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_2_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_2_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_2_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_2_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_2_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_2_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_2_0.set_intensity_range(-160, -70)

        self._qtgui_waterfall_sink_x_0_2_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_2_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_waterfall_sink_x_0_2_0_win, 4, 0, 4, 4)
        for r in range(4, 8):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_1 = qtgui.waterfall_sink_c(
            2048, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            rx_freq, #fc
            samp_rate / decim, #bw
            "", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_1.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_1.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_1.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_1.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_1.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_1.set_intensity_range(-140, -80)

        self._qtgui_waterfall_sink_x_0_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_waterfall_sink_x_0_1_win, 4, 0, 4, 4)
        for r in range(4, 8):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_0_0 = qtgui.waterfall_sink_c(
            2048, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            rx_freq, #fc
            samp_rate / decim, #bw
            "", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0_0.set_intensity_range(-140, -80)

        self._qtgui_waterfall_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_waterfall_sink_x_0_0_0_win, 4, 4, 4, 4)
        for r in range(4, 8):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
            2048, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            rx_freq, #fc
            samp_rate / decim, #bw
            "", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-140, -80)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 4, 4, 4, 4)
        for r in range(4, 8):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            2048, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            rx_freq, #fc
            samp_rate / decim, #bw
            "", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, -80)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win, 4, 0, 4, 4)
        for r in range(4, 8):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate / decim / decim2, #samp_rate
            "", #name
            2 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_1.set_update_time(0.010)
        self.qtgui_time_sink_x_0_1_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1_1.set_y_label('PLL Freq Offset [Hz]', "")

        self.qtgui_time_sink_x_0_1_1.enable_tags(True)
        self.qtgui_time_sink_x_0_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1_1.enable_grid(True)
        self.qtgui_time_sink_x_0_1_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_1.enable_stem_plot(False)


        labels = ['NS', 'EW', 'Range Delta [km]', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_5.addWidget(self._qtgui_time_sink_x_0_1_1_win, 0, 4, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_5.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_5.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_0_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate / decim / decim2, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0_1_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1_0_0.set_y_label('Freq Delta [Hz]', "")

        self.qtgui_time_sink_x_0_1_0_0.enable_tags(True)
        self.qtgui_time_sink_x_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_0_0.enable_stem_plot(False)


        labels = ['NSEW', 'LHCP', 'Range Delta [km]', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_5.addWidget(self._qtgui_time_sink_x_0_1_0_0_win, 2, 4, 2, 4)
        for r in range(2, 4):
            self.main_tab_grid_layout_5.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_5.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate / decim / decim2, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1_0.set_y_label('Freq Delta [Hz]', "")

        self.qtgui_time_sink_x_0_1_0.enable_tags(True)
        self.qtgui_time_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1_0.enable_grid(True)
        self.qtgui_time_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_0.enable_stem_plot(False)


        labels = ['RHCP', 'LHCP', 'Range Delta [km]', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_time_sink_x_0_1_0_win, 2, 4, 2, 4)
        for r in range(2, 4):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate / decim / decim2, #samp_rate
            "", #name
            2 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.010)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1.set_y_label('PLL Freq Offset [Hz]', "")

        self.qtgui_time_sink_x_0_1.enable_tags(True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1.enable_grid(True)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(False)


        labels = ['RHCP', 'LHCP', 'Range Delta [km]', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
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
        self.main_tab_grid_layout_4.addWidget(self._qtgui_time_sink_x_0_1_win, 0, 4, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_1_1_1 = qtgui.histogram_sink_f(
            100,
            1000,
            -4,
            4,
            "Freq Offset [Hz]",
            1
        )

        self.qtgui_histogram_sink_x_1_1_1.set_update_time(0.010)
        self.qtgui_histogram_sink_x_1_1_1.enable_autoscale(True)
        self.qtgui_histogram_sink_x_1_1_1.enable_accumulate(True)
        self.qtgui_histogram_sink_x_1_1_1.enable_grid(False)
        self.qtgui_histogram_sink_x_1_1_1.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers= [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_1_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_1_1_1.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_1_1_1.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_1_1_1.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_1_1_1.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_1_1_1.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_1_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_1_1_1_win = sip.wrapinstance(self.qtgui_histogram_sink_x_1_1_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_5.addWidget(self._qtgui_histogram_sink_x_1_1_1_win, 2, 0, 2, 4)
        for r in range(2, 4):
            self.main_tab_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_5.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_1_1_0_0 = qtgui.histogram_sink_f(
            100,
            1000,
            -10,
            10,
            "Freq [Hz]",
            2
        )

        self.qtgui_histogram_sink_x_1_1_0_0.set_update_time(0.010)
        self.qtgui_histogram_sink_x_1_1_0_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_1_1_0_0.enable_accumulate(True)
        self.qtgui_histogram_sink_x_1_1_0_0.enable_grid(False)
        self.qtgui_histogram_sink_x_1_1_0_0.enable_axis_labels(True)


        labels = ['NS', 'EW', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers= [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_1_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_1_1_0_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_1_1_0_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_1_1_0_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_1_1_0_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_1_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_1_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_1_1_0_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_1_1_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_5.addWidget(self._qtgui_histogram_sink_x_1_1_0_0_win, 4, 0, 2, 4)
        for r in range(4, 6):
            self.main_tab_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_5.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_1_1_0 = qtgui.histogram_sink_f(
            100,
            1000,
            -10,
            10,
            "Freq [Hz]",
            4
        )

        self.qtgui_histogram_sink_x_1_1_0.set_update_time(0.010)
        self.qtgui_histogram_sink_x_1_1_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_1_1_0.enable_accumulate(True)
        self.qtgui_histogram_sink_x_1_1_0.enable_grid(False)
        self.qtgui_histogram_sink_x_1_1_0.enable_axis_labels(True)


        labels = ['R', 'L', 'NS', 'EW', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers= [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(4):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_1_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_1_1_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_1_1_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_1_1_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_1_1_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_1_1_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_1_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_1_1_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_1_1_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_histogram_sink_x_1_1_0_win, 4, 0, 2, 4)
        for r in range(4, 6):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_1_1 = qtgui.histogram_sink_f(
            100,
            1000,
            -4,
            4,
            "Freq Offset [Hz]",
            1
        )

        self.qtgui_histogram_sink_x_1_1.set_update_time(0.010)
        self.qtgui_histogram_sink_x_1_1.enable_autoscale(True)
        self.qtgui_histogram_sink_x_1_1.enable_accumulate(True)
        self.qtgui_histogram_sink_x_1_1.enable_grid(False)
        self.qtgui_histogram_sink_x_1_1.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers= [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_1_1.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_1_1.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_1_1.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_1_1.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_1_1.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_1_1_win = sip.wrapinstance(self.qtgui_histogram_sink_x_1_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_histogram_sink_x_1_1_win, 2, 0, 2, 4)
        for r in range(2, 4):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1_0_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate / decim / decim2, #bw
            "", #name
            2
        )
        self.qtgui_freq_sink_x_1_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_1_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_1_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0_0.enable_control_panel(False)



        labels = ['RHCP', 'LHCP', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_5.addWidget(self._qtgui_freq_sink_x_1_0_0_win, 0, 0, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_5.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate / decim / decim2, #bw
            "", #name
            2
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0.enable_grid(True)
        self.qtgui_freq_sink_x_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0.enable_control_panel(False)



        labels = ['RHCP', 'LHCP', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_freq_sink_x_1_0_win, 0, 0, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_2_0 = qtgui.freq_sink_c(
            2048, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            rx_freq*0, #fc
            samp_rate / decim / decim2, #bw
            '', #name
            1
        )
        self.qtgui_freq_sink_x_0_2_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_2_0.set_y_axis(-160, -70)
        self.qtgui_freq_sink_x_0_2_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_2_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_2_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_2_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_2_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_2_0.enable_control_panel(False)



        labels = ['', 'E/W', 'RHCP', 'LHCP', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_2_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_2_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_2_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_2_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_2_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_2_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_freq_sink_x_0_2_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_c(
            2048, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            rx_freq*0, #fc
            samp_rate / decim, #bw
            "RHCP", #name
            1
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_1.set_y_axis(-140, -80)
        self.qtgui_freq_sink_x_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1.enable_grid(True)
        self.qtgui_freq_sink_x_0_1.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(False)

        self.qtgui_freq_sink_x_0_1.disable_legend()


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_1_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0_0 = qtgui.freq_sink_c(
            2048, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            rx_freq*0, #fc
            samp_rate / decim, #bw
            "LHCP", #name
            1
        )
        self.qtgui_freq_sink_x_0_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0_0.set_y_axis(-140, -80)
        self.qtgui_freq_sink_x_0_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0_0.enable_control_panel(False)

        self.qtgui_freq_sink_x_0_0_0.disable_legend()


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_0_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
            2048, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            rx_freq*0, #fc
            samp_rate / decim, #bw
            "East/West", #name
            1
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, -80)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(True)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)

        self.qtgui_freq_sink_x_0_0.disable_legend()


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_0_win, 0, 4, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(4, 8):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            2048, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            rx_freq*0, #fc
            samp_rate / decim, #bw
            "North/South", #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, -80)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        self.qtgui_freq_sink_x_0.disable_legend()


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.low_pass_filter_0_2 = filter.fir_filter_ccf(
            decim,
            firdes.low_pass(
                1,
                samp_rate,
                lpf_cutoff,
                10e3,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_1_2 = filter.fir_filter_ccf(
            decim2,
            firdes.low_pass(
                1,
                samp_rate / decim,
                pll_lpf_cut,
                10,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_1_1_0 = filter.fir_filter_ccf(
            decim2,
            firdes.low_pass(
                1,
                samp_rate/decim,
                lpf2_cut,
                100,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_1_1 = filter.fir_filter_ccf(
            decim,
            firdes.low_pass(
                1,
                samp_rate,
                lpf_cutoff,
                1e3,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_1_0_0 = filter.fir_filter_ccf(
            decim2,
            firdes.low_pass(
                1,
                samp_rate / decim,
                pll_lpf_cut,
                10,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_1_0 = filter.fir_filter_ccf(
            decim2,
            firdes.low_pass(
                1,
                samp_rate / decim,
                pll_lpf_cut,
                10,
                firdes.WIN_HAMMING,
                6.76))
        self.low_pass_filter_0_1 = filter.fir_filter_ccf(
            decim2,
            firdes.low_pass(
                1,
                samp_rate / decim,
                pll_lpf_cut,
                10,
                firdes.WIN_HAMMING,
                6.76))
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(1, filter_taps, lo_freq - usrp_ddc_freq, samp_rate / decim)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, filter_taps, lo_freq - usrp_ddc_freq, samp_rate / decim)
        self.blocks_sub_xx_1_1_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_1_1 = blocks.sub_ff(1)
        self.blocks_multiply_matrix_xx_0 = blocks.multiply_matrix_cc((selection[pol_select],), gr.TPP_ALL_TO_ALL)
        self.blocks_multiply_const_vxx_1_1_0 = blocks.multiply_const_ff(samp_rate/decim/decim2/(2*math.pi))
        self.blocks_multiply_const_vxx_1_1 = blocks.multiply_const_ff(samp_rate/decim/decim2/(2*math.pi))
        self.blocks_multiply_const_vxx_1_0_1_0 = blocks.multiply_const_ff(samp_rate/decim/decim2/(2*math.pi))
        self.blocks_multiply_const_vxx_1_0_1 = blocks.multiply_const_ff(samp_rate/decim/decim2/(2*math.pi))
        self.blocks_multiply_const_vxx_1_0_0 = blocks.multiply_const_cc(complex(math.cos(phase_rad),math.sin(phase_rad)))
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_cc(complex(math.cos(phase_rad),math.sin(phase_rad)))
        self.blocks_moving_average_xx_1_0 = blocks.moving_average_ff(int(pll_avg), 1.0/pll_avg, 4000, 1)
        self.blocks_moving_average_xx_1 = blocks.moving_average_ff(int(pll_avg), 1.0/pll_avg, 4000, 1)
        self.blocks_moving_average_xx_0_0_0_0 = blocks.moving_average_ff(int(pll_avg), 1.0/pll_avg, 4000, 1)
        self.blocks_moving_average_xx_0_0_0 = blocks.moving_average_ff(int(pll_avg), 1.0/pll_avg, 4000, 1)
        self.blocks_add_xx_0_0 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_pll_freqdet_cf_0_1 = analog.pll_freqdet_cf(math.pi/pll_lbw, math.pi/pll_freq, -math.pi/pll_freq)
        self.analog_pll_freqdet_cf_0_0_0 = analog.pll_freqdet_cf(math.pi/pll_lbw, math.pi/pll_freq, -math.pi/pll_freq)
        self.analog_pll_freqdet_cf_0_0 = analog.pll_freqdet_cf(math.pi/pll_lbw, math.pi/pll_freq, -math.pi/pll_freq)
        self.analog_pll_freqdet_cf_0 = analog.pll_freqdet_cf(math.pi/pll_lbw, math.pi/pll_freq, -math.pi/pll_freq)
        self.analog_agc2_xx_1 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_1.set_max_gain(65536)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_multiply_matrix_xx_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.low_pass_filter_0_1_2, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.analog_agc2_xx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_agc2_xx_1, 0), (self.blocks_multiply_const_vxx_1_0_0, 0))
        self.connect((self.analog_agc2_xx_1, 0), (self.blocks_multiply_matrix_xx_0, 1))
        self.connect((self.analog_agc2_xx_1, 0), (self.low_pass_filter_0_1_0_0, 0))
        self.connect((self.analog_agc2_xx_1, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.analog_agc2_xx_1, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.analog_pll_freqdet_cf_0, 0), (self.blocks_moving_average_xx_0_0_0, 0))
        self.connect((self.analog_pll_freqdet_cf_0_0, 0), (self.blocks_moving_average_xx_1, 0))
        self.connect((self.analog_pll_freqdet_cf_0_0_0, 0), (self.blocks_moving_average_xx_1_0, 0))
        self.connect((self.analog_pll_freqdet_cf_0_1, 0), (self.blocks_moving_average_xx_0_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_matrix_xx_0, 2))
        self.connect((self.blocks_add_xx_0, 0), (self.low_pass_filter_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_freq_sink_x_0_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_waterfall_sink_x_0_1, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_multiply_matrix_xx_0, 3))
        self.connect((self.blocks_add_xx_0_0, 0), (self.low_pass_filter_0_1_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_freq_sink_x_0_0_0, 0))
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_waterfall_sink_x_0_0_0, 0))
        self.connect((self.blocks_moving_average_xx_0_0_0, 0), (self.blocks_multiply_const_vxx_1_1, 0))
        self.connect((self.blocks_moving_average_xx_0_0_0_0, 0), (self.blocks_multiply_const_vxx_1_1_0, 0))
        self.connect((self.blocks_moving_average_xx_1, 0), (self.blocks_multiply_const_vxx_1_0_1, 0))
        self.connect((self.blocks_moving_average_xx_1_0, 0), (self.blocks_multiply_const_vxx_1_0_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_1, 0), (self.blocks_sub_xx_1_1, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_1, 0), (self.qtgui_histogram_sink_x_1_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0_1, 0), (self.qtgui_time_sink_x_0_1, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_1_0, 0), (self.blocks_sub_xx_1_1_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_1_0, 0), (self.qtgui_histogram_sink_x_1_1_0, 3))
        self.connect((self.blocks_multiply_const_vxx_1_0_1_0, 0), (self.qtgui_histogram_sink_x_1_1_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0_1_0, 0), (self.qtgui_time_sink_x_0_1_1, 1))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.blocks_sub_xx_1_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.qtgui_histogram_sink_x_1_1_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_1, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1_1_0, 0), (self.blocks_sub_xx_1_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_1_0, 0), (self.qtgui_histogram_sink_x_1_1_0, 2))
        self.connect((self.blocks_multiply_const_vxx_1_1_0, 0), (self.qtgui_histogram_sink_x_1_1_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_1_0, 0), (self.qtgui_time_sink_x_0_1_1, 0))
        self.connect((self.blocks_multiply_matrix_xx_0, 0), (self.low_pass_filter_0_1_1_0, 0))
        self.connect((self.blocks_sub_xx_1_1, 0), (self.qtgui_histogram_sink_x_1_1, 0))
        self.connect((self.blocks_sub_xx_1_1, 0), (self.qtgui_time_sink_x_0_1_0, 0))
        self.connect((self.blocks_sub_xx_1_1_0, 0), (self.qtgui_histogram_sink_x_1_1_1, 0))
        self.connect((self.blocks_sub_xx_1_1_0, 0), (self.qtgui_time_sink_x_0_1_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.analog_agc2_xx_1, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.analog_pll_freqdet_cf_0, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.qtgui_freq_sink_x_1_0, 0))
        self.connect((self.low_pass_filter_0_1_0, 0), (self.analog_pll_freqdet_cf_0_0, 0))
        self.connect((self.low_pass_filter_0_1_0, 0), (self.qtgui_freq_sink_x_1_0, 1))
        self.connect((self.low_pass_filter_0_1_0_0, 0), (self.analog_pll_freqdet_cf_0_0_0, 0))
        self.connect((self.low_pass_filter_0_1_0_0, 0), (self.qtgui_freq_sink_x_1_0_0, 1))
        self.connect((self.low_pass_filter_0_1_1, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))
        self.connect((self.low_pass_filter_0_1_1_0, 0), (self.qtgui_freq_sink_x_0_2_0, 0))
        self.connect((self.low_pass_filter_0_1_1_0, 0), (self.qtgui_waterfall_sink_x_0_2_0, 0))
        self.connect((self.low_pass_filter_0_1_2, 0), (self.analog_pll_freqdet_cf_0_1, 0))
        self.connect((self.low_pass_filter_0_1_2, 0), (self.qtgui_freq_sink_x_1_0_0, 0))
        self.connect((self.low_pass_filter_0_2, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.uhd_usrp_source_1, 1), (self.low_pass_filter_0_1_1, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.low_pass_filter_0_2, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "x310_cpol_simple_hf")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))
        self.set_usrp_tune_freq(self.rx_freq+ self.offset_tune)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_2_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim / self.decim2)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_2_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim / self.decim2)

    def get_offset_tune(self):
        return self.offset_tune

    def set_offset_tune(self, offset_tune):
        self.offset_tune = offset_tune
        self.set_lo_freq(self.usrp_ddc_freq - self.offset_tune)
        self.set_usrp_tune_freq(self.rx_freq+ self.offset_tune)

    def get_usrp_tune_freq(self):
        return self.usrp_tune_freq

    def set_usrp_tune_freq(self, usrp_tune_freq):
        self.usrp_tune_freq = usrp_tune_freq
        self.set_usrp_ddc_freq(np.round(self.usrp_tune_freq/self.usrp_clk_rate* 2**32)/2**32*self.usrp_clk_rate)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.usrp_tune_freq), 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.usrp_tune_freq), 1)

    def get_usrp_clk_rate(self):
        return self.usrp_clk_rate

    def set_usrp_clk_rate(self, usrp_clk_rate):
        self.usrp_clk_rate = usrp_clk_rate
        self.set_usrp_ddc_freq(np.round(self.usrp_tune_freq/self.usrp_clk_rate* 2**32)/2**32*self.usrp_clk_rate)

    def get_usrp_ddc_freq(self):
        return self.usrp_ddc_freq

    def set_usrp_ddc_freq(self, usrp_ddc_freq):
        self.usrp_ddc_freq = usrp_ddc_freq
        self.set_lo_freq(self.usrp_ddc_freq - self.offset_tune)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.lo_freq - self.usrp_ddc_freq)
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.lo_freq - self.usrp_ddc_freq)

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_title_str("Dual Polarization Phase Correlation, Start Time [UTC]: {:s}".format(self.ts_str))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_lpf_cutoff(self.samp_rate/2.0)
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.blocks_multiply_const_vxx_1_0_1.set_k(self.samp_rate/self.decim/self.decim2/(2*math.pi))
        self.blocks_multiply_const_vxx_1_0_1_0.set_k(self.samp_rate/self.decim/self.decim2/(2*math.pi))
        self.blocks_multiply_const_vxx_1_1.set_k(self.samp_rate/self.decim/self.decim2/(2*math.pi))
        self.blocks_multiply_const_vxx_1_1_0.set_k(self.samp_rate/self.decim/self.decim2/(2*math.pi))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 10, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 10, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 10, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_1.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_1_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.lpf2_cut, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 10, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_2.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cutoff, 10e3, firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_2_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim / self.decim2)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim / self.decim2)
        self.qtgui_freq_sink_x_1_0_0.set_frequency_range(0, self.samp_rate / self.decim / self.decim2)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate / self.decim / self.decim2)
        self.qtgui_time_sink_x_0_1_0.set_samp_rate(self.samp_rate / self.decim / self.decim2)
        self.qtgui_time_sink_x_0_1_0_0.set_samp_rate(self.samp_rate / self.decim / self.decim2)
        self.qtgui_time_sink_x_0_1_1.set_samp_rate(self.samp_rate / self.decim / self.decim2)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_2_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim / self.decim2)
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)

    def get_phase_shift_deg(self):
        return self.phase_shift_deg

    def set_phase_shift_deg(self, phase_shift_deg):
        self.phase_shift_deg = phase_shift_deg
        self.set_phase_rad(self.phase_shift_deg *math.pi / 180.0)

    def get_title_str(self):
        return self.title_str

    def set_title_str(self, title_str):
        self.title_str = title_str

    def get_selection(self):
        return self.selection

    def set_selection(self, selection):
        self.selection = selection
        self.blocks_multiply_matrix_xx_0.set_A((self.selection[self.pol_select],))

    def get_pol_select(self):
        return self.pol_select

    def set_pol_select(self, pol_select):
        self.pol_select = pol_select
        self._pol_select_callback(self.pol_select)
        self.blocks_multiply_matrix_xx_0.set_A((self.selection[self.pol_select],))

    def get_pll_lpf_cut(self):
        return self.pll_lpf_cut

    def set_pll_lpf_cut(self, pll_lpf_cut):
        self.pll_lpf_cut = pll_lpf_cut
        Qt.QMetaObject.invokeMethod(self._pll_lpf_cut_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.pll_lpf_cut)))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 10, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 10, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 10, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 10, firdes.WIN_HAMMING, 6.76))

    def get_pll_lbw(self):
        return self.pll_lbw

    def set_pll_lbw(self, pll_lbw):
        self.pll_lbw = pll_lbw
        Qt.QMetaObject.invokeMethod(self._pll_lbw_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.pll_lbw)))
        self.analog_pll_freqdet_cf_0.set_loop_bandwidth(math.pi/self.pll_lbw)
        self.analog_pll_freqdet_cf_0_0.set_loop_bandwidth(math.pi/self.pll_lbw)
        self.analog_pll_freqdet_cf_0_0_0.set_loop_bandwidth(math.pi/self.pll_lbw)
        self.analog_pll_freqdet_cf_0_1.set_loop_bandwidth(math.pi/self.pll_lbw)

    def get_pll_freq(self):
        return self.pll_freq

    def set_pll_freq(self, pll_freq):
        self.pll_freq = pll_freq
        Qt.QMetaObject.invokeMethod(self._pll_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.pll_freq)))
        self.analog_pll_freqdet_cf_0.set_max_freq(math.pi/self.pll_freq)
        self.analog_pll_freqdet_cf_0.set_min_freq(-math.pi/self.pll_freq)
        self.analog_pll_freqdet_cf_0_0.set_max_freq(math.pi/self.pll_freq)
        self.analog_pll_freqdet_cf_0_0.set_min_freq(-math.pi/self.pll_freq)
        self.analog_pll_freqdet_cf_0_0_0.set_max_freq(math.pi/self.pll_freq)
        self.analog_pll_freqdet_cf_0_0_0.set_min_freq(-math.pi/self.pll_freq)
        self.analog_pll_freqdet_cf_0_1.set_max_freq(math.pi/self.pll_freq)
        self.analog_pll_freqdet_cf_0_1.set_min_freq(-math.pi/self.pll_freq)

    def get_pll_avg(self):
        return self.pll_avg

    def set_pll_avg(self, pll_avg):
        self.pll_avg = pll_avg
        Qt.QMetaObject.invokeMethod(self._pll_avg_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.pll_avg)))
        self.blocks_moving_average_xx_0_0_0.set_length_and_scale(int(self.pll_avg), 1.0/self.pll_avg)
        self.blocks_moving_average_xx_0_0_0_0.set_length_and_scale(int(self.pll_avg), 1.0/self.pll_avg)
        self.blocks_moving_average_xx_1.set_length_and_scale(int(self.pll_avg), 1.0/self.pll_avg)
        self.blocks_moving_average_xx_1_0.set_length_and_scale(int(self.pll_avg), 1.0/self.pll_avg)

    def get_phase_rad(self):
        return self.phase_rad

    def set_phase_rad(self, phase_rad):
        self.phase_rad = phase_rad
        self.blocks_multiply_const_vxx_1_0.set_k(complex(math.cos(self.phase_rad),math.sin(self.phase_rad)))
        self.blocks_multiply_const_vxx_1_0_0.set_k(complex(math.cos(self.phase_rad),math.sin(self.phase_rad)))

    def get_lpf_cutoff(self):
        return self.lpf_cutoff

    def set_lpf_cutoff(self, lpf_cutoff):
        self.lpf_cutoff = lpf_cutoff
        Qt.QMetaObject.invokeMethod(self._lpf_cutoff_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.lpf_cutoff)))
        self.low_pass_filter_0_1_1.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cutoff, 1e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_2.set_taps(firdes.low_pass(1, self.samp_rate, self.lpf_cutoff, 10e3, firdes.WIN_HAMMING, 6.76))

    def get_lpf2_cut(self):
        return self.lpf2_cut

    def set_lpf2_cut(self, lpf2_cut):
        self.lpf2_cut = lpf2_cut
        Qt.QMetaObject.invokeMethod(self._lpf2_cut_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.lpf2_cut)))
        self.low_pass_filter_0_1_1_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.lpf2_cut, 100, firdes.WIN_HAMMING, 6.76))

    def get_lo_freq(self):
        return self.lo_freq

    def set_lo_freq(self, lo_freq):
        self.lo_freq = lo_freq
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.lo_freq - self.usrp_ddc_freq)
        self.freq_xlating_fir_filter_xxx_0_0.set_center_freq(self.lo_freq - self.usrp_ddc_freq)

    def get_filter_taps(self):
        return self.filter_taps

    def set_filter_taps(self, filter_taps):
        self.filter_taps = filter_taps
        self.freq_xlating_fir_filter_xxx_0.set_taps(self.filter_taps)
        self.freq_xlating_fir_filter_xxx_0_0.set_taps(self.filter_taps)

    def get_decim2(self):
        return self.decim2

    def set_decim2(self, decim2):
        self.decim2 = decim2
        self.blocks_multiply_const_vxx_1_0_1.set_k(self.samp_rate/self.decim/self.decim2/(2*math.pi))
        self.blocks_multiply_const_vxx_1_0_1_0.set_k(self.samp_rate/self.decim/self.decim2/(2*math.pi))
        self.blocks_multiply_const_vxx_1_1.set_k(self.samp_rate/self.decim/self.decim2/(2*math.pi))
        self.blocks_multiply_const_vxx_1_1_0.set_k(self.samp_rate/self.decim/self.decim2/(2*math.pi))
        self.qtgui_freq_sink_x_0_2_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim / self.decim2)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim / self.decim2)
        self.qtgui_freq_sink_x_1_0_0.set_frequency_range(0, self.samp_rate / self.decim / self.decim2)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate / self.decim / self.decim2)
        self.qtgui_time_sink_x_0_1_0.set_samp_rate(self.samp_rate / self.decim / self.decim2)
        self.qtgui_time_sink_x_0_1_0_0.set_samp_rate(self.samp_rate / self.decim / self.decim2)
        self.qtgui_time_sink_x_0_1_1.set_samp_rate(self.samp_rate / self.decim / self.decim2)
        self.qtgui_waterfall_sink_x_0_2_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim / self.decim2)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.blocks_multiply_const_vxx_1_0_1.set_k(self.samp_rate/self.decim/self.decim2/(2*math.pi))
        self.blocks_multiply_const_vxx_1_0_1_0.set_k(self.samp_rate/self.decim/self.decim2/(2*math.pi))
        self.blocks_multiply_const_vxx_1_1.set_k(self.samp_rate/self.decim/self.decim2/(2*math.pi))
        self.blocks_multiply_const_vxx_1_1_0.set_k(self.samp_rate/self.decim/self.decim2/(2*math.pi))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 10, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 10, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_0_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 10, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_1_0.set_taps(firdes.low_pass(1, self.samp_rate/self.decim, self.lpf2_cut, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2.set_taps(firdes.low_pass(1, self.samp_rate / self.decim, self.pll_lpf_cut, 10, firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_0_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim)
        self.qtgui_freq_sink_x_0_2_0.set_frequency_range(self.rx_freq*0, self.samp_rate / self.decim / self.decim2)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim / self.decim2)
        self.qtgui_freq_sink_x_1_0_0.set_frequency_range(0, self.samp_rate / self.decim / self.decim2)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate / self.decim / self.decim2)
        self.qtgui_time_sink_x_0_1_0.set_samp_rate(self.samp_rate / self.decim / self.decim2)
        self.qtgui_time_sink_x_0_1_0_0.set_samp_rate(self.samp_rate / self.decim / self.decim2)
        self.qtgui_time_sink_x_0_1_1.set_samp_rate(self.samp_rate / self.decim / self.decim2)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_1.set_frequency_range(self.rx_freq, self.samp_rate / self.decim)
        self.qtgui_waterfall_sink_x_0_2_0.set_frequency_range(self.rx_freq, self.samp_rate / self.decim / self.decim2)

    def get_c_ms(self):
        return self.c_ms

    def set_c_ms(self, c_ms):
        self.c_ms = c_ms





def main(top_block_cls=x310_cpol_simple_hf, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
