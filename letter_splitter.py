consonants = ["p","b","ɓ","t","d","ɗ","c","ɟ","k","g","ɡ","ʔ","m","n","ɲ","ŋ","ɳ","ɾ","r","f","v","s","z","ʃ","ʒ","h","l","ɥ","mp","mb","nt","nd","nc","nɟ","ɲɟ","nk","ŋk","ng","ŋg","nɡ","ŋɡ","nz","nʒ","pf","bv","tf","dv","kf","gv","ɡv","kp","gb","ɡb","bl","b̥","g̥","ɡ̥","d̥"]
vowels = ["I","Í","Ì","Í","Ì","i","í","ì","í","ī","ì","ǐ","î","ɪ","ɪ́","ɪ̄","ɪ̀","ɪ","̌","ɪ̂","E","É","È","É","È","e","é","è","é","ē","è","ě","ê","ɛ","ɛ́","ɛ̄","ɛ̀","ɛ̌","ɛ̂","œ́","œ̄","œ̀","œ̌","œ̂","A","Á","À","Á","À","a","á","à","á","ā","à","ǎ","â","ə","ə́","ə̄","ə̀","ə̌","ə̂","U","Ú","Ù","Ú","Ù","u","ú","ù","ú","ū","ù","ǔ","û","O","Ó","Ò","Ó","Ò","o","ó","ò","ó","ō","ò","ǒ","ô","ʊ","ʊ́","ʊ̄","ʊ̀","ʊ̌","ʊ̂","ɔ","ɔ́","ɔ̄","ɔ̀","ɔ̌","ɔ̂","ø","ǿ","ø̄","ø̀","ø̌","ø̂","V","V́","V̀"]


def get_first_letter(word):
    candidate_consonant = ""
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
            return {"letter": candidate_vowel, "is_consonant": False, "word": word.removeprefix(candidate_vowel)}
    return {"letter": candidate_consonant, "is_consonant": True, "word": word.removeprefix(candidate_consonant)}


def split_word(word):
    letters = []
    while len(word) > 0:
        letter = get_first_letter(word)
        letters.append(letter)
        word = letter["word"]
    return letters



