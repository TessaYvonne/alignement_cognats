# columns = ["C1a", "C1b", "V1a", "V1b", "C2a", "C2b", "V2a", "V2b", "C3a", "C3b", "V3a", "V3b"]
languages = ["swo", "gyeli", "bekwel", "bekol", "konzime", "makaa", "mpiemo", "kwasio", "njyem", "shiwa"]

columns = []
for i in range(1, 20):
    columns.append(f'C{i}a')
    columns.append(f'C{i}b')
    columns.append(f'V{i}a')
    columns.append(f'V{i}b')


def letters_to_output_format(data):
    letters = {}
    column = 0
    for letter in data:
        # print(f'{column}, {letter}')
        if column >= len(columns):
            print(f'too long: {column}, {letter}')
            return letters
        if letter["is_consonant"]:
            while columns[column].startswith('V'):
                letters[columns[column]] = ''
                column += 1
        else:
            while columns[column].startswith('C'):
                letters[columns[column]] = ''
                column += 1
        letters[columns[column]] = letter["letter"]
        column += 1

    while column < len(columns):
        letters[columns[column]] = ""
        column += 1
    return letters


def word_data_to_csv(word):
    data = []
    title = [word['line'], word['FR']]
    for i in range(2, 14):
        title.append('')
    data.append(title)

    data.append(['', ''] + columns)

    language_data = word['languages']
    for language in languages:
        line = ['', language]
        for column in columns:
            line.append(letters_to_output_format(language_data[language])[column])
        data.append(line)

    empty_line = ['']
    for i in range(1, 14):
        empty_line.append('')
    data.append(empty_line)

    return data


def matrix_to_csv(matrix):
    lines = []
    for line in matrix:
        output_line = ''
        for column in line:
            output_line += '"' + column + '";'
        lines.append(output_line.strip(";"))
    return lines


def write_output_to_file(outputfile, matrix):
    for line in matrix:
        outputfile.write(line + '\n')
