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
	session.setTableSource(1, file1)
	session.setTableSource(2, file2)
	session.setTableSource(3, file3)
	session.setTableSource(4, file4)
	session.setTableSource(8, file5)
	# set the fields list
	session.setFieldsList(1)
	session.setFieldsList(2)
	session.setFieldsList(3)
	session.setFieldsList(4)
	session.setFieldsList(8)
	
	# from WebView ##################################

	# create instance: web
	web = WebView()
	# define final dictionary
	for k, v in session.dictOfTables.iteritems():
		if v:
			web.pageSet[k] = v



	# test

	# WebView ######################################
	#print help(web)
	#print web.pageSet
	#print sorted(web.pageSet)
	for i,k in enumerate(sorted(web.pageSet)):
		print i,k, web.pageSet[k]
	#for i in range(0, web.)
	
	
	# Download ######################################
	#print help(session)
	#print session.getFieldNames("Samples")
	#print session.dictOfFields["Hole"][-1]
	#print session.dictOfTables
	#print session.dictOfFields
	#for fld in session.dictOfFields["Hole"]:
	#	print fld
	#for key in session.dictOfFields:
	#	print key, session.dictOfFields[key]
	#session.parseFile("Hole")



	#print colar.fileNameTest
	#colar.parseFileTest()
	#colar.getFieldNamesTest()
	
 

# main, calling main loop
if __name__ == '__main__':
	main()  










