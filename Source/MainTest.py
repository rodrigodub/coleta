#!/usr/bin/python

#################################################
## Main (Test)
## Main routine / test
## 
## v0.1.0
## 
## 
## Rodrigo Nobrega
## 20130914
#################################################



# import classes
from Download import *


# main loop
def main():  
	fnam = '../Test/acQuire Data/01 All Collar.csv' #03 Lithology.csv'
	colar = Download(fnam)
	print colar.fileNameTest
	colar.parseFileTest()
	
 

# main, calling main loop
if __name__ == '__main__':
    main()  










