#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Kerberos Sigmf Playback4
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
import adsb
import gr_sigmf
import math
import pyqt
import sip
import sys
import threading
import time
from gnuradio import qtgui


class kerberos_sigmf_playback4(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Kerberos Sigmf Playback4")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Kerberos Sigmf Playback4")
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

        self.settings = Qt.QSettings("GNU Radio", "kerberos_sigmf_playback4")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.function_probe_0_3 = function_probe_0_3 = 0
        self.function_probe_0_2 = function_probe_0_2 = 0
        self.function_probe_0_1 = function_probe_0_1 = 0
        self.trig_delay = trig_delay = 0.001
        self.trig_channel = trig_channel = 0
        self.throttle = throttle = 10
        self.thresh_phase = thresh_phase = 10
        self.thresh_comp = thresh_comp = 10
        self.thresh = thresh = 50
        self.samp_rate = samp_rate = 2e6
        self.samp_offset_0_3 = samp_offset_0_3 = function_probe_0_3
        self.samp_offset_0_2 = samp_offset_0_2 = function_probe_0_2
        self.samp_offset_0_1 = samp_offset_0_1 = function_probe_0_1
        self.nfft = nfft = 8192
        self.manual_fine_delay_3 = manual_fine_delay_3 = 0
        self.manual_fine_delay_2 = manual_fine_delay_2 = 0
        self.manual_fine_delay_1 = manual_fine_delay_1 = 0
        self.manual_fine_delay_0 = manual_fine_delay_0 = 0
        self.delay_3 = delay_3 = 1788
        self.delay_2 = delay_2 = 5261
        self.delay_1 = delay_1 = 734
        self.delay_0 = delay_0 = 0
        self.corr_alpha_0_3 = corr_alpha_0_3 = 0.01
        self.corr_alpha_0_2 = corr_alpha_0_2 = 0.01
        self.corr_alpha_0_1 = corr_alpha_0_1 = 0.01

        ##################################################
        # Blocks
        ##################################################
        self.probe_offset_0_3 = blocks.probe_signal_f()
        self.probe_offset_0_2 = blocks.probe_signal_f()
        self.probe_offset_0_1 = blocks.probe_signal_f()
        self.main_tab = Qt.QTabWidget()
        self.main_tab_widget_0 = Qt.QWidget()
        self.main_tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_0)
        self.main_tab_grid_layout_0 = Qt.QGridLayout()
        self.main_tab_layout_0.addLayout(self.main_tab_grid_layout_0)
        self.main_tab.addTab(self.main_tab_widget_0, 'Channel')
        self.main_tab_widget_1 = Qt.QWidget()
        self.main_tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_1)
        self.main_tab_grid_layout_1 = Qt.QGridLayout()
        self.main_tab_layout_1.addLayout(self.main_tab_grid_layout_1)
        self.main_tab.addTab(self.main_tab_widget_1, 'Coarse Adjust')
        self.main_tab_widget_2 = Qt.QWidget()
        self.main_tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_2)
        self.main_tab_grid_layout_2 = Qt.QGridLayout()
        self.main_tab_layout_2.addLayout(self.main_tab_grid_layout_2)
        self.main_tab.addTab(self.main_tab_widget_2, 'Correlate')
        self.main_tab_widget_3 = Qt.QWidget()
        self.main_tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_3)
        self.main_tab_grid_layout_3 = Qt.QGridLayout()
        self.main_tab_layout_3.addLayout(self.main_tab_grid_layout_3)
        self.main_tab.addTab(self.main_tab_widget_3, 'Single Decode')
        self.main_tab_widget_4 = Qt.QWidget()
        self.main_tab_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_4)
        self.main_tab_grid_layout_4 = Qt.QGridLayout()
        self.main_tab_layout_4.addLayout(self.main_tab_grid_layout_4)
        self.main_tab.addTab(self.main_tab_widget_4, 'Sum and Decode')
        self.main_tab_widget_5 = Qt.QWidget()
        self.main_tab_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.main_tab_widget_5)
        self.main_tab_grid_layout_5 = Qt.QGridLayout()
        self.main_tab_layout_5.addLayout(self.main_tab_grid_layout_5)
        self.main_tab.addTab(self.main_tab_widget_5, 'Phase Analysis')
        self.top_grid_layout.addWidget(self.main_tab, 0, 0, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._trig_delay_tool_bar = Qt.QToolBar(self)
        self._trig_delay_tool_bar.addWidget(Qt.QLabel("trig_delay"+": "))
        self._trig_delay_line_edit = Qt.QLineEdit(str(self.trig_delay))
        self._trig_delay_tool_bar.addWidget(self._trig_delay_line_edit)
        self._trig_delay_line_edit.returnPressed.connect(
        	lambda: self.set_trig_delay(eng_notation.str_to_num(str(self._trig_delay_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_1.addWidget(self._trig_delay_tool_bar, 2, 1, 1, 1)
        for r in range(2, 3):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self._trig_channel_options = (0, 1, 2, 3, )
        self._trig_channel_labels = ('chan0', 'chan1', 'chan2', 'chan3', )
        self._trig_channel_tool_bar = Qt.QToolBar(self)
        self._trig_channel_tool_bar.addWidget(Qt.QLabel("trig_channel"+": "))
        self._trig_channel_combo_box = Qt.QComboBox()
        self._trig_channel_tool_bar.addWidget(self._trig_channel_combo_box)
        for label in self._trig_channel_labels: self._trig_channel_combo_box.addItem(label)
        self._trig_channel_callback = lambda i: Qt.QMetaObject.invokeMethod(self._trig_channel_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._trig_channel_options.index(i)))
        self._trig_channel_callback(self.trig_channel)
        self._trig_channel_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_trig_channel(self._trig_channel_options[i]))
        self.main_tab_grid_layout_1.addWidget(self._trig_channel_tool_bar, 2, 0, 1, 1)
        for r in range(2, 3):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self._throttle_tool_bar = Qt.QToolBar(self)
        self._throttle_tool_bar.addWidget(Qt.QLabel('Throttle'+": "))
        self._throttle_line_edit = Qt.QLineEdit(str(self.throttle))
        self._throttle_tool_bar.addWidget(self._throttle_line_edit)
        self._throttle_line_edit.returnPressed.connect(
        	lambda: self.set_throttle(eng_notation.str_to_num(str(self._throttle_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._throttle_tool_bar, 9, 1, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._thresh_phase_tool_bar = Qt.QToolBar(self)
        self._thresh_phase_tool_bar.addWidget(Qt.QLabel('Complex Threshold'+": "))
        self._thresh_phase_line_edit = Qt.QLineEdit(str(self.thresh_phase))
        self._thresh_phase_tool_bar.addWidget(self._thresh_phase_line_edit)
        self._thresh_phase_line_edit.returnPressed.connect(
        	lambda: self.set_thresh_phase(eng_notation.str_to_num(str(self._thresh_phase_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_5.addWidget(self._thresh_phase_tool_bar, 5, 0, 1, 1)
        for r in range(5, 6):
            self.main_tab_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_5.setColumnStretch(c, 1)
        self._thresh_comp_tool_bar = Qt.QToolBar(self)
        self._thresh_comp_tool_bar.addWidget(Qt.QLabel('Complex Threshold'+": "))
        self._thresh_comp_line_edit = Qt.QLineEdit(str(self.thresh_comp))
        self._thresh_comp_tool_bar.addWidget(self._thresh_comp_line_edit)
        self._thresh_comp_line_edit.returnPressed.connect(
        	lambda: self.set_thresh_comp(eng_notation.str_to_num(str(self._thresh_comp_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_4.addWidget(self._thresh_comp_tool_bar, 8, 0, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self._thresh_tool_bar = Qt.QToolBar(self)
        self._thresh_tool_bar.addWidget(Qt.QLabel('GUI Threshold'+": "))
        self._thresh_line_edit = Qt.QLineEdit(str(self.thresh))
        self._thresh_tool_bar.addWidget(self._thresh_line_edit)
        self._thresh_line_edit.returnPressed.connect(
        	lambda: self.set_thresh(eng_notation.str_to_num(str(self._thresh_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._thresh_tool_bar, 9, 0, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._manual_fine_delay_3_tool_bar = Qt.QToolBar(self)
        self._manual_fine_delay_3_tool_bar.addWidget(Qt.QLabel("manual_fine_delay_3"+": "))
        self._manual_fine_delay_3_line_edit = Qt.QLineEdit(str(self.manual_fine_delay_3))
        self._manual_fine_delay_3_tool_bar.addWidget(self._manual_fine_delay_3_line_edit)
        self._manual_fine_delay_3_line_edit.returnPressed.connect(
        	lambda: self.set_manual_fine_delay_3(int(str(self._manual_fine_delay_3_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_4.addWidget(self._manual_fine_delay_3_tool_bar, 8, 1, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self._manual_fine_delay_2_tool_bar = Qt.QToolBar(self)
        self._manual_fine_delay_2_tool_bar.addWidget(Qt.QLabel("manual_fine_delay_2"+": "))
        self._manual_fine_delay_2_line_edit = Qt.QLineEdit(str(self.manual_fine_delay_2))
        self._manual_fine_delay_2_tool_bar.addWidget(self._manual_fine_delay_2_line_edit)
        self._manual_fine_delay_2_line_edit.returnPressed.connect(
        	lambda: self.set_manual_fine_delay_2(int(str(self._manual_fine_delay_2_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_4.addWidget(self._manual_fine_delay_2_tool_bar, 7, 1, 1, 1)
        for r in range(7, 8):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self._manual_fine_delay_1_tool_bar = Qt.QToolBar(self)
        self._manual_fine_delay_1_tool_bar.addWidget(Qt.QLabel("manual_fine_delay_1"+": "))
        self._manual_fine_delay_1_line_edit = Qt.QLineEdit(str(self.manual_fine_delay_1))
        self._manual_fine_delay_1_tool_bar.addWidget(self._manual_fine_delay_1_line_edit)
        self._manual_fine_delay_1_line_edit.returnPressed.connect(
        	lambda: self.set_manual_fine_delay_1(int(str(self._manual_fine_delay_1_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_4.addWidget(self._manual_fine_delay_1_tool_bar, 6, 1, 1, 1)
        for r in range(6, 7):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self._manual_fine_delay_0_tool_bar = Qt.QToolBar(self)
        self._manual_fine_delay_0_tool_bar.addWidget(Qt.QLabel("manual_fine_delay_0"+": "))
        self._manual_fine_delay_0_line_edit = Qt.QLineEdit(str(self.manual_fine_delay_0))
        self._manual_fine_delay_0_tool_bar.addWidget(self._manual_fine_delay_0_line_edit)
        self._manual_fine_delay_0_line_edit.returnPressed.connect(
        	lambda: self.set_manual_fine_delay_0(int(str(self._manual_fine_delay_0_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_4.addWidget(self._manual_fine_delay_0_tool_bar, 5, 1, 1, 1)
        for r in range(5, 6):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)

        def _function_probe_0_3_probe():
            while True:
                val = self.probe_offset_0_3.level()
                try:
                    self.set_function_probe_0_3(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (100))
        _function_probe_0_3_thread = threading.Thread(target=_function_probe_0_3_probe)
        _function_probe_0_3_thread.daemon = True
        _function_probe_0_3_thread.start()


        def _function_probe_0_2_probe():
            while True:
                val = self.probe_offset_0_2.level()
                try:
                    self.set_function_probe_0_2(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (100))
        _function_probe_0_2_thread = threading.Thread(target=_function_probe_0_2_probe)
        _function_probe_0_2_thread.daemon = True
        _function_probe_0_2_thread.start()


        def _function_probe_0_1_probe():
            while True:
                val = self.probe_offset_0_1.level()
                try:
                    self.set_function_probe_0_1(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (100))
        _function_probe_0_1_thread = threading.Thread(target=_function_probe_0_1_probe)
        _function_probe_0_1_thread.daemon = True
        _function_probe_0_1_thread.start()

        self._delay_3_tool_bar = Qt.QToolBar(self)
        self._delay_3_tool_bar.addWidget(Qt.QLabel("delay_3"+": "))
        self._delay_3_line_edit = Qt.QLineEdit(str(self.delay_3))
        self._delay_3_tool_bar.addWidget(self._delay_3_line_edit)
        self._delay_3_line_edit.returnPressed.connect(
        	lambda: self.set_delay_3(int(str(self._delay_3_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_1.addWidget(self._delay_3_tool_bar, 1, 3, 1, 1)
        for r in range(1, 2):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(3, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self._delay_2_tool_bar = Qt.QToolBar(self)
        self._delay_2_tool_bar.addWidget(Qt.QLabel("delay_2"+": "))
        self._delay_2_line_edit = Qt.QLineEdit(str(self.delay_2))
        self._delay_2_tool_bar.addWidget(self._delay_2_line_edit)
        self._delay_2_line_edit.returnPressed.connect(
        	lambda: self.set_delay_2(int(str(self._delay_2_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_1.addWidget(self._delay_2_tool_bar, 1, 2, 1, 1)
        for r in range(1, 2):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(2, 3):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self._delay_1_tool_bar = Qt.QToolBar(self)
        self._delay_1_tool_bar.addWidget(Qt.QLabel("delay_1"+": "))
        self._delay_1_line_edit = Qt.QLineEdit(str(self.delay_1))
        self._delay_1_tool_bar.addWidget(self._delay_1_line_edit)
        self._delay_1_line_edit.returnPressed.connect(
        	lambda: self.set_delay_1(int(str(self._delay_1_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_1.addWidget(self._delay_1_tool_bar, 1, 1, 1, 1)
        for r in range(1, 2):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self._delay_0_tool_bar = Qt.QToolBar(self)
        self._delay_0_tool_bar.addWidget(Qt.QLabel("delay_0"+": "))
        self._delay_0_line_edit = Qt.QLineEdit(str(self.delay_0))
        self._delay_0_tool_bar.addWidget(self._delay_0_line_edit)
        self._delay_0_line_edit.returnPressed.connect(
        	lambda: self.set_delay_0(int(str(self._delay_0_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_1.addWidget(self._delay_0_tool_bar, 1, 0, 1, 1)
        for r in range(1, 2):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self._corr_alpha_0_3_tool_bar = Qt.QToolBar(self)
        self._corr_alpha_0_3_tool_bar.addWidget(Qt.QLabel("corr_alpha_0_3"+": "))
        self._corr_alpha_0_3_line_edit = Qt.QLineEdit(str(self.corr_alpha_0_3))
        self._corr_alpha_0_3_tool_bar.addWidget(self._corr_alpha_0_3_line_edit)
        self._corr_alpha_0_3_line_edit.returnPressed.connect(
        	lambda: self.set_corr_alpha_0_3(eng_notation.str_to_num(str(self._corr_alpha_0_3_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_2.addWidget(self._corr_alpha_0_3_tool_bar, 8, 2, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self._corr_alpha_0_2_tool_bar = Qt.QToolBar(self)
        self._corr_alpha_0_2_tool_bar.addWidget(Qt.QLabel("corr_alpha_0_2"+": "))
        self._corr_alpha_0_2_line_edit = Qt.QLineEdit(str(self.corr_alpha_0_2))
        self._corr_alpha_0_2_tool_bar.addWidget(self._corr_alpha_0_2_line_edit)
        self._corr_alpha_0_2_line_edit.returnPressed.connect(
        	lambda: self.set_corr_alpha_0_2(eng_notation.str_to_num(str(self._corr_alpha_0_2_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_2.addWidget(self._corr_alpha_0_2_tool_bar, 8, 1, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self._corr_alpha_0_1_tool_bar = Qt.QToolBar(self)
        self._corr_alpha_0_1_tool_bar.addWidget(Qt.QLabel("corr_alpha_0_1"+": "))
        self._corr_alpha_0_1_line_edit = Qt.QLineEdit(str(self.corr_alpha_0_1))
        self._corr_alpha_0_1_tool_bar.addWidget(self._corr_alpha_0_1_line_edit)
        self._corr_alpha_0_1_line_edit.returnPressed.connect(
        	lambda: self.set_corr_alpha_0_1(eng_notation.str_to_num(str(self._corr_alpha_0_1_line_edit.text().toAscii()))))
        self.main_tab_grid_layout_2.addWidget(self._corr_alpha_0_1_tool_bar, 8, 0, 1, 1)
        for r in range(8, 9):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.single_pole_iir_filter_xx_0_0_0 = filter.single_pole_iir_filter_ff(corr_alpha_0_3, nfft)
        self.single_pole_iir_filter_xx_0_0 = filter.single_pole_iir_filter_ff(corr_alpha_0_2, nfft)
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(corr_alpha_0_1, nfft)
        self.sigmf_source_3 = gr_sigmf.source('/home/zleffke/captures/kerberos/20210330/2200/CHAN3_2021-03-30T22:00:02Z.sigmf-data', "cf32" + ("_le" if sys.byteorder == "little" else "_be"), True)
        self.sigmf_source_2 = gr_sigmf.source('/home/zleffke/captures/kerberos/20210330/2200/CHAN2_2021-03-30T22:00:02Z.sigmf-data', "cf32" + ("_le" if sys.byteorder == "little" else "_be"), True)
        self.sigmf_source_1 = gr_sigmf.source('/home/zleffke/captures/kerberos/20210330/2200/CHAN1_2021-03-30T22:00:02Z.sigmf-data', "cf32" + ("_le" if sys.byteorder == "little" else "_be"), True)
        self.sigmf_source_0 = gr_sigmf.source('/home/zleffke/captures/kerberos/20210330/2200/CHAN0_2021-03-30T22:00:02Z.sigmf-data', "cf32" + ("_le" if sys.byteorder == "little" else "_be"), True)
        self._samp_offset_0_3_tool_bar = Qt.QToolBar(self)

        if None:
          self._samp_offset_0_3_formatter = None
        else:
          self._samp_offset_0_3_formatter = lambda x: eng_notation.num_to_str(x)

        self._samp_offset_0_3_tool_bar.addWidget(Qt.QLabel("samp_offset_0_3"+": "))
        self._samp_offset_0_3_label = Qt.QLabel(str(self._samp_offset_0_3_formatter(self.samp_offset_0_3)))
        self._samp_offset_0_3_tool_bar.addWidget(self._samp_offset_0_3_label)
        self.main_tab_grid_layout_4.addWidget(self._samp_offset_0_3_tool_bar, 7, 0, 1, 1)
        for r in range(7, 8):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self._samp_offset_0_2_tool_bar = Qt.QToolBar(self)

        if None:
          self._samp_offset_0_2_formatter = None
        else:
          self._samp_offset_0_2_formatter = lambda x: eng_notation.num_to_str(x)

        self._samp_offset_0_2_tool_bar.addWidget(Qt.QLabel("samp_offset_0_2"+": "))
        self._samp_offset_0_2_label = Qt.QLabel(str(self._samp_offset_0_2_formatter(self.samp_offset_0_2)))
        self._samp_offset_0_2_tool_bar.addWidget(self._samp_offset_0_2_label)
        self.main_tab_grid_layout_4.addWidget(self._samp_offset_0_2_tool_bar, 6, 0, 1, 1)
        for r in range(6, 7):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self._samp_offset_0_1_tool_bar = Qt.QToolBar(self)

        if None:
          self._samp_offset_0_1_formatter = None
        else:
          self._samp_offset_0_1_formatter = lambda x: eng_notation.num_to_str(x)

        self._samp_offset_0_1_tool_bar.addWidget(Qt.QLabel("samp_offset_0_1"+": "))
        self._samp_offset_0_1_label = Qt.QLabel(str(self._samp_offset_0_1_formatter(self.samp_offset_0_1)))
        self._samp_offset_0_1_tool_bar.addWidget(self._samp_offset_0_1_label)
        self.main_tab_grid_layout_4.addWidget(self._samp_offset_0_1_tool_bar, 5, 0, 1, 1)
        for r in range(5, 6):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_0_1 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0_1.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_0_1.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0_1.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0_1.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0_1.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0_1.set_intensity_range(-100, 10)

        self._qtgui_waterfall_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_0_1_win, 2, 3, 2, 1)
        for r in range(2, 4):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(3, 4):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_0_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0_0.set_update_time(0.010)
        self.qtgui_waterfall_sink_x_0_0_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_0_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0_0_0.set_intensity_range(-100, 10)

        self._qtgui_waterfall_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_0_0_win, 2, 2, 2, 1)
        for r in range(2, 4):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 3):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	1024, #size
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

        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-100, 10)

        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_0_win, 2, 1, 2, 1)
        for r in range(2, 4):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	1024, #size
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

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-100, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win, 2, 0, 2, 1)
        for r in range(2, 4):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            nfft,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "Correlation",
            3 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0.enable_grid(True)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ['0 to 1', '0 to 2', '0 to 3', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_2.addWidget(self._qtgui_vector_sink_f_0_win, 0, 0, 4, 3)
        for r in range(0, 4):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 3):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
        	512, #size
        	samp_rate, #samp_rate
        	"Phase Delta", #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2.set_y_label('Phase', "deg")

        self.qtgui_time_sink_x_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, thresh_phase, 0.00005, 3, "")
        self.qtgui_time_sink_x_2.enable_autoscale(True)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_2.disable_legend()

        labels = ['0 to 1', '0 to 2', '0 to 3', '', '',
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

        for i in xrange(4):
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
        self.main_tab_grid_layout_5.addWidget(self._qtgui_time_sink_x_2_win, 2, 0, 2, 4)
        for r in range(2, 4):
            self.main_tab_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_5.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	128, #size
        	samp_rate / nfft, #samp_rate
        	"Correlation Magnitude", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(True)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

        labels = ['0 to 1', '0 to 2', '0 to 3', '', '',
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
        self.main_tab_grid_layout_2.addWidget(self._qtgui_time_sink_x_1_win, 4, 0, 4, 3)
        for r in range(4, 8):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 3):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_1_1 = qtgui.time_sink_f(
        	512, #size
        	samp_rate, #samp_rate
        	"Absolute Phase", #name
        	5 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_1_1.set_update_time(0.010)
        self.qtgui_time_sink_x_0_1_1_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1_1_1.set_y_label('Phase', "deg")

        self.qtgui_time_sink_x_0_1_1_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_1_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, thresh_phase, 0.00005, 4, "")
        self.qtgui_time_sink_x_0_1_1_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1_1_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1_1_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_1_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_1_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1_1_1.disable_legend()

        labels = ['Chan0', 'Chan1', 'Chan2', 'Chan3', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, 0, 0, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(5):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_1_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_1_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_1_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_1_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_1_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_1_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_1_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_5.addWidget(self._qtgui_time_sink_x_0_1_1_1_win, 0, 0, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_5.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_5.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_1_0 = qtgui.time_sink_c(
        	512, #size
        	samp_rate, #samp_rate
        	"", #name
        	5 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_1_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0_1_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_1_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, thresh_comp, 0.0001, trig_channel, "")
        self.qtgui_time_sink_x_0_1_1_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_1_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1_1_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "blue", "red", "red", "green",
                  "green", "black", "black", "cyan", "cyan"]
        styles = [1, 2, 1, 2, 1,
                  2, 1, 2, 1, 2]
        markers = [0, -1, 0, -1, 0,
                   -1, 0, -1, 0, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(10):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_1_1_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1_1_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_1_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_time_sink_x_0_1_1_0_win, 2, 0, 2, 4)
        for r in range(2, 4):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_1 = qtgui.time_sink_f(
        	512, #size
        	samp_rate, #samp_rate
        	"", #name
        	5 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_1.set_update_time(0.010)
        self.qtgui_time_sink_x_0_1_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, thresh, 0.0001, trig_channel, "")
        self.qtgui_time_sink_x_0_1_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1_1.disable_legend()

        labels = ['Chan0', 'Chan1', 'Chan2', 'Chan3', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, 0, 0, 0, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(5):
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
        self.main_tab_grid_layout_4.addWidget(self._qtgui_time_sink_x_0_1_1_win, 0, 0, 2, 4)
        for r in range(0, 2):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0 = qtgui.time_sink_f(
        	int(samp_rate*150e-6), #size
        	int(samp_rate), #samp_rate
        	"Combined", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_y_axis(0, 1)

        self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_0_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0, 1.25e-6, 0, "burst")
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_1_0_0_0_0_0.disable_legend()

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
                self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_4.addWidget(self._qtgui_time_sink_x_0_1_0_0_0_0_0_win, 0, 4, 4, 2)
        for r in range(0, 4):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(4, 6):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_0_0_0_0 = qtgui.time_sink_f(
        	int(samp_rate*150e-6), #size
        	int(samp_rate), #samp_rate
        	"CHAN3", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0_0_0_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0_1_0_0_0_0.set_y_axis(0, 1)

        self.qtgui_time_sink_x_0_1_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0, 1.25e-6, 0, "burst")
        self.qtgui_time_sink_x_0_1_0_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1_0_0_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_1_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_0_0_0_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_1_0_0_0_0.disable_legend()

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
                self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_1_0_0_0_0_win, 0, 3, 1, 1)
        for r in range(0, 1):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(3, 4):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_0_0_0 = qtgui.time_sink_f(
        	int(samp_rate*150e-6), #size
        	int(samp_rate), #samp_rate
        	"CHAN2", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0_0_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0_1_0_0_0.set_y_axis(0, 1)

        self.qtgui_time_sink_x_0_1_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0, 1.25e-6, 0, "burst")
        self.qtgui_time_sink_x_0_1_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1_0_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_1_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_0_0_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_1_0_0_0.disable_legend()

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
                self.qtgui_time_sink_x_0_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_1_0_0_0_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(2, 3):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_0_0 = qtgui.time_sink_f(
        	int(samp_rate*150e-6), #size
        	int(samp_rate), #samp_rate
        	"CHAN1", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0_1_0_0.set_y_axis(0, 1)

        self.qtgui_time_sink_x_0_1_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0, 1.25e-6, 0, "burst")
        self.qtgui_time_sink_x_0_1_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_0_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_1_0_0.disable_legend()

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
                self.qtgui_time_sink_x_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_1_0_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1_0 = qtgui.time_sink_f(
        	int(samp_rate*150e-6), #size
        	int(samp_rate), #samp_rate
        	"CHAN0", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0_1_0.set_y_axis(0, 1)

        self.qtgui_time_sink_x_0_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 0, 1.25e-6, 0, "burst")
        self.qtgui_time_sink_x_0_1_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1_0.enable_grid(True)
        self.qtgui_time_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1_0.enable_stem_plot(False)

        if not False:
          self.qtgui_time_sink_x_0_1_0.disable_legend()

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
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_3.addWidget(self._qtgui_time_sink_x_0_1_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	8192, #size
        	samp_rate, #samp_rate
        	"", #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.010)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, thresh, trig_delay, trig_channel, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()

        labels = ['Chan0', 'Chan1', 'Chan2', 'Chan3', '',
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

        for i in xrange(4):
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
        self.main_tab_grid_layout_1.addWidget(self._qtgui_time_sink_x_0_1_win, 0, 0, 1, 4)
        for r in range(0, 1):
            self.main_tab_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 4):
            self.main_tab_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1.set_update_time(0.010)
        self.qtgui_time_sink_x_0_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, thresh, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_1.disable_legend()

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
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_1_win, 4, 3, 2, 1)
        for r in range(4, 6):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(3, 4):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, thresh, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()

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
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_0_win, 4, 2, 2, 1)
        for r in range(4, 6):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 3):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, thresh, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
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
        self.main_tab_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_0_win, 4, 1, 2, 1)
        for r in range(4, 6):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, thresh, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
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
        self.main_tab_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_win, 4, 0, 2, 1)
        for r in range(4, 6):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_NONE,
            3
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("samp_offset")

        labels = ['0 to 1', '0 to 2', '0 to 3', '', '',
                  '', '', '', '', '']
        units = ['samples', 'samples', 'samples', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(3):
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
        self.main_tab_grid_layout_2.addWidget(self._qtgui_number_sink_0_win, 9, 0, 1, 3)
        for r in range(9, 10):
            self.main_tab_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 3):
            self.main_tab_grid_layout_2.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_1_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1_0.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0_1_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1_0.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_1_0_win, 0, 3, 2, 1)
        for r in range(0, 2):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(3, 4):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_1.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_1.enable_grid(False)
        self.qtgui_freq_sink_x_0_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_1.enable_control_panel(False)

        if not False:
          self.qtgui_freq_sink_x_0_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_1.set_plot_pos_half(not True)

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
                self.qtgui_freq_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.main_tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_1_win, 0, 2, 2, 1)
        for r in range(0, 2):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(2, 3):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
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
        self.main_tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_0_win, 0, 1, 2, 1)
        for r in range(0, 2):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
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
        self.main_tab_grid_layout_0.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 2, 1)
        for r in range(0, 2):
            self.main_tab_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_0.setColumnStretch(c, 1)
        self.pyqt_meta_text_output_0_0_0_0_0 = pyqt.meta_text_output()
        self._pyqt_meta_text_output_0_0_0_0_0_win = self.pyqt_meta_text_output_0_0_0_0_0;
        self.main_tab_grid_layout_4.addWidget(self._pyqt_meta_text_output_0_0_0_0_0_win, 4, 4, 4, 2)
        for r in range(4, 8):
            self.main_tab_grid_layout_4.setRowStretch(r, 1)
        for c in range(4, 6):
            self.main_tab_grid_layout_4.setColumnStretch(c, 1)

        self.pyqt_meta_text_output_0_0_0_0 = pyqt.meta_text_output()
        self._pyqt_meta_text_output_0_0_0_0_win = self.pyqt_meta_text_output_0_0_0_0;
        self.main_tab_grid_layout_3.addWidget(self._pyqt_meta_text_output_0_0_0_0_win, 1, 3, 1, 1)
        for r in range(1, 2):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(3, 4):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)

        self.pyqt_meta_text_output_0_0_0 = pyqt.meta_text_output()
        self._pyqt_meta_text_output_0_0_0_win = self.pyqt_meta_text_output_0_0_0;
        self.main_tab_grid_layout_3.addWidget(self._pyqt_meta_text_output_0_0_0_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(2, 3):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)

        self.pyqt_meta_text_output_0_0 = pyqt.meta_text_output()
        self._pyqt_meta_text_output_0_0_win = self.pyqt_meta_text_output_0_0;
        self.main_tab_grid_layout_3.addWidget(self._pyqt_meta_text_output_0_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(1, 2):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)

        self.pyqt_meta_text_output_0 = pyqt.meta_text_output()
        self._pyqt_meta_text_output_0_win = self.pyqt_meta_text_output_0;
        self.main_tab_grid_layout_3.addWidget(self._pyqt_meta_text_output_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.main_tab_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.main_tab_grid_layout_3.setColumnStretch(c, 1)

        self.fft_vxx_1_0_0 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 1)
        self.fft_vxx_1_0 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 1)
        self.fft_vxx_1 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 1)
        self.fft_vxx_0_1_0 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 1)
        self.fft_vxx_0_1 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 1)
        self.fft_vxx_0_0_0_0 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 1)
        self.fft_vxx_0_0_0 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 1)
        self.fft_vxx_0_0 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 1)
        self.fft_vxx_0 = fft.fft_vcc(nfft, True, (window.blackmanharris(nfft)), True, 1)
        self.blocks_throttle_3 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate / throttle,True)
        self.blocks_throttle_2 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate / throttle,True)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate /throttle,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate / throttle,True)
        self.blocks_sub_xx_0_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0_0 = blocks.sub_ff(1)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_stream_to_vector_0_1_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_stream_to_vector_0_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, nfft)
        self.blocks_skiphead_3 = blocks.skiphead(gr.sizeof_gr_complex*1, 0)
        self.blocks_skiphead_2 = blocks.skiphead(gr.sizeof_gr_complex*1, 0)
        self.blocks_skiphead_1 = blocks.skiphead(gr.sizeof_gr_complex*1, 0)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_gr_complex*1, 0)
        self.blocks_short_to_float_0_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0_0 = blocks.short_to_float(1, 1)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_null_sink_0_0_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_multiply_const_vxx_1_0_1_0_0_1 = blocks.multiply_const_vff((180.0/math.pi, ))
        self.blocks_multiply_const_vxx_1_0_1_0_0_0 = blocks.multiply_const_vff((180.0/math.pi, ))
        self.blocks_multiply_const_vxx_1_0_1_0_0 = blocks.multiply_const_vff((180.0/math.pi, ))
        self.blocks_multiply_const_vxx_1_0_1_0 = blocks.multiply_const_vff((180.0/math.pi, ))
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff((-1, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((-1, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((-1, ))
        self.blocks_multiply_conjugate_cc_0_0_0 = blocks.multiply_conjugate_cc(nfft)
        self.blocks_multiply_conjugate_cc_0_0 = blocks.multiply_conjugate_cc(nfft)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(nfft)
        self.blocks_max_xx_0_0_0 = blocks.max_ff(nfft,1)
        self.blocks_max_xx_0_0 = blocks.max_ff(nfft,1)
        self.blocks_max_xx_0 = blocks.max_ff(nfft,1)
        self.blocks_delay_3_0 = blocks.delay(gr.sizeof_gr_complex*1, delay_3 + int(function_probe_0_3)+manual_fine_delay_3)
        self.blocks_delay_3 = blocks.delay(gr.sizeof_gr_complex*1, delay_3)
        self.blocks_delay_2_0 = blocks.delay(gr.sizeof_gr_complex*1, delay_2 + int(function_probe_0_2) + manual_fine_delay_2)
        self.blocks_delay_2 = blocks.delay(gr.sizeof_gr_complex*1, delay_2)
        self.blocks_delay_1_0 = blocks.delay(gr.sizeof_gr_complex*1, delay_1 + int(function_probe_0_1) + manual_fine_delay_1)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_gr_complex*1, delay_1)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, delay_0 + manual_fine_delay_0)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, delay_0)
        self.blocks_complex_to_mag_squared_1_0_0_0_0_2 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_1_0_0_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_1_0_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_1_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_1_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_1 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_1_2_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_1_2 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_1_1_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_1_1_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_1_1 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_1_0_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_1_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_1_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_1 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_0_0_0 = blocks.complex_to_mag(nfft)
        self.blocks_complex_to_mag_0_0 = blocks.complex_to_mag(nfft)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(nfft)
        self.blocks_complex_to_arg_0_0_1 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0_0_0 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0_0 = blocks.complex_to_arg(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.blocks_argmax_xx_0_0_0 = blocks.argmax_fs(nfft)
        self.blocks_argmax_xx_0_0 = blocks.argmax_fs(nfft)
        self.blocks_argmax_xx_0 = blocks.argmax_fs(nfft)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0_0_0 = blocks.add_const_vff((-nfft / 2, ))
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vff((-nfft / 2, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-nfft / 2, ))
        self.analog_const_source_x_0_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, thresh)
        self.analog_const_source_x_0_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, thresh)
        self.analog_const_source_x_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, thresh)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, thresh)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, thresh)
        self.analog_agc2_xx_0_3 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0_3.set_max_gain(65536)
        self.analog_agc2_xx_0_2 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0_2.set_max_gain(65536)
        self.analog_agc2_xx_0_1 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0_1.set_max_gain(65536)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)
        self.adsb_framer_1_0_0_0_0 = adsb.framer(samp_rate, thresh)
        self.adsb_framer_1_0_0_0 = adsb.framer(samp_rate, thresh)
        self.adsb_framer_1_0_0 = adsb.framer(samp_rate, thresh)
        self.adsb_framer_1_0 = adsb.framer(samp_rate, thresh)
        self.adsb_framer_1 = adsb.framer(samp_rate, thresh)
        self.adsb_demod_0_0_0_0_0 = adsb.demod(samp_rate)
        self.adsb_demod_0_0_0_0 = adsb.demod(samp_rate)
        self.adsb_demod_0_0_0 = adsb.demod(samp_rate)
        self.adsb_demod_0_0 = adsb.demod(samp_rate)
        self.adsb_demod_0 = adsb.demod(samp_rate)
        self.adsb_decoder_0_0_0_0_0 = adsb.decoder("Extended Squitter Only", "None", "Verbose")
        self.adsb_decoder_0_0_0_0 = adsb.decoder("Extended Squitter Only", "None", "Verbose")
        self.adsb_decoder_0_0_0 = adsb.decoder("Extended Squitter Only", "None", "Verbose")
        self.adsb_decoder_0_0 = adsb.decoder("Extended Squitter Only", "None", "Verbose")
        self.adsb_decoder_0 = adsb.decoder("Extended Squitter Only", "None", "Verbose")



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.adsb_decoder_0, 'decoded'), (self.pyqt_meta_text_output_0, 'pdus'))
        self.msg_connect((self.adsb_decoder_0_0, 'decoded'), (self.pyqt_meta_text_output_0_0, 'pdus'))
        self.msg_connect((self.adsb_decoder_0_0_0, 'decoded'), (self.pyqt_meta_text_output_0_0_0, 'pdus'))
        self.msg_connect((self.adsb_decoder_0_0_0_0, 'decoded'), (self.pyqt_meta_text_output_0_0_0_0, 'pdus'))
        self.msg_connect((self.adsb_decoder_0_0_0_0_0, 'decoded'), (self.pyqt_meta_text_output_0_0_0_0_0, 'pdus'))
        self.msg_connect((self.adsb_demod_0, 'demodulated'), (self.adsb_decoder_0, 'demodulated'))
        self.msg_connect((self.adsb_demod_0_0, 'demodulated'), (self.adsb_decoder_0_0, 'demodulated'))
        self.msg_connect((self.adsb_demod_0_0_0, 'demodulated'), (self.adsb_decoder_0_0_0, 'demodulated'))
        self.msg_connect((self.adsb_demod_0_0_0_0, 'demodulated'), (self.adsb_decoder_0_0_0_0, 'demodulated'))
        self.msg_connect((self.adsb_demod_0_0_0_0_0, 'demodulated'), (self.adsb_decoder_0_0_0_0_0, 'demodulated'))
        self.connect((self.adsb_demod_0, 0), (self.qtgui_time_sink_x_0_1_0, 0))
        self.connect((self.adsb_demod_0_0, 0), (self.qtgui_time_sink_x_0_1_0_0, 0))
        self.connect((self.adsb_demod_0_0_0, 0), (self.qtgui_time_sink_x_0_1_0_0_0, 0))
        self.connect((self.adsb_demod_0_0_0_0, 0), (self.qtgui_time_sink_x_0_1_0_0_0_0, 0))
        self.connect((self.adsb_demod_0_0_0_0_0, 0), (self.qtgui_time_sink_x_0_1_0_0_0_0_0, 0))
        self.connect((self.adsb_framer_1, 0), (self.adsb_demod_0, 0))
        self.connect((self.adsb_framer_1_0, 0), (self.adsb_demod_0_0, 0))
        self.connect((self.adsb_framer_1_0_0, 0), (self.adsb_demod_0_0_0, 0))
        self.connect((self.adsb_framer_1_0_0_0, 0), (self.adsb_demod_0_0_0_0, 0))
        self.connect((self.adsb_framer_1_0_0_0_0, 0), (self.adsb_demod_0_0_0_0_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.analog_agc2_xx_0_1, 0), (self.blocks_complex_to_mag_squared_0_1, 0))
        self.connect((self.analog_agc2_xx_0_1, 0), (self.blocks_delay_1, 0))
        self.connect((self.analog_agc2_xx_0_1, 0), (self.blocks_delay_1_0, 0))
        self.connect((self.analog_agc2_xx_0_1, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.analog_agc2_xx_0_1, 0), (self.qtgui_waterfall_sink_x_0_0, 0))
        self.connect((self.analog_agc2_xx_0_2, 0), (self.blocks_complex_to_mag_squared_0_1_0, 0))
        self.connect((self.analog_agc2_xx_0_2, 0), (self.blocks_delay_2, 0))
        self.connect((self.analog_agc2_xx_0_2, 0), (self.blocks_delay_2_0, 0))
        self.connect((self.analog_agc2_xx_0_2, 0), (self.qtgui_freq_sink_x_0_1, 0))
        self.connect((self.analog_agc2_xx_0_2, 0), (self.qtgui_waterfall_sink_x_0_0_0, 0))
        self.connect((self.analog_agc2_xx_0_3, 0), (self.blocks_complex_to_mag_squared_0_1_1, 0))
        self.connect((self.analog_agc2_xx_0_3, 0), (self.blocks_delay_3, 0))
        self.connect((self.analog_agc2_xx_0_3, 0), (self.blocks_delay_3_0, 0))
        self.connect((self.analog_agc2_xx_0_3, 0), (self.qtgui_freq_sink_x_0_1_0, 0))
        self.connect((self.analog_agc2_xx_0_3, 0), (self.qtgui_waterfall_sink_x_0_0_1, 0))
        self.connect((self.analog_const_source_x_0, 0), (self.qtgui_time_sink_x_0_1_0, 1))
        self.connect((self.analog_const_source_x_0_0, 0), (self.qtgui_time_sink_x_0_1_0_0, 1))
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.qtgui_time_sink_x_0_1_0_0_0, 1))
        self.connect((self.analog_const_source_x_0_0_0_0, 0), (self.qtgui_time_sink_x_0_1_0_0_0_0, 1))
        self.connect((self.analog_const_source_x_0_0_0_0_0, 0), (self.qtgui_time_sink_x_0_1_0_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_complex_to_mag_squared_1_0_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0_1_1_0, 4))
        self.connect((self.blocks_argmax_xx_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_argmax_xx_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_argmax_xx_0_0, 1), (self.blocks_null_sink_0_0, 0))
        self.connect((self.blocks_argmax_xx_0_0, 0), (self.blocks_short_to_float_0_0, 0))
        self.connect((self.blocks_argmax_xx_0_0_0, 1), (self.blocks_null_sink_0_0_0, 0))
        self.connect((self.blocks_argmax_xx_0_0_0, 0), (self.blocks_short_to_float_0_0_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.blocks_multiply_const_vxx_1_0_1_0, 0))
        self.connect((self.blocks_complex_to_arg_0_0, 0), (self.blocks_multiply_const_vxx_1_0_1_0_0, 0))
        self.connect((self.blocks_complex_to_arg_0_0_0, 0), (self.blocks_multiply_const_vxx_1_0_1_0_0_0, 0))
        self.connect((self.blocks_complex_to_arg_0_0_1, 0), (self.blocks_multiply_const_vxx_1_0_1_0_0_1, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.single_pole_iir_filter_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_0_0, 0), (self.single_pole_iir_filter_xx_0_0, 0))
        self.connect((self.blocks_complex_to_mag_0_0_0, 0), (self.single_pole_iir_filter_xx_0_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_0_0, 0), (self.qtgui_time_sink_x_0_1_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_1, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_1_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_1_0_0, 0), (self.qtgui_time_sink_x_0_1, 2))
        self.connect((self.blocks_complex_to_mag_squared_0_1_0_0_0, 0), (self.qtgui_time_sink_x_0_1_1, 2))
        self.connect((self.blocks_complex_to_mag_squared_0_1_1, 0), (self.qtgui_time_sink_x_0_0_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0_1_1_0, 0), (self.qtgui_time_sink_x_0_1, 3))
        self.connect((self.blocks_complex_to_mag_squared_0_1_1_0_0, 0), (self.qtgui_time_sink_x_0_1_1, 3))
        self.connect((self.blocks_complex_to_mag_squared_0_1_2, 0), (self.qtgui_time_sink_x_0_1, 1))
        self.connect((self.blocks_complex_to_mag_squared_0_1_2_0, 0), (self.qtgui_time_sink_x_0_1_1, 1))
        self.connect((self.blocks_complex_to_mag_squared_1, 0), (self.adsb_framer_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_1_0, 0), (self.adsb_framer_1_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_1_0_0, 0), (self.adsb_framer_1_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_1_0_0_0, 0), (self.adsb_framer_1_0_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_1_0_0_0_0, 0), (self.adsb_framer_1_0_0_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_1_0_0_0_0, 0), (self.qtgui_time_sink_x_0_1_1, 4))
        self.connect((self.blocks_complex_to_mag_squared_1_0_0_0_0_2, 0), (self.qtgui_time_sink_x_0_1_1_1, 4))
        self.connect((self.blocks_complex_to_mag_squared_1_0_0_0_0_2, 0), (self.qtgui_time_sink_x_2, 3))
        self.connect((self.blocks_delay_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_complex_to_mag_squared_1, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_stream_to_vector_0_1, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_stream_to_vector_0_1_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_complex_to_mag_squared_0_0_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_complex_to_mag_squared_1_0_0_0_0_2, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_time_sink_x_0_1_1_0, 0))
        self.connect((self.blocks_delay_1, 0), (self.blocks_complex_to_mag_squared_0_1_2, 0))
        self.connect((self.blocks_delay_1, 0), (self.blocks_complex_to_mag_squared_1_0, 0))
        self.connect((self.blocks_delay_1, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_delay_1_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_delay_1_0, 0), (self.blocks_complex_to_arg_0_0, 0))
        self.connect((self.blocks_delay_1_0, 0), (self.blocks_complex_to_mag_squared_0_1_2_0, 0))
        self.connect((self.blocks_delay_1_0, 0), (self.qtgui_time_sink_x_0_1_1_0, 1))
        self.connect((self.blocks_delay_2, 0), (self.blocks_complex_to_mag_squared_0_1_0_0, 0))
        self.connect((self.blocks_delay_2, 0), (self.blocks_complex_to_mag_squared_1_0_0, 0))
        self.connect((self.blocks_delay_2, 0), (self.blocks_stream_to_vector_0_0_0, 0))
        self.connect((self.blocks_delay_2_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_delay_2_0, 0), (self.blocks_complex_to_arg_0_0_0, 0))
        self.connect((self.blocks_delay_2_0, 0), (self.blocks_complex_to_mag_squared_0_1_0_0_0, 0))
        self.connect((self.blocks_delay_2_0, 0), (self.qtgui_time_sink_x_0_1_1_0, 2))
        self.connect((self.blocks_delay_3, 0), (self.blocks_complex_to_mag_squared_0_1_1_0, 0))
        self.connect((self.blocks_delay_3, 0), (self.blocks_complex_to_mag_squared_1_0_0_0, 0))
        self.connect((self.blocks_delay_3, 0), (self.blocks_stream_to_vector_0_0_0_0, 0))
        self.connect((self.blocks_delay_3_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_delay_3_0, 0), (self.blocks_complex_to_arg_0_0_1, 0))
        self.connect((self.blocks_delay_3_0, 0), (self.blocks_complex_to_mag_squared_0_1_1_0_0, 0))
        self.connect((self.blocks_delay_3_0, 0), (self.qtgui_time_sink_x_0_1_1_0, 3))
        self.connect((self.blocks_max_xx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_max_xx_0_0, 0), (self.qtgui_time_sink_x_1, 1))
        self.connect((self.blocks_max_xx_0_0_0, 0), (self.qtgui_time_sink_x_1, 2))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.fft_vxx_0_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0_0, 0), (self.fft_vxx_0_0_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0_0_0, 0), (self.fft_vxx_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.probe_offset_0_1, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.probe_offset_0_2, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.qtgui_number_sink_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.probe_offset_0_3, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.qtgui_number_sink_0, 2))
        self.connect((self.blocks_multiply_const_vxx_1_0_1_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0_1_0, 0), (self.blocks_sub_xx_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0_1_0, 0), (self.blocks_sub_xx_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0_1_0, 0), (self.qtgui_time_sink_x_0_1_1_1, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0_1_0_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_1_0_0, 0), (self.qtgui_time_sink_x_0_1_1_1, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_1_0_0_0, 0), (self.blocks_sub_xx_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_1_0_0_0, 0), (self.qtgui_time_sink_x_0_1_1_1, 2))
        self.connect((self.blocks_multiply_const_vxx_1_0_1_0_0_1, 0), (self.blocks_sub_xx_0_0_0, 1))
        self.connect((self.blocks_multiply_const_vxx_1_0_1_0_0_1, 0), (self.qtgui_time_sink_x_0_1_1_1, 3))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_short_to_float_0_0, 0), (self.blocks_add_const_vxx_0_0, 0))
        self.connect((self.blocks_short_to_float_0_0_0, 0), (self.blocks_add_const_vxx_0_0_0, 0))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_skiphead_1, 0), (self.blocks_throttle_1, 0))
        self.connect((self.blocks_skiphead_2, 0), (self.blocks_throttle_2, 0))
        self.connect((self.blocks_skiphead_3, 0), (self.blocks_throttle_3, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_1, 0))
        self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.fft_vxx_1_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0_0_0, 0), (self.fft_vxx_1_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.fft_vxx_0_1, 0))
        self.connect((self.blocks_stream_to_vector_0_1_0, 0), (self.fft_vxx_0_1_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.blocks_sub_xx_0_0, 0), (self.qtgui_time_sink_x_2, 1))
        self.connect((self.blocks_sub_xx_0_0_0, 0), (self.qtgui_time_sink_x_2, 2))
        self.connect((self.blocks_throttle_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.blocks_throttle_1, 0), (self.analog_agc2_xx_0_1, 0))
        self.connect((self.blocks_throttle_2, 0), (self.analog_agc2_xx_0_2, 0))
        self.connect((self.blocks_throttle_3, 0), (self.analog_agc2_xx_0_3, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.fft_vxx_0_0_0, 0), (self.blocks_complex_to_mag_0_0, 0))
        self.connect((self.fft_vxx_0_0_0_0, 0), (self.blocks_complex_to_mag_0_0_0, 0))
        self.connect((self.fft_vxx_0_1, 0), (self.blocks_multiply_conjugate_cc_0_0, 0))
        self.connect((self.fft_vxx_0_1_0, 0), (self.blocks_multiply_conjugate_cc_0_0_0, 0))
        self.connect((self.fft_vxx_1, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.fft_vxx_1_0, 0), (self.blocks_multiply_conjugate_cc_0_0, 1))
        self.connect((self.fft_vxx_1_0_0, 0), (self.blocks_multiply_conjugate_cc_0_0_0, 1))
        self.connect((self.sigmf_source_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.sigmf_source_1, 0), (self.blocks_skiphead_1, 0))
        self.connect((self.sigmf_source_2, 0), (self.blocks_skiphead_2, 0))
        self.connect((self.sigmf_source_3, 0), (self.blocks_skiphead_3, 0))
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_argmax_xx_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_max_xx_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0_0, 0), (self.blocks_argmax_xx_0_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0_0, 0), (self.blocks_max_xx_0_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0_0, 0), (self.qtgui_vector_sink_f_0, 1))
        self.connect((self.single_pole_iir_filter_xx_0_0_0, 0), (self.blocks_argmax_xx_0_0_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0_0_0, 0), (self.blocks_max_xx_0_0_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0_0_0, 0), (self.qtgui_vector_sink_f_0, 2))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "kerberos_sigmf_playback4")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_function_probe_0_3(self):
        return self.function_probe_0_3

    def set_function_probe_0_3(self, function_probe_0_3):
        self.function_probe_0_3 = function_probe_0_3
        self.set_samp_offset_0_3(self._samp_offset_0_3_formatter(self.function_probe_0_3))
        self.blocks_delay_3_0.set_dly(self.delay_3 + int(self.function_probe_0_3)+self.manual_fine_delay_3)

    def get_function_probe_0_2(self):
        return self.function_probe_0_2

    def set_function_probe_0_2(self, function_probe_0_2):
        self.function_probe_0_2 = function_probe_0_2
        self.set_samp_offset_0_2(self._samp_offset_0_2_formatter(self.function_probe_0_2))
        self.blocks_delay_2_0.set_dly(self.delay_2 + int(self.function_probe_0_2) + self.manual_fine_delay_2)

    def get_function_probe_0_1(self):
        return self.function_probe_0_1

    def set_function_probe_0_1(self, function_probe_0_1):
        self.function_probe_0_1 = function_probe_0_1
        self.set_samp_offset_0_1(self._samp_offset_0_1_formatter(self.function_probe_0_1))
        self.blocks_delay_1_0.set_dly(self.delay_1 + int(self.function_probe_0_1) + self.manual_fine_delay_1)

    def get_trig_delay(self):
        return self.trig_delay

    def set_trig_delay(self, trig_delay):
        self.trig_delay = trig_delay
        Qt.QMetaObject.invokeMethod(self._trig_delay_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.trig_delay)))
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, self.thresh, self.trig_delay, self.trig_channel, "")

    def get_trig_channel(self):
        return self.trig_channel

    def set_trig_channel(self, trig_channel):
        self.trig_channel = trig_channel
        self._trig_channel_callback(self.trig_channel)
        self.qtgui_time_sink_x_0_1_1_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, self.thresh_comp, 0.0001, self.trig_channel, "")
        self.qtgui_time_sink_x_0_1_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, self.thresh, 0.0001, self.trig_channel, "")
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, self.thresh, self.trig_delay, self.trig_channel, "")

    def get_throttle(self):
        return self.throttle

    def set_throttle(self, throttle):
        self.throttle = throttle
        Qt.QMetaObject.invokeMethod(self._throttle_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.throttle)))
        self.blocks_throttle_3.set_sample_rate(self.samp_rate / self.throttle)
        self.blocks_throttle_2.set_sample_rate(self.samp_rate / self.throttle)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate /self.throttle)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate / self.throttle)

    def get_thresh_phase(self):
        return self.thresh_phase

    def set_thresh_phase(self, thresh_phase):
        self.thresh_phase = thresh_phase
        Qt.QMetaObject.invokeMethod(self._thresh_phase_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.thresh_phase)))
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, self.thresh_phase, 0.00005, 3, "")
        self.qtgui_time_sink_x_0_1_1_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, self.thresh_phase, 0.00005, 4, "")

    def get_thresh_comp(self):
        return self.thresh_comp

    def set_thresh_comp(self, thresh_comp):
        self.thresh_comp = thresh_comp
        Qt.QMetaObject.invokeMethod(self._thresh_comp_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.thresh_comp)))
        self.qtgui_time_sink_x_0_1_1_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, self.thresh_comp, 0.0001, self.trig_channel, "")

    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh
        Qt.QMetaObject.invokeMethod(self._thresh_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.thresh)))
        self.qtgui_time_sink_x_0_1_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, self.thresh, 0.0001, self.trig_channel, "")
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, self.thresh, self.trig_delay, self.trig_channel, "")
        self.qtgui_time_sink_x_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, self.thresh, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, self.thresh, 0, 0, "")
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, self.thresh, 0, 0, "")
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, self.thresh, 0, 0, "")
        self.analog_const_source_x_0_0_0_0_0.set_offset(self.thresh)
        self.analog_const_source_x_0_0_0_0.set_offset(self.thresh)
        self.analog_const_source_x_0_0_0.set_offset(self.thresh)
        self.analog_const_source_x_0_0.set_offset(self.thresh)
        self.analog_const_source_x_0.set_offset(self.thresh)
        self.adsb_framer_1_0_0_0_0.set_threshold(self.thresh)
        self.adsb_framer_1_0_0_0.set_threshold(self.thresh)
        self.adsb_framer_1_0_0.set_threshold(self.thresh)
        self.adsb_framer_1_0.set_threshold(self.thresh)
        self.adsb_framer_1.set_threshold(self.thresh)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate / self.nfft)
        self.qtgui_time_sink_x_0_1_1_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_0_0_0_0_0.set_samp_rate(int(self.samp_rate))
        self.qtgui_time_sink_x_0_1_0_0_0_0.set_samp_rate(int(self.samp_rate))
        self.qtgui_time_sink_x_0_1_0_0_0.set_samp_rate(int(self.samp_rate))
        self.qtgui_time_sink_x_0_1_0_0.set_samp_rate(int(self.samp_rate))
        self.qtgui_time_sink_x_0_1_0.set_samp_rate(int(self.samp_rate))
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_3.set_sample_rate(self.samp_rate / self.throttle)
        self.blocks_throttle_2.set_sample_rate(self.samp_rate / self.throttle)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate /self.throttle)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate / self.throttle)

    def get_samp_offset_0_3(self):
        return self.samp_offset_0_3

    def set_samp_offset_0_3(self, samp_offset_0_3):
        self.samp_offset_0_3 = samp_offset_0_3
        Qt.QMetaObject.invokeMethod(self._samp_offset_0_3_label, "setText", Qt.Q_ARG("QString", self.samp_offset_0_3))

    def get_samp_offset_0_2(self):
        return self.samp_offset_0_2

    def set_samp_offset_0_2(self, samp_offset_0_2):
        self.samp_offset_0_2 = samp_offset_0_2
        Qt.QMetaObject.invokeMethod(self._samp_offset_0_2_label, "setText", Qt.Q_ARG("QString", self.samp_offset_0_2))

    def get_samp_offset_0_1(self):
        return self.samp_offset_0_1

    def set_samp_offset_0_1(self, samp_offset_0_1):
        self.samp_offset_0_1 = samp_offset_0_1
        Qt.QMetaObject.invokeMethod(self._samp_offset_0_1_label, "setText", Qt.Q_ARG("QString", self.samp_offset_0_1))

    def get_nfft(self):
        return self.nfft

    def set_nfft(self, nfft):
        self.nfft = nfft
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate / self.nfft)
        self.blocks_add_const_vxx_0_0_0.set_k((-self.nfft / 2, ))
        self.blocks_add_const_vxx_0_0.set_k((-self.nfft / 2, ))
        self.blocks_add_const_vxx_0.set_k((-self.nfft / 2, ))

    def get_manual_fine_delay_3(self):
        return self.manual_fine_delay_3

    def set_manual_fine_delay_3(self, manual_fine_delay_3):
        self.manual_fine_delay_3 = manual_fine_delay_3
        Qt.QMetaObject.invokeMethod(self._manual_fine_delay_3_line_edit, "setText", Qt.Q_ARG("QString", str(self.manual_fine_delay_3)))
        self.blocks_delay_3_0.set_dly(self.delay_3 + int(self.function_probe_0_3)+self.manual_fine_delay_3)

    def get_manual_fine_delay_2(self):
        return self.manual_fine_delay_2

    def set_manual_fine_delay_2(self, manual_fine_delay_2):
        self.manual_fine_delay_2 = manual_fine_delay_2
        Qt.QMetaObject.invokeMethod(self._manual_fine_delay_2_line_edit, "setText", Qt.Q_ARG("QString", str(self.manual_fine_delay_2)))
        self.blocks_delay_2_0.set_dly(self.delay_2 + int(self.function_probe_0_2) + self.manual_fine_delay_2)

    def get_manual_fine_delay_1(self):
        return self.manual_fine_delay_1

    def set_manual_fine_delay_1(self, manual_fine_delay_1):
        self.manual_fine_delay_1 = manual_fine_delay_1
        Qt.QMetaObject.invokeMethod(self._manual_fine_delay_1_line_edit, "setText", Qt.Q_ARG("QString", str(self.manual_fine_delay_1)))
        self.blocks_delay_1_0.set_dly(self.delay_1 + int(self.function_probe_0_1) + self.manual_fine_delay_1)

    def get_manual_fine_delay_0(self):
        return self.manual_fine_delay_0

    def set_manual_fine_delay_0(self, manual_fine_delay_0):
        self.manual_fine_delay_0 = manual_fine_delay_0
        Qt.QMetaObject.invokeMethod(self._manual_fine_delay_0_line_edit, "setText", Qt.Q_ARG("QString", str(self.manual_fine_delay_0)))
        self.blocks_delay_0_0.set_dly(self.delay_0 + self.manual_fine_delay_0)

    def get_delay_3(self):
        return self.delay_3

    def set_delay_3(self, delay_3):
        self.delay_3 = delay_3
        Qt.QMetaObject.invokeMethod(self._delay_3_line_edit, "setText", Qt.Q_ARG("QString", str(self.delay_3)))
        self.blocks_delay_3_0.set_dly(self.delay_3 + int(self.function_probe_0_3)+self.manual_fine_delay_3)
        self.blocks_delay_3.set_dly(self.delay_3)

    def get_delay_2(self):
        return self.delay_2

    def set_delay_2(self, delay_2):
        self.delay_2 = delay_2
        Qt.QMetaObject.invokeMethod(self._delay_2_line_edit, "setText", Qt.Q_ARG("QString", str(self.delay_2)))
        self.blocks_delay_2_0.set_dly(self.delay_2 + int(self.function_probe_0_2) + self.manual_fine_delay_2)
        self.blocks_delay_2.set_dly(self.delay_2)

    def get_delay_1(self):
        return self.delay_1

    def set_delay_1(self, delay_1):
        self.delay_1 = delay_1
        Qt.QMetaObject.invokeMethod(self._delay_1_line_edit, "setText", Qt.Q_ARG("QString", str(self.delay_1)))
        self.blocks_delay_1_0.set_dly(self.delay_1 + int(self.function_probe_0_1) + self.manual_fine_delay_1)
        self.blocks_delay_1.set_dly(self.delay_1)

    def get_delay_0(self):
        return self.delay_0

    def set_delay_0(self, delay_0):
        self.delay_0 = delay_0
        Qt.QMetaObject.invokeMethod(self._delay_0_line_edit, "setText", Qt.Q_ARG("QString", str(self.delay_0)))
        self.blocks_delay_0_0.set_dly(self.delay_0 + self.manual_fine_delay_0)
        self.blocks_delay_0.set_dly(self.delay_0)

    def get_corr_alpha_0_3(self):
        return self.corr_alpha_0_3

    def set_corr_alpha_0_3(self, corr_alpha_0_3):
        self.corr_alpha_0_3 = corr_alpha_0_3
        Qt.QMetaObject.invokeMethod(self._corr_alpha_0_3_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.corr_alpha_0_3)))
        self.single_pole_iir_filter_xx_0_0_0.set_taps(self.corr_alpha_0_3)

    def get_corr_alpha_0_2(self):
        return self.corr_alpha_0_2

    def set_corr_alpha_0_2(self, corr_alpha_0_2):
        self.corr_alpha_0_2 = corr_alpha_0_2
        Qt.QMetaObject.invokeMethod(self._corr_alpha_0_2_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.corr_alpha_0_2)))
        self.single_pole_iir_filter_xx_0_0.set_taps(self.corr_alpha_0_2)

    def get_corr_alpha_0_1(self):
        return self.corr_alpha_0_1

    def set_corr_alpha_0_1(self, corr_alpha_0_1):
        self.corr_alpha_0_1 = corr_alpha_0_1
        Qt.QMetaObject.invokeMethod(self._corr_alpha_0_1_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.corr_alpha_0_1)))
        self.single_pole_iir_filter_xx_0.set_taps(self.corr_alpha_0_1)


def main(top_block_cls=kerberos_sigmf_playback4, options=None):

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
