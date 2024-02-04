import os
import shutil

languages = ["PA80","swo","gyeli","bekwel","bekol","konzime","makaa","mpiemo","kwasio","njyem","shiwa","Reconstr. Régionales (BLR 3)","Reconstr. Mougiama, Hombert"]

columns = []
for i in range(1, 15):
    columns.append(f'C{i}a')
    columns.append(f'C{i}b')
    columns.append(f'V{i}a')
    columns.append(f'V{i}b')


def letters_to_output_format(data):
    letters = {}
    column = 0
    for letter in data:
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
    for i in range(2, len(columns)):
        title.append('')
    data.append(title)

    data.append(['', ''] + columns)

    language_data = word['languages']
    if len(language_data) == 0:
        print (f'no language data for {word["line"]}')
    else:
        for language in languages:
            line = ['', language]
            for column in columns:
                one_language = language_data[language]
                output_format = letters_to_output_format(one_language)
                line.append(output_format[column])
            data.append(line)

        empty_line = ['']
        for i in range(1, len(columns) + 2):
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


def word_to_html_page(word):
    html: str = f'<html><head><title>{word["FR"]}</title></head><body><h1>{word["FR"]}</h1>'
    html += '<table><tr><th></th>'

    language_data = word['languages']
    number_of_columns = find_longest_row(language_data)

    for column in columns[:number_of_columns]:
        html += f'<th>{column}</th>'
    html += '</tr>'

    for language in languages:
        html += f'<tr><td>{language}</td>'
        one_language = language_data[language]
        output_format = letters_to_output_format(one_language)
        for column in columns[:number_of_columns]:
            html += f'<td>{output_format[column]}</td>'
        html += '</tr>'

    html += '</table></body></html>'
    return html


def find_last_non_empty_index(columns):
    i = 0
    last_non_empty = 0
    for column in columns:
        if columns[column] != "":
            last_non_empty = i
        i += 1
    return last_non_empty + 1


def find_longest_row(languages):
    length_longest_row = 0
    for language in languages:
        one_language = languages[language]
        output_format = letters_to_output_format(one_language)
        length_current_row = find_last_non_empty_index(output_format)
        if length_current_row > length_longest_row:
            length_longest_row = length_current_row
    return length_longest_row


def word_to_file_name(word):
    return word.replace(' ', '_').replace('/', '_').replace('(', '_').replace(')', '_') + ".html"


def cleanup_output_folder(outputfolder):
    if os.path.exists(outputfolder) and os.path.isdir(outputfolder):
        shutil.rmtree(outputfolder)
    os.makedirs(outputfolder, exist_ok=True)