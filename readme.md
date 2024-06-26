# Etymologie

## setup

Install:
- python 3.x
- pytest (`pip3 install -U pytest`)

## running tests

```bash
cd test
python3 -m pytest
```

## running

- export a spreadsheet to cvs format, use ; as column separators
- run 
 
```
python3 analyzer.py --datafile ./data/dataset_cognates.csv --outputfile ./output/analysed_words.csv --outputfolder output --normalized-output-file ./output/normalized.csv
```

or use

```
python3 analyzer.py --datafile ./data/dataset_cognates.csv --outputfile analysed_words.csv --outputfolder output --normalized-output-file normalized.csv
```


Import the output file in Excel or Numbers.

Upload the `output` folder to a webserver

--normalized-output-file is optional, if set, a cleaned up version of the data is stored in a spreadsheet that can
be used for other purposes.

## Theory

https://en.wikipedia.org/wiki/List_of_Unicode_characters#Phonetic_scripts

these characters should be split in two parts: a letter and a 'Spacing modifier'  
U+00C0 - U+024F
U+1E00 - U+1EFF 

spacing modifier:
U+02B0 - U+036F (U+0300 - U+036F only?)

à (U+00E0) -> should be *a* (U+0061) and *`* (U+0300) 

## Test data

datatest.xlsx is a sample file 

Columns:
* B: French word
* C: word in ? 
* D-M: word in several languages
* N: ?
* O: ?
* P: ?

### operations

#### remove prefix, remove second version if present

```
d-ɔ̀l / m-ɔ̀l 
```

becomes

```
ɔ̀l 
```


* remove everything from / until the end of the word
* remove `d-`

#### check for letters with additions:

```
à
```

make sure this is stored as two characters:

```
a (U+0061) and ` (U+0300)
```

#### update C column

in C column:

```
°cìnà 
```

replace with:

```
cìnà 
```

#### Remove text in parenthesis

In

```
nyú (wá nkwànò) / ba-nyú (bá nkwànò)
```

remove text in () and text after /

#### Translate C column to N column:

```
°bíà 
```

becomes

```
*b*i*à 
```

## experiments

read spreadsheet using library

https://pythonbasics.org/read-excel/

```bash
pip3 install openpyxl
pip3 install --upgrade pandas
pip3 install Pyarrow
```