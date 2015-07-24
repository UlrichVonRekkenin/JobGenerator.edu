import json
import os
import sys
import webbrowser
from tools import githubapi, tools

from PyQt4 import QtCore, uic
from PyQt4.QtCore import SIGNAL, Qt
from PyQt4.QtGui import QApplication, QDialog, QHBoxLayout, QLabel, QPushButton


def checkForUpdates(parent=None, params=None):

    class NewVersion(QDialog):

        def __init__(self, parent=None, answer=None):
            def browser():
                webbrowser.open(answer[3], new=2)
                self.close()

            QDialog.__init__(self)

            self.setWindowTitle('New version')

            self.btnOk = QPushButton('Ok', self)
            self.btnCancel = QPushButton('Cancel', self)
            self.label = QLabel(
                'The new version {tag} is available.\nClick "Ok" to download it.\n"Cancel" to exit.'.format(
                    tag=answer[1]
                ),
                self
            )

            self.hbox = QHBoxLayout()
            self.hbox.addWidget(self.label)
            self.hbox.addWidget(self.btnOk)
            self.hbox.addWidget(self.btnCancel)
            self.setLayout(self.hbox)

            self.setGeometry(50, 50, 200, 150)

            self.btnOk.clicked.connect(browser)
            self.btnCancel.clicked.connect(lambda: self.close())

    answer = githubapi.GitHubReleases(*params).downloadStableRelease()

    if answer[0]:

        new = NewVersion(parent, answer)
        new.exec_()


class HelpDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self)
        uic.loadUi('tools/help_widget.ui', self)


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
            'Write the correct form of the verbs in bracket.',
            ''
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

                elif self.TestCase == 7:
                    self.mMemoOut.insertPlainText(
                        'NAME:\nCLASS:\n{}\n\n{}'.format(
                            'Insert correct words: ' +
                            ', '.join(self.edOmittedWords.text().split(',')),
                            tools.OmittedWords(
                                self.mMemoIn.toPlainText(),
                                self.edOmittedWords.text()
                            ).OmitWords()
                        )
                    )
                    break

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
            self.edOmittedWords.setEnabled(False)

        elif self.TestCase == 1:
            self.spUnderscorePart.setEnabled(True)
            self.edMissedLetters.setEnabled(False)
            self.edOmittedWords.setEnabled(False)

        elif self.TestCase == 2:
            self.edMissedLetters.setEnabled(True)
            self.edOmittedWords.setEnabled(False)
            self.spUnderscorePart.setEnabled(False)

        elif self.TestCase == 7:
            self.edOmittedWords.setEnabled(True)
            self.edMissedLetters.setEnabled(False)
            self.spUnderscorePart.setEnabled(False)

    def UpdateMissedLetters(self):
        self.sTestCase[2] = 'Insert correct letters: "{}"'.format(
            ', '.join(
                [str(x) for x in self.edMissedLetters.text()]
            )
        )

    def showEvent(self, event):
        if os.path.isfile(self.JSONFile) and os.path.getsize(self.JSONFile):
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
            self.edOmittedWords.setText(d['OmittedWords'])

            self.setGeometry(*d['Geo'])

        self.UpdateUiByTestCase()

    def closeEvent(self, event):
        ''' Event::closeEvent = When app is closed save the state. '''

        with open(self.JSONFile, 'w') as output:
            json.dump(
                {
                    'MemoIn': str(self.mMemoIn.toPlainText()),
                    'MemoOut': str(self.mMemoOut.toPlainText()),
                    'Variant': int(self.spVariantNumber.text()),
                    'Missed': str(self.edMissedLetters.text()),
                    'Underscore': str(self.spUnderscorePart.text()),
                    'TestCase': int(self.cbTestCase.currentIndex()),
                    'OmittedWords': self.edOmittedWords.text(),
                    'Geo': self.geometry().getRect()
                },
                output
            )

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F1:
            help = HelpDialog(self)
            help.exec_()

        elif event.key() == QtCore.Qt.Key_Escape:
            self.close()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = TestDialog()
    checkForUpdates(window, ('UlrichVonRekkenin', 'JobGenerator.edu', '1.0.0'))
    window.show()

    sys.exit(app.exec_())
