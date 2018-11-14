import string

import nltk
from nltk.corpus import stopwords


def sentence_tokenizer(sentence):
    english_stop_words = [word for word in stopwords.words('english')]
    punctuations = list(string.punctuation)

    all_stop_words = english_stop_words + punctuations
    sentence_tokens = nltk.wordpunct_tokenize(sentence)

    filtered_sentence_tokens = [token for token in sentence_tokens if
                                token.lower() not in all_stop_words and not token.isdigit()]

    return filtered_sentence_tokens


def text_tokenizer(text):
    text_tokens = []
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        text_tokens.append(sentence_tokenizer(sentence))

    return text_tokens


def tokenize_query(query):
    query_tokens = []
    for text in query:
        text_tokens = sentence_tokenizer(text)
        query_tokens.append(text_tokens)

    return query_tokens


def tokenize_docs(docs):
    docs_tokens = []
    for doc in docs:
        docs_tokens.append(text_tokenizer(doc))

    return docs_tokens


if __name__ == '__main__':
    result = tokenize_docs([['panels of the x --15 vertical stabilizer when subjected to aerodynamic heating .']])

    print(result)
