from reader import read_query, read_docs
from similarity import score
from tfidf import tfidf_query, tfidf_docs
from tokenizer import tokenize_query, tokenize_docs
from writer import write_scores

if __name__ == "__main__":
    print('Processing Query...')
    query_file = 'Cranfield_collection_HW/cran.qry'
    query_id, query_texts = read_query(query_file)
    query_tokens = tokenize_query(query_texts)
    query_tfs, query_idfs = tfidf_query(query_tokens)

    print("Processing Docs...")
    docs_file = 'Cranfield_collection_HW/cran.all.1400'
    docs_id, docs_texts = read_docs(docs_file)
    docs_tokens = tokenize_docs(docs_texts)
    docs_tfs, docs_idfs = tfidf_docs(docs_tokens)

    print("Processing Scoring...")
    scores = score(query_tokens, query_tfs, query_idfs, docs_tfs, docs_idfs)

    print("Saving the Scores...")
    write_scores("scores.txt", scores)

    print("All Done!...")
