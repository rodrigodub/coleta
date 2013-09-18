#!/usr/bin/python

#################################################
## Main (Test)
## Main routine / test
## 
## v0.1.2
## 
## 
## Rodrigo Nobrega
## 20130914-20130918
#################################################



# import classes
from Download import *
from WebView import *


# main loop
def main():
	# prototype source of tables: csv files  
	file1 = '../Test/acQuire Data/01b All Collar.csv' 
	file2 = '../Test/acQuire Data/02 Survey.csv'
	file3 = '../Test/acQuire Data/03 Lithology.csv'
	file4 = '../Test/acQuire Data/04 Alteration.csv'
	file5 = '../Test/acQuire Data/05 Samples Checks.csv'

	# from Download #################################

	# create instance: session
	session = Download()
	# define source tables
	session.setTableSource("Hole", file1)
	session.setTableSource("Survey", file2)
	session.setTableSource("Interval1", file3)
	session.setTableSource("Interval2", file4)
	session.setTableSource("Samples", file5)
	# get the fields list
	session.setFieldsList("Hole")
	session.setFieldsList("Survey")
	session.setFieldsList("Interval1")
	session.setFieldsList("Interval2")
	session.setFieldsList("Samples")
	
	# from WebView ##################################

	# create instance: web
	web = WebView()
	# define final dictionary
	for k, v in session.iteritems():
		if v:
			web[k] = v



	# test
	print web
	# session.parseFile("Hole")
	
	# print session.getFieldNames("Samples")
	# print session.dictOfFields["Hole"][-1]
	# for fld in session.dictOfFields["Hole"]:
	#	print fld
	# for key in session.dictOfFields:
	#	print key, session.dictOfFields[key]



	#print colar.fileNameTest
	#colar.parseFileTest()
	#colar.getFieldNamesTest()
	
 

# main, calling main loop
if __name__ == '__main__':
	main()  










