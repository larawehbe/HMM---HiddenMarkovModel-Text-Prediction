import numpy as np

text = open('shakespear.txt', encoding='utf8').read()

words = text.split()

def make_pairs(words):
    for i in range(len(words)-1):
        yield (words[i], words[i+1])


pairs = make_pairs(words)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

first_word = 'ROMEO:'

while first_word.islower():
    first_word = np.random.choice(text)

chain = [first_word]

n_words = 100

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

' '.join(chain)
for c in chain:
    print(c, end=' ')
