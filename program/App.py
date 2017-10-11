from program.DocumentsLoader import DocumentsLoader
from program.TermsLoader import TermsLoader


class App:
    def __init__(self):
        self.documents = {}
        self.transformed_documents = {}
        self.terms = []
        self.transformed_terms = []
        self.stopwords = []
        self.tfidf = {}

    def load_stopwords(self, filename):
        self.stopwords = TermsLoader.load_stopwords(filename)

    def get_stopwords(self):
        return self.stopwords

    def load_documents(self, filename):
        self.documents = DocumentsLoader.load_documents(filename)
        self.transformed_documents = DocumentsLoader.transform_documents(self.documents, self.stopwords)

    def get_documents_list(self):
        if self.documents == {}:
            raise Exception("Documents list is empty")
        result_list = []
        for key, value in self.documents.items():
            result_list.append(key)
            for line in value:
                result_list.append(line)
            result_list.append("")
        return result_list

    def load_terms(self, filename):
        self.terms = TermsLoader.load_terms(filename)
        self.transformed_terms = TermsLoader.transform_terms(self.terms, self.stopwords)

    def get_terms_list(self):
        if not self.terms:
            raise Exception("Terms list is empty")
        return self.terms

    def get_transformed_documents(self):
        if self.documents == {}:
            raise Exception("Documents list is empty")
        trans_documents = []
        for key, value in self.transformed_documents.items():
            trans_documents.append(key)
            for line in value:
                new_line = ""
                for word in line:
                    new_line += word
                    new_line += " "
                trans_documents.append(new_line)
            trans_documents.append("")
        return trans_documents

    def get_transformed_terms(self):
        if not self.terms:
            raise Exception("Terms list is empty")
        return self.transformed_terms

    def query(self, query):
        print("list of documents")
