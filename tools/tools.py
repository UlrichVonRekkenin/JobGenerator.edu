import random
import re


def Shuffle(sequence):
    ''' Return a shuffled sequence. '''
    import copy
    seqin = copy.copy(sequence)
    while (sequence == seqin):
        random.shuffle(sequence)
    return sequence


class RandomOrderOfLetters(object):
    ''' Make letters in a random order of a given word. '''
    def __init__(self, word):
        self.word = word

    def RandomLetters(self):
        return ''.join([str(x) for x in Shuffle(list(self.word))])


class ReplaceSomeLettersByUnderline(object):
    ''' Replace some letters by _ in a given word. '''
    def __init__(self, word, percent=50):
        self.word = word
        self.percent = percent
        self.lenght = len(self.word)

    def ReplaceLetters(self):
        ret = ''

        for split_word in self.word.split():
            rword = list(split_word)
            for i in random.sample(
                range(len(split_word)),
                int(len(split_word) * self.percent / 100.)
            ):
                rword[i] = " __ "
            ret += ''.join([str(x) for x in rword]) + 5 * ' '

        return ret[:-5]


class MissSpecialLetters(object):
    ''' Miss special letters in a given word. '''
    def __init__(self, word, special='aeiouy'):
        self.word = word
        self.special = special

    def MissLetters(self):
        self.rword = list(self.word)

        for i, letter in enumerate(list(self.word)):
            if letter in self.special:
                self.rword[i] = '_'

        return ' '.join([str(x) for x in self.rword])


class MatchCoupleOfWords(object):
    '''M...'''
    def __init__(self, lines='foo : bar'):
        self.col1, self.col2 = [], []

        for line in tuple(filter(len, lines.split('\n'))):
            self.col1.append(str(line.split(':')[0]))
            self.col2.append(str(line.split(':')[1]))

    def Matching(self):
        if len(self.col1) > 1 or len(self.col2) > 1:
            Shuffle(self.col1)
            Shuffle(self.col2)

            self.result = ''

            for i in range(len(self.col1)):
                self.result += '{0}) {1}\t\t{0}) {2}\n'.format(
                    i + 1, self.col1[i].strip(), self.col2[i].strip()
                )

            return self.result
        else:
            return 'There is no way to shuffle. Please, add more pairs.'


class SuperParagraph(object):
    def __init__(self, sentences=''):
        self.container = list(zip(
            filter(len, re.split(r'[\.\!\?]', sentences)),
            re.findall(r'[\.\!\?]', sentences)
        ))


class RandomOrderOfWordsInSentences(SuperParagraph):
    ''' Randomize all words in a given sentences. '''
    def __init__(self, sentences=''):
        SuperParagraph.__init__(self, sentences)

    def RandomWords(self):
        result = ''

        for i, sent in enumerate(self.container, start=1):
            result += '{}) {}{}\n'.format(
                i,
                ' '.join(
                    [w.lower() for w in Shuffle(list(re.split('\W+', sent[0])))]
                ),
                sent[1]
            )

        return result


class RandomOrderOfSentenceInParagraph(SuperParagraph):
    ''''''
    def __init__(self, sentences=''):
        SuperParagraph.__init__(self, sentences)

    def RandomSentence(self):
        result = ''

        for i, sentence in enumerate(Shuffle(self.container), start=1):
            result += '{}) {}{}\n'.format(i, *sentence)

        return result


class RegExWrapper(object):
    def __init__(self, sentences=''):
        self.sentences = sentences

    def RandomSentence(self):
        ret = ''
        for i, s in enumerate(
            list(filter(len, self.sentences.split('\n'))),
            start=1
        ):
            ret += '{}) {}\n'.format(i, RegExTasker(s).do())

        return ret


class RegExTasker(object):
    def __init__(self, sentence='', flag='"', separator='/'):
        self.sentence = sentence
        self.separator = separator
        self.matches = [
            m.group() for m in
            re.compile(r'{0}.*?{0}'.format(flag)).finditer(self.sentence)
        ]

    def do(self):
        s = self.sentence

        for match in self.matches:

            word = random.choice(match[1:-1].split(self.separator))

            if word.startswith('to ') or word.startswith('not to '):
                s = s.replace(match, 20 * '_' + ' ({})'.format(word))
            else:
                s = s.replace(match, '{}'.format(word))

        return s


class OmittedWords(object):
    def __init__(self, paragraph='', words=''):
        self.paragraph = paragraph
        self.words = [word.strip() for word in words.split(',')]

    def OmitWords(self):
        for word in self.words:
            self.paragraph = re.sub(
                word,
                15*'_',
                self.paragraph,
                flags=re.IGNORECASE
            )

        return self.paragraph
