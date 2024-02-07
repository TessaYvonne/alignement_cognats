from reconstructions import tokens, read_and_process_excel_file

from reconstructions import read_and_process_csv_file

consonants = ["C", "ɲɟ̥", "g̥ʸ", "j̥", "r̥", "_", "?", "ɟ̥", "ndʰ", "nkʷ", "ndʰ", "kʷ", "mbʰ", "ʁ", "bʰ", "dʰ", "P",
              "ˤ", "C", "Ǹ", "N", "T", "K", "w", "y", "j", "p", "b", "ɓ", "t", "d", "ɗ", "c", "ɟ", "k", "g", "ɡ", "ʔ",
              "m", "n", "ɲ", "ŋ", "ɳ", "ɾ", "r", "f", "v", "s", "z", "ʃ", "ʒ", "h", "l", "ɥ", "mp", "mb", "nt", "nd",
              "nc", "nɟ", "ɲɟ", "nk", "ŋk", "ng", "ŋg", "nɡ", "ŋɡ", "nz", "nʒ", "pf", "bv", "tf", "dv", "kf", "gv",
              "ɡv", "kp", "gb", "ɡb", "bl", "b̥", "g̥", "ɡ̥", "d̥", "d̥", "ts"]
vowels = ["ə̀", "ʃ", "ʔ", "~", "ṵ̌", "ṵ̂", "â̰", "à̰", "ḭ́", "ḭ̂", "̰ḭ̀", "ɛ̰̂", "ɛ̰̂ ", "ɔ̰̀", "ɔ̰́", "á̰", "̰ṵ̀",
          "ṵ̂", "ḛ̀", "ǎ̰", "â̰", "ɛ̰̌", "ḭ̀", "ḛ́", "d̰̀", "̰à̰", "̰ŋ", "ṵ̀", "à̰", "̰̀l", "l", "ɔ̰̂", "̰ɛ", "Ù",
          "À", "Ê", "V̂", "Ô", "áʰ", "ǐ", "ǒ", "ǎ", "ɩ̌", "ɩ", "ê", "û", "î", "ɩ̌", "ô", "ê", "ɩ́", "ɩ̀", "ɩ̂", "I",
          "Í", "Ì", "Í", "Ì", "i", "í", "ì", "í", "ī", "ì", "ǐ", "î", "ɪ", "ɪ́", "ɪ̄", "ɪ̀", "ɪ", "̌", "ɪ̂", "E",
          "É", "È", "É", "È", "e", "é", "è", "é", "ē", "è", "ě", "ê", "ɛ", "ɛ́", "ɛ̄", "ɛ̀", "ɛ̌", "ɛ̂", "œ́",
          "œ̄", "œ̀", "œ̌", "œ̂", "A", "Á", "À", "Á", "À", "a", "á", "à", "á", "ā", "à", "ǎ", "â", "ə", "ə́",
          "ə̄", "ə̀", "ə̌", "ə̂", "U", "Ú", "Ù", "Ú", "Ù", "u", "ú", "ù", "ú", "ū", "ù", "ǔ", "û", "O", "Ó", "Ò",
          "Ó", "Ò", "o", "ó", "ò", "ó", "ō", "ò", "ǒ", "ô", "ʊ", "ʊ́", "ʊ̄", "ʊ̀", "ʊ̌", "ʊ̂", "ɔ", "ɔ́", "ɔ̄",
          "ɔ̀", "ɔ̌", "ɔ̂", "ø", "ǿ", "ø̄", "ø̀", "ø̌", "ø̂", "V", "V́", "V̀", "â", "I", "Í", "Ì", "Í", "Ì", "i",
          "í", "ì", "í", "ī", "ì", "ǐ", "î", "ɪ", "ɪ́", "ɪ̄", "ɪ̀", "ɪ", "̌", "ɪ̂", "E", "É", "È", "É", "È", "e",
          "é", "è", "é", "ē", "è", "ě", "ê", "ɛ", "ɛ́", "ɛ̄", "ɛ̀", "ɛ̌", "ɛ̂", "œ́", "œ̄", "œ̀", "œ̌", "œ̂", "A",
          "Á", "À", "Á", "À", "a", "á", "à", "á", "ā", "à", "ǎ", "â", "ə", "ə́", "ə̄", "ə̀", "ə̌", "ə̂", "U",
          "Ú", "Ù", "Ú", "Ù", "u", "ú", "ù", "ú", "ū", "ù", "ǔ", "û", "O", "Ó", "Ò", "Ó", "Ò", "o", "ó", "ò",
          "ó", "ō", "ò", "ǒ", "ô", "ʊ", "ʊ́", "ʊ̄", "ʊ̀", "ʊ̌", "ʊ̂", "ɔ", "ɔ́", "ɔ̄", "ɔ̀", "ɔ̌", "ɔ̂", "ø", "ǿ",
          "ø̄", "ø̀", "ø̌", "ø̂", "V", "V́", "V̀"]
