import sys

pyg = 'ay'

original = input('Enter a word: ').lower()

first_letter = original[0]
second_letter= original[1]
third_letter = original[2]


if len(original) > 0 and original.isalpha():
    
    new = original[2:len(original)] + first_letter + second_letter + pyg
        print (new)

else :
    print ('empty')

