# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=120 tabstop=4 softtabstop=4

###############################################################################
# Bert - Bert easily records talks                                            #
# --------------------------------------------------------------------------- #
# Copyright (c) 2015 NikuKatansa                                              #
# --------------------------------------------------------------------------- #
# This program is free software; you can redistribute it and/or modify it     #
# under the terms of the GNU General Public License as published by the Free  #
# Software Foundation; version 2 of the License.                              #
#                                                                             #
# This program is distributed in the hope that it will be useful, but WITHOUT #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or       #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for    #
# more details.                                                               #
#                                                                             #
# You should have received a copy of the GNU General Public License along     #
# with this program; if not, write to the Free Software Foundation, Inc., 59  #
# Temple Place, Suite 330, Boston, MA 02111-1307 USA                          #
###############################################################################

from PyQt4 import QtGui, QtCore
import pyaudio, pysoundcard, numpy, wave, time, sys
from datetime import timedelta
from pysoundcard import Stream, continue_flag
from soundfile import SoundFile
from bert_ui import Ui_BertUI

class BertWindow(QtGui.QMainWindow, Ui_BertUI):

    BLOCK_SIZE = 4410 # 10 blocks = 1 second
    SAMPLE_RATE = 44100
    CHANNELS = 1

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_BertUI.__init__(self)
        self.setupUi(self)
        self.rec_state = False
        self.preview_state = False
        self.tick_count = 0

        # Report audio input devices
        p = pyaudio.PyAudio()
        info = p.get_host_api_info_by_index(0)
        numdevices = info.get('deviceCount')
        for i in range (0,numdevices):
            if p.get_device_info_by_host_api_device_index(0,i).get('maxInputChannels')>0:
                print("Input Device id " + str(i) + " - " + p.get_device_info_by_host_api_device_index(0,i).get('name'))
        devinfo = p.get_device_info_by_index(1)
        print("Selected device is " + devinfo.get('name'))
        p.terminate()

        # Setup input stream and callback
        def callback(in_data, out_data, time_info, status):
            if self.rec_state==True:
                self.myfile.write(in_data)
                #self.tick_count += 1
                #if self.tick_count % 20 == 0:
                #    self.time_recorded_label.setText(time.strftime("%H:%M:%S", time.gmtime(self.tick_count / 20)))
            self.gain_fg.resize(20,100 - (100*numpy.amax(in_data)))
            return continue_flag

        self.stream = Stream(samplerate=self.SAMPLE_RATE, blocksize=self.BLOCK_SIZE, channels=self.CHANNELS, callback=callback)

        def on_preview_button_clicked(state):
            if state==True:
                # Start preview mode
                self.preview_state = True
                if self.rec_state==False:
                    self.stream.start() # otherwise stream already started
            else:
                # Stop preview mode.  Only stop stream if not recording
                self.preview_state = False
                if self.rec_state==False:
                    self.stream.stop()
                    self.gain_fg.resize(20,100) # Clear gain meter


        def on_start_button_clicked(state):
            if state==True:
                # Start recording to file
                self.gain_bg.setStyleSheet("color:rgb(255,0,0)")
                self.myfile = SoundFile('output/' + time.strftime("%Y-%m-%d %H_%M_%S") + '.wav', 'w', 44100, 1)
                self.rec_state = True
                self.tick_count = 0
                self.time_recorded_label.setText("00:00:00")
                self.stream.start()
            else:
                # Stop recording to file.  Keep stream active if preview_state is True
                self.gain_bg.setStyleSheet("color:rgb(255,127,0)")
                self.rec_state = False
                self.myfile.close()
                if self.preview_state==False:
                    self.stream.stop()
                    self.gain_fg.resize(20,100) # Clear gain meter


        QtCore.QObject.connect(self.preview_button, QtCore.SIGNAL ('clicked(bool)'), on_preview_button_clicked)
        QtCore.QObject.connect(self.start_button, QtCore.SIGNAL ('clicked(bool)'), on_start_button_clicked)


    def closeEvent(self, event):
        if self.rec_state == True:
            self.stream.stop()
            self.myfile.close()
        event.accept() # let the window close

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = BertWindow()
    window.show()
    sys.exit(app.exec_())
