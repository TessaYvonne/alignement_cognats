from letter_splitter import split_words_in_a_file
from output import letters_to_output_format, word_data_to_csv, matrix_to_csv


def test_swo_letter_data_is_correct():
    swo_data = [{'letter': 'b', 'is_consonant': True, 'word': 'yâ'},
                {'letter': 'y', 'is_consonant': True, 'word': 'â'},
                {'letter': 'â', 'is_consonant': False, 'word': ''}]
    assert (letters_to_output_format(swo_data) ==
            {'C1a': 'b','C1b': 'y','V1a': 'â','V1b': '','C2a': '',
              'C2b': '','V2a': '','V2b': '','C3a': '','C3b': '','V3a': '','V3b': ''},)


def test_word_to_output():
    data = split_words_in_a_file('line9.csv')
    assert word_data_to_csv(data[0]) == [['9.', 'accoucher', '', '', '', '', '', '', '', '', '', '', '', ''],
                                         ['', '', 'C1a', 'C1b', 'V1a', 'V1b', 'C2a', 'C2b', 'V2a', 'V2b', 'C3a', 'C3b', 'V3a', 'V3b'],
                                         ['', 'swo', 'b', 'y', 'â', '', '', '', '', '', '', '', '', ''],
                                         ['', 'gyeli', 'b', 'w', 'à', '', '', '', '', '', '', '', '', ''],
                                         ['', 'bekwel', 'b', 'j', 'â', '', '', '', '', '', '', '', '', ''],
                                         ['', 'bekol', 'b', 'j', 'â', '', '', '', '', '', '', '', '', ''],
                                         ['', 'konzime', 'b', 'j', 'â', '', '', '', '', '', '', '', '', ''],
                                         ['', 'makaa', 'b', 'j', 'â', '', '', '', '', '', '', '', '', ''],
                                         ['', 'mpiemo', 'ɓ', 'j', 'â', '', '', '', '', '', '', '', '', ''],
                                         ['', 'kwasio', 'b', '', 'i', 'a', '', '', '', '', '', '', '', ''],
                                         ['', 'njyem', 'b', 'w', 'â', '', '', '', '', '', '', '', '', ''],
                                         ['', 'shiwa', 'b', 'j', 'à', '', '', '', '', '', '', '', '', ''],
                                         ['', '', '', '', '', '', '', '', '', '', '', '', '', '']]


def test_output_to_csv():
    expected =  ['"9.";"accoucher";"";"";"";"";"";"";"";"";"";"";"";""',
                 '"";"";"C1a";"C1b";"V1a";"V1b";"C2a";"C2b";"V2a";"V2b";"C3a";"C3b";"V3a";"V3b"',
                 '"";"swo";"b";"y";"â";"";"";"";"";"";"";"";"";""',
                 '"";"gyeli";"b";"w";"à";"";"";"";"";"";"";"";"";""',
                 '"";"bekwel";"b";"j";"â";"";"";"";"";"";"";"";"";""',
                 '"";"bekol";"b";"j";"â";"";"";"";"";"";"";"";"";""',
                 '"";"konzime";"b";"j";"â";"";"";"";"";"";"";"";"";""',
                 '"";"makaa";"b";"j";"â";"";"";"";"";"";"";"";"";""',
                 '"";"mpiemo";"ɓ";"j";"â";"";"";"";"";"";"";"";"";""',
                 '"";"kwasio";"b";"";"i";"a";"";"";"";"";"";"";"";""',
                 '"";"njyem";"b";"w";"â";"";"";"";"";"";"";"";"";""',
                 '"";"shiwa";"b";"j";"à";"";"";"";"";"";"";"";"";""',
                 '"";"";"";"";"";"";"";"";"";"";"";"";"";""']
    assert matrix_to_csv(word_data_to_csv(split_words_in_a_file('line9.csv')[0])) == expected
