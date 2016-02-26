import requests
import json

Friendname = []
Friendnumber = []
#i = 0
#mean = 0
#median = 0
#stddev = 0
#total = 0
lastline = ' '
for line in open('TwitterData.txt','r'):
    a = ' '
    b = ' '
    #if '</node>'


    #Get all friend information
    if ' " ' in line  and ' ": ' in lastline:
        a = line[0:-1]
        Friendname.append(a)
        #print 'Name: ' + b
        
    if ' "twitter_followers_counts": ' in line and '},' in lastline:
        b = line[28:-1]
        b = int(b)
        Friendnumber.append(b)
        #print 'Number of Friends: ' + b
        print 'Name: ' + Friendname[i]
        print 'Number of Friends: ' + str(Friendnumber[i])
        i = i + 1
        print 'Counter: ' + str(i)
        print '\n'
    if '</node>' in line and '<data key="mutual_friend_count"' in lastline:
        b = 0
        Friendnumber.append(b)
        print 'Name: ' + Friendname[i]
        print 'Number of Friends: ' + str(Friendnumber[i])
        i = i + 1
        print 'Counter: ' + str(i)
        print '\n'
    lastline = line

#







