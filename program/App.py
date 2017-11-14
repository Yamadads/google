from program.DocumentsLoader import DocumentsLoader
from program.TermsLoader import TermsLoader
from program.TFIDF import TFIDF
from program.QueryHandler import QueryHandler
from program.Settings import Settings
from program.RelevanceFeedback import RelevanceFeedback
from program.KMeans import KMeans

class App:
    def __init__(self):
        self.documents = {}
        self.documents_groups = {}
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
        if self.settings.get_settings_value('mode') == 'k-means':
            self.documents, self.documents_groups = DocumentsLoader.load_documents_kmeans(filename)
        elif self.settings.get_settings_value('mode') == 'tf-idf':
            self.documents = DocumentsLoader.load_documents(filename)
        else:
            raise Exception("Wrong working mode. Check app:settings. mode must be equal to k-means or tf-idf")
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
        return QueryHandler.query(query, self.tfidf, self.documents_vec_len, self.stopwords, self.idf_terms, None)

    def relevance_feedback_query(self, query, documents_status):
        if not self.tfidf:
            raise Exception("Documents list is empty")
        good_docs = []
        bad_docs = []
        for key, value in documents_status.items():
            (doc_title, doc_value, doc_status) = value
            if doc_status == 'good':
                good_docs.append(doc_title)
            if doc_status == 'bad':
                bad_docs.append(doc_title)
        new_query = RelevanceFeedback.create_new_query(query, good_docs, bad_docs, self.settings, self.transformed_documents, self.stopwords, self.idf_terms)
        return QueryHandler.query(None, self.tfidf, self.documents_vec_len, self.stopwords, self.idf_terms, new_query)

    def group_documents(self):
        if self.documents == {}:
            raise Exception("Documents list is empty")
        return KMeans.get_groups(self.settings.get_settings_value('k'), self.settings.get_settings_value('i'),self.documents, self.documents_vec_len, self.documents_groups, self.tfidf)