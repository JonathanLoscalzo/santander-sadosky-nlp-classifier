

import unidecode
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, WordPunctTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer , TreebankWordTokenizer
import re
from toolz import pipe
from functools import partial


def get_stopwords(path = '../../data/external/stopwords.txt'):
    """
     Read stopwords in spanish
    """
    stop_arr = stopwords.words('spanish')

    with open(path) as f:
        for line in f:
            stop_arr.append(unidecode.unidecode(line.strip()))

    stop_arr = sorted(list(set(stop_arr)))

    return stop_arr

class Cleaner():
    def __init__(self):
        # nltk.download('punkt')
        self.tk = TreebankWordTokenizer()
        self.dtk = TreebankWordDetokenizer()
        self.BAD_CAT_REMOVE = re.compile('^Cat_')
        self.A_TILDE_REMOVE = re.compile('[á]')
        self.E_TILDE_REMOVE = re.compile('[é]')
        self.I_TILDE_REMOVE = re.compile('[í]')
        self.O_TILDE_REMOVE = re.compile('[ó]')
        self.U_TILDE_REMOVE = re.compile('[ú]')
        self.POINT_FOLLOWING_LETTER=re.compile('(?<=\S)\.(?=\w)')
        # self.BAD_SYMBOLS_REMOVE = re.compile('[^A-Za-z0-9_ áéíóú]')
    
    def applyRegex(self, value,regex,replacement):
        value = regex.sub(replacement,value)
        return value

    def text_cleaning(self, text):
        return pipe(
            text.lower(),
            # partial(self.BAD_SYMBOLS_REMOVE.sub,  ''), 
            partial(self.A_TILDE_REMOVE.sub, 'a'), 
            partial(self.E_TILDE_REMOVE.sub, 'e'), 
            partial(self.I_TILDE_REMOVE.sub, 'i'), 
            partial(self.O_TILDE_REMOVE.sub, 'o'), 
            partial(self.U_TILDE_REMOVE.sub, 'u'), 
            # partial(self.POINT_FOLLOWING_LETTER.sub('. '))
        )

    def sentence_cleaning(self, sentence, detokenize=False):
        word_tokens = pipe(
            sentence, 
            partial(self.POINT_FOLLOWING_LETTER.sub, '. '),
            self.tk.tokenize
        )       


        word_tokens = [self.text_cleaning(text) for text in word_tokens]
        # word_tokens.remove('')

        if detokenize:
            return self.dtk.detokenize(word_tokens)
        else: 
            return word_tokens
        