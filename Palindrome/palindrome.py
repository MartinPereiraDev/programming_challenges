def palindrome(text):
    """  return Palindrome 
    Palindrome is a word, this word can be read
    from back to the front
    samples: "ana", "otto", "ama"
    """
    text_invert = text[::-1]
    if text == text_invert:
        print(text, ": Is a palindrome")
    else:
        print(text, " : Not is a palindrome")
    
    return text_invert

palindrome("ana")

"""function reverse 
    returns the string in reverse
     since it takes the letter and positions it backwards in the sum of characters
"""
def reverse(text):
    s = ""
    for t in text:
        s = t + s
    return text == s 

reverse("otto")