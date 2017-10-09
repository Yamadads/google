class DocumentsLoader:
    @staticmethod
    def load_documents(filename):
        documents = {}
        f = open(filename, 'r')
        lines = [s.rstrip("\n\r") for s in f.readlines()]
        document_title = ""
        document_lines = []
        for line in lines:
            if line == "" and document_title != "":
                documents[document_title] = document_lines
                document_title = ""
                document_lines = []
            elif document_title == "":
                document_title = line
            else:
                document_lines.append(line)
        return documents

    @staticmethod
    def transform_documents(documents):
        return documents
