# -*- coding: utf-8 -*-
# vim: autoindent shiftwidth=4 expandtab textwidth=120 tabstop=4 softtabstop=4

###############################################################################
# Bert - Bert exports recorded talks                                          #
# --------------------------------------------------------------------------- #
# Copyright (c) 2016 NikuKatansa                                              #
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
import sys, json, os, shutil
from PyQt4 import QtGui, QtCore
from bert_ui import Ui_BertWindow
from bert_addtalk import Ui_BertAddTalkDialog
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TALB, TCMP, TIT2, TPE1, error
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QMessageBox

class PlaylistItemWidget(QtGui.QWidget):
    # Based on example code found at http://stackoverflow.com/questions/25187444/pyqt-qlistwidget-custom-items

    def __init__ (self, parent = None):
        super(PlaylistItemWidget, self).__init__(parent)
        self.posterUrl = ""
        self.mp3Url = ""

        self.titleLabel = QtGui.QLabel()
        self.artistLabel = QtGui.QLabel()
        self.dateLabel = QtGui.QLabel()
        self.posterLabel = QtGui.QLabel()

        self.textLayout = QtGui.QVBoxLayout()
        self.textLayout.addWidget(self.titleLabel)
        self.textLayout.addWidget(self.artistLabel)
        self.textLayout.addWidget(self.dateLabel)

        self.itemLayout = QtGui.QHBoxLayout()
        self.itemLayout.addWidget(self.posterLabel)
        self.itemLayout.addLayout(self.textLayout,0)

        self.setLayout(self.itemLayout)

    def setTitle(self, title):
        self.titleLabel.setText(title)

    def setArtist(self, artist):
        self.artistLabel.setText(artist)

    def setDate(self, date):
        self.dateLabel.setText(date)

    def setPoster(self, posterPath):
        self.posterUrl = posterPath
        img = QtGui.QPixmap(posterPath)
        self.posterLabel.setPixmap(img.scaled(50,50, Qt.KeepAspectRatio))

    def setMp3Url(self, mp3Path):
        self.mp3Url = mp3Path

    def getJsonData(self):
        return json.dumps({'title':self.titleLabel.text(), \
            'artist':self.artistLabel.text(), \
            'mp3':self.mp3Url, \
            'date':self.dateLabel.text(), \
            'poster':self.posterUrl})

    def setData(self, title, artist, date, posterPath, mp3Path):
        self.titleLabel.setText(title)
        self.artistLabel.setText(artist)
        self.dateLabel.setText(date)
        self.posterUrl = posterPath
        img = QtGui.QPixmap(posterPath)
        self.posterLabel.setPixmap(img.scaled(50,50, Qt.KeepAspectRatio))
        self.mp3Url = mp3Path

    def getData(self):
        return [self.titleLabel.text(), self.artistLabel.text(), self.dateLabel.text(), self.posterUrl, self.mp3Url]



