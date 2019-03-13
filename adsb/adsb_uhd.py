#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Adsb Uhd
# Generated: Sun Dec 11 23:31:39 2016
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
from baz import message_server
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import adsb
import sip
import sys
import threading
import time
from gnuradio import qtgui


class adsb_uhd(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Adsb Uhd")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Adsb Uhd")
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

        self.settings = Qt.QSettings("GNU Radio", "adsb_uhd")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.thresh_mult = thresh_mult = 2
        self.samp_rate = samp_rate = 2e6
        self.low_thresh = low_thresh = 0
        self.rx_gain = rx_gain = 40
        self.low_thresh_lbl = low_thresh_lbl = low_thresh
        self.high = high = .4
        self.hi_thresh_lbl = hi_thresh_lbl = low_thresh*thresh_mult
        self.freq = freq = 1090e6
        self.filter_taps = filter_taps = firdes.low_pass(1,samp_rate, samp_rate/2, 50000, firdes.WIN_FLATTOP, 6.76)
        self.decim = decim = 1
        self.center = center = 0
        self.bb_gain = bb_gain = .1e6

        ##################################################
        # Message Queues
        ##################################################
        adsb_decoder_0_msgq_out = baz_message_server_0_msgq_in = gr.msg_queue(2)
        adsb_decoder_0_msgq_out = blocks_message_source_0_msgq_in = gr.msg_queue(2)
        adsb_framer_0_msgq_out = adsb_decoder_0_msgq_in = gr.msg_queue(2)

        ##################################################
        # Blocks
        ##################################################
        self.probe_power = blocks.probe_signal_f()
        self._thresh_mult_tool_bar = Qt.QToolBar(self)
        self._thresh_mult_tool_bar.addWidget(Qt.QLabel("thresh_mult"+": "))
        self._thresh_mult_line_edit = Qt.QLineEdit(str(self.thresh_mult))
        self._thresh_mult_tool_bar.addWidget(self._thresh_mult_line_edit)
        self._thresh_mult_line_edit.returnPressed.connect(
        	lambda: self.set_thresh_mult(eng_notation.str_to_num(str(self._thresh_mult_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._thresh_mult_tool_bar)
        self._rx_gain_tool_bar = Qt.QToolBar(self)
        self._rx_gain_tool_bar.addWidget(Qt.QLabel("rx_gain"+": "))
        self._rx_gain_line_edit = Qt.QLineEdit(str(self.rx_gain))
        self._rx_gain_tool_bar.addWidget(self._rx_gain_line_edit)
        self._rx_gain_line_edit.returnPressed.connect(
        	lambda: self.set_rx_gain(eng_notation.str_to_num(str(self._rx_gain_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._rx_gain_tool_bar)
        
        def _low_thresh_probe():
            while True:
                val = self.probe_power.level()
                try:
                    self.set_low_thresh(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _low_thresh_thread = threading.Thread(target=_low_thresh_probe)
        _low_thresh_thread.daemon = True
        _low_thresh_thread.start()
            
        self._center_tool_bar = Qt.QToolBar(self)
        self._center_tool_bar.addWidget(Qt.QLabel("center"+": "))
        self._center_line_edit = Qt.QLineEdit(str(self.center))
        self._center_tool_bar.addWidget(self._center_line_edit)
        self._center_line_edit.returnPressed.connect(
        	lambda: self.set_center(eng_notation.str_to_num(str(self._center_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._center_tool_bar)
        self._bb_gain_tool_bar = Qt.QToolBar(self)
        self._bb_gain_tool_bar.addWidget(Qt.QLabel("bb_gain"+": "))
        self._bb_gain_line_edit = Qt.QLineEdit(str(self.bb_gain))
        self._bb_gain_tool_bar.addWidget(self._bb_gain_line_edit)
        self._bb_gain_line_edit.returnPressed.connect(
        	lambda: self.set_bb_gain(eng_notation.str_to_num(str(self._bb_gain_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._bb_gain_tool_bar)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(freq, samp_rate/2), 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.01)
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
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-130, -70)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	4096, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.010)
        self.qtgui_time_sink_x_0.set_y_axis(0, 1)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, .3, .0001, 0, "")
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
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	4096, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate/decim, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.01)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, -80)
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
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self._low_thresh_lbl_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._low_thresh_lbl_formatter = None
        else:
          self._low_thresh_lbl_formatter = lambda x: x
        
        self._low_thresh_lbl_tool_bar.addWidget(Qt.QLabel("low_thresh_lbl"+": "))
        self._low_thresh_lbl_label = Qt.QLabel(str(self._low_thresh_lbl_formatter(self.low_thresh_lbl)))
        self._low_thresh_lbl_tool_bar.addWidget(self._low_thresh_lbl_label)
        self.top_layout.addWidget(self._low_thresh_lbl_tool_bar)
          
        self._high_tool_bar = Qt.QToolBar(self)
        self._high_tool_bar.addWidget(Qt.QLabel("high"+": "))
        self._high_line_edit = Qt.QLineEdit(str(self.high))
        self._high_tool_bar.addWidget(self._high_line_edit)
        self._high_line_edit.returnPressed.connect(
        	lambda: self.set_high(eng_notation.str_to_num(str(self._high_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._high_tool_bar)
        self._hi_thresh_lbl_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._hi_thresh_lbl_formatter = None
        else:
          self._hi_thresh_lbl_formatter = lambda x: x
        
        self._hi_thresh_lbl_tool_bar.addWidget(Qt.QLabel("hi_thresh_lbl"+": "))
        self._hi_thresh_lbl_label = Qt.QLabel(str(self._hi_thresh_lbl_formatter(self.hi_thresh_lbl)))
        self._hi_thresh_lbl_tool_bar.addWidget(self._hi_thresh_lbl_label)
        self.top_layout.addWidget(self._hi_thresh_lbl_tool_bar)
          
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, (filter_taps), center, samp_rate)
        self.digital_correlate_access_code_tag_bb_0 = digital.correlate_access_code_tag_bb('1010000101000000', 0, 'adsb_preamble')
        self.blocks_threshold_ff_0 = blocks.threshold_ff(low_thresh, low_thresh*thresh_mult, 0)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((bb_gain, ))
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(1000, .0001, 4000)
        self.blocks_message_source_0 = blocks.message_source(gr.sizeof_char*1, blocks_message_source_0_msgq_in)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/dev/stdout', True)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.baz_message_server_0 = message_server.message_server(msgq=baz_message_server_0_msgq_in, port=12345)
        self.adsb_framer_0 = adsb.framer(tx_msgq=adsb_framer_0_msgq_out)
        self.adsb_decoder_0 = adsb.decoder(rx_msgq=adsb_decoder_0_msgq_in,tx_msgq=adsb_decoder_0_msgq_out,output_type="csv",check_parity=True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_float_to_uchar_0, 0), (self.digital_correlate_access_code_tag_bb_0, 0))    
        self.connect((self.blocks_message_source_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_moving_average_xx_0, 0), (self.probe_power, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_moving_average_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_threshold_ff_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_float_to_uchar_0, 0))    
        self.connect((self.blocks_threshold_ff_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.digital_correlate_access_code_tag_bb_0, 0), (self.adsb_framer_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "adsb_uhd")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_thresh_mult(self):
        return self.thresh_mult

    def set_thresh_mult(self, thresh_mult):
        self.thresh_mult = thresh_mult
        Qt.QMetaObject.invokeMethod(self._thresh_mult_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.thresh_mult)))
        self.set_hi_thresh_lbl(self._hi_thresh_lbl_formatter(self.low_thresh*self.thresh_mult))
        self.blocks_threshold_ff_0.set_hi(self.low_thresh*self.thresh_mult)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_filter_taps(firdes.low_pass(1,self.samp_rate, self.samp_rate/2, 50000, firdes.WIN_FLATTOP, 6.76))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq, self.samp_rate/2), 0)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)

    def get_low_thresh(self):
        return self.low_thresh

    def set_low_thresh(self, low_thresh):
        self.low_thresh = low_thresh
        self.set_low_thresh_lbl(self._low_thresh_lbl_formatter(self.low_thresh))
        self.set_hi_thresh_lbl(self._hi_thresh_lbl_formatter(self.low_thresh*self.thresh_mult))
        self.blocks_threshold_ff_0.set_hi(self.low_thresh*self.thresh_mult)
        self.blocks_threshold_ff_0.set_lo(self.low_thresh)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        Qt.QMetaObject.invokeMethod(self._rx_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rx_gain)))
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)
        	

    def get_low_thresh_lbl(self):
        return self.low_thresh_lbl

    def set_low_thresh_lbl(self, low_thresh_lbl):
        self.low_thresh_lbl = low_thresh_lbl
        Qt.QMetaObject.invokeMethod(self._low_thresh_lbl_label, "setText", Qt.Q_ARG("QString", str(self.low_thresh_lbl)))

    def get_high(self):
        return self.high

    def set_high(self, high):
        self.high = high
        Qt.QMetaObject.invokeMethod(self._high_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.high)))

    def get_hi_thresh_lbl(self):
        return self.hi_thresh_lbl

    def set_hi_thresh_lbl(self, hi_thresh_lbl):
        self.hi_thresh_lbl = hi_thresh_lbl
        Qt.QMetaObject.invokeMethod(self._hi_thresh_lbl_label, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.hi_thresh_lbl)))

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(uhd.tune_request(self.freq, self.samp_rate/2), 0)

    def get_filter_taps(self):
        return self.filter_taps

    def set_filter_taps(self, filter_taps):
        self.filter_taps = filter_taps
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.filter_taps))

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate/self.decim)

    def get_center(self):
        return self.center

    def set_center(self, center):
        self.center = center
        Qt.QMetaObject.invokeMethod(self._center_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.center)))
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.center)

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        Qt.QMetaObject.invokeMethod(self._bb_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.bb_gain)))
        self.blocks_multiply_const_vxx_0.set_k((self.bb_gain, ))


def main(top_block_cls=adsb_uhd, options=None):

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
