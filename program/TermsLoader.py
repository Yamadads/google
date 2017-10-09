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
    def transform_terms(terms):
        return terms

    @staticmethod
    def load_stopwords(filename):
        stopwords = []
        f = open(filename, 'r')
        lines = [s.rstrip("\n\r") for s in f.readlines()]
        for line in lines:
            stopwords.append(line)
        return stopwords
