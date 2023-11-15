def count_lines_in_file(path):
    count = 0
    with open(path, encoding='utf-8') as file:
        while file.readline():
            count += 1
    return count