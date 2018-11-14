from math import pow, sqrt
from tfidf import tfidf


def cosine_similarity(vec1, vec2):
    sum_of_squares_1 = sum([pow(x, 2) for x in vec1])
    sum_of_squares_2 = sum([pow(x, 2) for x in vec2])
    dot_product = sum([x * y for x, y in zip(vec1, vec2)])

    norm1 = sqrt(sum_of_squares_1)
    norm2 = sqrt(sum_of_squares_2)

    result = 0.0
    try:
        result = float(dot_product / float(norm1 * norm2))
    except:
        pass

    return result


def score(queries, query_tf, query_idf, docs_tf, docs_idf, ):
    scores = []
    for query_id, query in enumerate(queries):
        doc_scores = []
        vec_1 = tfidf(query, query_tf[query_id], query_idf)
        for doc_id, doc_tf in enumerate(docs_tf):
            vec_2 = tfidf(query, doc_tf, docs_idf)
            similarity = cosine_similarity(vec_1, vec_2)

            doc_score = (query_id + 1, doc_id + 1, similarity)
            doc_scores.append(doc_score)

        scores.append(doc_scores)

    sorted_scores = []
    for score in scores:
        sorted_score = sorted(score, key=lambda item: item[2], reverse=True)
        sorted_scores.append(sorted_score)

    return sorted_scores
