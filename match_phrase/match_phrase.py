""" Function receives a phrase and attaches the word to search for within the phrase.
     return if the word exists within the sentence and how many times the word is in the sentence.
"""
def match_phrase(phrase,word):
    phrase_l = phrase.lower()
    phrase_s = phrase_l.split()
    word_l = word.lower()
    
    count = 0 
    w = 0 
    for a in phrase_s:
        if word_l == a:
            count = count +1
            w = w +1
    
    
    return print ( "The ", word_l," match : ", count, " times") 

match_phrase("I am genius happy happy", "happy")