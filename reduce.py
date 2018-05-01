import string
f = open("hod.txt")
fr = f.readlines()
book = []
book_clean = []

for line in fr:
    book.append(line.split())

for line in book:
    for word in line:
        word = word.translate(string.maketrans("",""), string.punctuation)
        book_clean.append(word)

def frequency(word):
    return len([x for x in book_clean if x == word])

print "frequency of the:", frequency("the")
print "frequency of I:", frequency("I")
print "frequency of a:", frequency("a")

def total_frequency(words):
    return reduce(lambda a, b: a + b, [frequency(word) for word in words])

print "frequency of the, I, and a:", total_frequency(["the", "I", "a"])

def most_frequent():
    unique_words = list({x for x in book_clean})
    return reduce(lambda a, b: a if frequency(a) > frequency(b) else b, unique_words)

print "most frequent word:", most_frequent()