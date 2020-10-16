# -*- coding: utf-8 -*-
import pymorphy2
import nltk
class Dict_reader:
    """
    Dictionary reader class.
    Methods:
    - get_scientific(amount=1) - gets a scientific term from dictionary.
    - get_word(amount=1) - gets a random word from dictionary.
    - get_name(amount=1) - gets a name from dictionary.
    """
    def get_scientific(self, amount = 1):
        """
        Gets a scientific term from the dictionary. 

        Params: amount - amount of words that is being returned. By default is 1.

        Return value: list of scientific terms.
        """
        if self.__scientific_read == 0:
            with open("ru/scientific.txt", 'r') as f:
                self.__scientific = f.read()
                self.__scientific = self.__scientific.split("\n")

        result = self.__scientific[self.__scientific_read:self.__scientific_read + amount]
        self.__scientific_read += amount
        return list(result)
    
    def get_word(self, amount = 1):
        """
        Gets a random word from the dictionary. 

        Params: amount - amount of words that is being returned. By default is 1.

        Return value: list of random words.
        """
        if self.__words_read == 0:
            with open("ru/words.txt", 'r') as f:
                self.__words = f.read()
                self.__words = self.__words.split("\n")

        result = self.__words[self.__words_read:self.__words_read + amount]
        self.__words_read += amount
        return list(result)

    def get_name(self, amount = 1):
        """
        Gets a name from the dictionary. 

        Params: amount - amount of words that is being returned. By default is 1.

        Return value: list of names.
        """
        if self.__names_read == 0:
            with open("ru/names.txt", 'r') as f:
                self.__names = f.read()
                self.__names = self.__names.split("\n")

        result = self.__names[self.__names_read:self.__names_read + amount]
        self.__names_read += amount
        return list(result)

    def __init__(self):
        self.__MorphAnalyzer = pymorphy2.MorphAnalyzer(lang="ru")
        self.__scientific_read = 0
        self.__names_read = 0
        self.__words_read = 0
        self.__scientific = ""
        self.__names = ""
        self.__words = ""