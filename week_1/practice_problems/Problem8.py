import re

wordFreqDict = {}
def wordFrequency(wordString):
    regex = re.compile('[^a-zA-Z]')
    wordString = regex.sub('', wordString)
    
    for character in wordString.lower():
        wordFreqDict[character] = wordFreqDict.get(character, 0) + 1
    print (wordFreqDict)


wordFrequency("Hello World! 123")