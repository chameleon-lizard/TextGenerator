# -*- coding: utf-8 -*-
import pymorphy2
import nltk

m = pymorphy2.MorphAnalyzer(lang='ru')

with open("ru/ru_phys4.txt", 'r') as f:
   text = f.read()

text_tokenized = nltk.word_tokenize(text)
set_of_words = set()

for word in text_tokenized:
    set_of_words.add(m.normal_forms(word)[0])

with open("ru/scientific.txt", "w") as f:
   for word in set_of_words:
      f.write(word + '\n')

print("Done!")