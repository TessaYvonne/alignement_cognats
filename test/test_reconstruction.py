from Word import Word
from reconstructions import reconstruction, read_and_process_csv_file, is_diacritic, read_and_process_excel_file


def test_string_without_token_remains_unchanged():
    assert reconstruction(Word("aŋ", ""), ["º", "*"]) == Word("aŋ", "")


def test_degree_is_added_to_string_with_parentheses():
    assert reconstruction(Word("ºa(ŋ)c", ""), ["º"]) == Word("ºaº(ŋ)ºc", "")


def test_star_is_added_to_string_with_parentheses():
    assert reconstruction(Word("*a(ŋ)c", ""), ["*"]) == Word("*a*(ŋ)*c", "")


def test_tokens_are_added_to_string_with_parentheses_and_diacritics():
    assert reconstruction(Word("*á(ŋ)ć", ""), ["*"]) == Word("*á*(ŋ)*ć", "")


def test_tokens_are_added_to_string_with_closing_parenthesis_at_the_end():
    assert reconstruction(Word("*á(ŋ)", ""), ["*"]) == Word("*á*(ŋ)", "")


def test_error_is_returned_if_opening_parenthesis_is_last_character():
    assert reconstruction(Word("*á(", ""), ["*"]) == Word("Warning: formatting error in '*á('",'')


def test_tokens_are_added_to_string_with_opening_parenthesis_at_the_beginning():
    assert reconstruction(Word("*(ŋ)ɔ́", ""), ["*"]) == Word("*(ŋ)*ɔ́", "")


def test_error_is_returned_if_closing_parenthesis_is_missing():
    assert reconstruction(Word("*á(ŋ", ""), ["*"]) == Word("Warning: formatting error in '*á(ŋ'",'')


def test_tokens_are_added_to_string_with_more_than_one_element_between_parentheses():
    assert reconstruction(Word("*á(ŋb)", ""), ["*"]) == Word("*á*(ŋb)", "")


def test_temp():
    assert reconstruction(Word("*ci", ""), ["*"]) == Word("*c*i", "")


def test_token_is_added_with_empty_string_in_parentheses():
    assert reconstruction(Word("*á()", ""), ["*"]) == Word("Warning: formatting error in '*á()'",'')


def test_string_of_spaces_remains_unchanged():
    assert reconstruction(Word(" ", ""), ["*"]) == Word(" ", "")


def test_empty_string_remains_unchanged():
    assert reconstruction(Word("", ""), ["*"]) == Word("", "")


def test_error_is_returned_if_opening_parenthesis_is_missing():
    assert reconstruction(Word("*áŋ)", ""), ["*"]) == Word("Warning: formatting error in '*áŋ)'",'')


def test_reconstructions_adds_special_token():
    assert reconstruction(Word("*á(ŋ)ć", ""), ["*", "º", "°"]) == Word("*á*(ŋ)*ć", "")
    assert reconstruction(Word("°á(ŋ)ć", ""), ["*", "º", "°"]) == Word("°á°(ŋ)°ć", "")
    assert reconstruction(Word("ºá(ŋ)ć", ""), ["*", "º", "°"]) == Word("ºáº(ŋ)ºć", "")
    assert reconstruction(Word("", ""), ["*", "º", "°"]) == Word("", "")
    assert reconstruction(Word("á(ŋ)ć", ""), ["*", "º", "°"]) == Word("á(ŋ)ć", "")
    assert reconstruction(Word("ºcìnà", ""), ["*", "º"]) == Word("ºcºìºnºà", "")


def test_read_and_process_csv_file():
    data = read_and_process_csv_file("test_data_one_line.csv")
    expected = [
        {"nº": "1.", "FR": "abandonner 1", "PA80": Word("°c°ì°n°à", "(N-)"), "swo": Word("", ""),
         "gyeli": Word("", ""), "bekwel": Word("cìn", "ɛ̀-"), "bekol": Word("", ""),
         "konzime": Word("cìnè", "è-"), "makaa": Word("", ""), "mpiemo": Word("", ""),
         "kwasio": Word("", ""), "njyem": Word("cììnò", "lè-"), "shiwa": Word("", ""),
         "BC (BLR3)": Word("", ""), "Reconstr. Régionales (BLR 3)": Word("", ""),
         "Reconstr. Mougiama, Hombert": Word("*c*ì*n*e", "")}]
    assert data == expected


# TODO: fix this
def xx_read_and_process_excel_file():
    data = read_and_process_excel_file("3lines.xlsx")
    record1 = {"BC (BLR3)": Word("bc1", ""),
               "FR": "fr1",
               "PA80": Word("pa801", ""),
               "Reconstr. Mougiama,""), Hombert": Word("mougiama1", ""),
               "Reconstr. Régionales (BLR 3)": Word("blr1", ""),
               "bekol": Word("bekol1", ""),
               "bekwel": Word("bewel1", ""),
               "gyeli": Word("gyeli1", ""),
               "konzime": Word("konzime1", ""),
               "kwasio": Word("kwasio1", ""),
               "makaa": Word("makaa1", ""),
               "mpiemo": Word("mpiemo1", ""),
               "njyem": Word("njyem1", ""),
               "nº": "1.",
               "shiwa": Word("shiwa1", ""),
               "swo": Word("sow1", "")}
    record2 = {"BC (BLR3)": Word("bc2", ""),
               "FR": "fr2",
               "PA80": Word("pa802", ""),
               "Reconstr. Mougiama,""), Hombert": Word("mougiama2", ""),
               "Reconstr. Régionales (BLR 3)": Word("blr2", ""),
               "bekol": Word("bekol2", ""),
               "bekwel": Word("bewel2", ""),
               "gyeli": Word("gyeli2", ""),
               "konzime": Word("konzime2", ""),
               "kwasio": Word("kwasio2", ""),
               "makaa": Word("makaa2", ""),
               "mpiemo": Word("mpiemo2", ""),
               "njyem": Word("njyem2", ""),
               "nº": "2.",
               "shiwa": Word("shiwa2", ""),
               "swo": Word("sow2", "")
               }
    expected = [
        record1,
        record2]
    assert data[0] == record1
    assert data[1] == record2
    # assert data == expected


def test_is_diacritic():
    assert is_diacritic("\u02B0")
    assert is_diacritic("\u02FF")
    assert is_diacritic("\u0300")
    assert is_diacritic("\u036F")
    assert not is_diacritic("\u0370")
