from letter_splitter import get_first_letter, split_word, split_words_in_a_file, Word


def test_letter_splitter_finds_kind_of_character():
    assert get_first_letter("ɲɟ", "ɲɟ", 1) == {"letter": "ɲɟ", "is_consonant": True, "word": ""}
    assert get_first_letter("ɲɲɟ", "ɲɲɟ", 1) == {"letter": "ɲ", "is_consonant": True, "word": "ɲɟ"}
    assert get_first_letter("à", "à", 1) == {"letter": "à", "is_consonant": False, "word": ""}
    assert get_first_letter("[", "[", 1) == {"letter": "error", "is_consonant": False, "word": "["}


def test_letter_splitter_splits_word():
    assert split_word(Word("ɲɟà", ""), 1) == Word("ɲɟà", "", [{"letter": "ɲɟ", "is_consonant": True, "word": "à"},
                                                                {"letter": "à", "is_consonant": False, "word": ""}])
    assert split_word(Word("bw", ""), 1) == Word("bw", "", [{"letter": "b", "is_consonant": True, "word": "w"},
                                                            {"letter": "w", "is_consonant": True, "word": ""}])
    assert split_word(Word("àw", ""), 1) == Word("àw", "", [{"letter": "à", "is_consonant": False, "word": "w"},
                                                              {"letter": "w", "is_consonant": True, "word": ""}])


def test_letter_splitter_rejects_unknown_letters():
    assert split_word(Word("a$̀",""), 1) == Word("a$̀", "", [{"letter": "a", "is_consonant": False, "word": "$̀"},
                                                {"letter": "error", "is_consonant": False, "word": "$̀"}])


def test_letter_splitter_accepts_special_tokens():
    assert split_word(Word("°à°w",""), 1) == Word("°à°w", "", [{"letter": "°à", "is_consonant": False, "word": "°w"},
                                                    {"letter": "°w", "is_consonant": True, "word": ""}])
    assert split_word(Word("*à*w",""), 1) == Word("*à*w", "", [{"letter": "*à", "is_consonant": False, "word": "*w"},
                                                    {"letter": "*w", "is_consonant": True, "word": ""}])


def test_split_words_in_a_csv_file():
    word_data = split_words_in_a_file("line9.csv")
    assert (word_data[0]['line'] == '9.')
    assert (word_data[0]['FR'] == 'accoucher')
    assert (len(word_data[0]['languages']) == 13)
    languages = word_data[0]['languages']
    assert (languages['PA80'].text == "°b°í°à")
    assert (languages['PA80'].letters == [{'is_consonant': True,
                                           'letter': '°b',
                                           'word': '°í°à'},
                                          {'is_consonant': False,
                                           'letter': '°í',
                                           'word': '°à'},
                                          {'is_consonant': False, 'letter': '°à', 'word': ''}])


def test_split_words_in_a_excel_file():
    word_data = split_words_in_a_file("line9.xlsx")
    assert (word_data[0]['line'] == '9.')
    assert (word_data[0]['FR'] == 'accoucher')
    assert (len(word_data[0]['languages']) == 13)
    languages = word_data[0]['languages']
    assert (languages['PA80'].text == "°b°í°à")
    assert (languages['PA80'].letters == [{'is_consonant': True,
                                           'letter': '°b',
                                           'word': '°í°à'},
                                          {'is_consonant': False,
                                           'letter': '°í',
                                           'word': '°à'},
                                          {'is_consonant': False, 'letter': '°à', 'word': ''}])
