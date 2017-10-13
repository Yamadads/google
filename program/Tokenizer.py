from .PorterStemmer import PorterStemmer


class Tokenizer:
    @staticmethod
    def tokenize(text, stopwords):
        def clean_text(text_to_clean):
            intab = '-·~!@#$%^&*()_+=`{}[]|/:;,.<>?"\\'
            outtab = '                                '
            processed_text = text_to_clean.lower()
            processed_text = processed_text.translate({ord(x): y for (x, y) in zip(intab, outtab)})
            # processed_text = processed_text.replace(" - ", " ")
            return processed_text

        def remove_stopwords(tokens_list, stopwords_list):
            cleaned_tokens = [token for token in tokens_list if token not in stopwords_list]
            return cleaned_tokens

        def stemming(tokens_list):
            stemmer = PorterStemmer()
            tokens_stems = [stemmer.stem(token, 0, len(token) - 1) for token in tokens_list if
                            stemmer.stem(token, 0, len(token) - 1) != ""]
            return tokens_stems

        cleaned_text = clean_text(text)
        tokens = cleaned_text.split()
        if stopwords:
            tokens = remove_stopwords(tokens, stopwords)
        tokens = stemming(tokens)
        return tokens
