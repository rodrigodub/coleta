#!/usr/bin/python

#################################################
## Main (Test)
## Main routine / test
## 
## v0.1.1
## 
## 
## Rodrigo Nobrega
## 20130914-20130915
#################################################



# import classes
from Download import *


# main loop
def main():
	# prototype source of tables: csv files  
	file1 = '../Test/acQuire Data/01 All Collar.csv' 
	file2 = '../Test/acQuire Data/02 Survey.csv'
	file3 = '../Test/acQuire Data/03 Lithology.csv'
	file4 = '../Test/acQuire Data/04 Alteration.csv'
	file5 = '../Test/acQuire Data/05 Samples Checks.csv'
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
	# test
	# print session.getFieldNames("Samples")
	# print session.dictOfFields["Hole"][-1]
	for fld in session.dictOfFields["Survey"]:
		print fld


	#print colar.fileNameTest
	#colar.parseFileTest()
	#colar.getFieldNamesTest()
	
 

# main, calling main loop
if __name__ == '__main__':
	main()  










