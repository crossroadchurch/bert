# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bert_addtalk.ui'
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

class Ui_BertAddTalkDialog(object):
    def setupUi(self, BertAddTalkDialog):
        BertAddTalkDialog.setObjectName(_fromUtf8("BertAddTalkDialog"))
        BertAddTalkDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        BertAddTalkDialog.resize(580, 268)
        BertAddTalkDialog.setAutoFillBackground(False)
        self.buttonBox = QtGui.QDialogButtonBox(BertAddTalkDialog)
        self.buttonBox.setGeometry(QtCore.QRect(220, 220, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.posterLabel = QtGui.QLabel(BertAddTalkDialog)
        self.posterLabel.setGeometry(QtCore.QRect(11, 12, 200, 200))
        self.posterLabel.setMaximumSize(QtCore.QSize(200, 200))
        self.posterLabel.setText(_fromUtf8(""))
        self.posterLabel.setPixmap(QtGui.QPixmap(_fromUtf8("images/ccf.jpg")))
        self.posterLabel.setScaledContents(True)
        self.posterLabel.setObjectName(_fromUtf8("posterLabel"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(BertAddTalkDialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(248, 11, 312, 202))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelMedia = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.labelMedia.setObjectName(_fromUtf8("labelMedia"))
        self.verticalLayout_3.addWidget(self.labelMedia)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.inputMedia = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.inputMedia.setReadOnly(True)
        self.inputMedia.setObjectName(_fromUtf8("inputMedia"))
        self.horizontalLayout_2.addWidget(self.inputMedia)
        self.chooseMediaButton = QtGui.QToolButton(self.verticalLayoutWidget_2)
        self.chooseMediaButton.setObjectName(_fromUtf8("chooseMediaButton"))
        self.horizontalLayout_2.addWidget(self.chooseMediaButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.labelTitle = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.labelTitle.setObjectName(_fromUtf8("labelTitle"))
        self.verticalLayout_3.addWidget(self.labelTitle)
        self.inputTitle = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.inputTitle.setObjectName(_fromUtf8("inputTitle"))
        self.verticalLayout_3.addWidget(self.inputTitle)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.labelSpeaker = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.labelSpeaker.setObjectName(_fromUtf8("labelSpeaker"))
        self.verticalLayout_3.addWidget(self.labelSpeaker)
        self.inputSpeaker = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.inputSpeaker.setEditable(True)
        self.inputSpeaker.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.inputSpeaker.setObjectName(_fromUtf8("inputSpeaker"))
        self.inputSpeaker.addItem(_fromUtf8(""))
        self.inputSpeaker.addItem(_fromUtf8(""))
        self.inputSpeaker.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.inputSpeaker)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.labelDate = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.labelDate.setObjectName(_fromUtf8("labelDate"))
        self.verticalLayout_3.addWidget(self.labelDate)
        self.inputDate = QtGui.QDateEdit(self.verticalLayoutWidget_2)
        self.inputDate.setCalendarPopup(True)
        self.inputDate.setObjectName(_fromUtf8("inputDate"))
        self.verticalLayout_3.addWidget(self.inputDate)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.choosePosterButton = QtGui.QToolButton(BertAddTalkDialog)
        self.choosePosterButton.setGeometry(QtCore.QRect(180, 190, 25, 19))
        self.choosePosterButton.setObjectName(_fromUtf8("choosePosterButton"))

        self.retranslateUi(BertAddTalkDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), BertAddTalkDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), BertAddTalkDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(BertAddTalkDialog)

    def retranslateUi(self, BertAddTalkDialog):
        BertAddTalkDialog.setWindowTitle(_translate("BertAddTalkDialog", "Add talk", None))
        self.labelMedia.setText(_translate("BertAddTalkDialog", "Media location", None))
        self.chooseMediaButton.setText(_translate("BertAddTalkDialog", "...", None))
        self.labelTitle.setText(_translate("BertAddTalkDialog", "Talk title:", None))
        self.labelSpeaker.setText(_translate("BertAddTalkDialog", "Speaker:", None))
        self.inputSpeaker.setItemText(0, _translate("BertAddTalkDialog", "Jon Sibley", None))
        self.inputSpeaker.setItemText(1, _translate("BertAddTalkDialog", "Robert Spiller", None))
        self.inputSpeaker.setItemText(2, _translate("BertAddTalkDialog", "Louise Sibley", None))
        self.labelDate.setText(_translate("BertAddTalkDialog", "Date:", None))
        self.choosePosterButton.setText(_translate("BertAddTalkDialog", "...", None))
