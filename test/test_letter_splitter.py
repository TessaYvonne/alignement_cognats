from letter_splitter import get_first_letter, split_word, split_words_in_a_file


def test_letter_splitter_finds_kind_of_character():
    assert get_first_letter("ɲɟ","ɲɟ") == {"letter": "ɲɟ", "is_consonant": True, "word": ""}
    assert get_first_letter("ɲɲɟ","ɲɲɟ") == {"letter": "ɲ", "is_consonant": True, "word": "ɲɟ"}
    assert get_first_letter("à","à") == {"letter": "à", "is_consonant": False, "word": ""}
    assert get_first_letter("[","[") == {"letter": "error", "is_consonant": False, "word": "["}


def test_letter_splitter_splits_word():
    assert split_word("ɲɟà") == [{"letter": "ɲɟ", "is_consonant": True, "word": "à"},
                                  {"letter": "à", "is_consonant": False, "word": ""}]
    assert split_word("bw") == [{"letter": "b", "is_consonant": True, "word": "w"},
                                {"letter": "w", "is_consonant": True, "word": ""}]
    assert split_word("àw") == [{"letter": "à", "is_consonant": False, "word": "w"},
                                 {"letter": "w", "is_consonant": True, "word": ""}]


def test_letter_splitter_rejects_unknown_letters():
    assert split_word("a$̀") == [{"letter": "a", "is_consonant": False, "word": "$̀"},
                                {"letter": "error", "is_consonant": False,  "word": "$̀"}]


def test_letter_splitter_accepts_special_tokens():
    assert split_word("°à°w") == [{"letter": "°à", "is_consonant": False, "word": "°w"},
                                 {"letter": "°w", "is_consonant": True, "word": ""}]
    assert split_word("*à*w") == [{"letter": "*à", "is_consonant": False, "word": "*w"},
                                 {"letter": "*w", "is_consonant": True, "word": ""}]


def test_split_words_in_a_file():
    assert (split_words_in_a_file("line9.csv") ==
            [{'line': '9.', 'FR': 'accoucher',
              'languages':{'PA80': [{'is_consonant': True,
                                     'letter': '°b',
                                     'word': '°í°à'},
                                    {'is_consonant': False,
                                     'letter': '°í',
                                     'word': '°à'},
                                    {'is_consonant': False, 'letter': '°à', 'word': ''}],
                            'swo':
                                [{'letter': 'b',
                                  'is_consonant': True,
                                  'word': 'yâ'},
                                 {'letter': 'y',
                                  'is_consonant': True,
                                  'word': 'â'},
                                 {'letter': 'â',
                                  'is_consonant': False,
                                  'word': ''}],
                            'gyeli':
                                [{'letter': 'b',
                                  'is_consonant': True,
                                  'word': 'wà'},
                                 {'letter': 'w',
                                  'is_consonant': True,
                                  'word': 'à'},
                                 {'letter': 'à',
                                  'is_consonant': False,
                                  'word': ''}],
                            'bekwel':
                                [{'letter': 'b',
                                  'is_consonant': True,
                                  'word': 'jâ'},
                                 {'letter': 'j',
                                  'is_consonant': True,
                                  'word': 'â'},
                                 {'letter': 'â',
                                  'is_consonant': False,
                                  'word': ''}],
                            'bekol':
                                [{'letter': 'b',
                                  'is_consonant': True,
                                  'word': 'jâ'},
                                 {'letter': 'j',
                                  'is_consonant': True,
                                  'word': 'â'},
                                 {'letter': 'â',
                                  'is_consonant': False,
                                  'word': ''}],
                            'konzime':
                                [{'letter': 'b',
                                  'is_consonant': True,
                                  'word': 'jâ'},
                                 {'letter': 'j',
                                  'is_consonant': True,
                                  'word': 'â'},
                                 {'letter': 'â',
                                  'is_consonant': False,
                                  'word': ''}],
                            'makaa':
                                [{'letter': 'b',
                                  'is_consonant': True,
                                  'word': 'jâ'},
                                 {'letter': 'j',
                                  'is_consonant': True,
                                  'word': 'â'},
                                 {'letter': 'â',
                                  'is_consonant': False,
                                  'word': ''}],
                            'mpiemo':
                                [{'letter': 'ɓ',
                                  'is_consonant': True,
                                  'word': 'jâ'},
                                 {'letter': 'j',
                                  'is_consonant': True,
                                  'word': 'â'},
                                 {'letter': 'â',
                                  'is_consonant': False,
                                  'word': ''}],
                            'kwasio':
                                [{'letter': 'b',
                                  'is_consonant': True,
                                  'word': 'ia'},
                                 {'letter': 'i',
                                  'is_consonant': False,
                                  'word': 'a'},
                                 {'letter': 'a',
                                  'is_consonant': False,
                                  'word': ''}],
                            'njyem':
                                [{'letter': 'b',
                                  'is_consonant': True,
                                  'word': 'wâ'},
                                 {'letter': 'w',
                                  'is_consonant': True,
                                  'word': 'â'},
                                 {'letter': 'â',
                                  'is_consonant': False,
                                  'word': ''}],
                            'shiwa':
                                [{'letter': 'b',
                                  'is_consonant': True,
                                  'word': 'jà'},
                                 {'letter': 'j',
                                  'is_consonant': True,
                                  'word': 'à'},
                                 {'letter': 'à',
                                  'is_consonant': False,
                                  'word': ''}],
                            'Reconstr. Mougiama, Hombert': [],
                            'Reconstr. Régionales (BLR 3)': []
                            }}])
