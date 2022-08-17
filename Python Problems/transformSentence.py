# goal to transform a sentence according to certain capitalization rules

import math
import os
import random
import re
import sys



#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    # split into individual words
    words = sentence.split()
    
    output = '' 
    for word in words:
        length = len(word)
        output += word[0]                                  # first letter stays the same
        for i in range(0,length-1):
            # if previous char comes before this char 
            if ord(word[i].lower()) < ord(word[i+1].lower()):
                output += word[i+1].upper()
            elif ord(word[i].lower()) > ord(word[i+1].lower()):            # this char comes before previous char
                output += word[i+1].lower()
            elif ord(word[i].lower()) == ord(word[i+1].lower()):            # compare word[i].lower() to standardize ASCII value comparisons
                output += word[i+1]
        output += ' '        # add space between words
    
    return output

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    print(result)
