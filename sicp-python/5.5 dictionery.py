# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 15:26:51 2018

@author: kevin
"""

monthNumbers = {'Jan':1,'Feb':2,'Mar':3,'April':4,'May':5,
                1:'Jan',2:'Feb',3:'Mar',4:'April',5:'May'}
print('The third month is '+monthNumbers[3])
dist = monthNumbers['April'] - monthNumbers['Jan']
print('April and Jan are',dist,'months apart')
print(monthNumbers.keys())

EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je',
'eat':'mange', 'drink':'bois', 'John':'Jean',
'friends':'amis', 'and': 'et', 'of':'du','red':'rouge'}
FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I',
'mange':'eat', 'bois':'drink', 'Jean':'John',
'amis':'friends', 'et':'and', 'du':'of', 'rouge':'red'}
dicts = {'English to French':EtoF, 'French to English':FtoE}
def translateWord(word, dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word
def translate(phrase, dicts, direction):
    UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCLetters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCLetters + LCLetters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word = word + c
        else:
            translation = translation\
            + translateWord(word, dictionary) + c
            word = ''
    return translation + ' ' + translateWord(word, dictionary)
print (translate('I drink good red wine, and eat bread.',
                dicts,'English to French'))
print (translate('Je bois du vin rouge.',
                dicts, 'French to English'))
FtoE['du'] = 'good'
print(FtoE['du'])
print (translate('Je bois du vin rouge.',
                dicts, 'French to English'))



