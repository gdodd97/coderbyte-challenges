import string

def LetterChanges(s):
    
    
    orig = string.letters
    new = string.ascii_lowercase[1:] + 'a' + string.ascii_uppercase[1:] + 'A'
    
    for vowel in 'aeiou':
        new = new.replace(vowel, vowel.upper())

    table = string.maketrans(orig, new)
    return s.translate(table)
    
# keep this function call here  
print LetterChanges(raw_input())