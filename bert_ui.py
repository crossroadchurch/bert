# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bert.ui'
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

class Ui_BertUI(object):
    def setupUi(self, BertUI):
        BertUI.setObjectName(_fromUtf8("BertUI"))
        BertUI.resize(288, 232)
        self.centralwidget = QtGui.QWidget(BertUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.record_button = QtGui.QToolButton(self.centralwidget)
        self.record_button.setGeometry(QtCore.QRect(20, 20, 75, 41))
        self.record_button.setCheckable(True)
        self.record_button.setChecked(False)
        self.record_button.setObjectName(_fromUtf8("record_button"))
        self.gain_bg = QtGui.QFrame(self.centralwidget)
        self.gain_bg.setGeometry(QtCore.QRect(100, 20, 20, 100))
        self.gain_bg.setStyleSheet(_fromUtf8("color:rgb(255,0,0)"))
        self.gain_bg.setFrameShadow(QtGui.QFrame.Plain)
        self.gain_bg.setLineWidth(20)
        self.gain_bg.setFrameShape(QtGui.QFrame.VLine)
        self.gain_bg.setObjectName(_fromUtf8("gain_bg"))
        self.gain_fg = QtGui.QFrame(self.centralwidget)
        self.gain_fg.setGeometry(QtCore.QRect(100, 20, 20, 100))
        self.gain_fg.setStyleSheet(_fromUtf8("color:rgb(255,255,255)"))
        self.gain_fg.setFrameShadow(QtGui.QFrame.Plain)
        self.gain_fg.setLineWidth(20)
        self.gain_fg.setFrameShape(QtGui.QFrame.VLine)
        self.gain_fg.setObjectName(_fromUtf8("gain_fg"))
        self.gain_border = QtGui.QFrame(self.centralwidget)
        self.gain_border.setGeometry(QtCore.QRect(99, 19, 22, 102))
        self.gain_border.setStyleSheet(_fromUtf8("color:rgb(0,0,0)"))
        self.gain_border.setFrameShadow(QtGui.QFrame.Plain)
        self.gain_border.setLineWidth(22)
        self.gain_border.setFrameShape(QtGui.QFrame.VLine)
        self.gain_border.setObjectName(_fromUtf8("gain_border"))
        self.gain_border.raise_()
        self.record_button.raise_()
        self.gain_bg.raise_()
        self.gain_fg.raise_()
        BertUI.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(BertUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 288, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        BertUI.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(BertUI)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BertUI.setStatusBar(self.statusbar)

        self.retranslateUi(BertUI)
        QtCore.QMetaObject.connectSlotsByName(BertUI)

    def retranslateUi(self, BertUI):
        BertUI.setWindowTitle(_translate("BertUI", "Bert", None))
        self.record_button.setText(_translate("BertUI", "Record", None))

