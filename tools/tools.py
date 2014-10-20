import random


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


class RandomOrderOfWordsInSentences(object):
    ''' Randomize all words in a given sentences. '''
    def __init__(self, sentences=''):
        self.sentences = tuple(filter(len, sentences.split('.')))

    def RandomWords(self):

        self.result = ''

        for i, sentence in enumerate(self.sentences, start=1):
            self.result += '{0}) {1}.\n'.format(
                i, str.join(' ', Shuffle(
                    list(
                        filter(len, tuple(
                            filter(len, str(sentence).split(' '))
                        ))
                    )
                ))
            )

        return self.result



class RandomOrderOfSentenceInParagraph(object):
    ''''''
    def __init__(self, sentences=''):
        self.sentences = list(filter(len, str(sentences).split('.')))

    def RandomSentence(self):
        self.result = ''

        for i, sentence in enumerate(Shuffle(self.sentences), start=1):
            self.result += '{}) {}.\n'.format(i, sentence)

        return self.result
