from nltk.corpus import wordnet as wn
from itertools import chain
import random


class WordNetManager:
    @staticmethod
    def get_list_of_proposed_queries(query, list_size):
        def get_last_word(query_text):
            intab = '-·~!@#$%^&*()_+=`{}[]|/:;,.<>?"\\'
            outtab = '                                '
            processed_text = query_text.lower()
            processed_text = processed_text.translate({ord(x): y for (x, y) in zip(intab, outtab)})
            tokens = processed_text.split()
            if len(tokens) >= 1:
                return tokens[len(tokens) - 1]
            else:
                return None

        proposed_queries_list = []
        last_word = get_last_word(query)
        print("word: " + str(last_word))
        if last_word is None:
            return proposed_queries_list
        synonyms = wn.synsets(last_word)
        lemmas = set(chain.from_iterable([word.lemma_names() for word in synonyms]))
        if len(lemmas) > 5:
            rand_words_list = random.sample(lemmas, list_size)
        else:
            rand_words_list = lemmas
        for i in rand_words_list:
            proposed_queries_list.append(query + " " + i)
        return proposed_queries_list
