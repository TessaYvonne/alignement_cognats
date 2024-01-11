#GENERAL INTRODUCTION
'''
Code to align data from more than one language based on the position of the element within the word.
The positions are on the horizontal axis, the words in the different languages on the vertical axis.
The element of each word is aligned: the first consonant in C1, the first vowel in V1, etc.
'''

#DATA CLEANING SECTION
'''
First, we strip the raw data of characters that are not necessary for the comparison analysis. 
In my case, this is a slash separating singular and plural forms; elements between brackets, and prefixes.
The function def cleanup_all combines all the clean-up functions together. 
'''
def cleanup_slash(raw_data):
    index_of_slash = raw_data.find("/")
    result = raw_data
    if (index_of_slash >= 0):
        result = raw_data[:index_of_slash]
    result = result.strip()
    return(result)


def cleanup_parenthesis(raw_data):
    index_of_parenthesis = raw_data.find("(")
    result = raw_data
    if (index_of_parenthesis >= 0):
        result = raw_data[:index_of_parenthesis]
    result = result.strip()
    return(result)


def cleanup_prefix(raw_data):
    index_of_dash = raw_data.find("-")
    result = raw_data
    if (index_of_dash >= 0):
        result = raw_data[(index_of_dash+1):]
    result = result.strip()
    return(result)


def cleanup_all(raw_data):
    return(cleanup_prefix(cleanup_parenthesis(cleanup_slash(raw_data))))


#Clean-up tests

cleanup_testdata = cleanup_all("d-ɔ̀l (fskbvs) / m-ɔ̀l")
if (cleanup_testdata == "ɔ̀l"):
    print("OK: clean_data = ɔ̀l")
else:
    print("clean_data = '{clean_data}' but expected 'ɔ̀l'".format(clean_data=cleanup_testdata))


#RECONSTRUCTION SECTION
'''
In this section, we work on reconstructed forms. I want the final table to reflect which elements are reconstructed.
The code first looks for reconstructed words, indicated in the raw data with a º or a *.
It then adds these characters to each element of the word before aligning it in the final table.
Brackets are ignored, as well as diacritics.
'''
def is_diacritic(letter):
    return (letter >= "\u02B0" and letter <= "\u02FF") or (letter >= "\u0300" and letter <= "\u036F")


for diacritic in ["\u02B0", "\u02FF", "\u0300", "\u036F"]:
    if is_diacritic(diacritic):
        print(f"OK: is_diacritic {diacritic} = diacritic")
    else:
        print(f"expected {diacritic} to be a diacritic")

if not is_diacritic("\u0370"):
    print("OK: is_diacritic \u0370 = false")
else:
    print("expected \u0370 to not be a diacritic")

def reconstruction_PA80(raw_data, token):
    letters = list(raw_data)
    if letters[0] != token:
        return(raw_data)
    result = ""
    in_paren = False
    for letter in letters[1:]:
        if not in_paren:
            if not is_diacritic(letter):
                result += token
        result += letter
        if letter == "(":
            in_paren = True
        else:
            if letter == ")":
                in_paren = False
    return(result)


#Reconstruction tests
reconstruction_testdata = reconstruction_PA80("aŋ", "º")
expected_result = "aŋ"
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")

reconstruction_testdata = reconstruction_PA80("ºa(ŋ)c", "º")
expected_result = "ºaº(ŋ)ºc"
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")

reconstruction_testdata = reconstruction_PA80("aŋ", "*")
expected_result = "aŋ"
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")

#Are brackets ignored?
reconstruction_testdata = reconstruction_PA80("*a(ŋ)c", "*")
expected_result = "*a*(ŋ)*c"
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")

#Are diacritics ignored?
reconstruction_testdata = reconstruction_PA80("*á(ŋ)ć", "*")
expected_result = "*á*(ŋ)*ć"
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")

#Does it work with the closing bracket in final position?
reconstruction_testdata = reconstruction_PA80("*á(ŋ)", "*")
expected_result = "*á*(ŋ)"
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")

#Does it work with the opening bracket in final position?
reconstruction_testdata = reconstruction_PA80("*á(", "*")
expected_result = "*á("
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")

#Does it work with the opening bracket in the first position?
reconstruction_testdata = reconstruction_PA80("*(ŋ)ɔ́", "*")
expected_result = "*(ŋ)*ɔ́"
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")

#Does it work with no closing bracket?
reconstruction_testdata = reconstruction_PA80("*á(ŋ", "*")
expected_result = "*á*(ŋ"
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")

#Does it work with more than one element between brackets?
reconstruction_testdata = reconstruction_PA80("*á(ŋb)", "*")
expected_result = "*á*(ŋb)"
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")

#Does it work with empty brackets?
reconstruction_testdata = reconstruction_PA80("*á()", "*")
expected_result = "*á*()"
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")

#Does it work with a space within the brackets?
reconstruction_testdata = reconstruction_PA80("*á( )", "*")
expected_result = "*á*( )"
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")

#Does it work with empty input?
reconstruction_testdata = reconstruction_PA80(" ", "*")
expected_result = " "
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")

#Does it work with only a closing bracket?
reconstruction_testdata = reconstruction_PA80("*áŋ)", "*")
expected_result = "*á*ŋ)"
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"formatting error: '{reconstruction_testdata}'")
