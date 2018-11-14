from math import log


def tfidf_query(query):
    query_tfs = []
    token_vocab = {}
    for item_tokens in query:
        item_tf = {}
        for token in item_tokens:
            item_tf[token] = item_tf.get(token, 0) + 1
            if token not in token_vocab:
                token_vocab[token] = 1
        query_tfs.append(item_tf)

    query_idfs = {}
    all_query_items = len(query)
    for token in token_vocab.keys():
        for item_tfs in query_tfs:
            if token in item_tfs:
                query_idfs[token] = query_idfs.get(token, 0) + 1

        query_idfs[token] = log(float(all_query_items) / float(query_idfs[token]))

    return query_tfs, query_idfs


def tfidf_docs(docs):
    docs_tfs = []
    token_vocab = {}
    for doc in docs:
        doc_tfs = {}
        for item_tokens in doc:
            for token in item_tokens:
                doc_tfs[token] = doc_tfs.get(token, 0) + 1
                if token not in token_vocab:
                    token_vocab[token] = 1
        docs_tfs.append(doc_tfs)

    docs_idfs = {}
    all_docs_items = len(docs)
    for token in token_vocab.keys():
        for doc_tfs in docs_tfs:
            if token in doc_tfs:
                docs_idfs[token] = docs_idfs.get(token, 0) + 1

        docs_idfs[token] = log(float(all_docs_items) / float(docs_idfs[token]))

    return docs_tfs, docs_idfs


def tfidf(tokens, tfs, idfs):
    vector = []
    for token in tokens:
        tf = tfs.get(token, 0.0)
        idf = idfs.get(token, 0.0)
        vector.append(float(tf * idf))
    return vector


if __name__ == '__main__':
    print('dasdada')
