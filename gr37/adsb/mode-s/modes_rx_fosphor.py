#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: MODE-S Spectrum Monitor
# Author: Zach Leffke
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
from gnuradio import eng_notation
from gnuradio import fosphor
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import time
from gnuradio import qtgui


class modes_rx_fosphor(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "MODE-S Spectrum Monitor")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("MODE-S Spectrum Monitor")
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

        self.settings = Qt.QSettings("GNU Radio", "modes_rx_fosphor")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.custom_freq = custom_freq = 915e6
        self.fc = fc = [1030e6, 1090e6, custom_freq]
        self.band_select_qt = band_select_qt = 0
        self.ota_str = ota_str = "Over The Air: {:3.1f} MHz".format(fc[band_select_qt]/1e6)
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = ota_str
        self.samp_rate = samp_rate = 4e6
        self.ota_serial = ota_serial = "serial=3070390"
        self.gain_ota = gain_ota = 40

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel("samp_rate"+": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._samp_rate_tool_bar, 9, 3, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._gain_ota_tool_bar = Qt.QToolBar(self)
        self._gain_ota_tool_bar.addWidget(Qt.QLabel('Gain (dB)'+": "))
        self._gain_ota_line_edit = Qt.QLineEdit(str(self.gain_ota))
        self._gain_ota_tool_bar.addWidget(self._gain_ota_line_edit)
        self._gain_ota_line_edit.returnPressed.connect(
        	lambda: self.set_gain_ota(eng_notation.str_to_num(str(self._gain_ota_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._gain_ota_tool_bar, 9, 0, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._band_select_qt_options = (0, 1, 2, )
        self._band_select_qt_labels = ('1030 MHz', '1090 MHz', 'CUSTOM', )
        self._band_select_qt_group_box = Qt.QGroupBox('Channel Select')
        self._band_select_qt_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._band_select_qt_button_group = variable_chooser_button_group()
        self._band_select_qt_group_box.setLayout(self._band_select_qt_box)
        for i, label in enumerate(self._band_select_qt_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._band_select_qt_box.addWidget(radio_button)
        	self._band_select_qt_button_group.addButton(radio_button, i)
        self._band_select_qt_callback = lambda i: Qt.QMetaObject.invokeMethod(self._band_select_qt_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._band_select_qt_options.index(i)))
        self._band_select_qt_callback(self.band_select_qt)
        self._band_select_qt_button_group.buttonClicked[int].connect(
        	lambda i: self.set_band_select_qt(self._band_select_qt_options[i]))
        self.top_grid_layout.addWidget(self._band_select_qt_group_box, 9, 2, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: str(x)

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Spectrum'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_grid_layout.addWidget(self._variable_qtgui_label_0_tool_bar, 0, 0, 1, 4)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", ota_serial)),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(fc[band_select_qt], samp_rate/2), 0)
        self.uhd_usrp_source_0.set_gain(gain_ota, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_0.set_auto_iq_balance(True, 0)
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
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 10, 0, 1, 4)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0.set_frequency_range(0, samp_rate)
        self._fosphor_qt_sink_c_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._fosphor_qt_sink_c_0_win, 1, 0, 8, 4)
        for r in range(1, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._custom_freq_tool_bar = Qt.QToolBar(self)
        self._custom_freq_tool_bar.addWidget(Qt.QLabel("custom_freq"+": "))
        self._custom_freq_line_edit = Qt.QLineEdit(str(self.custom_freq))
        self._custom_freq_tool_bar.addWidget(self._custom_freq_line_edit)
        self._custom_freq_line_edit.returnPressed.connect(
        	lambda: self.set_custom_freq(eng_notation.str_to_num(str(self._custom_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._custom_freq_tool_bar, 9, 1, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_0, 0), (self.fosphor_qt_sink_c_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "modes_rx_fosphor")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_custom_freq(self):
        return self.custom_freq

    def set_custom_freq(self, custom_freq):
        self.custom_freq = custom_freq
        self.set_fc([1030e6, 1090e6, self.custom_freq])
        Qt.QMetaObject.invokeMethod(self._custom_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.custom_freq)))

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.fc[self.band_select_qt], self.samp_rate/2), 0)
        self.set_ota_str("Over The Air: {:3.1f} MHz".format(self.fc[self.band_select_qt]/1e6))

    def get_band_select_qt(self):
        return self.band_select_qt

    def set_band_select_qt(self, band_select_qt):
        self.band_select_qt = band_select_qt
        self._band_select_qt_callback(self.band_select_qt)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.fc[self.band_select_qt], self.samp_rate/2), 0)
        self.set_ota_str("Over The Air: {:3.1f} MHz".format(self.fc[self.band_select_qt]/1e6))

    def get_ota_str(self):
        return self.ota_str

    def set_ota_str(self, ota_str):
        self.ota_str = ota_str
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.ota_str))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", self.variable_qtgui_label_0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.fc[self.band_select_qt], self.samp_rate/2), 0)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.fosphor_qt_sink_c_0.set_frequency_range(0, self.samp_rate)

    def get_ota_serial(self):
        return self.ota_serial

    def set_ota_serial(self, ota_serial):
        self.ota_serial = ota_serial

    def get_gain_ota(self):
        return self.gain_ota

    def set_gain_ota(self, gain_ota):
        self.gain_ota = gain_ota
        Qt.QMetaObject.invokeMethod(self._gain_ota_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.gain_ota)))
        self.uhd_usrp_source_0.set_gain(self.gain_ota, 0)



def main(top_block_cls=modes_rx_fosphor, options=None):

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
