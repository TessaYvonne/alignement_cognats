from letter_splitter import split_words_in_a_file
from output import letters_to_output_format, word_data_to_csv, matrix_to_csv, columns, find_longest_row


def test_swo_letter_data_is_correct():
    swo_data = [{'letter': 'b', 'is_consonant': True, 'word': 'yâ'},
                {'letter': 'y', 'is_consonant': True, 'word': 'â'},
                {'letter': 'â', 'is_consonant': False, 'word': ''}]
    assert (letters_to_output_format(swo_data) ==
            {'C1a': 'b', 'C1b': 'y', 'V1a': 'â', 'V1b': '', 'C2a': '',
             'C2b': '', 'V2a': '', 'V2b': '', 'C3a': '', 'C3b': '', 'V3a': '', 'V3b': ''},)


def test_word_to_output():
    data = split_words_in_a_file('line9.csv')
    assert (word_data_to_csv(data[0]) ==
            [['9.', 'accoucher', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', ''],
             ['', '', 'Pfx', 'word', 'C1a', 'C1b', 'V1a', 'V1b', 'C2a', 'C2b', 'V2a', 'V2b', 'C3a', 'C3b', 'V3a', 'V3b', 'C4a',
              'C4b', 'V4a', 'V4b', 'C5a', 'C5b', 'V5a', 'V5b', 'C6a', 'C6b', 'V6a', 'V6b', 'C7a', 'C7b', 'V7a', 'V7b',
              'C8a', 'C8b', 'V8a', 'V8b', 'C9a', 'C9b', 'V9a', 'V9b', 'C10a', 'C10b', 'V10a', 'V10b', 'C11a', 'C11b',
              'V11a', 'V11b', 'C12a', 'C12b', 'V12a', 'V12b', 'C13a', 'C13b', 'V13a', 'V13b', 'C14a', 'C14b', 'V14a',
              'V14b'],
             ['', 'swo', '', 'byâ', 'b', 'y', 'â', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', ''],
             ['', 'gyeli', '', 'bwà', 'b', 'w', 'à', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', ''],
             ['', 'bekwel', 'ɛ̀-', 'bjâ', 'b', 'j', 'â', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', ''],
             ['', 'bekol', '', 'bjâ', 'b', 'j', 'â', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', ''],
             ['', 'konzime', 'è-', 'bjâ', 'b', 'j', 'â', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', ''],
             ['', 'makaa', '', 'bjâ', 'b', 'j', 'â', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', ''],
             ['', 'mpiemo', 'à-', 'ɓjâ', 'ɓ', 'j', 'â', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', ''],
             ['', 'kwasio', '', 'bia', 'b', '', 'i', 'a', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', ''],
             ['', 'njyem', 'lè-', 'bwâ', 'b', 'w', 'â', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', ''],
             ['', 'shiwa', '', 'bjà', 'b', 'j', 'à', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', ''],
             ['', 'PA80', '', '°b°í°à', '°b', '', '°í', '°à', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', ''],
             ['', 'Reconstr. Régionales (BLR 3)', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
             ['', 'Reconstr. Mougiama, Hombert', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
              '', '', '', '', '']])


def test_output_to_csv():
    expected = ['"9.";"accoucher";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
                '"";"";"Pfx";"word";"C1a";"C1b";"V1a";"V1b";"C2a";"C2b";"V2a";"V2b";"C3a";"C3b";"V3a";"V3b";"C4a";"C4b";"V4a";"V4b";"C5a";"C5b";"V5a";"V5b";"C6a";"C6b";"V6a";"V6b";"C7a";"C7b";"V7a";"V7b";"C8a";"C8b";"V8a";"V8b";"C9a";"C9b";"V9a";"V9b";"C10a";"C10b";"V10a";"V10b";"C11a";"C11b";"V11a";"V11b";"C12a";"C12b";"V12a";"V12b";"C13a";"C13b";"V13a";"V13b";"C14a";"C14b";"V14a";"V14b"',
                '"";"swo";"";"byâ";"b";"y";"â";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
                '"";"gyeli";"";"bwà";"b";"w";"à";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
                '"";"bekwel";"ɛ̀-";"bjâ";"b";"j";"â";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
                '"";"bekol";"";"bjâ";"b";"j";"â";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
                '"";"konzime";"è-";"bjâ";"b";"j";"â";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
                '"";"makaa";"";"bjâ";"b";"j";"â";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
                '"";"mpiemo";"à-";"ɓjâ";"ɓ";"j";"â";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
                '"";"kwasio";"";"bia";"b";"";"i";"a";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
                '"";"njyem";"lè-";"bwâ";"b";"w";"â";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
                '"";"shiwa";"";"bjà";"b";"j";"à";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
                '"";"PA80";"";"°b°í°à";"°b";"";"°í";"°à";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
                '"";"Reconstr. Régionales (BLR '
                '3)";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
                '"";"Reconstr. Mougiama, '
                'Hombert";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
                '"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""']
    # expected =  ['"9.";"accoucher";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
    #              '"";"";"C1a";"C1b";"V1a";"V1b";"C2a";"C2b";"V2a";"V2b";"C3a";"C3b";"V3a";"V3b";"C4a";"C4b";"V4a";"V4b";"C5a";"C5b";"V5a";"V5b";"C6a";"C6b";"V6a";"V6b";"C7a";"C7b";"V7a";"V7b";"C8a";"C8b";"V8a";"V8b";"C9a";"C9b";"V9a";"V9b";"C10a";"C10b";"V10a";"V10b";"C11a";"C11b";"V11a";"V11b";"C12a";"C12b";"V12a";"V12b";"C13a";"C13b";"V13a";"V13b";"C14a";"C14b";"V14a";"V14b"',
    #              '"";"PA80";"°b";"";"°í";"°à";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
    #              '"";"swo";"b";"y";"â";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
    #              '"";"gyeli";"b";"w";"à";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
    #              '"";"bekwel";"b";"j";"â";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
    #              '"";"bekol";"b";"j";"â";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
    #              '"";"konzime";"b";"j";"â";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
    #              '"";"makaa";"b";"j";"â";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
    #              '"";"mpiemo";"ɓ";"j";"â";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
    #              '"";"kwasio";"b";"";"i";"a";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
    #              '"";"njyem";"b";"w";"â";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
    #              '"";"shiwa";"b";"j";"à";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
    #              '"";"Reconstr. Régionales (BLR '
    #              '3)";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
    #              '"";"Reconstr. Mougiama, '
    #              'Hombert";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""',
    #              '"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";"";""']
    assert matrix_to_csv(word_data_to_csv(split_words_in_a_file('line9.csv')[0])) == expected


def test_find_longest_row():
    # split_lines.append({'line': line['nº'], 'FR': line['FR'], 'languages':split_words})
    languages = split_words_in_a_file('line9.csv')[0]['languages']
    longest_row = find_longest_row(languages)
    assert longest_row == 4
