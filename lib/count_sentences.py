#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
            self._value = ''  
        else:
            self._value = value

    def is_sentence(self):
        """Returns True if the string ends with a period ('.')"""
        return self.value.endswith('.')

    def is_question(self):
        """Returns True if the string ends with a question mark ('?')"""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Returns True if the string ends with an exclamation mark ('!')"""
        return self.value.endswith('!')

    def count_sentences(self):
        '''returns the number of sentences in the value.'''
        sentences = [sentence.strip() for sentence in self.value.replace('!', '.').replace('?', '.').split('.') if sentence.strip()]
        return len(sentences)