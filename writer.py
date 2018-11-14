def write_scores(filename, scores):
    with open(filename, "w") as f:
        for score in scores:
            for item in score:
                line = ' '.join([str(it) for it in item]) + '\n'
                f.write(line)
