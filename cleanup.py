# DATA CLEANING SECTION
"""
First, we strip the raw data of characters that are not necessary for the comparison analysis.
In my case, this is a slash separating singular and plural forms; elements between brackets, and prefixes.
The function def cleanup_all combines all the clean-up functions together.
"""


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
    if index_of_dash >= 0:
        result = raw_data[(index_of_dash + 1):]
    result = result.strip()
    return result


def remove_duplicate_tokens(raw_data):
    if len(raw_data) == 0:
        return raw_data
    first_letter_is_token = raw_data[0] in ["*", "º", "°"]
    result = raw_data
    for token in ["*", "º", "°"]:
        result = result.replace(token,"")
    if first_letter_is_token:
        result = raw_data[0] + result
    return result


def cleanup_all(raw_data):
    return remove_duplicate_tokens(cleanup_prefix(cleanup_parenthesis(cleanup_slash(raw_data)))).replace(" ","")


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