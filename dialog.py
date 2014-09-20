﻿#!python3


from PyQt4.QtGui import QDialog, QApplication
from PyQt4.QtCore import SIGNAL, QThread
from os.path import isfile, getsize
import sys

from tools import tools
from tools.uidialog import Ui_TestDialog


#-----------------------------------------------
class TestDialog( QDialog ):
    #-----------------------------------------------
    def __init__( self, parent = None ):
        QDialog.__init__(self)

        self.ui = Ui_TestDialog()
        self.ui.setupUi(self)

        self.TestCase = 0
        self.JSONFile = 'dialog.json'

        self.sTestCase = ['Place the letters on correct order.',
                          'Insert the correct letters.',
                          '',
                          'Match the words.',
                          'Place the words in sentences on correct order.',
                          'Place the sentences on correct order.',
                         ]

        #
        self.ui.btnTestGenerate.clicked.connect(self.TestGenerate)

        #
        self.connect(self.ui.cbTestCase, SIGNAL("activated(int)"), self.UpdateUiByTestCase)

        #
        self.connect(self.ui.edMissedLetters, SIGNAL("textChanged(QString)"), self.UpdateMissedLetters)

        #
#        self.connect(self.ui.mMemoIn, SIGNAL("textChanged()"), self.TestGenerate)

        #
        self.LoadDialogFromPickle()


    #-----------------------------------------------
    def TestGenerate( self ):

        if len(self.ui.mMemoIn.toPlainText()):
            self.ui.mMemoOut.clear()

            for var in range(self.ui.spVariantNumber.value()):
                foo = ''

                if self.TestCase in [0, 1, 2]:

                        results, words = [], tuple(filter(len, self.ui.mMemoIn.toPlainText().split('\n')))

                        if self.TestCase == 0:
                            for word in words:
                                results.append(tools.RandomOrderOfLetters(word).RandomLetters())

                        elif self.TestCase == 1:
                            for word in words:
                                results.append(tools.ReplaceSomeLettersByUnderline(word).ReplaceLetters())

                        elif self.TestCase == 2:
                            for word in words:
                                results.append(tools.MissSpecialLetters(word, self.ui.edMissedLetters.text()).MissLetters())


                        for i, result in enumerate(results, start = 1):
                            foo += '{0}) {1}\n'.format(i, result)


                elif self.TestCase == 3:
                    foo = tools.MatchCoupleOfWords(self.ui.mMemoIn.toPlainText()).Matching()

                elif self.TestCase == 4:
                    foo = tools.RandomOrderOfWordsInSentences(self.ui.mMemoIn.toPlainText()).RandomWords()

                elif self.TestCase == 5:
                    foo = tools.RandomOrderOfSentenceInParagraph(self.ui.mMemoIn.toPlainText()).RandomSentence()

                self.ui.mMemoOut.insertPlainText('Variant #{0}\n{1}\nNAME:\nCLASS:\n{2}\n'.format(var+1, self.sTestCase[self.TestCase], foo))

    #-----------------------------------------------
    def UpdateUiByTestCase( self ):
       self.TestCase = self.ui.cbTestCase.currentIndex()

       if self.TestCase in [0, 3, 4]:
           self.ui.edMissedLetters.setEnabled(False)
           self.ui.spUnderscorePart.setEnabled(False)
       elif self.TestCase == 1:
           self.ui.edMissedLetters.setEnabled(False)
           self.ui.spUnderscorePart.setEnabled(True)
       elif self.TestCase == 2:
           self.ui.edMissedLetters.setEnabled(True)
           self.ui.spUnderscorePart.setEnabled(False)


    #-----------------------------------------------
    def UpdateMissedLetters( self ):
        self.sTestCase[2] = 'Insert correct letters {}'.format(set(self.ui.edMissedLetters.text()))


    #-----------------------------------------------
    def closeEvent( self, event ):
        ''' Event::closeEvent = When app is closed save the state. '''
        import json

        with open(self.JSONFile, 'w') as output:

            d = dict()

            d['MemoIn'] = self.ui.mMemoIn.toPlainText()
            d['MemoOut'] = self.ui.mMemoOut.toPlainText()
            d['Variant'] = self.ui.spVariantNumber.text()
            d['Missed'] = self.ui.edMissedLetters.text()
            d['Underscore'] = self.ui.spUnderscorePart.text()
            d['TestCase'] = self.ui.cbTestCase.currentIndex()

            json.dump(d, output)


    #-----------------------------------------------
    def LoadDialogFromPickle( self ):
        import json

        if isfile(self.JSONFile) and getsize(self.JSONFile):
            d = json.load( open(self.JSONFile, 'r') )

            self.ui.mMemoIn.clear()
            self.ui.mMemoIn.insertPlainText(d['MemoIn'])
            self.ui.mMemoOut.clear()
            self.ui.mMemoOut.insertPlainText(d['MemoOut'])
            self.ui.spVariantNumber.setProperty('value', d['Variant'])
            self.ui.edMissedLetters.setText(d['Missed'])
            self.ui.spUnderscorePart.setProperty('value', d['Underscore'])
            self.ui.cbTestCase.setCurrentIndex(d['TestCase'])
            self.TestCase = d['TestCase']


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = TestDialog()
    window.show()

    sys.exit(app.exec_())

