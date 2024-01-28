from letter_splitter import split_words_in_a_file
from output import word_to_csv, write_output_to_file, word_to_output
import argparse

def analyze_spreadsheet(datafile, outputfile):
    with open(outputfile, "w") as file:
        words = split_words_in_a_file(datafile)
        for word in words:
            one_word = word_to_csv(word_to_output(word))
            write_output_to_file(file, one_word)


parser = argparse.ArgumentParser()
parser.add_argument('--datafile', dest='datafile', type=str, help='The file that contains the data to be analyzed', required=True)
parser.add_argument('--outputfile', dest='outputfile', type=str, help='The file that will contain the output', required=True)
args = parser.parse_args()

analyze_spreadsheet(args.datafile, args.outputfile)
