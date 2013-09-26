#!/usr/bin/python

#################################################
## Main (Test)
## Main routine / test
## 
## v0.1.3
## 
## 
## Rodrigo Nobrega
## 20130914-20130926
#################################################



# import classes
from Download import *
from WebView import *


# main loop
def main():
	# prototype source of tables: csv files  
	file1 = '../Test/acQuire Data/01c All Collar.csv' 
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
	# set the fields list
	session.setFieldsList("Hole")
	session.setFieldsList("Survey")
	session.setFieldsList("Interval1")
	session.setFieldsList("Interval2")
	session.setFieldsList("Samples")
	# define the Hole List
	session.defineHoleList()
	# define final contents to create offline db
	session.setAvailableContent()

	
	# from WebView ##################################

	# create instance: web
	web = WebView()
	# create files list
	web.createFileList(session.contentList, session.holeList)
	# create index.html file
	web.createIndexPage(session.contentList, session.holeList)
	# create Hole%.html files
	web.createHolePages(session.contentList, session.holeList)





	# TEST ##########################################

	
	
	# Download ######################################
	print session.holeList
	print session.contentList
	
	#print session.tableOrder["Samples"]
	#print session.tableOrder.keys()
	#print help(session)
	#print session.getFieldNames("Interval1")
	#print session.dictOfTables
	#print session.dictOfTables[session.tableOrder["Hole"]]
	#print session.dictOfFields
	#print session.dictOfFields[session.tableOrder["Hole"]][-1]
	#for fld in session.dictOfFields[session.tableOrder["Hole"]]:
	#	print fld
	#for key in session.dictOfFields:
	#	print key, session.dictOfFields[key]
	#session.parseFile("Hole")



	# WebView ######################################
	#print help(web)
	#print web.pageSet
	#print web.pageSet[session.tableOrder["Samples"]]
	#print sorted(web.pageSet)
	#for i,k in enumerate(sorted(web.pageSet)):
	#	print k, web.pageSet[k]
	print web.fileList


	
 

# main, calling main loop
if __name__ == '__main__':
	main()  










