#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Sdrplay Test
# Generated: Thu Jan  3 17:30:46 2019
# GNU Radio version: 3.7.12.0
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
from gnuradio import eng_notation
from gnuradio import fosphor
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import math
import sdrplay
import sip
import sys
from gnuradio import qtgui


class sdrplay_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Sdrplay Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Sdrplay Test")
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

        self.settings = Qt.QSettings("GNU Radio", "sdrplay_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1.536e6
        self.rx_gain = rx_gain = 30
        self.rx_freq = rx_freq = 162.475e6 + 75e3
        self.lna_attn = lna_attn = 0
        self.if_attn = if_attn = 40
        self.agc = agc = True

        ##################################################
        # Blocks
        ##################################################
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel("rx_freq"+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_freq_tool_bar, 4, 0, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._lna_attn_tool_bar = Qt.QToolBar(self)
        self._lna_attn_tool_bar.addWidget(Qt.QLabel("lna_attn"+": "))
        self._lna_attn_line_edit = Qt.QLineEdit(str(self.lna_attn))
        self._lna_attn_tool_bar.addWidget(self._lna_attn_line_edit)
        self._lna_attn_line_edit.returnPressed.connect(
        	lambda: self.set_lna_attn(int(str(self._lna_attn_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._lna_attn_tool_bar, 4, 3, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._if_attn_tool_bar = Qt.QToolBar(self)
        self._if_attn_tool_bar.addWidget(Qt.QLabel("if_attn"+": "))
        self._if_attn_line_edit = Qt.QLineEdit(str(self.if_attn))
        self._if_attn_tool_bar.addWidget(self._if_attn_line_edit)
        self._if_attn_line_edit.returnPressed.connect(
        	lambda: self.set_if_attn(int(str(self._if_attn_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._if_attn_tool_bar, 4, 1, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        _agc_check_box = Qt.QCheckBox("agc")
        self._agc_choices = {True: True, False: False}
        self._agc_choices_inv = dict((v,k) for k,v in self._agc_choices.iteritems())
        self._agc_callback = lambda i: Qt.QMetaObject.invokeMethod(_agc_check_box, "setChecked", Qt.Q_ARG("bool", self._agc_choices_inv[i]))
        self._agc_callback(self.agc)
        _agc_check_box.stateChanged.connect(lambda i: self.set_agc(self._agc_choices[bool(i)]))
        self.top_grid_layout.addWidget(_agc_check_box)
        self.sdrplay_rspduo_source_0 = sdrplay.rspduo_source(rx_freq, 1536, bool(agc), if_attn, True, True,
                False, 0, 1, samp_rate, True, True, lna_attn, False,
                '0', 'T1_50ohm')

        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel("rx_gain"+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_gain_tool_bar, 4, 2, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
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
        self.fosphor_qt_sink_c_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0.set_frequency_range(rx_freq, samp_rate)
        self._fosphor_qt_sink_c_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._fosphor_qt_sink_c_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.sdrplay_rspduo_source_0, 0), (self.fosphor_qt_sink_c_0, 0))
        self.connect((self.sdrplay_rspduo_source_0, 0), (self.qtgui_freq_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "sdrplay_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rx_freq, self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))
        self.sdrplay_rspduo_source_0.set_rf_freq(self.rx_freq)
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rx_freq, self.samp_rate)

    def get_lna_attn(self):
        return self.lna_attn

    def set_lna_attn(self, lna_attn):
        self.lna_attn = lna_attn
        Qt.QMetaObject.invokeMethod(self._lna_attn_line_edit, "setText", Qt.Q_ARG("QString", str(self.lna_attn)))
        self.sdrplay_rspduo_source_0.set_lna_atten_step(self.lna_attn)

    def get_if_attn(self):
        return self.if_attn

    def set_if_attn(self, if_attn):
        self.if_attn = if_attn
        Qt.QMetaObject.invokeMethod(self._if_attn_line_edit, "setText", Qt.Q_ARG("QString", str(self.if_attn)))
        self.sdrplay_rspduo_source_0.set_if_atten_db(self.if_attn)

    def get_agc(self):
        return self.agc

    def set_agc(self, agc):
        self.agc = agc
        self._agc_callback(self.agc)
        self.sdrplay_rspduo_source_0.set_agc_enabled(bool(self.agc))


def main(top_block_cls=sdrplay_test, options=None):

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
