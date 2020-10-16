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

# Creating dict to store words
translate_dict = dict()
text = "Прошлое – это поезд, который ушёл. Будущее – это мечта, которая может сбыться. А настоящее – это просто мгновение, в котором мы живём."
tokens = nltk.word_tokenize(text)

# For statement in which we iterate over the text
for token in tokens:
    # Parsing the word
    current_word = morph.parse(token)[0]
    # Getting the original word's grammemes 
    params = set(current_word.tag.grammemes)

    # Checking if it's actually a word and if it's a stop-word
    if "LATN" in params or "PNCT" in params or "NUMB" in params or "intg" in params or "real" in params or "ROMN" in params or "UNKN" in params or current_word.normal_form in stop:
        continue

    # Checking if it already exists in our dictionary
    if current_word.normal_form in translate_dict:
        tokens[tokens.index(token)] = dict_word.inflect(params)
        continue

    # Starting to cycle through the dictionary in search for compatible words
    dict_word = ""
    while True:
        # If the word is name
        if "Name" in params:
            dict_word = morph.parse(dr.get_name()[0])[0]
            
            # Checking for unchangable parameters of the word
            if dict_word.tag.POS in params and dict_word.tag.gender in params:
                break
        else:
            kek = dr.get_word()
            lol = morph.parse(kek[0])
            dict_word = lol[0]
            
            # Checking for unchangable parameters of the word
            if dict_word.tag.POS in params and dict_word.tag.gender in params and dict_word.tag.animacy in params:
                break
    
    # Adding resulting word to the dictionary and replacing the original word
    translate_dict[current_word.normal_form] = dict_word.normal_form
    tokens[tokens.index(token)] = dict_word.inflect(params)

print(tokens)
