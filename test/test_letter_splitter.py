from letter_splitter import get_first_letter, split_word


def test_letter_splitter_finds_kind_of_character() :
    assert get_first_letter("ɲɟ") == {"letter": "ɲɟ", "is_consonant": True, "word": ""}
    assert get_first_letter("ɲɲɟ") == {"letter": "ɲ", "is_consonant": True, "word": "ɲɟ"}
    assert get_first_letter("à") == {"letter": "à", "is_consonant": False, "word": ""}
    assert get_first_letter("[") == {"letter": "error", "is_consonant": False, "word": "["}


def test_letter_splitter_splits_word():
    assert split_word("ɲɟà") == [{"letter": "ɲɟ", "is_consonant": True, "word": "à"}, {"letter": "à", "is_consonant": False, "word": ""}]