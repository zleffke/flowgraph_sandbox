#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: VCC FSK Receiver
# Author: Zach Leffke, KJ4QLP
# Description: GMSK AX.25 Receiver
# GNU Radio version: v3.8.3.1-13-g6c7e7843

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
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
import math
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
import satellites

from gnuradio import qtgui

class fsk_rx_hier(gr.top_block, Qt.QWidget):

    def __init__(self, rx_freq=401.5e6, rx_offset=125e3):
        gr.top_block.__init__(self, "VCC FSK Receiver")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("VCC FSK Receiver")
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

        self.settings = Qt.QSettings("GNU Radio", "fsk_rx_hier")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Parameters
        ##################################################
        self.rx_freq = rx_freq
        self.rx_offset = rx_offset

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250000
        self.interp = interp = 24
        self.decim = decim = 25*5
        self.baud = baud = 9600
        self.samps_per_symb = samps_per_symb = (samp_rate/decim*interp)/baud
        self.rx_gain = rx_gain = 0
        self.rx_correct = rx_correct = -300
        self.lpf_trans = lpf_trans = 1e3
        self.lpf_cutoff = lpf_cutoff = 12.5e3
        self.fsk_dev = fsk_dev = 10000

        ##################################################
        # Blocks
        ##################################################
        self._rx_gain_range = Range(0, 86, 1, 0, 200)
        self._rx_gain_win = RangeWidget(self._rx_gain_range, self.set_rx_gain, 'RX Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_gain_win, 4, 0, 1, 4)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._rx_correct_range = Range(-10000, 10000, 1, -300, 200)
        self._rx_correct_win = RangeWidget(self._rx_correct_range, self.set_rx_correct, 'rx_correct', "counter_slider", float)
        self.top_grid_layout.addWidget(self._rx_correct_win, 5, 0, 1, 4)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(rx_freq+rx_correct, rx_offset), 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec())
        self.satellites_pdu_to_kiss_0 = satellites.pdu_to_kiss(control_byte = True, include_timestamp = False)
        self.satellites_nrzi_decode_0 = satellites.nrzi_decode()
        self.satellites_hdlc_deframer_0 = satellites.hdlc_deframer(check_fcs=True, max_length=10000)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=interp,
                decimation=decim,
                taps=None,
                fractional_bw=0)
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
            2048, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate / decim*interp, #bw
            "RX Spectrum", #name
            2
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.010)
        self.qtgui_freq_sink_x_1_0.set_y_axis(-150, 0)
        self.qtgui_freq_sink_x_1_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0.enable_grid(True)
        self.qtgui_freq_sink_x_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0.enable_control_panel(False)

        self.qtgui_freq_sink_x_1_0.disable_legend()


        labels = ['', '', '', '', '',
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_win, 0, 0, 4, 4)
        for r in range(0, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                samp_rate / decim *interp,
                lpf_cutoff,
                lpf_trans,
                firdes.WIN_HAMMING,
                6.76))
        self.digital_descrambler_bb_0 = digital.descrambler_bb(0x21, 0, 16)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(samps_per_symb*(1+0.0), 0.25*0.175*0.175, 0.25, 0.175, 0.005)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_socket_pdu_0_2_0 = blocks.socket_pdu('TCP_SERVER', '0.0.0.0', '8001', 1024, False)
        self.analog_quadrature_demod_cf_1 = analog.quadrature_demod_cf((samp_rate/decim*interp)/(2*math.pi*fsk_dev/8.0))
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-1, 1e-2, 1.0, 1.0)
        self.analog_agc2_xx_0.set_max_gain(65536)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.satellites_hdlc_deframer_0, 'out'), (self.satellites_pdu_to_kiss_0, 'in'))
        self.msg_connect((self.satellites_pdu_to_kiss_0, 'out'), (self.blocks_socket_pdu_0_2_0, 'pdus'))
        self.connect((self.analog_agc2_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.analog_quadrature_demod_cf_1, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_descrambler_bb_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_descrambler_bb_0, 0), (self.satellites_nrzi_decode_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_quadrature_demod_cf_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_1_0, 1))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.qtgui_freq_sink_x_1_0, 0))
        self.connect((self.satellites_nrzi_decode_0, 0), (self.satellites_hdlc_deframer_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.rational_resampler_xxx_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fsk_rx_hier")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.rx_freq+self.rx_correct, self.rx_offset), 0)

    def get_rx_offset(self):
        return self.rx_offset

    def set_rx_offset(self, rx_offset):
        self.rx_offset = rx_offset
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.rx_freq+self.rx_correct, self.rx_offset), 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samps_per_symb((self.samp_rate/self.decim*self.interp)/self.baud)
        self.analog_quadrature_demod_cf_1.set_gain((self.samp_rate/self.decim*self.interp)/(2*math.pi*self.fsk_dev/8.0))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.lpf_cutoff, self.lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_interp(self):
        return self.interp

    def set_interp(self, interp):
        self.interp = interp
        self.set_samps_per_symb((self.samp_rate/self.decim*self.interp)/self.baud)
        self.analog_quadrature_demod_cf_1.set_gain((self.samp_rate/self.decim*self.interp)/(2*math.pi*self.fsk_dev/8.0))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.lpf_cutoff, self.lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.set_samps_per_symb((self.samp_rate/self.decim*self.interp)/self.baud)
        self.analog_quadrature_demod_cf_1.set_gain((self.samp_rate/self.decim*self.interp)/(2*math.pi*self.fsk_dev/8.0))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.lpf_cutoff, self.lpf_trans, firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate / self.decim*self.interp)

    def get_baud(self):
        return self.baud

    def set_baud(self, baud):
        self.baud = baud
        self.set_samps_per_symb((self.samp_rate/self.decim*self.interp)/self.baud)

    def get_samps_per_symb(self):
        return self.samps_per_symb

    def set_samps_per_symb(self, samps_per_symb):
        self.samps_per_symb = samps_per_symb
        self.digital_clock_recovery_mm_xx_0.set_omega(self.samps_per_symb*(1+0.0))

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)

    def get_rx_correct(self):
        return self.rx_correct

    def set_rx_correct(self, rx_correct):
        self.rx_correct = rx_correct
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.rx_freq+self.rx_correct, self.rx_offset), 0)

    def get_lpf_trans(self):
        return self.lpf_trans

    def set_lpf_trans(self, lpf_trans):
        self.lpf_trans = lpf_trans
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.lpf_cutoff, self.lpf_trans, firdes.WIN_HAMMING, 6.76))

    def get_lpf_cutoff(self):
        return self.lpf_cutoff

    def set_lpf_cutoff(self, lpf_cutoff):
        self.lpf_cutoff = lpf_cutoff
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate / self.decim *self.interp, self.lpf_cutoff, self.lpf_trans, firdes.WIN_HAMMING, 6.76))

    def get_fsk_dev(self):
        return self.fsk_dev

    def set_fsk_dev(self, fsk_dev):
        self.fsk_dev = fsk_dev
        self.analog_quadrature_demod_cf_1.set_gain((self.samp_rate/self.decim*self.interp)/(2*math.pi*self.fsk_dev/8.0))




def argument_parser():
    description = 'GMSK AX.25 Receiver'
    parser = ArgumentParser(description=description)
    parser.add_argument(
        "--rx-freq", dest="rx_freq", type=eng_float, default="401.5M",
        help="Set rx_freq [default=%(default)r]")
    parser.add_argument(
        "--rx-offset", dest="rx_offset", type=eng_float, default="125.0k",
        help="Set rx_offset [default=%(default)r]")
    return parser


def main(top_block_cls=fsk_rx_hier, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(rx_freq=options.rx_freq, rx_offset=options.rx_offset)

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
