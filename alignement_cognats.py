#data clean section
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


cleanup_testdata = cleanup_all("d-ɔ̀l (fskbvs) / m-ɔ̀l")
if (cleanup_testdata == "ɔ̀l"):
    print("OK: clean_data = ɔ̀l")
else:
    print("clean_data = '{clean_data}' but expected 'ɔ̀l'".format(clean_data=cleanup_testdata))

#reconstruction section
'''
If first letter = º: bb
make list of letters
if letter =/ ( : false
if letter = ( : true
add to 'result' º(
if ( is seen, add next letter without º
make function to detect ) 
if letter = ) :
'''
def reconstruction_PA80(raw_data, token):
    letters = list(raw_data)
    if letters[0] != token:
        return(raw_data)
    result = ""
    in_paren = False
    for letter in letters[1:]:
        if not in_paren:
            result += token
        result += letter
        if letter == "(":
            in_paren = True
        else:
            if letter == ")":
                in_paren = False
    return(result)

#reconstruction_testdata = reconstruction_PA80("ºaŋ")
#expected_result = "ºaŋ"
#if (reconstruction_testdata == expected_result):
#    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
#else:
#    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")

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

reconstruction_testdata = reconstruction_PA80("*a(ŋ)c", "*")
expected_result = "*a*(ŋ)*c"
if (reconstruction_testdata == expected_result):
    print("OK: reconstruction_testdata = {result}".format(result = expected_result))
else:
    print(f"reconstruction = '{reconstruction_testdata}' but expected {expected_result}")