class BertAddTalkDialog(QtGui.QDialog, Ui_BertAddTalkDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        Ui_BertAddTalkDialog.__init__(self)
        self.setupUi(self)
        self.inputDate.setDateTime(QtCore.QDateTime.currentDateTime())
        self.posterUrl = './images/ccf.jpg'
        self.mp3Url = ''
        self.choosePosterButton.clicked.connect(self.setPosterImage)
        self.chooseMediaButton.clicked.connect(self.setMediaLocation)


    def setMediaLocation(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open MP3 file', filter="MP3 files (*.mp3)")
        # Check if filename is in ./playlists/ - if not copy to this directory
        if filename:
            head, tail = os.path.split(filename)
            if not os.path.isfile(os.path.join('./playlists/', tail)):
                shutil.copy(filename, './playlists/')
            self.mp3Url = os.path.join('./playlists/', tail)
            self.inputMedia.setText(self.mp3Url)
        return


    def setPosterImage(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open poster image', directory='./images/', filter="JPG files (*.jpg)")
        # Check if filename is in ./images/ - if not copy to this directory
        if filename:
            head, tail = os.path.split(filename)
            if not os.path.isfile(os.path.join('./images/', tail)):
                shutil.copy(filename, './images/')
            self.posterUrl = os.path.join('./images/', tail)
            img = QtGui.QPixmap(self.posterUrl)
            self.posterLabel.setPixmap(img.scaled(200, 200, Qt.KeepAspectRatio))
        return


    def setTalkData(self, iTitle, iSpeaker, iDate, iPoster, iMP3):
        self.inputTitle.setText(iTitle)
        self.inputSpeaker.lineEdit().setText(iSpeaker)
        self.inputDate.setDateTime(QtCore.QDateTime.fromString(iDate, 'dd/MM/yyyy'))
        self.posterUrl = iPoster
        img = QtGui.QPixmap(iPoster)
        self.posterLabel.setPixmap(img.scaled(200, 200, Qt.KeepAspectRatio))
        self.mp3Url = iMP3
        self.inputMedia.setText(iMP3)


    def getTalkData(self):
        return [self.inputTitle.text(), self.inputSpeaker.currentText(), self.inputDate.text(), self.posterUrl, self.mp3Url]



class BertWindow(QtGui.QMainWindow, Ui_BertWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_BertWindow.__init__(self)
        self.setupUi(self)
        self.actionNew_playlist.triggered.connect(self.newPlaylist)
        self.actionOpen_playlist.triggered.connect(self.loadPlaylist)
        self.actionSave_playlist.triggered.connect(self.savePlaylist)
        self.actionSave_playlist_as.triggered.connect(self.savePlaylistAs)
        self.actionExit.triggered.connect(self.close)
        self.actionAdd_talk.triggered.connect(self.addTalk)
        self.actionEdit_talk.triggered.connect(self.editTalk)
        self.actionMove_talk_up.triggered.connect(self.moveTalkUp)
        self.actionMove_talk_down.triggered.connect(self.moveTalkDown)
        self.moveTalkUpButton.clicked.connect(self.moveTalkUp)
        self.moveTalkDownButton.clicked.connect(self.moveTalkDown)
        self.addTalkButton.clicked.connect(self.addTalk)
        self.playlistList.itemDoubleClicked.connect(self.editTalk)
        self.saveNeeded = False
        self.saveUrl = None
        return


    def closeEvent(self, event):
        if self.saveNeeded == True:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText("Do you wish to save changes made to this playlist?")
            msg.setWindowTitle("Save changes?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            result = msg.exec_()
            if result == QMessageBox.Yes:
                if self.saveUrl == None:
                    self.savePlaylist()
                else:
                    self.savePlaylistToFile(self.saveUrl)
            elif result == QMessageBox.Cancel:
                event.ignore()
                return
        self.deleteLater()
        return


    def newPlaylist(self):
        if self.saveNeeded == True:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText("Do you wish to save changes made to this playlist?")
            msg.setWindowTitle("Save changes?")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            result = msg.exec_()
            if result == QMessageBox.Yes:
                if self.saveUrl == None:
                    self.savePlaylist()
                else:
                    self.savePlaylistToFile(self.saveUrl)
            elif result == QMessageBox.Cancel:
                return
        self.playlistList.clear()
        self.setWindowTitle("Bert - [New playlist]")
        self.saveNeeded = False
        self.saveUrl = None
        return


    def editMP3tags(self, title, artist, date, poster, mp3file):
        audio = MP3(mp3file, ID3=ID3)

        # add ID3 tag if it doesn't exist
        try:
            audio.add_tags()
        except error:
            pass

        audio.tags.delall('APIC') # picutre
        audio.tags.delall('TALB') # album title
        audio.tags.delall('TCMP') # compilation
        audio.tags.delall('TIT2') # title
        audio.tags.delall('TPE1') # performing artist
        audio.tags.add(
            APIC(
                encoding=3,
                mime='image/jpeg',
                type=3,
                desc=u'Cover',
                data=open(poster, 'rb').read()
            )
        )
        audio.tags.add(TALB(text='Crossroad Talks'))
        audio.tags.add(TCMP(text='1'))
        audio.tags.add(TIT2(text=title + ' (' + date + ')'))
        audio.tags.add(TPE1(text=artist))
        audio.save(v2_version=3)


    def addTalk(self):
        addTalkDialog = BertAddTalkDialog()
        addTalkDialog.setWindowTitle("Add talk")
        if addTalkDialog.exec_():
            result = addTalkDialog.getTalkData()
            # Deal with no media file
            if result[4].strip() == '':
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("No media file was chosen, so the talk could not be added to the playlist")
                msg.setWindowTitle("No media file chosen")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return
            # Deal with empty title field
            if result[0].strip() == '':
                result[0] = 'Crossroad talk'
            # Deal with empty speaker field
            if result[1].strip() == '':
                result[1] = 'Crossroad'

            added_item_widget = PlaylistItemWidget()
            added_item_widget.setData(result[0], result[1], result[2], result[3], result[4])
            added_item = QtGui.QListWidgetItem(self.playlistList)
            added_item.setSizeHint(added_item_widget.sizeHint())
            self.playlistList.setItemWidget(added_item, added_item_widget)
            self.playlistList.addItem(added_item)
            self.playlistList.setCurrentRow(self.playlistList.count()-1)
            self.editMP3tags(result[0], result[1], result[2], result[3], result[4])
            if self.saveNeeded == False:
                self.saveNeeded = True
                self.setWindowTitle(self.windowTitle() + " *")
        return


    def editTalk(self):
        if self.playlistList.currentRow() == -1:
            return
        editTalkDialog = BertAddTalkDialog()
        editTalkDialog.setWindowTitle("Edit talk")
        cur_row = self.playlistList.currentRow()
        cur_data = self.playlistList.itemWidget(self.playlistList.item(cur_row)).getData()
        editTalkDialog.setTalkData(cur_data[0], cur_data[1], cur_data[2], cur_data[3], cur_data[4])
        if editTalkDialog.exec_():
            result = editTalkDialog.getTalkData()
            # Deal with empty title field
            if result[0].strip() == '':
                result[0] = 'Crossroad talk'
            # Deal with empty speaker field
            if result[1].strip() == '':
                result[1] = 'Crossroad'

            edited_item_widget = PlaylistItemWidget()
            edited_item_widget.setData(result[0], result[1], result[2], result[3], result[4])
            edited_item = self.playlistList.item(cur_row)
            edited_item.setSizeHint(edited_item_widget.sizeHint())
            self.playlistList.setItemWidget(edited_item, edited_item_widget)
            # See if save is needed by comparing cur_data to result
            if self.saveNeeded == False:
                if (cur_data[0] != result[0]) or (cur_data[1] != result[1]) or (cur_data[2] != result[2]) \
                    or (cur_data[3] != result[3]) or (cur_data[4] != result[4]):
                    self.saveNeeded = True
                    self.setWindowTitle(self.windowTitle() + " *")
        return


    def moveTalkUp(self):
        if self.playlistList.selectedIndexes():
            cur_row = self.playlistList.currentRow()
            if cur_row > 0:
                cur_data = self.playlistList.itemWidget(self.playlistList.item(cur_row)).getData()
                cur_item_widget = PlaylistItemWidget()
                cur_item_widget.setData(cur_data[0], cur_data[1], cur_data[2], cur_data[3], cur_data[4])

                prev_data = self.playlistList.itemWidget(self.playlistList.item(cur_row-1)).getData()
                prev_item_widget = PlaylistItemWidget()
                prev_item_widget.setData(prev_data[0], prev_data[1], prev_data[2], prev_data[3], prev_data[4])

                cur_item = self.playlistList.item(cur_row)
                prev_item = self.playlistList.item(cur_row-1)
                self.playlistList.setItemWidget(cur_item, prev_item_widget)
                self.playlistList.setItemWidget(prev_item, cur_item_widget)
                self.playlistList.setCurrentRow(cur_row-1)
                if self.saveNeeded == False:
                    self.saveNeeded = True
                    self.setWindowTitle(self.windowTitle() + " *")


    def moveTalkDown(self):
        if self.playlistList.selectedIndexes():
            cur_row = self.playlistList.currentRow()
            if cur_row < (self.playlistList.count() - 1):
                cur_data = self.playlistList.itemWidget(self.playlistList.item(cur_row)).getData()
                cur_item_widget = PlaylistItemWidget()
                cur_item_widget.setData(cur_data[0], cur_data[1], cur_data[2], cur_data[3], cur_data[4])

                next_data = self.playlistList.itemWidget(self.playlistList.item(cur_row+1)).getData()
                next_item_widget = PlaylistItemWidget()
                next_item_widget.setData(next_data[0], next_data[1], next_data[2], next_data[3], next_data[4])

                cur_item = self.playlistList.item(cur_row)
                next_item = self.playlistList.item(cur_row+1)
                self.playlistList.setItemWidget(cur_item, next_item_widget)
                self.playlistList.setItemWidget(next_item, cur_item_widget)
                self.playlistList.setCurrentRow(cur_row+1)
                if self.saveNeeded == False:
                    self.saveNeeded = True
                    self.setWindowTitle(self.windowTitle() + " *")


    def savePlaylistAs(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save playlist', filter="JSON files (*.json)")
        if filename:
            self.savePlaylistToFile(filename)
        return


    def savePlaylist(self):
        if self.saveUrl == None:
            filename = QtGui.QFileDialog.getSaveFileName(self, 'Save playlist', filter="JSON files (*.json)")
            if filename:
                self.savePlaylistToFile(filename)
        else:
            self.savePlaylistToFile(self.saveUrl)
        return


    def savePlaylistToFile(self, playlist_url):
        json_list = []
        for i in range(self.playlistList.count()):
            cur_item = self.playlistList.item(i)
            cur_widget = self.playlistList.itemWidget(cur_item)
            json_list.append(json.loads(cur_widget.getJsonData()))
        json_content = {'podcasts':json_list}
        with open(playlist_url, 'w') as out_file:
            json.dump(json_content, out_file, indent=4)
        self.saveNeeded = False
        self.saveUrl = playlist_url
        self.setWindowTitle("Bert - " + os.path.basename(playlist_url))
        return


    def loadPlaylist(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open playlist', filter="JSON files (*.json)")
        if filename:
            self.loadPlaylistFromFile(filename)
        return


    def loadPlaylistFromFile(self, playlist_url):
        try:
            with open(playlist_url) as in_file:
                json_data = json.load(in_file)
                in_file.close()

            self.playlistList.clear()
            for json_item in json_data['podcasts']:
                playlist_item_widget = PlaylistItemWidget()
                playlist_item_widget.setData(json_item['title'], json_item['artist'], json_item['date'], json_item['poster'], json_item['mp3'])
                # Create QListWidgetItem
                playlist_item = QtGui.QListWidgetItem(self.playlistList)
                # Set size hint
                playlist_item.setSizeHint(playlist_item_widget.sizeHint())
                # Add QListWidgetItem into QListWidget
                self.playlistList.setItemWidget(playlist_item, playlist_item_widget)
                self.playlistList.addItem(playlist_item)

            self.setWindowTitle("Bert - " + os.path.basename(playlist_url))
            self.saveNeeded = False
            self.saveUrl = playlist_url

        except KeyError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("The selected playlist could not be loaded as it is incorrectly constructed.")
            msg.setWindowTitle("Malformed JSON file")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            self.playlistList.clear()
            self.setWindowTitle("Bert - [New playlist]")
        return


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = BertWindow()
    window.show()
    sys.exit(app.exec_())
