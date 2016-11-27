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
        BertWindow.resize(295, 450)
        self.centralwidget = QtGui.QWidget(BertWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.addTalkButton = QtGui.QPushButton(self.centralwidget)
        self.addTalkButton.setGeometry(QtCore.QRect(10, 10, 75, 31))
        self.addTalkButton.setObjectName(_fromUtf8("addTalkButton"))
        self.moveTalkUpButton = QtGui.QPushButton(self.centralwidget)
        self.moveTalkUpButton.setGeometry(QtCore.QRect(130, 10, 71, 31))
        self.moveTalkUpButton.setObjectName(_fromUtf8("moveTalkUpButton"))
        self.moveTalkDownButton = QtGui.QPushButton(self.centralwidget)
        self.moveTalkDownButton.setGeometry(QtCore.QRect(210, 10, 71, 31))
        self.moveTalkDownButton.setObjectName(_fromUtf8("moveTalkDownButton"))
        self.playlistList = QtGui.QListWidget(self.centralwidget)
        self.playlistList.setGeometry(QtCore.QRect(10, 50, 271, 351))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlistList.sizePolicy().hasHeightForWidth())
        self.playlistList.setSizePolicy(sizePolicy)
        self.playlistList.setObjectName(_fromUtf8("playlistList"))
        BertWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BertWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 295, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        BertWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(BertWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BertWindow.setStatusBar(self.statusbar)
        self.actionNew_playlist = QtGui.QAction(BertWindow)
        self.actionNew_playlist.setObjectName(_fromUtf8("actionNew_playlist"))
        self.actionOpen_playlist = QtGui.QAction(BertWindow)
        self.actionOpen_playlist.setObjectName(_fromUtf8("actionOpen_playlist"))
        self.actionSave_playlist = QtGui.QAction(BertWindow)
        self.actionSave_playlist.setObjectName(_fromUtf8("actionSave_playlist"))
        self.actionExit = QtGui.QAction(BertWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSave_playlist_as = QtGui.QAction(BertWindow)
        self.actionSave_playlist_as.setObjectName(_fromUtf8("actionSave_playlist_as"))
        self.actionAdd_talk = QtGui.QAction(BertWindow)
        self.actionAdd_talk.setObjectName(_fromUtf8("actionAdd_talk"))
        self.actionEdit_talk = QtGui.QAction(BertWindow)
        self.actionEdit_talk.setObjectName(_fromUtf8("actionEdit_talk"))
        self.actionMove_talk_up = QtGui.QAction(BertWindow)
        self.actionMove_talk_up.setObjectName(_fromUtf8("actionMove_talk_up"))
        self.actionMove_talk_down = QtGui.QAction(BertWindow)
        self.actionMove_talk_down.setObjectName(_fromUtf8("actionMove_talk_down"))
        self.actionUpload_playlist = QtGui.QAction(BertWindow)
        self.actionUpload_playlist.setObjectName(_fromUtf8("actionUpload_playlist"))
        self.menuFile.addAction(self.actionNew_playlist)
        self.menuFile.addAction(self.actionOpen_playlist)
        self.menuFile.addAction(self.actionSave_playlist)
        self.menuFile.addAction(self.actionSave_playlist_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionUpload_playlist)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionAdd_talk)
        self.menuEdit.addAction(self.actionEdit_talk)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionMove_talk_up)
        self.menuEdit.addAction(self.actionMove_talk_down)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(BertWindow)
        QtCore.QMetaObject.connectSlotsByName(BertWindow)

    def retranslateUi(self, BertWindow):
        BertWindow.setWindowTitle(_translate("BertWindow", "Bert - [New playlist]", None))
        self.addTalkButton.setText(_translate("BertWindow", "Add talk", None))
        self.moveTalkUpButton.setText(_translate("BertWindow", "Move up", None))
        self.moveTalkDownButton.setText(_translate("BertWindow", "Move down", None))
        self.menuFile.setTitle(_translate("BertWindow", "&File", None))
        self.menuEdit.setTitle(_translate("BertWindow", "&Edit", None))
        self.actionNew_playlist.setText(_translate("BertWindow", "&New playlist", None))
        self.actionNew_playlist.setShortcut(_translate("BertWindow", "Ctrl+N", None))
        self.actionOpen_playlist.setText(_translate("BertWindow", "&Open playlist...", None))
        self.actionOpen_playlist.setShortcut(_translate("BertWindow", "Ctrl+O", None))
        self.actionSave_playlist.setText(_translate("BertWindow", "&Save playlist...", None))
        self.actionSave_playlist.setShortcut(_translate("BertWindow", "Ctrl+S", None))
        self.actionExit.setText(_translate("BertWindow", "E&xit", None))
        self.actionSave_playlist_as.setText(_translate("BertWindow", "Save playlist &as...", None))
        self.actionAdd_talk.setText(_translate("BertWindow", "&Add talk...", None))
        self.actionAdd_talk.setShortcut(_translate("BertWindow", "Ctrl+A", None))
        self.actionEdit_talk.setText(_translate("BertWindow", "&Edit talk...", None))
        self.actionEdit_talk.setShortcut(_translate("BertWindow", "Ctrl+E", None))
        self.actionMove_talk_up.setText(_translate("BertWindow", "Move talk &up", None))
        self.actionMove_talk_up.setShortcut(_translate("BertWindow", "Ctrl+Up", None))
        self.actionMove_talk_down.setText(_translate("BertWindow", "Move talk &down", None))
        self.actionMove_talk_down.setShortcut(_translate("BertWindow", "Ctrl+Down", None))
        self.actionUpload_playlist.setText(_translate("BertWindow", "&Upload playlist", None))
        self.actionUpload_playlist.setShortcut(_translate("BertWindow", "Ctrl+U", None))

