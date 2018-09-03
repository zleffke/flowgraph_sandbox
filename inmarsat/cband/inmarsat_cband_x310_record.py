#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: 4F3_F5BE35_20180903_043626.400121_UTC_80M.short
# Generated: Mon Sep  3 00:58:09 2018
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
from datetime import datetime as dt; import string
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fosphor
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from optparse import OptionParser
import sys
import time
from gnuradio import qtgui


class inmarsat_cband_x310_record(gr.top_block, Qt.QWidget):

    def __init__(self, datatype='short', radio_id='F5BE35', sat_name='4F3'):
        gr.top_block.__init__(self, "4F3_F5BE35_20180903_043626.400121_UTC_80M.short")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("4F3_F5BE35_20180903_043626.400121_UTC_80M.short")
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

        self.settings = Qt.QSettings("GNU Radio", "inmarsat_cband_x310_record")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.datatype = datatype
        self.radio_id = radio_id
        self.sat_name = sat_name

        ##################################################
        # Variables
        ##################################################
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y%m%d_%H%M%S.%f" )+'_UTC'
        self.samp_rate = samp_rate = 100e6
        self.rf_freq = rf_freq = 3627.5e6
        self.resamp_rate = resamp_rate = 0.8
        self.hs_lo = hs_lo = 5150e6
        self.path = path = "/data1/captures/inmarsat_c/"
        self.if_freq = if_freq = hs_lo-rf_freq
        self.fn = fn = "{:s}_{:s}_{:s}_{:s}M.{:s}".format(sat_name, radio_id, ts_str, str(int(samp_rate/1e6*resamp_rate)), datatype)
        self.rx_gain = rx_gain = 10
        self.if_freq_lbl = if_freq_lbl = if_freq
        self.fp = fp = "{:s}{:s}".format(path,fn)

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
        self.top_grid_layout.addWidget(self._rx_gain_tool_bar, 9, 3, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rf_freq_tool_bar = Qt.QToolBar(self)
        self._rf_freq_tool_bar.addWidget(Qt.QLabel("rf_freq"+": "))
        self._rf_freq_line_edit = Qt.QLineEdit(str(self.rf_freq))
        self._rf_freq_tool_bar.addWidget(self._rf_freq_line_edit)
        self._rf_freq_line_edit.returnPressed.connect(
        	lambda: self.set_rf_freq(eng_notation.str_to_num(str(self._rf_freq_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._rf_freq_tool_bar, 10, 0, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("addr=192.168.40.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_clock_source('gpsdo', 0)
        self.uhd_usrp_source_0.set_time_source('gpsdo', 0)
        self.uhd_usrp_source_0.set_subdev_spec('A:0', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0.set_center_freq(if_freq, 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  resamp_rate,
                  taps=None,
        	  flt_size=64)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)

        self._if_freq_lbl_tool_bar = Qt.QToolBar(self)

        if None:
          self._if_freq_lbl_formatter = None
        else:
          self._if_freq_lbl_formatter = lambda x: eng_notation.num_to_str(x)

        self._if_freq_lbl_tool_bar.addWidget(Qt.QLabel('IF [MHz]'+": "))
        self._if_freq_lbl_label = Qt.QLabel(str(self._if_freq_lbl_formatter(self.if_freq_lbl)))
        self._if_freq_lbl_tool_bar.addWidget(self._if_freq_lbl_label)
        self.top_grid_layout.addWidget(self._if_freq_lbl_tool_bar, 10, 1, 1, 1)
        for r in range(10, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_glfw_sink_c_0 = fosphor.glfw_sink_c()
        self.fosphor_glfw_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_glfw_sink_c_0.set_frequency_range(rf_freq, samp_rate*resamp_rate)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((-1, ))
        self.blocks_interleaved_short_to_complex_0 = blocks.interleaved_short_to_complex(False, True)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_short*1, fp, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_interleaved_short_0 = blocks.complex_to_interleaved_short(False)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_interleaved_short_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_complex_to_interleaved_short_0, 0), (self.blocks_interleaved_short_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_complex_to_interleaved_short_0, 0))
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.fosphor_glfw_sink_c_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.pfb_arb_resampler_xxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "inmarsat_cband_x310_record")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_datatype(self):
        return self.datatype

    def set_datatype(self, datatype):
        self.datatype = datatype
        self.set_fn("{:s}_{:s}_{:s}_{:s}M.{:s}".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate/1e6*self.resamp_rate)), self.datatype))

    def get_radio_id(self):
        return self.radio_id

    def set_radio_id(self, radio_id):
        self.radio_id = radio_id
        self.set_fn("{:s}_{:s}_{:s}_{:s}M.{:s}".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate/1e6*self.resamp_rate)), self.datatype))

    def get_sat_name(self):
        return self.sat_name

    def set_sat_name(self, sat_name):
        self.sat_name = sat_name
        self.set_fn("{:s}_{:s}_{:s}_{:s}M.{:s}".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate/1e6*self.resamp_rate)), self.datatype))

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_fn("{:s}_{:s}_{:s}_{:s}M.{:s}".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate/1e6*self.resamp_rate)), self.datatype))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.fosphor_glfw_sink_c_0.set_frequency_range(self.rf_freq, self.samp_rate*self.resamp_rate)
        self.set_fn("{:s}_{:s}_{:s}_{:s}M.{:s}".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate/1e6*self.resamp_rate)), self.datatype))

    def get_rf_freq(self):
        return self.rf_freq

    def set_rf_freq(self, rf_freq):
        self.rf_freq = rf_freq
        Qt.QMetaObject.invokeMethod(self._rf_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rf_freq)))
        self.set_if_freq(self.hs_lo-self.rf_freq)
        self.fosphor_glfw_sink_c_0.set_frequency_range(self.rf_freq, self.samp_rate*self.resamp_rate)

    def get_resamp_rate(self):
        return self.resamp_rate

    def set_resamp_rate(self, resamp_rate):
        self.resamp_rate = resamp_rate
        self.pfb_arb_resampler_xxx_0.set_rate(self.resamp_rate)
        self.fosphor_glfw_sink_c_0.set_frequency_range(self.rf_freq, self.samp_rate*self.resamp_rate)
        self.set_fn("{:s}_{:s}_{:s}_{:s}M.{:s}".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate/1e6*self.resamp_rate)), self.datatype))

    def get_hs_lo(self):
        return self.hs_lo

    def set_hs_lo(self, hs_lo):
        self.hs_lo = hs_lo
        self.set_if_freq(self.hs_lo-self.rf_freq)

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path
        self.set_fp("{:s}{:s}".format(self.path,self.fn))

    def get_if_freq(self):
        return self.if_freq

    def set_if_freq(self, if_freq):
        self.if_freq = if_freq
        self.uhd_usrp_source_0.set_center_freq(self.if_freq, 0)
        self.set_if_freq_lbl(self._if_freq_lbl_formatter(self.if_freq))

    def get_fn(self):
        return self.fn

    def set_fn(self, fn):
        self.fn = fn
        self.set_fp("{:s}{:s}".format(self.path,self.fn))

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)


    def get_if_freq_lbl(self):
        return self.if_freq_lbl

    def set_if_freq_lbl(self, if_freq_lbl):
        self.if_freq_lbl = if_freq_lbl
        Qt.QMetaObject.invokeMethod(self._if_freq_lbl_label, "setText", Qt.Q_ARG("QString", self.if_freq_lbl))

    def get_fp(self):
        return self.fp

    def set_fp(self, fp):
        self.fp = fp
        self.blocks_file_sink_0.open(self.fp)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--datatype", dest="datatype", type="string", default='short',
        help="Set datatype [default=%default]")
    parser.add_option(
        "", "--radio-id", dest="radio_id", type="string", default='F5BE35',
        help="Set radio_id [default=%default]")
    parser.add_option(
        "", "--sat-name", dest="sat_name", type="string", default='4F3',
        help="Set sat_name [default=%default]")
    return parser


def main(top_block_cls=inmarsat_cband_x310_record, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(datatype=options.datatype, radio_id=options.radio_id, sat_name=options.sat_name)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
