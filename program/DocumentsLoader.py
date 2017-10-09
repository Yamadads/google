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
        def tokenize(line):
            intab = '~!@#$%^&*()_+=`{}[]|/:;,.<>?"\\'
            outtab = '                              '
            lower_line = line.lower()
            translated_line = lower_line.translate({ord(x): y for (x, y) in zip(intab, outtab)})
            translated_line = translated_line.replace(" - ", " ")
            tokens = translated_line.split();
            return tokens;

        transformed_documents = {}
        for key, value in documents.items():
            tokens_lines = []
            tokens_lines.append(tokenize(key))
            for line in value:
                tokens_lines.append(tokenize(line))
            transformed_documents[key] = tokens_lines
        return transformed_documents

