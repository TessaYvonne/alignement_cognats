import codecs
with codecs.open('test.txt', encoding='utf-16') as f:
    for line in f:
        print(list(line))
        print (line)
        for i in range(0, len(line)):
            print (hex(ord(line[i])))
        print ("----------")



# https://en.wikipedia.org/wiki/List_of_Unicode_characters#Phonetic_scripts