#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: asr_record_sigmf
# Author: Zach Leffke
# Description: Generic SigMF Recorder
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fosphor
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import sys
import time
from gnuradio import qtgui


class asr_record_sigmf(gr.top_block, Qt.QWidget):

    def __init__(self, addr='serial=314FC3C', antenna_type='Vehicle mounted brass discone', clock_rate=60e6, output_format='Complex Int16', path="/captures/20191215", rx_alt=501, rx_lat=37.250745, rx_lon=-79.932505, signal_type='ASR', tx_alt=340, tx_lat=37.326980, tx_lon=-79.982361, usrp_type='B200', wire_format='Complex Int12'):
        gr.top_block.__init__(self, "asr_record_sigmf")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("asr_record_sigmf")
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

        self.settings = Qt.QSettings("GNU Radio", "asr_record_sigmf")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.addr = addr
        self.antenna_type = antenna_type
        self.clock_rate = clock_rate
        self.output_format = output_format
        self.path = path
        self.rx_alt = rx_alt
        self.rx_lat = rx_lat
        self.rx_lon = rx_lon
        self.signal_type = signal_type
        self.tx_alt = tx_alt
        self.tx_lat = tx_lat
        self.tx_lon = tx_lon
        self.usrp_type = usrp_type
        self.wire_format = wire_format

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y-%m-%dT%H:%M:%SZ")
        self.fn = fn = "{:s}_{:s}".format(signal_type.upper(), ts_str)
        self.samp_rate = samp_rate = 15e6
        self.rx_gain = rx_gain = 30
        self.rx_freq = rx_freq = 2779.5e6
        self.fp = fp = "{:s}/{:s}".format(path, fn)

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel("samp_rate"+": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._samp_rate_tool_bar)
        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel('Gain'+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_gain_tool_bar)
        self._rx_freq_tool_bar = Qt.QToolBar(self)
        self._rx_freq_tool_bar.addWidget(Qt.QLabel('Freq [Hz]'+": "))
        self._rx_freq_line_edit = Qt.QLineEdit(str(self.rx_freq))
        self._rx_freq_tool_bar.addWidget(self._rx_freq_line_edit)
        self._rx_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rx_freq(eng_notation.str_to_num(str(self._rx_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rx_freq_tool_bar)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join((addr, "")),
        	uhd.stream_args(
        		cpu_format="sc16",
        		otw_format='sc12',
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_clock_rate(60e6, uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_clock_source('external', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(rx_freq, samp_rate/2), 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_source_0.set_auto_dc_offset(True, 0)
        self.uhd_usrp_source_0.set_auto_iq_balance(True, 0)
        self.fosphor_glfw_sink_c_0 = fosphor.glfw_sink_c()
        self.fosphor_glfw_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_glfw_sink_c_0.set_frequency_range(0, samp_rate)
        self.blocks_interleaved_short_to_complex_0 = blocks.interleaved_short_to_complex(True, False)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.fosphor_glfw_sink_c_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_interleaved_short_to_complex_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "asr_record_sigmf")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_addr(self):
        return self.addr

    def set_addr(self, addr):
        self.addr = addr

    def get_antenna_type(self):
        return self.antenna_type

    def set_antenna_type(self, antenna_type):
        self.antenna_type = antenna_type

    def get_clock_rate(self):
        return self.clock_rate

    def set_clock_rate(self, clock_rate):
        self.clock_rate = clock_rate

    def get_output_format(self):
        return self.output_format

    def set_output_format(self, output_format):
        self.output_format = output_format

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        self.set_fp("{:s}/{:s}".format(self.path, self.fn))

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

    def get_tx_alt(self):
        return self.tx_alt

    def set_tx_alt(self, tx_alt):
        self.tx_alt = tx_alt

    def get_tx_lat(self):
        return self.tx_lat

    def set_tx_lat(self, tx_lat):
        self.tx_lat = tx_lat

    def get_tx_lon(self):
        return self.tx_lon

    def set_tx_lon(self, tx_lon):
        self.tx_lon = tx_lon

    def get_usrp_type(self):
        return self.usrp_type

    def set_usrp_type(self, usrp_type):
        self.usrp_type = usrp_type

    def get_wire_format(self):
        return self.wire_format

    def set_wire_format(self, wire_format):
        self.wire_format = wire_format

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_fn("{:s}_{:s}".format(signal_type.upper(), self.ts_str))

    def get_fn(self):
        return self.fn

    def set_fn(self, fn):
        self.fn = fn
        self.set_fp("{:s}/{:s}".format(self.path, self.fn))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.rx_freq, self.samp_rate/2), 0)
        self.fosphor_glfw_sink_c_0.set_frequency_range(0, self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)


    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        Qt.QMetaObject.invokeMethod(self._rx_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_freq)))
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.rx_freq, self.samp_rate/2), 0)

    def get_fp(self):
        return self.fp

    def set_fp(self, fp):
        self.fp = fp


