import string
f = open("hod.txt")
fr = f.readlines()
book = []
book_clean = []

for line in fr:
    book.append(line.split())

for line in book:
    for word in line:
        if any (string.punctuation in word):
            word.strip(".?!%&,;:")
        book_clean.append(word)



    
