def count_lines_in_file(path):
    count = 0
    with open(path, encoding='utf-8') as file:
        while file.readline():
            count += 1
    return count

def remove_empty_lines(source, destination):
    with open(source, encoding='utf-8') as file:
        with open(destination, 'w', encoding='utf-8') as output:
            for line in file:
                if line != '\n':
                    output.write(line)

def remove_duplicate_lines(source, destination):
    with open(source, encoding='utf-8') as file:
        with open(destination, 'w', encoding='utf-8') as output:
            previous_line = None
            for line in file:
                if line != previous_line:
                    output.write(line)
                    previous_line = line