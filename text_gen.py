# -*- coding: utf-8 -*-
from nltk.corpus import stopwords
import dict_reader
import pymorphy2
import nltk
import re

class TextGenerator:
    """
    Text generator class.

    Methods:

    - text(text) - generate text from given input.

    - status() - generate a random status for social network.
    """
    def text(self, text):
        """
        Method that generates text from given input.

        Params: text - string with original text.

        Return value: tuple - original text and generated text.
        """
        # Creating dict to store words
        translate_dict = dict()
        tokens = nltk.word_tokenize(text)

        # For statement in which we iterate over the text
        for token in tokens:
            # Parsing the word
            current_word = self.__morph.parse(token)[0]
            current_normal = self.__morph.parse(current_word.normal_form)[0]

            # Getting the original word's unchangeable grammemes 
            if current_normal.tag.grammemes <= current_word.tag.grammemes:
                params = set(current_normal.tag.grammemes)
            else:
                continue

            # Checking if it's actually a word and if it's a self.__stop-word
            if "LATN" in params or "PNCT" in params or "NUMB" in params or "intg" in params or "real" in params or "ROMN" in params or "UNKN" in params or current_word.normal_form in self.__stop:
                continue
            
            # Checking if it already exists in our dictionary
            if current_normal.word in translate_dict:
                tokens[tokens.index(token)] = self.__morph.parse(translate_dict[current_normal.word])[0].inflect(current_word.tag.grammemes).word
                continue
            
            # If the word is name
            if "Name" in params:
                getword = self.__dr.get_name
            else:
                getword = self.__dr.get_word

            # Starting to cycle through the dictionary in search for compatible words
            dict_word = getword()
            while len(dict_word) != 0:
                dict_word = self.__morph.parse(dict_word[0])[0]
                dict_normal = self.__morph.parse(dict_word.normal_form)[0]

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

        tokens = " ".join(tokens)
        tokens = re.sub(r"\s+(?=[.,?!():;\"\'\\/»])", "", tokens, 0, re.MULTILINE)
        tokens = re.sub(r"[«]\s", " «", tokens, 0, re.MULTILINE)
        tokens = nltk.sent_tokenize(tokens, language="russian")
        result = ""

        for sent in tokens:
            if result != "":
                result += " "
            result += sent[0].capitalize() + sent[1:]

        return result

    def __init__(self):
        # Initializing and creating objects for later use
        self.__morph = pymorphy2.MorphAnalyzer(lang="ru")
        self.__dr = dict_reader.DictReader()
        stopwords_nltk = stopwords.words("russian")
        self.__stop = set()

        # Making our own set of stop words, because NLTK's list contains words not in normal from
        for word in stopwords_nltk:
            self.__stop.add(self.__morph.parse(word)[0].normal_form)
        self.__stop.add(self.__morph.parse("который")[0].normal_form)

gen = TextGenerator()
print(gen.text(text='может сделать датасет на своем ебале и сказать, что процесс обучения это "калибровка под индивидульный рельеф лица пользователя"'))