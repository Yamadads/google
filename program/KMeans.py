import random
import numpy as np


class KMeans:
    @staticmethod
    def get_groups(k, i, documents, documents_vec_len, documents_groups, tfidf):
        def calc_query_len(query):
            result_len = 0
            vec_sum = 0
            for term in query:
                vec_sum += pow(query[term], 2)
                result_len = np.sqrt(vec_sum)
            return result_len

        def calc_similarity(document1, document2, doc1_len, doc2_len):
            length = doc1_len * doc2_len
            if length == 0:
                return 0
            terms_mul = 0
            for term in document1:
                terms_mul += document1[term] * document2[term]
            return terms_mul / length

        def get_random_documents():
            random_docs_keys = random.sample(list(documents), k)
            random_docs = {}
            for doc_title in random_docs_keys:
                random_docs[doc_title] = tfidf[doc_title]
            return random_docs

        def get_best_group(k_means_docs, doc, doc_len):
            best_sim_group = 0
            best_sim_group_value = 0
            group_id = 0
            for k_mean_doc in k_means_docs:
                group_id += 1
                k_mean_len = calc_query_len(k_means_docs[k_mean_doc])
                sim = calc_similarity(k_means_docs[k_mean_doc], doc, k_mean_len, doc_len)
                if sim > best_sim_group_value:
                    best_sim_group_value = sim
                    best_sim_group = group_id
            return best_sim_group

        def set_new_documents_groups(k_means_docs, actual_docs_groups):
            changed = False
            new_doc_groups = {}
            for doc in actual_docs_groups:
                group = get_best_group(k_means_docs, tfidf[doc], documents_vec_len[doc])
                if group != actual_docs_groups[doc]:
                    changed = True
                new_doc_groups[doc] = group
            return new_doc_groups, changed

        def calc_mean_dict(list_of_dicts):
            mean_dict = {}
            for term in list_of_dicts[0]:
                sum = 0
                count = 0
                for single_dict in list_of_dicts:
                    sum += single_dict[term]
                    count += 1
                mean_dict[term] = sum/count
            return mean_dict

        def calc_new_k_means_docs(actual_docs_groups):
            new_k_means_docs = {}
            for group_id in range(1, k + 1):
                group_docs = [x for x in actual_docs_groups if actual_docs_groups[x] == group_id]
                docs = [tfidf[x] for x in tfidf if x in group_docs]
                k_mean_doc = calc_mean_dict(docs)
                new_k_means_docs[group_id] = k_mean_doc
            return new_k_means_docs

        def prepare_output(actual_docs_groups):
            output = []
            for group_id in range(1, k + 1):
                output.append('Grupa ' + str(group_id) + ':')
                group_docs = [x for x in actual_docs_groups if actual_docs_groups[x] == group_id]
                for name in group_docs:
                    output.append(documents_groups[name])
                output.append(' ')
            return output

        k_means_documents = get_random_documents()
        actual_documents_groups = documents_groups
        iterator = 0
        not_changed_iterator = 0
        while iterator < i and not_changed_iterator < 2:
            actual_documents_groups, groups_changed = set_new_documents_groups(k_means_documents,
                                                                               actual_documents_groups)
            k_means_documents = calc_new_k_means_docs(actual_documents_groups)
            if groups_changed:
                not_changed_iterator = 0
            else:
                not_changed_iterator += 1
        return prepare_output(actual_documents_groups)
