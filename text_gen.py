# -*- coding: utf-8 -*-
from nltk.corpus import stopwords
import dict_reader
import pymorphy2
import nltk

# Initializing and creating objects for later use
morph = pymorphy2.MorphAnalyzer(lang="ru")
dr = dict_reader.Dict_reader()
stopwords_nltk = stopwords.words("russian")
stop = set()

# Making our own set of stop words, because NLTK's list contains words not in normal from
for word in stopwords_nltk:
    stop.add(morph.parse(word)[0].normal_form)
stop.add(morph.parse("который")[0].normal_form)

# Creating dict to store words
translate_dict = dict()
text = "Если вы что-то боитесь сделать, то это как раз и есть то, что вам необходимо сделать в первую очередь."
tokens = nltk.word_tokenize(text)

# For statement in which we iterate over the text
for token in tokens:
    # Parsing the word
    current_word = morph.parse(token)[0]
    current_normal = morph.parse(current_word.normal_form)[0]

    # Getting the original word's unchangeable grammemes 
    params = set(current_normal.tag.grammemes)

    # Checking if it's actually a word and if it's a stop-word
    if "LATN" in params or "PNCT" in params or "NUMB" in params or "intg" in params or "real" in params or "ROMN" in params or "UNKN" in params or current_word.normal_form in stop:
        continue

    # Checking if it already exists in our dictionary
    if current_normal.word in translate_dict:
        tokens[tokens.index(token)] = dict_word.inflect(current_word.tag.grammemes)
        continue

    # If the word is name
    if "Name" in params:
        getword = dr.get_name
    else:
        getword = dr.get_word

    # Starting to cycle through the dictionary in search for compatible words
    dict_word = getword()
    while len(dict_word) != 0:
        dict_word = morph.parse(dict_word[0])[0]
        dict_normal = morph.parse(dict_word.normal_form)[0]

        # If the word is name
        if "Name" in params:
            # Checking for unchangable parameters of the word
            if dict_normal.tag == current_normal.tag:
                break
        else:
            # Checking for unchangable parameters of the word
            if dict_normal.tag == current_normal.tag:
                break
        dict_word = getword()
    else:
        continue
    
    # Adding resulting word to the dictionary and replacing the original word
    translate_dict[current_normal.word] = dict_normal.word
    tokens[tokens.index(token)] = dict_word.inflect(current_word.tag.grammemes).word

print(" ".join(tokens))
