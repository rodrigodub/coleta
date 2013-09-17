#!/usr/bin/python

file1 = 'acQuire Data/01 All Collar.csv' 
list1 = []
list2 = []


arq = open(file1,'r')
# iterate
for eachLine in arq:
	#print eachLine
	#a = arq.readline()
	list1.append(eachLine.replace("\r\n","").split(","))
#print list1
	

idxhole = list1[0].index("HOLEID")
print idxhole

for linha in list1[1:]:
	list2.append(linha[idxhole])

print list2

# close
arq.close()


