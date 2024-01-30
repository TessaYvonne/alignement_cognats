from letter_splitter import split_words_in_a_file
from output import matrix_to_csv, word_data_to_csv


matrix_to_csv(word_data_to_csv(split_words_in_a_file('./dataset_big.csv')[0]))

