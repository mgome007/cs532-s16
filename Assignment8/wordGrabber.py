#!/usr/local/bin/python
#https://github.com/shawnmjones/
#A majority of this code was aquired from a programmer GItHub profile by a : Shawn Jones


# "Programming Collective Intelligence, Chapter 3"
import sys
import argparse 

sys.path.insert(0, '../libs')

import clusters
import operator

import pprint

def getWordscores(words, data):

    wordscores = {}

    for i in range(len(words)):
        sys.stderr.write('examining ' + words[i] + '\n')
    
        for j in range(len(data)):
    
            if words[i] in wordscores:
                wordscores[words[i]] += data[j][i]
            else:
                wordscores[words[i]] = data[j][i]

    return wordscores

def getTopNWords(wordscores, n):

    topNWords = []

    reversedWordscores = sorted(
        wordscores.iteritems(), key=operator.itemgetter(1), reverse=True
        )

    for i in range(n):
        sys.stderr.write(
            "adding " + reversedWordscores[i][0] + " with a score of "
                + str(reversedWordscores[i][1]) + '\n'
            )
        topNWords.append(reversedWordscores[i][0])

    return topNWords


if __name__ == '__main__':
    fileName = None
    saveFileName = None
    blognames = None 
    words = None 
    data = None 
    clust = None

  
    n = 500
    blognames,words,data = clusters.readfile('blogdata1.txt')
    wordscores = getWordscores(words, data) 

    topNWords = getTopNWords(wordscores, n)

    indexlist = []

    for word in topNWords:
        indexlist.append(words.index(word))

    lines = []

    line = []
    line.append('Blog')

    for i in range(len(words)):

        if i in indexlist:
            line.append(words[i])

    lines.append(line)

    for i in range(len(blognames)):
        line = []
        line.append(blognames[i])

        for j in range(len(words)):
            if j in indexlist:
                line.append(str(int(data[i][j])))

        lines.append(line)
   
    for line in lines:
        print "\t".join(line)
print lines
f = open('wordData.txt', 'w+')
f.write(str(lines)) 
