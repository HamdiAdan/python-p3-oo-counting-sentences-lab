#!/usr/bin/env python3

class MyString:
    def __init__(self,value =""):
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self,string_value):
        if isinstance (string_value,str):
            self._value = string_value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        if self._value.endswith("."):
            return True
        else:
            return False
        
    def is_question(self):
        if self._value.endswith("?"):
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self._value.endswith("!"):
            return True
        else:
            return False
    

    def count_sentences(self):
        replaced_value= self._value.replace("!",".").replace("?",".")
        sentences = replaced_value.split(".")
        non_empty_sentences = filter(None,sentences)
        num_sentences= len(list(non_empty_sentences))
        return num_sentences


        




        
        
        
    

    
   