'''
This part of the code determines weather a given character is a consonant or a vowel, based on the list of consonants and vowels it receives as input.
If the character is not in the consonant list, it will check the vowel list, and finally return the character, say if it is a consonant or not, then remove the character from the word it is reading, until all the characters have been treated.
'''


def get_first_letter(remainder, word, line_number):
    candidate_consonant = ""
    the_token = ""
    if remainder[0] in tokens:
        the_token = remainder[0]
        remainder = remainder[1:]
    for consonant in consonants:
        if remainder.startswith(consonant):
            if len(consonant) > len(candidate_consonant):
                candidate_consonant = consonant
    if candidate_consonant == "":
        candidate_vowel = ""
        for vowel in vowels:
            if remainder.startswith(vowel):
                if len(vowel) > len(candidate_vowel):
                    candidate_vowel = vowel
        if candidate_vowel == "":
            print(
                "error on line {line_number}: '{remainder}' in '{word}' starts with unknown character '{letter}'".format(
                    line_number=line_number, remainder=remainder, word=word, letter=hex(ord(remainder[0]))))
            return {"letter": "error", "is_consonant": False, "word": remainder}
        else:
            return {"letter": the_token + candidate_vowel, "is_consonant": False,
                    "word": remainder.removeprefix(candidate_vowel)}
    return {"letter": the_token + candidate_consonant, "is_consonant": True,
            "word": remainder.removeprefix(candidate_consonant)}


'''
This part of the code splits words into letters. It then calls for the get_first_letter def and loops over the characters until the word is finished.
'''


def split_word(word, line_number):
    result_letter_data = []
    error_found = False
    remainder = word
    while len(remainder) > 0 and not error_found:
        letter_data = get_first_letter(remainder, word, line_number)
        if letter_data["letter"] == "error":
            error_found = True
        result_letter_data.append(letter_data)
        remainder = letter_data["word"]
    return result_letter_data


splittable_columns = ["PA80", "swo", "gyeli", "bekwel", "bekol", "konzime", "makaa", "mpiemo", "kwasio", "njyem",
                      "shiwa", "Reconstr. Régionales (BLR 3)", "Reconstr. Mougiama, Hombert"]
languages = ["PA80", "swo", "gyeli", "bekwel", "bekol", "konzime", "makaa", "mpiemo", "kwasio", "njyem", "shiwa",
             "Reconstr. Régionales (BLR 3)", "Reconstr. Mougiama, Hombert"]


def split_words_in_a_line(line):
    split_words = {}
    line_number = line['nº']
    for column in splittable_columns:
        if column in line:
            split_words.update({column: split_word(line[column], line_number)})
    return split_words


def split_words_in_a_file(datafile):
    if datafile.endswith(".csv"):
        data = read_and_process_csv_file(datafile)
    elif datafile.endswith(".xlsx"):
        data = read_and_process_excel_file(datafile)
    else:
        raise ValueError("The file must be a .csv or .xlsx file")
    split_lines = []
    for line in data:
        split_words = split_words_in_a_line(line)
        split_lines.append({'line': line['nº'], 'FR': line['FR'], 'languages': split_words})
    return split_lines
