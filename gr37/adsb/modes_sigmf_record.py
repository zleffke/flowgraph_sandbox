#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Modes Sigmf Record
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
from datetime import datetime as dt; import string
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fosphor
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import gr_sigmf
import sip
import sys
import time
from gnuradio import qtgui


class modes_sigmf_record(gr.top_block, Qt.QWidget):

    def __init__(self, mod_order=2, mod_scheme='DBPSK', path="/captures/adsb/20210127", rx_alt=652.272, rx_ant_model='Flightaware 1090 MHz ADS-B Antenna - 66 cm / 26 in', rx_db_ser='na', rx_db_type='na', rx_lat=37.206852, rx_lon=-80.419101, rx_ser_tag='3070390', rx_ser_uhd='3070390', rx_type='B200', signal_name='MODE-S', symbol_rate=4e6):
        gr.top_block.__init__(self, "Modes Sigmf Record")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Modes Sigmf Record")
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

        self.settings = Qt.QSettings("GNU Radio", "modes_sigmf_record")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.mod_order = mod_order
        self.mod_scheme = mod_scheme
        self.path = path
        self.rx_alt = rx_alt
        self.rx_ant_model = rx_ant_model
        self.rx_db_ser = rx_db_ser
        self.rx_db_type = rx_db_type
        self.rx_lat = rx_lat
        self.rx_lon = rx_lon
        self.rx_ser_tag = rx_ser_tag
        self.rx_ser_uhd = rx_ser_uhd
        self.rx_type = rx_type
        self.signal_name = signal_name
        self.symbol_rate = symbol_rate

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y-%m-%dT%H:%M:%S.%fZ")
        self.fn = fn = "{:s}_{:s}".format(signal_name, ts_str)
        self.tune = tune = 0
        self.thresh = thresh = 15
        self.samp_rate = samp_rate = 8e6
        self.rx_gain = rx_gain = 65
        self.rx_freq = rx_freq = 1030e6
        self.fp = fp = "{:s}/{:s}".format(path,fn)
        self.fn_adsb = fn_adsb = "{:s}_{:s}.csv".format('ADSB-log', ts_str)

        ##################################################
        # Blocks
        ##################################################
        self._thresh_tool_bar = Qt.QToolBar(self)
        self._thresh_tool_bar.addWidget(Qt.QLabel('GUI Threshold'+": "))
        self._thresh_line_edit = Qt.QLineEdit(str(self.thresh))
        self._thresh_tool_bar.addWidget(self._thresh_line_edit)
        self._thresh_line_edit.returnPressed.connect(
        	lambda: self.set_thresh(eng_notation.str_to_num(str(self._thresh_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._thresh_tool_bar, 9, 0, 1, 2)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel("rx_gain"+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_gain_tool_bar, 8, 0, 1, 2)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_1 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="sc16",
        		otw_format='sc16',
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_1.set_samp_rate(samp_rate)
        self.uhd_usrp_source_1.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(rx_freq, samp_rate/2), 0)
        self.uhd_usrp_source_1.set_gain(rx_gain, 0)
        self.uhd_usrp_source_1.set_antenna('RX2', 0)
        self.uhd_usrp_source_1.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_1.set_auto_iq_balance(True, 0)
        self._tune_tool_bar = Qt.QToolBar(self)
        self._tune_tool_bar.addWidget(Qt.QLabel("tune"+": "))
        self._tune_line_edit = Qt.QLineEdit(str(self.tune))
        self._tune_tool_bar.addWidget(self._tune_line_edit)
        self._tune_line_edit.returnPressed.connect(
        	lambda: self.set_tune(eng_notation.str_to_num(str(self._tune_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._tune_tool_bar, 8, 2, 1, 2)
        for r in range(8, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.sigmf_sink_0 = gr_sigmf.sink("ci16", fp, gr_sigmf.sigmf_time_mode_absolute, False)
        self.sigmf_sink_0.set_global_meta("core:sample_rate", samp_rate)
        self.sigmf_sink_0.set_global_meta("core:description", 'MODE-S SigMF Record, ')
        self.sigmf_sink_0.set_global_meta("core:author", 'Zach Leffke')
        self.sigmf_sink_0.set_global_meta("core:license", 'MIT')
        self.sigmf_sink_0.set_global_meta("core:hw", 'B200, RX2 port, External ADSB Antenna on RB1311 Roof, with ADSB RX logging')
        self.sigmf_sink_0.set_global_meta('usrp:rx_type', 'B200')
        self.sigmf_sink_0.set_global_meta('usrp:rx_ser_uhd', '3070390')
        self.sigmf_sink_0.set_global_meta('usrp:rx_ser_tag', '3070390')
        self.sigmf_sink_0.set_global_meta('usrp:rx_db_type', 'na')
        self.sigmf_sink_0.set_global_meta('usrp:rx_db_ser', 'na')
        self.sigmf_sink_0.set_global_meta('modulation:scheme', 'DBPSK')
        self.sigmf_sink_0.set_global_meta('modulation:order', 2)
        self.sigmf_sink_0.set_global_meta('modulation:symbol_rate', 4000000.0)
        self.sigmf_sink_0.set_global_meta('usrp:version', 'v0.1.0')
        self.sigmf_sink_0.set_global_meta('usrp:rx_rf_gain', 65)
        self.sigmf_sink_0.set_global_meta('usrp:rx_freq', 1030000000.0)
        self.sigmf_sink_0.set_global_meta('usrp:rx_ant_model', 'Flightaware 1090 MHz ADS-B Antenna - 66 cm / 26 in')
        self.sigmf_sink_0.set_global_meta('geo:rx_lat', 37.206852)
        self.sigmf_sink_0.set_global_meta('geo:rx_lon', -80.419101)
        self.sigmf_sink_0.set_global_meta('geo:rx_alt', 652.272)
        self.sigmf_sink_0.set_global_meta('misc:adsb_log', 'ADSB-log_2021-01-27T23:43:06.434883Z.csv')

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
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_glfw_sink_c_0 = fosphor.glfw_sink_c()
        self.fosphor_glfw_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_glfw_sink_c_0.set_frequency_range(0, samp_rate)
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_cc(1.0 / 65536.0)
        self.blocks_interleaved_short_to_complex_0 = blocks.interleaved_short_to_complex(True, False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.blocks_multiply_const_xx_0, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.fosphor_glfw_sink_c_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.blocks_interleaved_short_to_complex_0, 0))
        self.connect((self.uhd_usrp_source_1, 0), (self.sigmf_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "modes_sigmf_record")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_mod_order(self):
        return self.mod_order

    def set_mod_order(self, mod_order):
        self.mod_order = mod_order

    def get_mod_scheme(self):
        return self.mod_scheme

    def set_mod_scheme(self, mod_scheme):
        self.mod_scheme = mod_scheme

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        self.set_fp("{:s}/{:s}".format(self.path,self.fn))

    def get_rx_alt(self):
        return self.rx_alt

    def set_rx_alt(self, rx_alt):
        self.rx_alt = rx_alt

    def get_rx_ant_model(self):
        return self.rx_ant_model

    def set_rx_ant_model(self, rx_ant_model):
        self.rx_ant_model = rx_ant_model

    def get_rx_db_ser(self):
        return self.rx_db_ser

    def set_rx_db_ser(self, rx_db_ser):
        self.rx_db_ser = rx_db_ser

    def get_rx_db_type(self):
        return self.rx_db_type

    def set_rx_db_type(self, rx_db_type):
        self.rx_db_type = rx_db_type

    def get_rx_lat(self):
        return self.rx_lat

    def set_rx_lat(self, rx_lat):
        self.rx_lat = rx_lat

    def get_rx_lon(self):
        return self.rx_lon

    def set_rx_lon(self, rx_lon):
        self.rx_lon = rx_lon

    def get_rx_ser_tag(self):
        return self.rx_ser_tag

    def set_rx_ser_tag(self, rx_ser_tag):
        self.rx_ser_tag = rx_ser_tag

    def get_rx_ser_uhd(self):
        return self.rx_ser_uhd

    def set_rx_ser_uhd(self, rx_ser_uhd):
        self.rx_ser_uhd = rx_ser_uhd

    def get_rx_type(self):
        return self.rx_type

    def set_rx_type(self, rx_type):
        self.rx_type = rx_type

    def get_signal_name(self):
        return self.signal_name

    def set_signal_name(self, signal_name):
        self.signal_name = signal_name
        self.set_fn("{:s}_{:s}".format(self.signal_name, self.ts_str))

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_fn_adsb("{:s}_{:s}.csv".format('ADSB-log', self.ts_str))
        self.set_fn("{:s}_{:s}".format(self.signal_name, self.ts_str))

    def get_fn(self):
        return self.fn

    def set_fn(self, fn):
        self.fn = fn
        self.set_fp("{:s}/{:s}".format(self.path,self.fn))

    def get_tune(self):
        return self.tune

    def set_tune(self, tune):
        self.tune = tune
        Qt.QMetaObject.invokeMethod(self._tune_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.tune)))

    def get_thresh(self):
        return self.thresh

    def set_thresh(self, thresh):
        self.thresh = thresh
        Qt.QMetaObject.invokeMethod(self._thresh_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.thresh)))
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, self.thresh, 0, 0, "")

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_1.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq, self.samp_rate/2), 0)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.fosphor_glfw_sink_c_0.set_frequency_range(0, self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))
        self.uhd_usrp_source_1.set_gain(self.rx_gain, 0)


    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self.uhd_usrp_source_1.set_center_freq(uhd.tune_request(self.rx_freq, self.samp_rate/2), 0)

    def get_fp(self):
        return self.fp

    def set_fp(self, fp):
        self.fp = fp

    def get_fn_adsb(self):
        return self.fn_adsb

    def set_fn_adsb(self, fn_adsb):
        self.fn_adsb = fn_adsb


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--mod-order", dest="mod_order", type="intx", default=2,
        help="Set mod_order [default=%default]")
    parser.add_option(
        "", "--mod-scheme", dest="mod_scheme", type="string", default='DBPSK',
        help="Set mod_scheme [default=%default]")
    parser.add_option(
        "", "--path", dest="path", type="string", default="/captures/adsb/20210127",
        help="Set path [default=%default]")
    parser.add_option(
        "", "--rx-alt", dest="rx_alt", type="eng_float", default=eng_notation.num_to_str(652.272),
        help="Set rx_alt [default=%default]")
    parser.add_option(
        "", "--rx-ant-model", dest="rx_ant_model", type="string", default='Flightaware 1090 MHz ADS-B Antenna - 66 cm / 26 in',
        help="Set rx_ant_model [default=%default]")
    parser.add_option(
        "", "--rx-db-ser", dest="rx_db_ser", type="string", default='na',
        help="Set rx_db_ser [default=%default]")
    parser.add_option(
        "", "--rx-db-type", dest="rx_db_type", type="string", default='na',
        help="Set rx_db_type [default=%default]")
    parser.add_option(
        "", "--rx-lat", dest="rx_lat", type="eng_float", default=eng_notation.num_to_str(37.206852),
        help="Set rx_lat [default=%default]")
    parser.add_option(
        "", "--rx-lon", dest="rx_lon", type="eng_float", default=eng_notation.num_to_str(-80.419101),
        help="Set rx_lon [default=%default]")
    parser.add_option(
        "", "--rx-ser-tag", dest="rx_ser_tag", type="string", default='3070390',
        help="Set rx_ser_tag [default=%default]")
    parser.add_option(
        "", "--rx-ser-uhd", dest="rx_ser_uhd", type="string", default='3070390',
        help="Set rx_ser_uhd [default=%default]")
    parser.add_option(
        "", "--rx-type", dest="rx_type", type="string", default='B200',
        help="Set rx_type [default=%default]")
    parser.add_option(
        "", "--signal-name", dest="signal_name", type="string", default='MODE-S',
        help="Set signal_name [default=%default]")
    parser.add_option(
        "", "--symbol-rate", dest="symbol_rate", type="eng_float", default=eng_notation.num_to_str(4e6),
        help="Set symbol_rate [default=%default]")
    return parser


def main(top_block_cls=modes_sigmf_record, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(mod_order=options.mod_order, mod_scheme=options.mod_scheme, path=options.path, rx_alt=options.rx_alt, rx_ant_model=options.rx_ant_model, rx_db_ser=options.rx_db_ser, rx_db_type=options.rx_db_type, rx_lat=options.rx_lat, rx_lon=options.rx_lon, rx_ser_tag=options.rx_ser_tag, rx_ser_uhd=options.rx_ser_uhd, rx_type=options.rx_type, signal_name=options.signal_name, symbol_rate=options.symbol_rate)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
