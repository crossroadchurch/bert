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
import pyaudio, pysoundcard, wave, time, sys
from pysoundcard import Stream, continue_flag
from soundfile import SoundFile
from bert_ui import Ui_BertUI

class BertWindow(QtGui.QMainWindow, Ui_BertUI):

    QTR_BLOCK_SIZE = 256
    QB1 = QTR_BLOCK_SIZE
    QB2 = 2 * QTR_BLOCK_SIZE
    QB3 = 3 * QTR_BLOCK_SIZE

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_BertUI.__init__(self)
        self.setupUi(self)
        self.rec_state = False

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
            self.myfile.write(in_data)
            gain_avg = (abs(in_data[0]) + abs(in_data[self.QB1]) + abs(in_data[self.QB2]) + abs(in_data[self.QB3])) / 4
            self.gain_fg.resize(20,100 - int(100*gain_avg))
            return continue_flag

        self.stream = Stream(samplerate=44100, blocksize=4*self.QTR_BLOCK_SIZE, channels=1, callback=callback)

        def on_record_button_clicked(state):
            if state==True:
                self.myfile = SoundFile('output/' + time.strftime("%Y-%m-%d %H_%M_%S") + '.wav', 'w', 44100, 1)
                self.rec_state = True
                self.stream.start()
            else:
                self.stream.stop()
                self.myfile.close()
                self.gain_fg.resize(20,100) # Clear gain meter
                self.rec_state = False

        QtCore.QObject.connect(self.record_button, QtCore.SIGNAL ('clicked(bool)'), on_record_button_clicked)

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
