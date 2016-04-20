#!/urs/bin/python

import os
import shutil
import csv

def returnCSVinFolder(path='./temp'):
	"""The following reads content in a directory and returns all the files that have an extension of .csv"""
	files = [] #empty list
	for filename in os.listdir(path):
		if filename.lower().endswith('.csv'):
			files.append(filename)
	return files


def parseCSV(pathToFile):
	"""returns a list of the parsed csv content in a two dimensional array"""
	csvfile = open(pathToFile, 'rb')
	spamreader = csv.reader(csvfile)
	return spamreader

if __name__ == '__main__':
	while 1: #infinite loop to keep polling the directory
		listfiles = returnCSVinFolder()
		for afile in listfiles:
			for row in parseCSV('./temp/'+afile):
				#this is where you would add code to insert the parsed file into the DB or handle the data in another way
				print row
			shutil.move('./temp/'+afile, './save/'+afile)
