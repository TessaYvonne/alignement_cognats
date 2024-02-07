from letter_splitter import split_words_in_a_file, splittable_columns
from output import matrix_to_csv, write_output_to_file, word_data_to_csv, word_to_html_page, word_to_file_name, \
    cleanup_output_folder, word_data_to_normalized_csv
import argparse

from reconstructions import read_and_process_csv_file


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


def to_normalized_csv_file(inputfile, outputfile):
    words = read_and_process_csv_file(inputfile)
    with open(outputfile, "w") as file:
        file.write("nº;FR;PA80;swo;gyeli;bekwel;bekol;konzime;makaa;mpiemo;kwasio;njem;shiwa;BC (BLR3);Reconstr. Régionales (BLR 3);Reconstr. Mougiama, Hombert;;;;\n")
        for word in words:
            output_line = ''
            output_line += word['nº'] + ';' + word['FR'] + ';'
            for column in splittable_columns:
                output_line += word[column] + ';'
            output_line.strip(';')
            file.write(output_line + '\n')


parser = argparse.ArgumentParser()
parser.add_argument('--datafile', dest='datafile', type=str, help='The file that contains the data to be analyzed. Both csv (;-separated) and xlsx are supported', required=True)
parser.add_argument('--outputfile', dest='outputfile', type=str, help='The file that will contain the output', required=True)
parser.add_argument('--outputfolder', dest='outputfolder', type=str, help='The folder that will contain the html files', required=True)
parser.add_argument('--normalized-output-file', dest='normalized_output_file', type=str, help='The file that will contain the words in their cleand-up form', required=False)
args = parser.parse_args()

words = split_words_in_a_file(args.datafile)

print(f"write spreadsheet {args.outputfile}")
analyze_spreadsheet(words, args.outputfile)
print(f"write website in {args.outputfolder}")
to_website(words, args.outputfolder)
if args.normalized_output_file is not None:
    print(f"write normalized csv file in {args.normalized_output_file}")
    to_normalized_csv_file(args.datafile, args.normalized_output_file)
