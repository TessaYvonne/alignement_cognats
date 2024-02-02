from letter_splitter import split_words_in_a_file
from output import matrix_to_csv, write_output_to_file, word_data_to_csv, word_to_html_page, word_to_file_name, \
    cleanup_output_folder
import argparse
import pathlib

def analyze_spreadsheet(datafile, outputfile):
    with open(outputfile, "w") as file:
        words = split_words_in_a_file(datafile)
        for word in words:
            one_word = matrix_to_csv(word_data_to_csv(word))
            write_output_to_file(file, one_word)


def to_website(datafile, outputfolder):
    words = split_words_in_a_file(datafile)
    pathlib.Path(outputfolder).mkdir(parents=True, exist_ok=True)

    for word in words:
        html_page = word_to_html_page(word)
        file_name = word_to_file_name(word['FR'])
        cleanup_output_folder(outputfolder)
        with open(f"{outputfolder}/{file_name}", "w") as file:
            file.write(html_page)

# {'line': '1033', 'FR': 'vouloir 2', 'languages': {'PA80': [{'letter': '°ɡ', 'is_consonant': True, 'word': '°ó°m°b°Ì'}, {'letter': '°ó', 'is_consonant': False, 'word': '°m°b°Ì'}, {'letter': '°m', 'is_consonant': True, 'word': '°b°Ì'}, {'letter': '°b', 'is_consonant': True, 'word': '°Ì'}, {'letter': '°Ì', 'is_consonant': False, 'word': ''}], 'swo': [{'letter': 'ɡ', 'is_consonant': True, 'word': 'ì'}, {'letter': 'ì', 'is_consonant': False, 'word': ''}], 'gyeli': [{'letter': 'w', 'is_consonant': True, 'word': 'úmbɛ'}, {'letter': 'ú', 'is_consonant': False, 'word': 'mbɛ'}, {'letter': 'mb', 'is_consonant': True, 'word': 'ɛ'}, {'letter': 'ɛ', 'is_consonant': False, 'word': ''}], 'bekwel': [], 'bekol': [{'letter': 'w', 'is_consonant': True, 'word': 'îmb'}, {'letter': 'î', 'is_consonant': False, 'word': 'mb'}, {'letter': 'mb', 'is_consonant': True, 'word': ''}], 'konzime': [{'letter': 'ɡ', 'is_consonant': True, 'word': 'ø̂m'}, {'letter': 'ø̂', 'is_consonant': False, 'word': 'm'}, {'letter': 'm', 'is_consonant': True, 'word': ''}], 'makaa': [{'letter': 'w', 'is_consonant': True, 'word': 'ímb'}, {'letter': 'í', 'is_consonant': False, 'word': 'mb'}, {'letter': 'mb', 'is_consonant': True, 'word': ''}], 'mpiemo': [{'letter': 'w', 'is_consonant': True, 'word': 'ōmbī'}, {'letter': 'ō', 'is_consonant': False, 'word': 'mbī'}, {'letter': 'mb', 'is_consonant': True, 'word': 'ī'}, {'letter': 'ī', 'is_consonant': False, 'word': ''}], 'kwasio': [{'letter': 'w', 'is_consonant': True, 'word': 'um'}, {'letter': 'u', 'is_consonant': False, 'word': 'm'}, {'letter': 'm', 'is_consonant': True, 'word': ''}], 'njyem': [{'letter': 'ɡ', 'is_consonant': True, 'word': 'wɩ̂m'}, {'letter': 'w', 'is_consonant': True, 'word': 'ɩ̂m'}, {'letter': 'ɩ̂', 'is_consonant': False, 'word': 'm'}, {'letter': 'm', 'is_consonant': True, 'word': ''}], 'shiwa': [], 'Reconstr. Régionales (BLR 3)': [], 'Reconstr. Mougiama, Hombert': []}}

parser = argparse.ArgumentParser()
parser.add_argument('--datafile', dest='datafile', type=str, help='The file that contains the data to be analyzed', required=True)
parser.add_argument('--outputfile', dest='outputfile', type=str, help='The file that will contain the output', required=True)
parser.add_argument('--outputfolder', dest='outputfolder', type=str, help='The folder that will contain the html files', required=True)
args = parser.parse_args()

# analyze_spreadsheet(args.datafile, args.outputfile)
to_website(args.datafile, args.outputfolder)
