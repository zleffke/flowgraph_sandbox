#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Uhd Adsb 3
# Generated: Mon Dec 12 19:03:55 2016
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
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import adsb
import sip
import sys
from gnuradio import qtgui


class uhd_adsb_3(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Uhd Adsb 3")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Uhd Adsb 3")
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

        self.settings = Qt.QSettings("GNU Radio", "uhd_adsb_3")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.rx_gain = rx_gain = 40
        self.low = low = .3
        self.high = high = .31
        self.freq = freq = 1090e6
        self.bb_gain = bb_gain = 100e3

        ##################################################
        # Message Queues
        ##################################################
        adsb_decoder_0_msgq_out = blocks_message_source_0_msgq_in = gr.msg_queue(2)
        adsb_framer_0_msgq_out = adsb_decoder_0_msgq_in = gr.msg_queue(2)

        ##################################################
        # Blocks
        ##################################################
        self._low_tool_bar = Qt.QToolBar(self)
        self._low_tool_bar.addWidget(Qt.QLabel("low"+": "))
        self._low_line_edit = Qt.QLineEdit(str(self.low))
        self._low_tool_bar.addWidget(self._low_line_edit)
        self._low_line_edit.returnPressed.connect(
        	lambda: self.set_low(eng_notation.str_to_num(str(self._low_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._low_tool_bar)
        self._high_tool_bar = Qt.QToolBar(self)
        self._high_tool_bar.addWidget(Qt.QLabel("high"+": "))
        self._high_line_edit = Qt.QLineEdit(str(self.high))
        self._high_tool_bar.addWidget(self._high_line_edit)
        self._high_line_edit.returnPressed.connect(
        	lambda: self.set_high(eng_notation.str_to_num(str(self._high_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._high_tool_bar)
        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel("rx_gain"+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._rx_gain_tool_bar)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	512, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0.set_y_axis(0, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, .2, .00005, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['pre', 'post', '', '', '',
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
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.digital_correlate_access_code_tag_bb_0 = digital.correlate_access_code_tag_bb('1010000101000000', 3, 'adsb_preamble')
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(low, high, 0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((100e3, ))
        self.blocks_message_source_0 = blocks.message_source(gr.sizeof_char*1, blocks_message_source_0_msgq_in)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, '/home/leffke/sandbox/adsb/adsb_20161212_2M_2.32fc', True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/dev/stdout', True)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self._bb_gain_tool_bar = Qt.QToolBar(self)
        self._bb_gain_tool_bar.addWidget(Qt.QLabel("bb_gain"+": "))
        self._bb_gain_line_edit = Qt.QLineEdit(str(self.bb_gain))
        self._bb_gain_tool_bar.addWidget(self._bb_gain_line_edit)
        self._bb_gain_line_edit.returnPressed.connect(
        	lambda: self.set_bb_gain(eng_notation.str_to_num(str(self._bb_gain_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._bb_gain_tool_bar)
        self.adsb_framer_0 = adsb.framer(tx_msgq=adsb_framer_0_msgq_out)
        self.adsb_decoder_0 = adsb.decoder(rx_msgq=adsb_decoder_0_msgq_in,tx_msgq=adsb_decoder_0_msgq_out,output_type="csv",check_parity=True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.digital_correlate_access_code_tag_bb_0, 0))
        self.connect((self.blocks_message_source_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.digital_correlate_access_code_tag_bb_0, 0), (self.adsb_framer_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "uhd_adsb_3")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))

    def get_low(self):
        return self.low

    def set_low(self, low):
        self.low = low
        Qt.QMetaObject.invokeMethod(self._low_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.low)))
        self.blocks_threshold_ff_0.set_lo(self.low)

    def get_high(self):
        return self.high

    def set_high(self, high):
        self.high = high
        Qt.QMetaObject.invokeMethod(self._high_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.high)))
        self.blocks_threshold_ff_0.set_hi(self.high)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        Qt.QMetaObject.invokeMethod(self._bb_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.bb_gain)))


def main(top_block_cls=uhd_adsb_3, options=None):

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
