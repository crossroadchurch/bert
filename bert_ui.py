# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bert_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BertWindow(object):
    def setupUi(self, BertWindow):
        BertWindow.setObjectName(_fromUtf8("BertWindow"))
        BertWindow.resize(276, 490)
        self.centralwidget = QtGui.QWidget(BertWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.playlistList = QtGui.QListWidget(self.centralwidget)
        self.playlistList.setGeometry(QtCore.QRect(10, 50, 251, 351))
        self.playlistList.setObjectName(_fromUtf8("playlistList"))
        self.savePlaylistButton = QtGui.QPushButton(self.centralwidget)
        self.savePlaylistButton.setGeometry(QtCore.QRect(144, 410, 121, 31))
        self.savePlaylistButton.setObjectName(_fromUtf8("savePlaylistButton"))
        self.loadPlaylistButton = QtGui.QPushButton(self.centralwidget)
        self.loadPlaylistButton.setGeometry(QtCore.QRect(10, 410, 121, 31))
        self.loadPlaylistButton.setObjectName(_fromUtf8("loadPlaylistButton"))
        self.addTalkButton = QtGui.QPushButton(self.centralwidget)
        self.addTalkButton.setGeometry(QtCore.QRect(10, 10, 75, 31))
        self.addTalkButton.setObjectName(_fromUtf8("addTalkButton"))
        self.moveTalkUpButton = QtGui.QPushButton(self.centralwidget)
        self.moveTalkUpButton.setGeometry(QtCore.QRect(110, 10, 71, 31))
        self.moveTalkUpButton.setObjectName(_fromUtf8("moveTalkUpButton"))
        self.moveTalkDownButton = QtGui.QPushButton(self.centralwidget)
        self.moveTalkDownButton.setGeometry(QtCore.QRect(190, 10, 71, 31))
        self.moveTalkDownButton.setObjectName(_fromUtf8("moveTalkDownButton"))
        BertWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BertWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 276, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        BertWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(BertWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BertWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BertWindow)
        QtCore.QMetaObject.connectSlotsByName(BertWindow)

    def retranslateUi(self, BertWindow):
        BertWindow.setWindowTitle(_translate("BertWindow", "Bert - [New playlist]", None))
        self.savePlaylistButton.setText(_translate("BertWindow", "Save playlist", None))
        self.loadPlaylistButton.setText(_translate("BertWindow", "Load playlist", None))
        self.addTalkButton.setText(_translate("BertWindow", "Add talk", None))
        self.moveTalkUpButton.setText(_translate("BertWindow", "Move up", None))
        self.moveTalkDownButton.setText(_translate("BertWindow", "Move down", None))

