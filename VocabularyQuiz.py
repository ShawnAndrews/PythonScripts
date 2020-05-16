import random
import csv
import itertools
import re
import sys
from os import system

# Example usage in terminal: <path-to-python-exe> <path-to-this-script> <path-to-vocab-csv-file>
# ie: C:\Users\Shawn\AppData\Local\Programs\Python\Python38-32\python.exe C:\Users\Shawn\PycharmProjects\vocab\vocab.py C:/Users/Shawn/Desktop/vocab.csv

# error-checking
if len(sys.argv) != 2:
    sys.exit("Program requires 1 file path argument.")

# functions
def trimandlowerword(string) -> str:
    return string.lower()[slice(string.index(' '))] if " " in string else string.lower()


wrongAnswersDict = {}

system('cls')

# load vocab word translations
with open('C:/Users/Shawn/Desktop/vocab.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    vocab_dict = {}
    for row in csv_reader:
        vocab_dict[row[0]] = row[1]

# randomly shuffle vocabulary
randomizedKeys = list(vocab_dict.keys())
random.shuffle(randomizedKeys)
vocab_dict = dict([(key, vocab_dict[key]) for key in randomizedKeys])

print(f'Starting vocabulary quiz with {len(vocab_dict)} words...')
input("*Press ENTER to begin*\n")

# start quiz
for word in itertools.islice(vocab_dict, 0, 5):
    wordVariations = word.count('/') + 1
    if wordVariations == 1:
        print(f'\nTranslate the following word to french: {vocab_dict[word]}')
        translation = input()
        strippedWord = trimandlowerword(word)
        if translation != strippedWord:
            wrongAnswersDict[word] = translation
    else:
        noSpacesAllWords = re.sub(r"\s+", "", word)
        allWordsList = noSpacesAllWords.split('/')
        for index, wordVariation in enumerate(allWordsList):
            print(f'\nTranslate variation ({index}/{len(allWordsList)}) of the following word to french: {vocab_dict[word]}')
            translation = input()
            if translation not in allWordsList:
                wrongAnswersDict[word] = translation

# results
print(f'\n********************* RESULTS - {100 - ((len(wrongAnswersDict) / len(vocab_dict)) * 100):.2f}% ***********************')
print('{0: <20}'.format('English') + '{0: <25}'.format('French') + '{0: <25}'.format('Attempt'))
for word in wrongAnswersDict:
    print('{0: <20}'.format(vocab_dict[word]) + '{0: <25}'.format(word) + '{0: <25}'.format(wrongAnswersDict[word]))
print('**************************************************************')

