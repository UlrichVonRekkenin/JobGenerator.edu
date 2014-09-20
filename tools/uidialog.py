# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tools/dialog_widget.ui'
#
# Created by: PyQt4 UI code generator 4.9.6
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

class Ui_TestDialog(object):
    def setupUi(self, TestDialog):
        TestDialog.setObjectName(_fromUtf8("TestDialog"))
        TestDialog.resize(850, 650)
        TestDialog.setMinimumSize(QtCore.QSize(700, 550))
        TestDialog.setMaximumSize(QtCore.QSize(850, 700))
        TestDialog.setSizeIncrement(QtCore.QSize(5, 5))
        self.spVariantNumber = QtGui.QSpinBox(TestDialog)
        self.spVariantNumber.setGeometry(QtCore.QRect(670, 40, 61, 22))
        self.spVariantNumber.setMinimum(1)
        self.spVariantNumber.setMaximum(100)
        self.spVariantNumber.setProperty("value", 12)
        self.spVariantNumber.setObjectName(_fromUtf8("spVariantNumber"))
        self.spUnderscorePart = QtGui.QDoubleSpinBox(TestDialog)
        self.spUnderscorePart.setEnabled(False)
        self.spUnderscorePart.setGeometry(QtCore.QRect(670, 70, 61, 22))
        self.spUnderscorePart.setMinimum(0.1)
        self.spUnderscorePart.setMaximum(0.9)
        self.spUnderscorePart.setSingleStep(0.05)
        self.spUnderscorePart.setProperty("value", 0.5)
        self.spUnderscorePart.setObjectName(_fromUtf8("spUnderscorePart"))
        self.mMemoIn = QtGui.QPlainTextEdit(TestDialog)
        self.mMemoIn.setGeometry(QtCore.QRect(0, 140, 365, 531))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mMemoIn.sizePolicy().hasHeightForWidth())
        self.mMemoIn.setSizePolicy(sizePolicy)
        self.mMemoIn.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.mMemoIn.setCenterOnScroll(True)
        self.mMemoIn.setObjectName(_fromUtf8("mMemoIn"))
        self.label_4 = QtGui.QLabel(TestDialog)
        self.label_4.setGeometry(QtCore.QRect(50, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.cbTestCase = QtGui.QComboBox(TestDialog)
        self.cbTestCase.setGeometry(QtCore.QRect(50, 40, 330, 22))
        self.cbTestCase.setObjectName(_fromUtf8("cbTestCase"))
        self.cbTestCase.addItem(_fromUtf8(""))
        self.cbTestCase.addItem(_fromUtf8(""))
        self.cbTestCase.addItem(_fromUtf8(""))
        self.cbTestCase.addItem(_fromUtf8(""))
        self.cbTestCase.addItem(_fromUtf8(""))
        self.cbTestCase.addItem(_fromUtf8(""))
        self.edMissedLetters = QtGui.QLineEdit(TestDialog)
        self.edMissedLetters.setEnabled(False)
        self.edMissedLetters.setGeometry(QtCore.QRect(670, 100, 61, 20))
        self.edMissedLetters.setObjectName(_fromUtf8("edMissedLetters"))
        self.label_3 = QtGui.QLabel(TestDialog)
        self.label_3.setGeometry(QtCore.QRect(410, 100, 220, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(TestDialog)
        self.label.setGeometry(QtCore.QRect(410, 40, 220, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(TestDialog)
        self.label_2.setGeometry(QtCore.QRect(410, 70, 220, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.mMemoOut = QtGui.QPlainTextEdit(TestDialog)
        self.mMemoOut.setGeometry(QtCore.QRect(360, 140, 501, 531))
        self.mMemoOut.setReadOnly(True)
        self.mMemoOut.setCenterOnScroll(True)
        self.mMemoOut.setObjectName(_fromUtf8("mMemoOut"))
        self.btnTestGenerate = QtGui.QPushButton(TestDialog)
        self.btnTestGenerate.setGeometry(QtCore.QRect(50, 90, 330, 23))
        self.btnTestGenerate.setObjectName(_fromUtf8("btnTestGenerate"))

        self.retranslateUi(TestDialog)
        QtCore.QMetaObject.connectSlotsByName(TestDialog)

    def retranslateUi(self, TestDialog):
        TestDialog.setWindowTitle(_translate("TestDialog", "Генератор заданий", None))
        self.label_4.setText(_translate("TestDialog", "Тип задания:", None))
        self.cbTestCase.setItemText(0, _translate("TestDialog", "1. Расположить буквы в словах в случайном порядке", None))
        self.cbTestCase.setItemText(1, _translate("TestDialog", "2. Заменить часть букв нижним подчеркиванием", None))
        self.cbTestCase.setItemText(2, _translate("TestDialog", "3. Пропустить определенные буквы в слове", None))
        self.cbTestCase.setItemText(3, _translate("TestDialog", "4. Сопоставить слова", None))
        self.cbTestCase.setItemText(4, _translate("TestDialog", "5. Расположить слова в предложениях в случайном порядке", None))
        self.cbTestCase.setItemText(5, _translate("TestDialog", "6. Расположить предложения в случайном порядке", None))
        self.edMissedLetters.setText(_translate("TestDialog", "aeiouy", None))
        self.label_3.setText(_translate("TestDialog", "Пропустить эти буквы:", None))
        self.label.setText(_translate("TestDialog", "Количество варинтов:", None))
        self.label_2.setText(_translate("TestDialog", "Часть пропущенных букв:", None))
        self.btnTestGenerate.setText(_translate("TestDialog", "Генерировать задания", None))

