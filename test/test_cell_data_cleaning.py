from alignement_cognats import reconstruction_PA80


def test_string_without_token_remains_unchanged():
    reconstruction_testdata = reconstruction_PA80("aŋ", "º")
    assert reconstruction_testdata == "aŋ"


def test_token_is_added_to_a_string_with_parentheses():
    reconstruction_testdata = reconstruction_PA80("ºa(ŋ)c", "º")
    assert reconstruction_testdata == "ºaº(ŋ)ºc"


def test_asterisk_as_token():
    reconstruction_testdata = reconstruction_PA80("aŋ", "*")
    assert reconstruction_testdata == "aŋ"


def test_asterisk_as_token_with_parentheses():
    reconstruction_testdata = reconstruction_PA80("*a(ŋ)c", "*")
    assert reconstruction_testdata == "*a*(ŋ)*c"


def test_add_asterisks_in_string_with_parenthesis():
    reconstruction_testdata = reconstruction_PA80("*á(ŋ)ć", "*")
    assert reconstruction_testdata == "*á*(ŋ)*ć"
