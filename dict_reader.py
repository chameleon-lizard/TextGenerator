# -*- coding: utf-8 -*-
import pymorphy2
import nltk
import random

class DictReader:
    """
    Dictionary reader class.

    Methods:

    - get_word(amount=1) - gets a random word from dictionary.

    - get_name(amount=1) - gets a name from dictionary.
    """

    
    def get_word(self, amount = 1):
        """
        Gets a random word from the dictionary. 

        Params: amount - amount of words that is being returned. By default is 1.

        Return value: list of random words.
        """
        if len(self.__words) != 0 and self.__words_read  == len(self.__words):
            self.__words_read = 1

        if self.__words_read == 0:
            with open("ru/words.txt", 'r') as f:
                self.__words = f.read()
                self.__words = self.__words.split("\n")
                self.__words_read = random.randint(0, 387)

        result = self.__words[self.__words_read:self.__words_read + amount]
        self.__words_read += amount
        return list(result)

    def get_simple(self, amount = 1):
        """
        Gets a random simple word from the dictionary. 

        Params: amount - amount of words that is being returned. By default is 1.

        Return value: list of random words.
        """
        if len(self.__words) != 0 and self.__words_read  == len(self.__words):
            self.__words_read = 1

        if self.__words_read == 0:
            with open("ru/words.txt", 'r') as f:
                self.__words = f.read()
                self.__words = self.__words.split("\n")
                self.__words_read = random.randint(0, 387)

        result = self.__words[self.__words_read:self.__words_read + amount]
        self.__words_read += amount
        return list(result)

    def get_name(self, amount = 1):
        """
        Gets a name from the dictionary. 

        Params: amount - amount of words that is being returned. By default is 1.

        Return value: list of names.
        """
        if len(self.__names) != 0 and self.__names_read  == len(self.__names):
            self.__names_read = 1

        if self.__names_read == 0:
            with open("ru/names.txt", 'r') as f:
                self.__names = f.read()
                self.__names = self.__names.split("\n")
                self.__names_read = random.randint(0, 50785)

        result = self.__names[self.__names_read:self.__names_read + amount]
        self.__names_read += amount
        return list(result)

    def __init__(self):
        random.seed()
        self.__MorphAnalyzer = pymorphy2.MorphAnalyzer(lang="ru")
        self.__names_read = 0
        self.__words_read = 0
        self.__names = ""
        self.__words = ""