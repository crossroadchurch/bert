# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bert_upload.ui'
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

class Ui_BertUpload(object):
    def setupUi(self, BertUpload):
        BertUpload.setObjectName(_fromUtf8("BertUpload"))
        BertUpload.setWindowModality(QtCore.Qt.ApplicationModal)
        BertUpload.resize(321, 348)
        self.fileProgressBar = QtGui.QProgressBar(BertUpload)
        self.fileProgressBar.setGeometry(QtCore.QRect(20, 100, 281, 23))
        self.fileProgressBar.setProperty("value", 24)
        self.fileProgressBar.setTextVisible(False)
        self.fileProgressBar.setObjectName(_fromUtf8("fileProgressBar"))
        self.jobProgressBar = QtGui.QProgressBar(BertUpload)
        self.jobProgressBar.setGeometry(QtCore.QRect(20, 40, 281, 23))
        self.jobProgressBar.setProperty("value", 24)
        self.jobProgressBar.setTextVisible(False)
        self.jobProgressBar.setObjectName(_fromUtf8("jobProgressBar"))
        self.label = QtGui.QLabel(BertUpload)
        self.label.setGeometry(QtCore.QRect(20, 10, 101, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(BertUpload)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 111, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(BertUpload)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.progressText = QtGui.QTextEdit(BertUpload)
        self.progressText.setGeometry(QtCore.QRect(20, 160, 281, 131))
        self.progressText.setReadOnly(True)
        self.progressText.setObjectName(_fromUtf8("progressText"))
        self.closeButton = QtGui.QPushButton(BertUpload)
        self.closeButton.setEnabled(False)
        self.closeButton.setGeometry(QtCore.QRect(210, 300, 91, 31))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))

        self.retranslateUi(BertUpload)
        QtCore.QMetaObject.connectSlotsByName(BertUpload)

    def retranslateUi(self, BertUpload):
        BertUpload.setWindowTitle(_translate("BertUpload", "Upload progress", None))
        self.label.setText(_translate("BertUpload", "Overall progress:", None))
        self.label_2.setText(_translate("BertUpload", "Current file progress:", None))
        self.label_3.setText(_translate("BertUpload", "Details:", None))
        self.progressText.setHtml(_translate("BertUpload", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.closeButton.setText(_translate("BertUpload", "Close", None))

