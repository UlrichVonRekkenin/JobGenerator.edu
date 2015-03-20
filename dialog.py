import sys

from PyQt4 import uic
from PyQt4.QtGui import QDialog, QApplication
from PyQt4.QtCore import SIGNAL
from os.path import isfile, getsize

from tools import tools


class TestDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        uic.loadUi('tools/dialog_widget.ui', self)

        self.TestCase = 0
        self.JSONFile = 'dialog.json'

        self.sTestCase = [
            'Place the letters on correct order.',
            'Insert the correct letters.',
            '',
            'Match the words.',
            'Place the words in sentences on correct order.',
            'Place the sentences on correct order.',
            'Write the correct form of the verbs in bracket.'
        ]

        self.btnTestGenerate.clicked.connect(self.TestGenerate)

        self.connect(
            self.cbTestCase,
            SIGNAL("activated(int)"),
            self.UpdateUiByTestCase
        )

        self.connect(
            self.edMissedLetters,
            SIGNAL("textChanged(QString)"),
            self.UpdateMissedLetters
        )

        self.LoadDialogFromPickle()

    def TestGenerate(self):

        if len(self.mMemoIn.toPlainText()):
            self.mMemoOut.clear()

            for var in range(self.spVariantNumber.value()):
                foo = ''

                if self.TestCase in [0, 1, 2]:

                    results = []
                    words = tools.Shuffle(
                        list(
                            filter(
                                len,
                                self.mMemoIn.toPlainText().split('\n')
                            )
                        )
                    )

                    if self.TestCase == 0:
                        for word in words:
                            results.append(tools.RandomOrderOfLetters(word).RandomLetters())

                    elif self.TestCase == 1:
                        for word in words:
                            results.append(
                                tools.ReplaceSomeLettersByUnderline(
                                    word,
                                    int(self.spUnderscorePart.text())
                                ).ReplaceLetters()
                            )

                    elif self.TestCase == 2:
                        for word in words:
                            results.append(
                                tools.MissSpecialLetters(
                                    word, self.edMissedLetters.text()
                                ).MissLetters()
                            )

                    foo = '\n'.join('{}) {}'.format(*r) for r in enumerate(results, start=1))

                elif self.TestCase == 3:
                    foo = tools.MatchCoupleOfWords(
                        self.mMemoIn.toPlainText()
                    ).Matching()

                elif self.TestCase == 4:
                    foo = tools.RandomOrderOfWordsInSentences(
                        self.mMemoIn.toPlainText()
                    ).RandomWords()

                elif self.TestCase == 5:
                    foo = tools.RandomOrderOfSentenceInParagraph(
                        self.mMemoIn.toPlainText()
                    ).RandomSentence()

                elif self.TestCase == 6:
                    foo = tools.RegExWrapper(
                        self.mMemoIn.toPlainText()
                    ).RandomSentence()

                self.mMemoOut.insertPlainText(
                    'Variant #{0}\n{1}\nNAME:\nCLASS:\n{2}\n\n'.format(
                        var + 1, self.sTestCase[self.TestCase], foo
                    )
                )

    def UpdateUiByTestCase(self):
        self.TestCase = self.cbTestCase.currentIndex()

        if self.TestCase in [0, 3, 4, 5, 6]:
            self.edMissedLetters.setEnabled(False)
            self.spUnderscorePart.setEnabled(False)
        elif self.TestCase == 1:
            self.edMissedLetters.setEnabled(False)
            self.spUnderscorePart.setEnabled(True)
        elif self.TestCase == 2:
            self.edMissedLetters.setEnabled(True)
            self.spUnderscorePart.setEnabled(False)

    def UpdateMissedLetters(self):
        self.sTestCase[2] = 'Insert correct letters: "{}"'.format(
            str.join(
                ',',
                [str(x) for x in self.edMissedLetters.text()]
            )
        )

    def closeEvent(self, event):
        ''' Event::closeEvent = When app is closed save the state. '''
        import json

        with open(self.JSONFile, 'w') as output:
            json.dump({
                'MemoIn': str(self.mMemoIn.toPlainText()),
                'MemoOut': str(self.mMemoOut.toPlainText()),
                'Variant': int(self.spVariantNumber.text()),
                'Missed': str(self.edMissedLetters.text()),
                'Underscore': str(self.spUnderscorePart.text()),
                'TestCase': int(self.cbTestCase.currentIndex())},
                output
            )

    def LoadDialogFromPickle(self):
        import json

        if isfile(self.JSONFile) and getsize(self.JSONFile):
            d = json.load(open(self.JSONFile, 'r'))

            self.mMemoIn.clear()
            self.mMemoIn.insertPlainText(d['MemoIn'])
            self.mMemoOut.clear()
            self.mMemoOut.insertPlainText(d['MemoOut'])
            self.spVariantNumber.setProperty('value', d['Variant'])
            self.edMissedLetters.setText(d['Missed'])
            self.spUnderscorePart.setProperty('value', d['Underscore'])
            self.cbTestCase.setCurrentIndex(d['TestCase'])
            self.TestCase = d['TestCase']

        self.UpdateUiByTestCase()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = TestDialog()
    window.show()

    sys.exit(app.exec_())
