from program.DocumentsLoader import DocumentsLoader
from program.TermsLoader import TermsLoader


class App:
    def __init__(self):
        self.documents = {}
        self.transformed_documents = {}
        self.terms = []
        self.transformed_terms = []

    def load_documents(self, filename):
        self.documents = DocumentsLoader.load_documents(filename)
        self.transformed_documents = DocumentsLoader.transform_documents(self.documents)

    def get_documents_list(self):
        result_list = []
        for key, value in self.documents.items():
            result_list.append(key)
            for line in value:
                result_list.append(line)
            result_list.append("")
        return result_list

    def load_terms(self, filename):
        self.terms = TermsLoader.load_terms(filename)
        self.transformed_terms = TermsLoader.transform_terms(self.terms)

    def get_terms_list(self):
        return self.terms

    def get_transformed_documents_(self):
        return self.transformed_documents

    def get_transformed_terms(self):
        return self.transformed_terms

    def query(self, query):
        print("list of documents")
