#!/usr/local/bin/python

#https://github.com/shawnmjones/
#A majority of this code was aquired from a programmer GItHub profile by a : Shawn Jones


# "Programming Collective Intelligence, Chapter 3"

import sys
import argparse

sys.path.insert(0, '../libs')

import clusters


if __name__ == '__main__':
	fileName = None
	blognames = None 
	words = None 
	data = None 
	clust = None

	parser = argparse.ArgumentParser(description='Makes a dendrogram in either ascii or jpeg format.')
	parser.add_argument('-f',action='store',dest='matrixFile',nargs=1,help='Name of the file containing the blog matrix.')
	parser.add_argument('-ascii',action='store_true',dest='asciiDendrogram',help='Prints a dendrogram to the standard output.')
	parser.add_argument('-jpeg',action='store',dest='jpegDraw',nargs=1,help='Print the dendrogram to a jepeg file.')

	args = parser.parse_args()

	if args.matrixFile:
		fileName = str(args.matrixFile[0])
		blognames,words,data=clusters.readfile(fileName)

	if data is not None:
		sys.stderr.write('Performing hcluster for {0}\n'.format(fileName))
		clust = clusters.hcluster(data)
		sys.stderr.write('...Finished hcluster for {0}\n'.format(fileName))

	if args.asciiDendrogram:
		if clust is not None:
			clusters.printclust(clust, labels=blognames)

	if args.jpegDraw:
		if clust is not None:
			jpegFileName = str(args.jpegDraw[0])
			if '.jpg' not in jpegFileName:
				jpegFileName = jpegFileName + '.jpg'

			
			sys.stderr.write('Writing dendrogram to {0}\n'.format(jpegFileName))

			clusters.drawdendrogram(clust, blognames, jpeg=jpegFileName)

			sys.stderr.write('...Dendrogram written to {0}\n'.format(jpegFileName))