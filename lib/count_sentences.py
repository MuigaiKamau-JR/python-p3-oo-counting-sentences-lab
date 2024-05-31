#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            print("The value must be a string.\n")
            self.value = ''
        else:
            self.value = value


    # def is_sentence(self):
    #     return self.value.endswith('.')

    # def is_question(self):
    #     return self.value.endswith('?')

    # def is_exclamation(self):
    #     return self.value.endswith('!')

    # def count_sentences(self):
    #     sentences = [sentence.strip() for sentence in self.value.split('.') if sentence.strip()]
    #     sentences += [sentence.strip() for sentence in self.value.split('?') if sentence.strip()]
    #     sentences += [sentence.strip() for sentence in self.value.split('!') if sentence.strip()]
    #     return len(sentences)

