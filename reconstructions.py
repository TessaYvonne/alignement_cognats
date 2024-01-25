# GENERAL INTRODUCTION
"""
Code to align data from more than one language based on the position of the element within the word.
The positions are on the horizontal axis, the words in the different languages on the vertical axis.
The element of each word is aligned: the first consonant in C1, the first vowel in V1, etc.
"""
from cleanup import cleanup_all

# RECONSTRUCTION SECTION
'''
In this section, we work on reconstructed forms. I want the final table to reflect which elements are reconstructed.
The code first looks for reconstructed words, indicated in the raw data with a º or a *.
It then adds these characters to each element of the word before aligning it in the final table.
Brackets are ignored, as well as diacritics, which are a separate unicode character.
'''


def is_diacritic(letter):
    return (letter >= "\u02B0" and letter <= "\u02FF") or (letter >= "\u0300" and letter <= "\u036F")


def reconstruction(raw_data, tokens):
    if raw_data == "":
        return ""
    letters = list(raw_data)
    if letters[0] not in tokens:
        return raw_data
    token = letters[0]
    result = ""
    in_paren = False
    position = 0
    position_of_opening_bracket = 0
    for letter in letters[1:]:
        position += 1
        if not in_paren:
            if not is_diacritic(letter):
                result += token
        result += letter
        if letter == "(":
            position_of_opening_bracket = position
            in_paren = True
        else:
            if letter == ")":
                if in_paren:
                    if position == position_of_opening_bracket + 1:
                        return f"Warning: formatting error in '{raw_data}'"
                    in_paren = False
                else:
                    return f"Warning: formatting error in '{raw_data}'"
    if in_paren:
        return f"Warning: formatting error in '{raw_data}'"
    return result


'''
This part of the code reads a data file formatted as a table. It first skips the line containing the column headers.
Then it splits lines into cells. The words in the cells are added to a Python dictionary, and coupled with the column headings.
'''

column_headers = ["nº","FR","PA80","swo","gyeli","bekwel","bekol","konzime","makaa","mpiemo","kwasio","njyem","shiwa","BC (BLR3)","Reconstr. Régionales (BLR 3)","Reconstr. Mougiama, Hombert"]


def read_and_process_data(datafile):
    with open(datafile) as file:
        result = []
        skip_line = True
        for line in file:
            if len(line.strip()) == 0:
                continue
            if skip_line:
                skip_line = False
                continue
            cells = line.split(';')
            words = {}
            word_count = 0
            for cell in cells:
                if word_count <= 1:
                    words.update({column_headers[word_count]:cell.strip()})
                else:
                    words.update({column_headers[word_count]:reconstruction(cleanup_all(cell), ["*", "º", "°"])})
                word_count += 1
            result.append(words)
    return result
