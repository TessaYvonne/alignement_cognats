from alignement_cognats import reconstruction, read_and_process_data


def test_string_without_token_remains_unchanged():
    assert reconstruction("aŋ", ["º"]) == "aŋ"


def test_token_is_added_to_a_string_with_parentheses():
    assert reconstruction("ºa(ŋ)c", ["º"]) == "ºaº(ŋ)ºc"


def test_asterisk_as_token():
    assert reconstruction("aŋ", ["*"]) == "aŋ"


def test_asterisk_as_token_with_parentheses():
    assert reconstruction("*a(ŋ)c", ["*"]) == "*a*(ŋ)*c"


def test_add_asterisks_in_string_with_parenthesis():
    assert reconstruction("*á(ŋ)ć", ["*"]) == "*á*(ŋ)*ć"


def test_reconstructions_adds_special_token():
    assert reconstruction("*á(ŋ)ć", ["*", "º", "°"]) == "*á*(ŋ)*ć"
    assert reconstruction("°á(ŋ)ć", ["*", "º", "°"]) == "°á°(ŋ)°ć"
    assert reconstruction("ºá(ŋ)ć", ["*", "º", "°"]) == "ºáº(ŋ)ºć"
    assert reconstruction("", ["*", "º", "°"]) == ""
    assert reconstruction("á(ŋ)ć", ["*", "º", "°"]) == "á(ŋ)ć"


def test_read_and_process_data():
    data = read_and_process_data("test_data_one_line.csv")
    assert data == [
        ["1.", "abandonner 1", "ºcºìºnºà", "", "", "cìn", "", "cìnè", "", "", "", "cììnò", "", "", "",
         "*c*ì*n*e", "", "", ""]]
