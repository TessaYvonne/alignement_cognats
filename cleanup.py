# DATA CLEANING SECTION
"""
First, we strip the raw data of characters that are not necessary for the comparison analysis.
In my case, this is a slash separating singular and plural forms; elements between brackets, and prefixes.
The function def cleanup_all combines all the clean-up functions together.
"""
import copy

from Word import Word

OPEN_CIRCLE = "°"
TOKENS = ["*", "º", OPEN_CIRCLE]

def cleanup_slash(raw_data):
    index_of_slash = raw_data.find("/")
    result = raw_data
    if index_of_slash >= 0:
        result = raw_data[:index_of_slash]
    result = result.strip()
    return result


def cleanup_parenthesis(raw_data):
    index_of_parenthesis = raw_data.find("(")
    result = raw_data
    if index_of_parenthesis >= 0:
        result = raw_data[:index_of_parenthesis]
    result = result.strip()
    return result


def cleanup_prefix(raw_data):
    index_of_dash = raw_data.find("-")
    result = raw_data
    prefix = ""
    if index_of_dash >= 0:
        result = raw_data[(index_of_dash + 1):]
        prefix = raw_data[:index_of_dash + 1]
    result = result.strip()
    return Word(result, prefix)


def remove_duplicate_tokens(raw_data):
    if len(raw_data.text) == 0:
        return raw_data
    first_letter_is_token = raw_data.text[0] in TOKENS
    result = copy.deepcopy(raw_data)
    for token in TOKENS:
        result.text = result.text.replace(token,"")
    if first_letter_is_token:
        result.text = raw_data.text[0] + result.text
    return result


def cleanup_all(raw_data):
    word_data = remove_duplicate_tokens(cleanup_prefix(cleanup_parenthesis(cleanup_slash(raw_data))))
    word_data.text = word_data.text.replace(" ","")
    word_data.prefix = word_data.prefix.replace(" ","")
    return word_data


def cleanup_pa80(raw_data):
    if len(raw_data)>0:
        while raw_data[0] in ['-', 'º', '°']:
            raw_data = raw_data[1:]
        word_data = Word(cleanup_slash(raw_data),"")
        if raw_data.find('(') == 0:
            closing_parenthesis = word_data.text.find(')')
            if closing_parenthesis >=0:
                word_data.prefix = word_data.text[:closing_parenthesis+1]
                word_data.text = word_data.text[closing_parenthesis+1:]
        else:
            word_data = cleanup_prefix(word_data.text)
        word_data.text = OPEN_CIRCLE + word_data.text
        word_data = remove_duplicate_tokens(word_data)
        word_data.text = word_data.text.replace(" ","")
        word_data.prefix = word_data.prefix.replace(" ","")
    else:
        word_data = Word('','')
    return word_data


def clean_data_to_csv(input_file_name, output_file_name):
    with open(input_file_name) as input_file, open(output_file_name, 'w') as output_file:
        for line in input_file:
            if len(line.strip()) == 0:
                continue
            cells = line.split(';')
            for cell in cells:
                output_file.write(cleanup_all(cell) + ";")
            output_file.write('\n')


#clean_data_to_csv("test/test_data.csv", "clean_test_data.csv")