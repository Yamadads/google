from math import log
from math import pow
from math import sqrt


class TFIDF:
    @staticmethod
    def create_tfidf(terms, documents):
        def tf_for_document(document_lines, terms_list):
            doc_tf = {}
            for term in terms_list:
                doc_tf[term] = 0
            for line in document_lines:
                for term in line:
                    if term in doc_tf:
                        doc_tf[term] += 1
            max_value = max(doc_tf.values())
            if max_value == 0:
                return doc_tf
            for key in doc_tf:
                doc_tf[key] /= max_value
            return doc_tf

        def tf_for_documents(document_terms, all_documents):
            tf_rep = {}
            for document in all_documents:
                tf_rep[document] = tf_for_document(all_documents[document], document_terms)
            return tf_rep

        def idf_terms(documents_terms, tf_documents):
            term_doc_count = {}
            for term in documents_terms:
                term_doc_count[term] = 0
            for term in documents_terms:
                for document in tf_documents:
                    if tf_documents[document][term] > 0:
                        term_doc_count[term] += 1
            idf = {}
            for term in documents_terms:
                if term_doc_count[term] == 0:
                    idf[term] = 0
                else:
                    idf[term] = log(len(tf_documents) / term_doc_count[term], 2)
            return idf

        def tfidf_for_document(tf_document, idf):
            tfidf_doc = {}
            for term in tf_document:
                tfidf_doc[term] = tf_document[term] * idf[term]
            return tfidf_doc

        def tfidf_for_documents(tf_documents, idf):
            tfidf_docs = {}
            for doc in tf_documents:
                tfidf_docs[doc] = tfidf_for_document(tf_documents[doc], idf)
            return tfidf_docs

        def doc_vectors_len(tfidf_documents):
            doc_vec_len = {}
            for doc in tfidf_documents:
                vec_sum = 0
                for term in tfidf_documents[doc]:
                    vec_sum += pow(tfidf_documents[doc][term], 2)
                doc_vec_len[doc] = sqrt(vec_sum)
            return doc_vec_len

        tf_repr = tf_for_documents(terms, documents)
        idf_terms_rep = idf_terms(terms, tf_repr)
        tfidf_repr = tfidf_for_documents(tf_repr, idf_terms_rep)
        documents_vectors_len = doc_vectors_len(tfidf_repr)

        return tfidf_repr, documents_vectors_len, idf_terms_rep
