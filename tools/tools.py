import random

#-----------------------------------------------
def Shuffle( sequence ):
    ''' Return a shuffled sequence. '''
    import copy
    seqin = copy.copy(sequence)
    while (sequence == seqin): random.shuffle(sequence)
    return sequence


#-----------------------------------------------
class RandomOrderOfLetters( object ):
    ''' Make letters in a random order of a given word. '''
    #-----------------------------------------------
    def __init__( self, word ):
        self.word = word
        self.lenght = len(self.word)

    #-----------------------------------------------
    def RandomLetters( self ):
        return str.join('', Shuffle(list(self.word)))


#-----------------------------------------------
class ReplaceSomeLettersByUnderline( object ):
    ''' Replace some letters by _ in a given word. '''
    #-----------------------------------------------
    def __init__( self, word, percent = 50 ):
        self.word = word
        self.percent = percent
        self.lenght = len(self.word)

    #-----------------------------------------------
    def ReplaceLetters( self ):
        self.rword = list(self.word)

        for i in random.sample( range(self.lenght), int(self.lenght * self.percent / 100.0) ):
            self.rword[i] = "_"
        return str.join(' ', self.rword)


#-----------------------------------------------
class MissSpecialLetters( object ):
    ''' Miss special letters in a given word. '''
    #-----------------------------------------------
    def __init__( self, word, special = 'aeiouy' ):
        self.word = word
        self.special = special

    #-----------------------------------------------
    def MissLetters( self ):
        self.rword = list(self.word)

        for i, letter in enumerate(list(self.word)):
            if letter in self.special:
                self.rword[i] = '_'

        return str.join(' ', self.rword)


#-----------------------------------------------
class MatchCoupleOfWords( object ):
    '''M...'''
    #-----------------------------------------------
    def __init__( self, lines = 'foo : bar' ):
        self.col1, self.col2 = [], []

        for line in tuple(filter(len, lines.split('\n'))):
            self.col1.append(line.split(':')[0])
            self.col2.append(line.split(':')[1])

            print(self.col1, self.col2)

    #-----------------------------------------------
    def Matching( self ):
        if len(self.col1) > 1 or len(self.col2) > 1:
            Shuffle(self.col1)
            Shuffle(self.col2)

            self.result = ''

            for i in range(len(self.col1)):
                self.result += '{0}) {1}\t\t\t{0}) {2}\n'.format(i+1, self.col1[i].strip(), self.col2[i].strip())

            return self.result
        else:
            return 'There is no way to shuffle. Please, add more pairs.'


###----------------------------------------------
class RandomOrderOfSentenceInParagraph( object ):
    ''''''
    #-----------------------------------------------
    def __init__( self, sentences = 'This is the first simple sentence.      And another one.' ):
        self.sentences = list(filter(len, sentences.split('.')))

    def RandomSentence( self ):
        self.result = ''

        for i, sentence in enumerate(Shuffle(self.sentences), start = 1):
            self.result += '{}) {}.\n'.format(i, sentence)

        return self.result

#-----------------------------------------------
class RandomOrderOfWordsInSentences( object ):
    ''' Randomize all words in a given sentences. '''
    #-----------------------------------------------
    def __init__( self, sentences = 'This is the first simple sentence.      And another one.' ):
        self.sentences = tuple(filter(len, sentences.split('.')))

    #-----------------------------------------------
    def RandomWords( self ):

        self.result = ''

        for i, sentence in enumerate(self.sentences, start = 1):
            self.result += '{0}) {1}.\n'.format(
                    i, str.join(' ', Shuffle(
                        list(
                            filter(len, tuple(
                                filter(len, sentence.split(' '))
                                ))
                            )
                        ))
                    )

        return self.result




if __name__ == "__main__":
    for i in range(5):
        print(  str.join('; ',
                [
                    RandomOrderOfLetters('abc').RandomLetters(),
                    ReplaceSomeLettersByUnderline('foobar').ReplaceLetters(),
                    MissSpecialLetters('this is a special line').MissLetters()
                ]
        ))

        print(MatchCoupleOfWords('foo:bar\nfoo1:bar1\nfoo2:bar2').Matching())

        print(RandomOrderOfWordsInSentences().RandomWords())

