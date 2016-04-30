#Majority of this code was aquired from Collective Intelligence Programming Book and the logic for it was refered to by a fellow GithUb user I came across to. 
#Collective Intelligence Programming textbook

import math 
from random import random,randint
import math

def readfile(filename):
 lines=[]
 for line in open(filename):
   lines.append(line)
    
 colnames=lines[0].strip().split('\t')[1:]
 rownames=[]
 data=[]
 for line in lines[1:]:
   p=line.strip().split('\t')
   rownames.append(p[0])
   data.append([float(x) for x in p[1:]])
 return rownames,colnames,data
 

blognames,words,data=readfile(r'Z:\cs432\A10\categories.txt')


if __name__ == '__main__':
	categories = ['Zika', 'Research', 'Cancer', 'Ebola', 'HIV', 'Outbreak']
	notStrings = ['not-{0}'.format(i) for i in categories]
	contraStrings = {}
	for i in categories:
		contraStrings[i] = [j for j in range(len(notStrings)) if i not in notStrings[j]]
#THe logic behind thsi code portion was shown to me by my fellow colleague Kevin Clemmons
	for i in contraStrings.keys():
		print("{0}: ".format(i))
		for contraString in contraStrings[i]:
			print("\t{0}".format(notStrings[contraString]))
		print('\n')
