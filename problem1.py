"""
Created on Mon Nov 27 22:41:16 2017

@author: Sant
"""
import re
import nltk
def main(): 
    test = open('spanishtest.txt', 'r') 
    # opening a file in write mode to write the sentences after conversion from spanish to english
    spntoend = open('spatoengtrastled.txt', 'w') 
    dic = dict() 
    closeddic = open('spntoeng.txt', 'r') 
    for i in closeddic.readlines(): 
        words = i.split()
        print(words)
        original = words[0]
        t_english = ''
        for i in range(1, len(words)): 
            t_english += words[i] + ' '
        t_english = t_english.strip()
        dic[original] = t_english

    for i in test.readlines(): 
        for w in i.split(): 
            word = w.lower() 
            word = re.sub('[.?!",]', '', word) 
            
            spntoend.write(dic[word] + ' ')
        spntoend.write('\n')
        conversion()


if __name__ == "__main__":
    main()
