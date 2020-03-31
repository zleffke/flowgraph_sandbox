#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: /captures/20200329/QUEQIAO_RHCP_2020-03-31T02:40:21Z
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
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import time
from gnuradio import qtgui


class queqiao_track(gr.top_block, Qt.QWidget):

    def __init__(self, path="/captures/20200329", rx_alt=542, rx_lat=37.148745, rx_lon=-80.578557, signal_type='QUEQIAO', usrp_type='B210'):
        gr.top_block.__init__(self, "/captures/20200329/QUEQIAO_RHCP_2020-03-31T02:40:21Z")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("/captures/20200329/QUEQIAO_RHCP_2020-03-31T02:40:21Z")
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

        self.settings = Qt.QSettings("GNU Radio", "queqiao_track")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.path = path
        self.rx_alt = rx_alt
        self.rx_lat = rx_lat
        self.rx_lon = rx_lon
        self.signal_type = signal_type
        self.usrp_type = usrp_type

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y-%m-%dT%H:%M:%SZ")
        self.fn_rhcp = fn_rhcp = "{:s}_RHCP_{:s}".format(signal_type.upper(), ts_str)
        self.fn_lhcp = fn_lhcp = "{:s}_LHCP_{:s}".format(signal_type.upper(), ts_str)
        self.samp_rate = samp_rate = 250e3
        self.rx_gain = rx_gain = 20
        self.rx_freq = rx_freq = 2234.52205e6
        self.fp_rhcp = fp_rhcp = "{:s}/{:s}".format(path, fn_rhcp)
        self.fp_lhcp = fp_lhcp = "{:s}/{:s}".format(path, fn_lhcp)
        self.fft_min = fft_min = -120
        self.fft_max = fft_max = -80

        ##################################################
        # Blocks
        ##################################################
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
        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel('GAIN'+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_gain_tool_bar, 9, 2, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
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
        self._fft_min_tool_bar = Qt.QToolBar(self)
        self._fft_min_tool_bar.addWidget(Qt.QLabel('fft_min'+": "))
        self._fft_min_line_edit = Qt.QLineEdit(str(self.fft_min))
        self._fft_min_tool_bar.addWidget(self._fft_min_line_edit)
        self._fft_min_line_edit.returnPressed.connect(
        	lambda: self.set_fft_min(eng_notation.str_to_num(str(self._fft_min_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._fft_min_tool_bar, 9, 3, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._fft_max_tool_bar = Qt.QToolBar(self)
        self._fft_max_tool_bar.addWidget(Qt.QLabel('fft_max'+": "))
        self._fft_max_line_edit = Qt.QLineEdit(str(self.fft_max))
        self._fft_max_tool_bar.addWidget(self._fft_max_line_edit)
        self._fft_max_line_edit.returnPressed.connect(
        	lambda: self.set_fft_max(eng_notation.str_to_num(str(self._fft_max_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._fft_max_tool_bar, 9, 4, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_1 = uhd.usrp_source(
        	",".join(("serial=30CF9D2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_1.set_clock_source('external', 0)
        self.uhd_usrp_source_1.set_time_source('external', 0)
        self.uhd_usrp_source_1.set_subdev_spec('A:A', 0)
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(rx_freq, samp_rate/2), 0)
        self.uhd_usrp_source_1.set_gain(rx_gain, 0)
        self.uhd_usrp_source_1.set_antenna('RX2', 0)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 0)
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.uhd_usrp_source_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.qtgui_waterfall_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "queqiao_track")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        self.set_fp_rhcp("{:s}/{:s}".format(self.path, self.fn_rhcp))
        self.set_fp_lhcp("{:s}/{:s}".format(self.path, self.fn_lhcp))

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

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq, self.samp_rate/2), 0)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq, self.samp_rate/2), 1)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

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
        self.qtgui_waterfall_sink_x_0.set_intensity_range(self.fft_min, self.fft_max)
        self.qtgui_freq_sink_x_0.set_y_axis(self.fft_min, self.fft_max)

    def get_fft_max(self):
        return self.fft_max

    def set_fft_max(self, fft_max):
        self.fft_max = fft_max
        Qt.QMetaObject.invokeMethod(self._fft_max_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.fft_max)))
        self.qtgui_waterfall_sink_x_0.set_intensity_range(self.fft_min, self.fft_max)
        self.qtgui_freq_sink_x_0.set_y_axis(self.fft_min, self.fft_max)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--path", dest="path", type="string", default="/captures/20200329",
        help="Set path [default=%default]")
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
        "", "--signal-type", dest="signal_type", type="string", default='QUEQIAO',
        help="Set signal_type [default=%default]")
    parser.add_option(
        "", "--usrp-type", dest="usrp_type", type="string", default='B210',
        help="Set usrp_type [default=%default]")
    return parser


def main(top_block_cls=queqiao_track, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(path=options.path, rx_alt=options.rx_alt, rx_lat=options.rx_lat, rx_lon=options.rx_lon, signal_type=options.signal_type, usrp_type=options.usrp_type)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
