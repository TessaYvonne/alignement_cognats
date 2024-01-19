from reconstructions import reconstruction, read_and_process_data, is_diacritic


def test_string_without_token_remains_unchanged():
    assert reconstruction("aŋ", ["º", "*"]) == "aŋ"


def test_degree_is_added_to_string_with_parentheses():
    assert reconstruction("ºa(ŋ)c", ["º"]) == "ºaº(ŋ)ºc"


def test_star_is_added_to_string_with_parentheses():
    assert reconstruction("*a(ŋ)c", ["*"]) == "*a*(ŋ)*c"


def test_tokens_are_added_to_string_with_parentheses_and_diacritics():
    assert reconstruction("*á(ŋ)ć", ["*"]) == "*á*(ŋ)*ć"


def test_tokens_are_added_to_string_with_closing_parenthesis_at_the_end():
    assert reconstruction("*á(ŋ)", ["*"]) == "*á*(ŋ)"


def test_error_is_returned_if_opening_parenthesis_is_last_character():
    assert reconstruction("*á(", ["*"]) == "Warning: formatting error in '*á('"


def test_tokens_are_added_to_string_with_opening_parenthesis_at_the_beginning():
    assert reconstruction("*(ŋ)ɔ́", ["*"]) == "*(ŋ)*ɔ́"


def test_error_is_returned_if_closing_parenthesis_is_missing():
    assert reconstruction("*á(ŋ", ["*"]) == "Warning: formatting error in '*á(ŋ'"


def test_tokens_are_added_to_string_with_more_than_one_element_between_parentheses():
    assert reconstruction("*á(ŋb)", ["*"]) == "*á*(ŋb)"


def test_token_is_added_with_empty_string_in_parentheses():
    assert reconstruction("*á()", ["*"]) == "Warning: formatting error in '*á()'"


def test_string_of_spaces_remains_unchanged():
    assert reconstruction(" ", ["*"]) == " "


def test_empty_string_remains_unchanged():
    assert reconstruction("", ["*"]) == ""


def test_error_is_returned_if_opening_parenthesis_is_missing():
    assert reconstruction("*áŋ)", ["*"]) == "Warning: formatting error in '*áŋ)'"


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


def test_is_diacritic():
    assert is_diacritic("\u02B0")
    assert is_diacritic("\u02FF")
    assert is_diacritic("\u0300")
    assert is_diacritic("\u036F")
    assert not is_diacritic("\u0370")
