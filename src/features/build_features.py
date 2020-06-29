

import unidecode
from nltk.corpus import stopwords

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