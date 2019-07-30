#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Satellite Monitor, VTGS FED-VU subsystem
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
from datetime import datetime as dt; import string
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import gr_sigmf
import sip
import sys
from gnuradio import qtgui


class fedvu_sat_mon(gr.top_block, Qt.QWidget):

    def __init__(self, name='SATMON', radio_id='FED-VU'):
        gr.top_block.__init__(self, "Satellite Monitor, VTGS FED-VU subsystem")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Satellite Monitor, VTGS FED-VU subsystem")
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

        self.settings = Qt.QSettings("GNU Radio", "fedvu_sat_mon")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.name = name
        self.radio_id = radio_id

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y%m%d_%H%M%S.%f" )+'_UTC'
        self.fn = fn = "{:s}_{:s}_{:s}.fc32".format(name,radio_id,ts_str)
        self.y_max = y_max = 0.01
        self.trig_lvl = trig_lvl = 0.005
        self.throttle_rate = throttle_rate = 1
        self.samp_rate = samp_rate = 250e3
        self.rx_freq = rx_freq = 401.5e6
        self.fp = fp = "/home/zleffke/captures/satmon/{:s}".format(fn)
        self.decim = decim = 5

        ##################################################
        # Blocks
        ##################################################
        self._y_max_tool_bar = Qt.QToolBar(self)
        self._y_max_tool_bar.addWidget(Qt.QLabel('Y Max'+": "))
        self._y_max_line_edit = Qt.QLineEdit(str(self.y_max))
        self._y_max_tool_bar.addWidget(self._y_max_line_edit)
        self._y_max_line_edit.returnPressed.connect(
        	lambda: self.set_y_max(eng_notation.str_to_num(str(self._y_max_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._y_max_tool_bar)
        self._trig_lvl_tool_bar = Qt.QToolBar(self)
        self._trig_lvl_tool_bar.addWidget(Qt.QLabel('Trigger Level'+": "))
        self._trig_lvl_line_edit = Qt.QLineEdit(str(self.trig_lvl))
        self._trig_lvl_tool_bar.addWidget(self._trig_lvl_line_edit)
        self._trig_lvl_line_edit.returnPressed.connect(
        	lambda: self.set_trig_lvl(eng_notation.str_to_num(str(self._trig_lvl_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._trig_lvl_tool_bar)
        self._throttle_rate_tool_bar = Qt.QToolBar(self)
        self._throttle_rate_tool_bar.addWidget(Qt.QLabel("throttle_rate"+": "))
        self._throttle_rate_line_edit = Qt.QLineEdit(str(self.throttle_rate))
        self._throttle_rate_tool_bar.addWidget(self._throttle_rate_line_edit)
        self._throttle_rate_line_edit.returnPressed.connect(
        	lambda: self.set_throttle_rate(eng_notation.str_to_num(str(self._throttle_rate_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._throttle_rate_tool_bar)
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('FREQ'+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_freq_tool_bar)
        self.sigmf_source_0 = gr_sigmf.source('/home/zleffke/captures/satmon/SATMON_FED-VU_20190730_203504.242069_UTC.sigmf-data', "cf32" + ("_le" if sys.byteorder == "little" else "_be"), False)
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

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, -40)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	512, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-y_max, y_max)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, trig_lvl, 0, 0, "")
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

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	2048, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	rx_freq, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, -80)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.1)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(True)

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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate*throttle_rate,True)
        self.blocks_message_debug_0 = blocks.message_debug()



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.sigmf_source_0, 'meta'), (self.blocks_message_debug_0, 'print'))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.sigmf_source_0, 0), (self.blocks_throttle_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fedvu_sat_mon")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        self.set_fn("{:s}_{:s}_{:s}.fc32".format(self.name,self.radio_id,self.ts_str))

    def get_radio_id(self):
        return self.radio_id

    def set_radio_id(self, radio_id):
        self.radio_id = radio_id
        self.set_fn("{:s}_{:s}_{:s}.fc32".format(self.name,self.radio_id,self.ts_str))

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_fn("{:s}_{:s}_{:s}.fc32".format(self.name,self.radio_id,self.ts_str))

    def get_fn(self):
        return self.fn

    def set_fn(self, fn):
        self.fn = fn
        self.set_fp("/home/zleffke/captures/satmon/{:s}".format(self.fn))

    def get_y_max(self):
        return self.y_max

    def set_y_max(self, y_max):
        self.y_max = y_max
        Qt.QMetaObject.invokeMethod(self._y_max_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.y_max)))
        self.qtgui_time_sink_x_0.set_y_axis(-self.y_max, self.y_max)

    def get_trig_lvl(self):
        return self.trig_lvl

    def set_trig_lvl(self, trig_lvl):
        self.trig_lvl = trig_lvl
        Qt.QMetaObject.invokeMethod(self._trig_lvl_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.trig_lvl)))
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, self.trig_lvl, 0, 0, "")

    def get_throttle_rate(self):
        return self.throttle_rate

    def set_throttle_rate(self, throttle_rate):
        self.throttle_rate = throttle_rate
        Qt.QMetaObject.invokeMethod(self._throttle_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.throttle_rate)))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.throttle_rate)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate*self.throttle_rate)

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))
        self.qtgui_freq_sink_x_0.set_frequency_range(self.rx_freq, self.samp_rate)

    def get_fp(self):
        return self.fp

    def set_fp(self, fp):
        self.fp = fp

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--name", dest="name", type="string", default='SATMON',
        help="Set name [default=%default]")
    parser.add_option(
        "", "--radio-id", dest="radio_id", type="string", default='FED-VU',
        help="Set radio_id [default=%default]")
    return parser


def main(top_block_cls=fedvu_sat_mon, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(name=options.name, radio_id=options.radio_id)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
