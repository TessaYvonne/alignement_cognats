from letter_splitter import split_words_in_a_file
from output import matrix_to_csv, write_output_to_file, word_data_to_csv, word_to_html_page, word_to_file_name, \
    cleanup_output_folder
import argparse


def analyze_spreadsheet(words, outputfile):
    with open(outputfile, "w") as file:
        for word in words:
            one_word = matrix_to_csv(word_data_to_csv(word))
            write_output_to_file(file, one_word)


def to_website(words, outputfolder):
    cleanup_output_folder(outputfolder)
    with open(f"{outputfolder}/index.html", "w") as index_file:
        for word in words:
            html_page = word_to_html_page(word)
            file_name = word_to_file_name(word['FR'])
            index_file.write(f'<a href="{file_name}">{word["FR"]}</a><br>')
            with open(f"{outputfolder}/{file_name}", "w") as file:
                file.write(html_page)


parser = argparse.ArgumentParser()
parser.add_argument('--datafile', dest='datafile', type=str, help='The file that contains the data to be analyzed', required=True)
parser.add_argument('--outputfile', dest='outputfile', type=str, help='The file that will contain the output', required=True)
parser.add_argument('--outputfolder', dest='outputfolder', type=str, help='The folder that will contain the html files', required=True)
args = parser.parse_args()

words = split_words_in_a_file(args.datafile)

analyze_spreadsheet(words, args.outputfile)
to_website(words, args.outputfolder)
