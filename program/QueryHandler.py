from .Tokenizer import Tokenizer
from math import sqrt


class QueryHandler:
    @staticmethod
    def query(query_text, documents_tfidf_rep, documents_vec_len, stopwords, idf_terms):
        def prepare_query():
            query = {}
            query_tokens = Tokenizer.tokenize(query_text, stopwords)
            print(query_tokens)
            print(idf_terms)
            for term in idf_terms:
                query[term] = 0
            for token in query_tokens:
                if token in query:
                    query[token] += 1
            max_value = max(query.values())
            print(max_value)
            if max_value == 0:
                return query
            for key in query:
                query[key] /= max_value
            for key in query:
                query[key] *= idf_terms[key]
            print(query)
            return query

        def calc_query_len(query):
            result_len = 0
            vec_sum = 0
            for term in query:
                vec_sum += pow(query[term], 2)
                result_len = sqrt(vec_sum)
            return result_len

        def calc_similarity(query, document, doc_len, query_len):
            lenghts = doc_len * query_len
            if lenghts == 0:
                return 0
            terms_mul = 0
            for term in query:
                terms_mul += query[term] * document[term]

            return terms_mul / lenghts

        def calc_similarities(query, documents, doc_lenghts):
            doc_similarities = {}
            for document in documents:
                doc_similarities[document] = calc_similarity(query, documents[document], doc_lenghts[document],
                                                             calc_query_len(query))
            return doc_similarities

        def prepare_response_list(similarities):
            resp_list = []
            for w in sorted(similarities.items(), key=lambda x: x[1], reverse=True):
                resp_list.append(w[0] + "        " + str(w[1]))
            return resp_list

        tfidf_query = prepare_query()
        documents_similarities = calc_similarities(tfidf_query, documents_tfidf_rep, documents_vec_len)
        response_list = prepare_response_list(documents_similarities)
        return response_list
