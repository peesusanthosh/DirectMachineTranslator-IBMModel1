# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:19:58 2017

@author: santh
"""
def main(): 
    t_eng = open('spatoengtrastled.txt', 'r')
    posTagList = []
    for i in t_eng:
        token = nltk.word_tokenize(i)
        tags = nltk.pos_tag(token)
        print (tags)
        posTagList.append(tags)


    finalTranslated = open('result.txt', 'w')
    for pos in posTagList: 
        pos = properNounArticles(pos)
        pos = attributeAdjectives(pos)
        pos = consecutiveSameWords(pos)
        pos = Vowel(pos)
        pos = objectVerbs(pos)
        pos = removeBeBeforeVerbs(pos)

        for t in pos: 
            finalTranslated.write(t[0] + ' ')
        finalTranslated.write('\n')


def noun(pos): 
    if pos[1] == 'NN' or pos[1] == 'NNS' or pos[1] == 'NNP' or pos[1] == 'NNPS': 
        return True
    return False

def non_proper_non(pos): 
    if pos[1] == 'NN' or pos[1] == 'NNS': 
        return True
    return False

def proper_noun(pos): 
    if pos[1] == 'NNP' or pos[1] == 'NNPS': 
        return True
    return False

def verb(pos): 
    if pos[1] == 'VB' or pos[1] == 'VBD' or pos[1] == 'VBG' or pos[1] == 'VBN' or pos[1] == 'VBP' or pos[1] == 'VBZ': 
        return True
    return False

def adjective(pos): 
    return pos[1] == 'JJ'

def adverb(pos): 
    return pos[1] == 'RB'

def vowel(pos):
    if pos == 'a' or pos == 'e' or pos == 'i' or pos == 'o' or pos == 'u': 
        return True
    return False

# RULE 1: 
def properNounArticles(line): 
    removeArticle = []
    for i in range(0, len(line)): 
        current = line[i]
        #print 'curr = ', curr
        if current[1] == 'DT' and i != len(line)-1: 
            next = line[i+1]
            if proper_noun(next) is False: 
                removeArticle.append(current)
        else: 
            removeArticle.append(current)
       
    return removeArticle

# RULE 2: 
def attributeAdjectives(line): 
    for i in range(1, len(line)): 
        current = line[i]
        previous = line[i-1]
        if adjective(current) and noun(previous): 
            line[i-1] = current
            line[i] = previous
    return line

# RULE 3: 
def consecutiveSameWords(line): 
    removeWords = []
    removeWords.append(line[0])
    for i in range(1, len(line)): 
        current = line[i]
        previous = line[i-1]
        if current[0] != previous[0]: 
            removeWords.append(current)
    return removeWords

# RULE 4: 
def Vowel(line): 
    for i in range(0, len(line)): 
        current = line[i]
        if current[0] == 'a' and i < len(line)-1:
            next = line[i+1]
            if vowel(next[0][0]): 
                line[i] = ('an', 'DT')
        if current[0] == 'an' and i < len(line)-1: 
            next = line[i+1]
            if vowel(next[0][0]) is False:
                line[i] = ('a', 'DT')
    return line

# RULE 7: 
def objectVerbs(line):
    reordered = []
    i = 0
    while i < len(line):
        currTuple = line[i]
        currWord = currTuple[0]
        if currTuple[1] == 'PRP':
            nextTuple = line[i+1]
            nextWord = nextTuple[0]
            if verb(nextTuple):
                print (currWord + ' ' + nextWord)
                reordered.append(nextTuple)
                reordered.append(currTuple)
                i += 1
        else:
            reordered.append(line[i])
        i += 1
    return reordered

# RULE 6: 
def removeBeBeforeVerbs(line): 
    removeBe = []
    for index in range(0, len(line)): 
        current = line[index]
        #print 'curr = ', curr
        if current[0] == 'be' and index != len(line)-1: 
            next = line[index+1]
            if verb(next) is False: 
                removeBe.append(current)
        else: 
            removeBe.append(current)
        
    return removeBe



def Adverb(tup):
    currWordPOS = tup[1]
    if currWordPOS == 'RB' or currWordPOS == 'RBR' or currWordPOS == 'RBS':
        return True
    return False

if __name__ == "__main__":
    main()
