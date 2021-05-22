#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: 4F3_30CF9D2_20180903_054255.650380_UTC_50M.fc32
# Generated: Mon Sep  3 02:08:00 2018
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
from gnuradio import filter
from gnuradio import fosphor
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import time
from gnuradio import qtgui


class inmarsat_cband_x310(gr.top_block, Qt.QWidget):

    def __init__(self, decim=5, decim2=10, radio_id='30CF9D2', sat_name='4F3'):
        gr.top_block.__init__(self, "4F3_30CF9D2_20180903_054255.650380_UTC_50M.fc32")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("4F3_30CF9D2_20180903_054255.650380_UTC_50M.fc32")
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

        self.settings = Qt.QSettings("GNU Radio", "inmarsat_cband_x310")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.decim = decim
        self.decim2 = decim2
        self.radio_id = radio_id
        self.sat_name = sat_name

        ##################################################
        # Variables
        ##################################################
        self.rf_freq = rf_freq = 3625e6
        self.hs_lo = hs_lo = 5150e6
        self.ts_str = ts_str = dt.strftime(dt.utcnow(), "%Y%m%d_%H%M%S.%f" )+'_UTC'
        self.samp_rate = samp_rate = 50e6
        self.if_freq = if_freq = hs_lo-rf_freq
        self.rx_gain = rx_gain = 10
        self.offset = offset = 0
        self.if_freq_lbl = if_freq_lbl = if_freq
        self.fn = fn = "{:s}_{:s}_{:s}_{:s}M.fc32".format(sat_name, radio_id, ts_str, str(int(samp_rate/1e6)))
        self.chan_offset = chan_offset = 0

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
        self._offset_tool_bar = Qt.QToolBar(self)
        self._offset_tool_bar.addWidget(Qt.QLabel('offset'+": "))
        self._offset_line_edit = Qt.QLineEdit(str(self.offset))
        self._offset_tool_bar.addWidget(self._offset_line_edit)
        self._offset_line_edit.returnPressed.connect(
        	lambda: self.set_offset(eng_notation.str_to_num(str(self._offset_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._offset_tool_bar, 9, 2, 1, 1)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._chan_offset_tool_bar = Qt.QToolBar(self)
        self._chan_offset_tool_bar.addWidget(Qt.QLabel('chan_offset'+": "))
        self._chan_offset_line_edit = Qt.QLineEdit(str(self.chan_offset))
        self._chan_offset_tool_bar.addWidget(self._chan_offset_line_edit)
        self._chan_offset_line_edit.returnPressed.connect(
        	lambda: self.set_chan_offset(eng_notation.str_to_num(str(self._chan_offset_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._chan_offset_tool_bar, 9, 4, 1, 2)
        for r in range(9, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 6):
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
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decim2,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=decim,
                taps=None,
                fractional_bw=None,
        )
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
        self.fosphor_qt_sink_c_0_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0_0.set_frequency_range(rf_freq + offset + chan_offset, samp_rate/decim/decim2)
        self._fosphor_qt_sink_c_0_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._fosphor_qt_sink_c_0_0_win, 0, 4, 8, 4)
        for r in range(0, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(4, 8):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_qt_sink_c_0 = fosphor.qt_sink_c()
        self.fosphor_qt_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_qt_sink_c_0.set_frequency_range(rf_freq + offset, samp_rate/decim)
        self._fosphor_qt_sink_c_0_win = sip.wrapinstance(self.fosphor_qt_sink_c_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._fosphor_qt_sink_c_0_win, 0, 0, 8, 4)
        for r in range(0, 8):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.fosphor_glfw_sink_c_0 = fosphor.glfw_sink_c()
        self.fosphor_glfw_sink_c_0.set_fft_window(window.WIN_BLACKMAN_hARRIS)
        self.fosphor_glfw_sink_c_0.set_frequency_range(rf_freq, samp_rate)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((-1, ))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1*(decim*chan_offset), 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -1*offset, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.fosphor_glfw_sink_c_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.fosphor_qt_sink_c_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.fosphor_qt_sink_c_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_complex_to_float_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "inmarsat_cband_x310")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.fosphor_qt_sink_c_0_0.set_frequency_range(self.rf_freq + self.offset + self.chan_offset, self.samp_rate/self.decim/self.decim2)
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rf_freq + self.offset, self.samp_rate/self.decim)
        self.analog_sig_source_x_0_0.set_frequency(-1*(self.decim*self.chan_offset))

    def get_decim2(self):
        return self.decim2

    def set_decim2(self, decim2):
        self.decim2 = decim2
        self.fosphor_qt_sink_c_0_0.set_frequency_range(self.rf_freq + self.offset + self.chan_offset, self.samp_rate/self.decim/self.decim2)

    def get_radio_id(self):
        return self.radio_id

    def set_radio_id(self, radio_id):
        self.radio_id = radio_id
        self.set_fn("{:s}_{:s}_{:s}_{:s}M.fc32".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate/1e6))))

    def get_sat_name(self):
        return self.sat_name

    def set_sat_name(self, sat_name):
        self.sat_name = sat_name
        self.set_fn("{:s}_{:s}_{:s}_{:s}M.fc32".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate/1e6))))

    def get_rf_freq(self):
        return self.rf_freq

    def set_rf_freq(self, rf_freq):
        self.rf_freq = rf_freq
        Qt.QMetaObject.invokeMethod(self._rf_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rf_freq)))
        self.set_if_freq(self.hs_lo-self.rf_freq)
        self.fosphor_qt_sink_c_0_0.set_frequency_range(self.rf_freq + self.offset + self.chan_offset, self.samp_rate/self.decim/self.decim2)
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rf_freq + self.offset, self.samp_rate/self.decim)
        self.fosphor_glfw_sink_c_0.set_frequency_range(self.rf_freq, self.samp_rate)

    def get_hs_lo(self):
        return self.hs_lo

    def set_hs_lo(self, hs_lo):
        self.hs_lo = hs_lo
        self.set_if_freq(self.hs_lo-self.rf_freq)

    def get_ts_str(self):
        return self.ts_str

    def set_ts_str(self, ts_str):
        self.ts_str = ts_str
        self.set_fn("{:s}_{:s}_{:s}_{:s}M.fc32".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate/1e6))))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.fosphor_qt_sink_c_0_0.set_frequency_range(self.rf_freq + self.offset + self.chan_offset, self.samp_rate/self.decim/self.decim2)
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rf_freq + self.offset, self.samp_rate/self.decim)
        self.fosphor_glfw_sink_c_0.set_frequency_range(self.rf_freq, self.samp_rate)
        self.set_fn("{:s}_{:s}_{:s}_{:s}M.fc32".format(self.sat_name, self.radio_id, self.ts_str, str(int(self.samp_rate/1e6))))
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_if_freq(self):
        return self.if_freq

    def set_if_freq(self, if_freq):
        self.if_freq = if_freq
        self.uhd_usrp_source_0.set_center_freq(self.if_freq, 0)
        self.set_if_freq_lbl(self._if_freq_lbl_formatter(self.if_freq))

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)


    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        Qt.QMetaObject.invokeMethod(self._offset_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.offset)))
        self.fosphor_qt_sink_c_0_0.set_frequency_range(self.rf_freq + self.offset + self.chan_offset, self.samp_rate/self.decim/self.decim2)
        self.fosphor_qt_sink_c_0.set_frequency_range(self.rf_freq + self.offset, self.samp_rate/self.decim)
        self.analog_sig_source_x_0.set_frequency(-1*self.offset)

    def get_if_freq_lbl(self):
        return self.if_freq_lbl

    def set_if_freq_lbl(self, if_freq_lbl):
        self.if_freq_lbl = if_freq_lbl
        Qt.QMetaObject.invokeMethod(self._if_freq_lbl_label, "setText", Qt.Q_ARG("QString", self.if_freq_lbl))

    def get_fn(self):
        return self.fn

    def set_fn(self, fn):
        self.fn = fn

    def get_chan_offset(self):
        return self.chan_offset

    def set_chan_offset(self, chan_offset):
        self.chan_offset = chan_offset
        Qt.QMetaObject.invokeMethod(self._chan_offset_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.chan_offset)))
        self.fosphor_qt_sink_c_0_0.set_frequency_range(self.rf_freq + self.offset + self.chan_offset, self.samp_rate/self.decim/self.decim2)
        self.analog_sig_source_x_0_0.set_frequency(-1*(self.decim*self.chan_offset))


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--decim", dest="decim", type="intx", default=5,
        help="Set decim [default=%default]")
    parser.add_option(
        "", "--decim2", dest="decim2", type="intx", default=10,
        help="Set decim2 [default=%default]")
    parser.add_option(
        "", "--radio-id", dest="radio_id", type="string", default='30CF9D2',
        help="Set radio_id [default=%default]")
    parser.add_option(
        "", "--sat-name", dest="sat_name", type="string", default='4F3',
        help="Set sat_name [default=%default]")
    return parser


def main(top_block_cls=inmarsat_cband_x310, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(decim=options.decim, decim2=options.decim2, radio_id=options.radio_id, sat_name=options.sat_name)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
