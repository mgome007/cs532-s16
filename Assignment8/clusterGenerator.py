#!/usr/local/bin/python

#https://github.com/shawnmjones/
#A majority of this code was aquired from a programmer GItHub profile by a : Shawn Jones


# "Programming Collective Intelligence, Chapter 3"
import sys
import argparse 

sys.path.insert(0, '../libs')

import clusters

blognames,words,data=clusters.readfile('blogdata1.txt')

print "For k=5"
kclust=clusters.kcluster(data, k=5)
print

print "For k=10"
kclust=clusters.kcluster(data, k=10)
print

print "For k=20"
kclust=clusters.kcluster(data, k=20)
print