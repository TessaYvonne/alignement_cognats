from alignement_cognats import reconstruction_PA80


def test_string_without_token_remains_unchanged():
    assert reconstruction_PA80("aŋ", "º") == "aŋ"


def test_token_is_added_to_a_string_with_parentheses():
    assert reconstruction_PA80("ºa(ŋ)c", "º") == "ºaº(ŋ)ºc"


def test_asterisk_as_token():
    assert reconstruction_PA80("aŋ", "*") == "aŋ"


def test_asterisk_as_token_with_parentheses():
    assert reconstruction_PA80("*a(ŋ)c", "*") == "*a*(ŋ)*c"


def test_add_asterisks_in_string_with_parenthesis():
    assert reconstruction_PA80("*á(ŋ)ć", "*") == "*á*(ŋ)*ć"
