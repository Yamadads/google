from .Tokenizer import Tokenizer


class TermsLoader:
    @staticmethod
    def load_terms(filename):
        terms = []
        f = open(filename, 'r')
        lines = [s.rstrip("\n\r") for s in f.readlines()]
        for line in lines:
            terms.append(line)
        return terms

    @staticmethod
    def transform_terms(terms, stopwords):
        transformed_terms = []
        for line in terms:
            transformed_terms += Tokenizer.tokenize(line, stopwords)
        unique_transformed_terms = list(set(transformed_terms))
        return unique_transformed_terms

    @staticmethod
    def load_stopwords(filename):
        stopwords = []
        f = open(filename, 'r')
        lines = [s.rstrip("\n\r") for s in f.readlines()]
        for line in lines:
            stopwords.append(line)
        return stopwords
