from program.DocumentsLoader import DocumentsLoader
from program.TermsLoader import TermsLoader
from program.TFIDF import TFIDF
from program.QueryHandler import QueryHandler
from program.Settings import Settings


class App:
    def __init__(self):
        self.documents = {}
        self.transformed_documents = {}
        self.terms = []
        self.transformed_terms = []
        self.stopwords = []
        self.tfidf = {}
        self.documents_vec_len = {}
        self.idf_terms = {}
        self.settings = Settings()

    def load_stopwords(self, filename):
        self.stopwords = TermsLoader.load_stopwords(filename)

    def get_stopwords(self):
        return self.stopwords

    def load_documents(self, filename):
        if not self.terms:
            raise Exception("Please load terms first")
        self.documents = DocumentsLoader.load_documents(filename)
        self.transformed_documents = DocumentsLoader.transform_documents(self.documents, self.stopwords)
        self.tfidf, self.documents_vec_len, self.idf_terms = TFIDF.create_tfidf(self.transformed_terms,
                                                                                self.transformed_documents)

    def get_documents_list(self):
        if self.documents == {}:
            raise Exception("Documents list is empty")
        result_list = []
        for key, value in sorted(self.documents.items()):
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
        return sorted(self.terms)

    def get_transformed_documents(self):
        if self.documents == {}:
            raise Exception("Documents list is empty")
        trans_documents = []
        for key, value in sorted(self.transformed_documents.items()):
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
        return sorted(self.transformed_terms)

    def settings_request(self, request):
        if request == 'app:settings':
            return self.settings.get_settings_list()
        else:
            return self.settings.set_settings_values(request)

    def query(self, query):
        if not self.tfidf:
            raise Exception("Documents list is empty")
        return QueryHandler.query(query, self.tfidf, self.documents_vec_len, self.stopwords, self.idf_terms)
