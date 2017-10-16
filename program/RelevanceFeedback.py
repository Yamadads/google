from .Tokenizer import Tokenizer


class RelevanceFeedback:
    @staticmethod
    def create_new_query(old_query, good_documents, bad_documents, settings, transfered_documents, stopwords,
                         idf_terms):
        def prepare_query_bag_words():
            query_bw = {}
            query_tokens = Tokenizer.tokenize(old_query, stopwords)
            for term in idf_terms:
                query_bw[term] = 0
            for token in query_tokens:
                if token in query_bw:
                    query_bw[token] += 1
            return query_bw

        def prepare_document_bag_words(document_lines):
            document = {}
            for term in idf_terms:
                document[term] = 0
            for line in document_lines:
                for token in line:
                    if token in document:
                        document[token] += 1
            return document

        def prepare_documents_bag_words(documents_titles):
            documents_bag_words = {}
            for key, value in transfered_documents.items():
                if key in documents_titles:
                    documents_bag_words[key] = prepare_document_bag_words(value)
            return documents_bag_words

        def documents_sum_bag_words(documents_bag_words):
            documents_bag_words_sum = {}
            for term in idf_terms:
                documents_bag_words_sum[term] = 0
            for document in documents_bag_words:
                for term, value in documents_bag_words[document].items():
                    documents_bag_words_sum[term] += value
            return documents_bag_words_sum

        def prepare_new_query_bag_words(query, good_docs, bad_docs):
            new_query = {}
            for key, value in query.items():
                new_query[key] = settings.get_settings_value('alpha') * value
            for key, value in good_docs.items():
                new_query[key] += settings.get_settings_value('beta') * value
            for key, value in bad_docs.items():
                new_query[key] -= settings.get_settings_value('gamma') * value
                if new_query[key] < 0:
                    new_query[key] = 0
            return new_query

        def normalize_query(new_query):
            max_value = max(new_query.values())
            if max_value == 0:
                raise Exception("Empty query")
            for key in new_query:
                new_query[key] /= max_value
            for key in new_query:
                new_query[key] *= idf_terms[key]
            return new_query

        query = prepare_query_bag_words()
        good_documents_bag_words = documents_sum_bag_words(prepare_documents_bag_words(good_documents))
        bad_documents_bag_words = documents_sum_bag_words(prepare_documents_bag_words(bad_documents))
        new_query_from_feedback = prepare_new_query_bag_words(query, good_documents_bag_words, bad_documents_bag_words)
        return normalize_query(new_query_from_feedback)
