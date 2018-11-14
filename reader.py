def read_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

        return lines


def read_query(filename):
    lines = read_lines(filename)

    ids = []
    query_items = []

    content = ''
    cur_id = lines[0].split()[1]
    for line in lines[1:]:
        if line.startswith('.I'):
            ids.append(cur_id)
            query_items.append(content)
            content = ''
            cur_id = line.split()[1]
            continue
        elif line.startswith('.W'):
            continue
        else:
            content += line

    return ids, query_items


def read_docs(filename):
    lines = read_lines(filename)

    ids = []
    query_items = []

    content = ''
    continue_reading = False
    cur_id = lines[0].split()[1]
    for line in lines[1:]:
        if line.startswith('.I'):
            ids.append(cur_id)
            query_items.append(content)
            content = ''
            cur_id = line.split()[1]
            continue_reading = False
            continue
        elif line.startswith('.W'):
            continue_reading = True
            continue
        if continue_reading:
            content += line

    return ids, query_items


if __name__ == '__main__':
    filename = 'Cranfield_collection_HW/cran.qry'
    # filename = 'Cranfield_collection_HW/cran.all.1400'
    result = read_docs(filename)
    print(result)
