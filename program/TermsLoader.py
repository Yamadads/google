class TermsLoader:
    @staticmethod
    def load_terms(filename):
        terms = []
        f = open(filename, 'r')
        lines = [s.rstrip("\n\r") for s in f.readlines()]
        print(lines)
        for line in lines:
            print(line)
            terms.append(line)
        return terms

    @staticmethod
    def transform_terms(terms):
        return terms