def argument_parser():
    description = 'Generic SigMF Recorder'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "", "--addr", dest="addr", type="string", default='serial=314FC3C',
        help="Set addr [default=%default]")
    parser.add_option(
        "", "--antenna-type", dest="antenna_type", type="string", default='Vehicle mounted brass discone',
        help="Set antenna_type [default=%default]")
    parser.add_option(
        "", "--clock-rate", dest="clock_rate", type="eng_float", default=eng_notation.num_to_str(60e6),
        help="Set clock_rate [default=%default]")
    parser.add_option(
        "", "--output-format", dest="output_format", type="string", default='Complex Int16',
        help="Set output_format [default=%default]")
    parser.add_option(
        "", "--path", dest="path", type="string", default="/captures/20191215",
        help="Set path [default=%default]")
    parser.add_option(
        "", "--rx-alt", dest="rx_alt", type="eng_float", default=eng_notation.num_to_str(501),
        help="Set rx_alt [default=%default]")
    parser.add_option(
        "", "--rx-lat", dest="rx_lat", type="eng_float", default=eng_notation.num_to_str(37.250745),
        help="Set rx_lat [default=%default]")
    parser.add_option(
        "", "--rx-lon", dest="rx_lon", type="eng_float", default=eng_notation.num_to_str(-79.932505),
        help="Set rx_lon [default=%default]")
    parser.add_option(
        "", "--signal-type", dest="signal_type", type="string", default='ASR',
        help="Set signal_type [default=%default]")
    parser.add_option(
        "", "--tx-alt", dest="tx_alt", type="eng_float", default=eng_notation.num_to_str(340),
        help="Set tx_alt [default=%default]")
    parser.add_option(
        "", "--tx-lat", dest="tx_lat", type="eng_float", default=eng_notation.num_to_str(37.326980),
        help="Set tx_lat [default=%default]")
    parser.add_option(
        "", "--tx-lon", dest="tx_lon", type="eng_float", default=eng_notation.num_to_str(-79.982361),
        help="Set tx_lon [default=%default]")
    parser.add_option(
        "", "--usrp-type", dest="usrp_type", type="string", default='B200',
        help="Set usrp_type [default=%default]")
    parser.add_option(
        "", "--wire-format", dest="wire_format", type="string", default='Complex Int12',
        help="Set wire_format [default=%default]")
    return parser


def main(top_block_cls=asr_record_sigmf, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(addr=options.addr, antenna_type=options.antenna_type, clock_rate=options.clock_rate, output_format=options.output_format, path=options.path, rx_alt=options.rx_alt, rx_lat=options.rx_lat, rx_lon=options.rx_lon, signal_type=options.signal_type, tx_alt=options.tx_alt, tx_lat=options.tx_lat, tx_lon=options.tx_lon, usrp_type=options.usrp_type, wire_format=options.wire_format)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
