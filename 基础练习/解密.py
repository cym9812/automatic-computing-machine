import hashlib

word_file = open("word.txt", 'r')
word = word_file.read()
word = word.split('\n')

for i in word:
    temp = "jina:CS@UoA:" + i
    md5 = hashlib.md5(temp.encode('utf-8')).hexdigest()
    if md5 == "ad790cf6708acfc21cf507ef484ffc77":
        print(i)

