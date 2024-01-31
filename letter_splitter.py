from reconstructions import tokens

from reconstructions import read_and_process_data

consonants = ["ndʰ","nkʷ","ndʰ","kʷ","mbʰ","ʁ","bʰ","dʰ","P","ˤ","C","Ǹ","N","T","K","w","y","j","p","b","ɓ","t","d","ɗ","c","ɟ","k","g","ɡ","ʔ","m","n","ɲ","ŋ","ɳ","ɾ","r","f","v","s","z","ʃ","ʒ","h","l","ɥ","mp","mb","nt","nd","nc","nɟ","ɲɟ","nk","ŋk","ng","ŋg","nɡ","ŋɡ","nz","nʒ","pf","bv","tf","dv","kf","gv","ɡv","kp","gb","ɡb","bl","b̥","g̥","ɡ̥","d̥","d̥","ts"]
vowels = ["ǐ","ǒ","ǎ","ɩ̌","ɩ","ê","û","î","ɩ̌","ô","ê","ɩ́","ɩ̀","ɩ̂","I","Í","Ì","Í","Ì","i","í","ì","í","ī","ì","ǐ","î","ɪ","ɪ́","ɪ̄","ɪ̀","ɪ","̌","ɪ̂","E","É","È","É","È","e","é","è","é","ē","è","ě","ê","ɛ","ɛ́","ɛ̄","ɛ̀","ɛ̌","ɛ̂","œ́","œ̄","œ̀","œ̌","œ̂","A","Á","À","Á","À","a","á","à","á","ā","à","ǎ","â","ə","ə́","ə̄","ə̀","ə̌","ə̂","U","Ú","Ù","Ú","Ù","u","ú","ù","ú","ū","ù","ǔ","û","O","Ó","Ò","Ó","Ò","o","ó","ò","ó","ō","ò","ǒ","ô","ʊ","ʊ́","ʊ̄","ʊ̀","ʊ̌","ʊ̂","ɔ","ɔ́","ɔ̄","ɔ̀","ɔ̌","ɔ̂","ø","ǿ","ø̄","ø̀","ø̌","ø̂","V","V́","V̀","â","I","Í","Ì","Í","Ì","i","í","ì","í","ī","ì","ǐ","î","ɪ","ɪ́","ɪ̄","ɪ̀","ɪ","̌","ɪ̂","E","É","È","É","È","e","é","è","é","ē","è","ě","ê","ɛ","ɛ́","ɛ̄","ɛ̀","ɛ̌","ɛ̂","œ́","œ̄","œ̀","œ̌","œ̂","A","Á","À","Á","À","a","á","à","á","ā","à","ǎ","â","ə","ə́","ə̄","ə̀","ə̌","ə̂","U","Ú","Ù","Ú","Ù","u","ú","ù","ú","ū","ù","ǔ","û","O","Ó","Ò","Ó","Ò","o","ó","ò","ó","ō","ò","ǒ","ô","ʊ","ʊ́","ʊ̄","ʊ̀","ʊ̌","ʊ̂","ɔ","ɔ́","ɔ̄","ɔ̀","ɔ̌","ɔ̂","ø","ǿ","ø̄","ø̀","ø̌","ø̂","V","V́","V̀"]
'''
This part of the code determines weather a given character is a consonant or a vowel, based on the list of consonants and vowels it receives as input.
If the character is not in the consonant list, it will check the vowel list, and finally return the character, say if it is a consonant or not, then remove the character from the word it is reading, until all the characters have been treated.
'''


def get_first_letter(word):
    candidate_consonant = ""
    the_token = ""
    if word[0] in tokens:
        the_token = word[0]
        word = word[1:]
    for consonant in consonants:
        if word.startswith(consonant):
            if len(consonant) > len(candidate_consonant):
                candidate_consonant = consonant
    if candidate_consonant == "":
        candidate_vowel = ""
        for vowel in vowels:
            if word.startswith(vowel):
                if len(vowel) > len(candidate_vowel):
                    candidate_vowel = vowel
        if candidate_vowel == "":
            print("error: {word} starts with unknown character".format(word=word))
            return {"letter": "error", "is_consonant": False, "word": word}
        else:
            return {"letter": the_token + candidate_vowel, "is_consonant": False, "word": word.removeprefix(candidate_vowel)}
    return {"letter": the_token + candidate_consonant, "is_consonant": True, "word": word.removeprefix(candidate_consonant)}


'''
This part of the code splits words into letters. It then calls for the get_first_letter def and loops over the characters until the word is finished.
'''


def split_word(word):
    result_letter_data = []
    error_found = False
    while len(word) > 0 and not error_found:
        letter_data = get_first_letter(word)
        if letter_data["letter"] == "error":
            error_found = True
        result_letter_data.append(letter_data)
        word = letter_data["word"]
    return result_letter_data


splittable_columns = ["PA80","swo","gyeli","bekwel","bekol","konzime","makaa","mpiemo","kwasio","njyem","shiwa","Reconstr. Régionales (BLR 3)","Reconstr. Mougiama, Hombert"]
languages = ["PA80","swo","gyeli","bekwel","bekol","konzime","makaa","mpiemo","kwasio","njyem","shiwa","Reconstr. Régionales (BLR 3)","Reconstr. Mougiama, Hombert"]


def split_words_in_a_line(line):
    split_words = {}
    for column in splittable_columns:
        if column in line:
            split_words.update({column: split_word(line[column])})
    return split_words


def split_words_in_a_file(datafile):
    data = read_and_process_data(datafile)
    split_lines = []
    for line in data:
        split_words = split_words_in_a_line(line)
        split_lines.append({'line': line['nº'], 'FR': line['FR'], 'languages':split_words})
    return split_lines
