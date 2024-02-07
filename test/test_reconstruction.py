from reconstructions import reconstruction, read_and_process_csv_file, is_diacritic, read_and_process_excel_file


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

def test_temp():
    assert reconstruction("*ci", ["*"]) == "*c*i"


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


def test_read_and_process_csv_file():
    data = read_and_process_csv_file("test_data_one_line.csv")
    expected = [
        {"nº": "1.", "FR": "abandonner 1", "PA80": "ºcºìºnºà", "swo": "", "gyeli": "", "bekwel": "cìn", "bekol": "",
         "konzime": "cìnè", "makaa": "", "mpiemo": "", "kwasio": "", "njyem": "cììnò", "shiwa": "",
         "BC (BLR3)": "", "Reconstr. Régionales (BLR 3)": "", "Reconstr. Mougiama, Hombert": "*c*ì*n*e"}]
    assert data == expected


def test_read_and_process_excel_file():
    data = read_and_process_excel_file("3lines.xlsx")
    expected = [
        {'BC (BLR3)': 'bc1',
          'FR': 'fr1',
          'PA80': 'pa801',
          'Reconstr. Mougiama, Hombert': 'mougiama1',
          'Reconstr. Régionales (BLR 3)': 'blr1',
          'bekol': 'bekol1',
          'bekwel': 'bewel1',
          'gyeli': 'gyeli1',
          'konzime': 'konzime1',
          'kwasio': 'kwasio1',
          'makaa': 'makaa1',
          'mpiemo': 'mpiemo1',
          'njyem': 'njyem1',
          'nº': '1',
          'shiwa': 'shiwa1',
          'swo': 'sow1'},
         {'BC (BLR3)': 'bc2',
          'FR': 'fr2',
          'PA80': 'pa802',
          'Reconstr. Mougiama, Hombert': 'mougiama2',
          'Reconstr. Régionales (BLR 3)': 'blr2',
          'bekol': 'bekol2',
          'bekwel': 'bewel2',
          'gyeli': 'gyeli2',
          'konzime': 'konzime2',
          'kwasio': 'kwasio2',
          'makaa': 'makaa2',
          'mpiemo': 'mpiemo2',
          'njyem': 'njyem2',
          'nº': '2',
          'shiwa': 'shiwa2',
          'swo': 'sow2'}]
    assert data == expected


def test_is_diacritic():
    assert is_diacritic("\u02B0")
    assert is_diacritic("\u02FF")
    assert is_diacritic("\u0300")
    assert is_diacritic("\u036F")
    assert not is_diacritic("\u0370")
