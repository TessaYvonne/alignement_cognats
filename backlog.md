# Backlog

List of tasks in order of priority

- ~~clean up data in a spreadsheet cell~~
  - ~~remove white space, text to the right of slashes, prefixes like 'd-'~~
- ~~construct reconstruction_PA80~~
- ~~improve test coverage~~
- ~~handle data format errors~~
  - ~~missing parenthesis of a pair~~
- ~~read a comma separated file and apply clean up rules~~
- ~~apply clean up rules to all cells in a row~~
- ~~use dict to represent a line of data (see below)~~
- ~~create a list of vowels and consonants~~
- ~~split a word in vowels and consonants~~
- ~~process a file, apply clean up rules and split words~~ 
- create new file with matrix for each term (in my case, each French term)
- align input column headers in a single column
- new column headers for each matrix: Pfx ; C1a ; C1b ; V1a ; V1b ; C2a ; C2b ; V2a ; V2b ; C3a ; C3b ; V3a ; V3b
- align words of each language into the matrix
- add prefixes in the Pfx column
- add full words of each language into the matrix
- celebrate if everything works!


## dicts

A dict is a list of key/value pairs. A pair can be added to the dict and later retrieved using the key.
This would allow us to store the word for a language using the name of the language as the key. This is 
more robust than using positions. 

```python

def test():
  line = {}
  line["sequence-number"] = 1
  line["french-word"] = "abandonner 1"
  line["PA80"] = "°cìnà"
  line["bekwel"] = "cìn"
```

with the code above, getting the value for the `bekwel` language can be changed from

```python
  print(line[3])
```

to

```python
  print(line["bekwel"])
```

which is way less error prone.