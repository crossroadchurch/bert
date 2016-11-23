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
import sys, json, os
from PyQt4 import QtGui, QtCore
from bert_ui import Ui_BertWindow
from PyQt4.QtCore import Qt

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


class BertWindow(QtGui.QMainWindow, Ui_BertWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_BertWindow.__init__(self)
        self.setupUi(self)
        self.savePlaylistButton.clicked.connect(self.savePlaylist)
        self.loadPlaylistButton.clicked.connect(self.loadPlaylist)
        self.moveTalkUpButton.clicked.connect(self.moveTalkUp)
        self.moveTalkDownButton.clicked.connect(self.moveTalkDown)


    def closeEvent(self, event):
        self.deleteLater()
        return

    def moveTalkUp(self):
        if self.playlistList.selectedIndexes():
            cur_row = self.playlistList.currentRow()
            if cur_row > 0:

                cur_data = self.playlistList.itemWidget(self.playlistList.item(cur_row)).getData()
                cur_item_widget = PlaylistItemWidget()
                cur_item_widget.setData(cur_data[0], cur_data[1], cur_data[2], cur_data[3], cur_data[4])
                # Create QListWidgetItem
                cur_item = QtGui.QListWidgetItem(self.playlistList)
                cur_item.setSizeHint(cur_item_widget.sizeHint())

                prev_data = self.playlistList.itemWidget(self.playlistList.item(cur_row-1)).getData()
                prev_item_widget = PlaylistItemWidget()
                prev_item_widget.setData(prev_data[0], prev_data[1], prev_data[2], prev_data[3], prev_data[4])
                # Create QListWidgetItem
                prev_item = QtGui.QListWidgetItem(self.playlistList)
                prev_item.setSizeHint(prev_item_widget.sizeHint())

                self.playlistList.takeItem(cur_row)
                self.playlistList.takeItem(cur_row-1)
                self.playlistList.setItemWidget(cur_item, cur_item_widget)
                self.playlistList.setItemWidget(prev_item, prev_item_widget)
                self.playlistList.insertItem(cur_row, prev_item)
                self.playlistList.insertItem(cur_row-1, cur_item)


    def moveTalkDown(self):
        if self.playlistList.selectedIndexes():
            cur_row = self.playlistList.currentRow()
            if cur_row < (self.playlistList.count() - 1):
                self.playlistList.setCurrentRow(cur_row + 1)
                self.moveTalkUp()
                self.playlistList.setCurrentRow(cur_row + 1)


    def savePlaylist(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save playlist', filter="JSON files (*.json)")
        if filename:
            self.savePlaylistToFile(filename)
            print("Playlist saved")

    def savePlaylistToFile(self, playlist_url):
        json_list = []
        for i in range(self.playlistList.count()):
            cur_item = self.playlistList.item(i)
            cur_widget = self.playlistList.itemWidget(cur_item)
            json_list.append(json.loads(cur_widget.getJsonData()))
        json_content = {'podcasts':json_list}
        with open(playlist_url, 'w') as out_file:
            json.dump(json_content, out_file, indent=4)
        return

    def loadPlaylist(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open playlist', filter="JSON files (*.json)")
        self.loadPlaylistFromFile(filename)
        return

    def loadPlaylistFromFile(self, playlist_url):
        # TODO: Catch malformed JSON files

        with open(playlist_url) as in_file:
            json_data = json.load(in_file)
            in_file.close()

        self.playlistList.clear()
        for json_item in json_data['podcasts']:
            print(json_item['title'])
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
        return

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = BertWindow()
    window.show()
    sys.exit(app.exec_())
