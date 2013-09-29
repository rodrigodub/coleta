#################################################
## Download
## Routine to get Data to Work on
## 
## v0.1.3
## for ticket ID43
## 
## Rodrigo Nobrega
## 20130914-20130919
#################################################


# class Download
class Download(object):
	"""
	Define the Download data to go offline
	"""

	# constructor with attributes
	def __init__(self):
		super(Download, self).__init__()
		#self.fileName = fileName
		self.tableOrder = {"Hole":1, "Survey":2, "Interval1":3, "Interval2":4, "Interval3":5, "Interval4":6, "Interval5":7, "Samples":8}
		self.dictOfTables = {1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:""}
		self.dictOfFields = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
		self.holeList = []
		self.contentList = {1:"Hole", 2:"Survey", 3:"Interval1", 4:"Interval2", 5:"Interval3", 6:"Interval4", 7:"Interval5", 8:"Samples"}


	# parse file passed as parameter 
	def parseFile(self,dictval):
		# open
		arq = open(self.dictOfTables[self.tableOrder[dictval]],'r')
		# iterate
		for eachLine in arq:
			print eachLine
		# close
		arq.close()


	# define tables source that will fill dictOfTables
	def setTableSource(self,dictval,fileName):
		self.dictOfTables[self.tableOrder[dictval]] = fileName

		
	# get field names from file 
	def getFieldNames(self,dictval):
		# open
		arq = open(self.dictOfTables[self.tableOrder[dictval]],'r')
		# get first line
		fieldList = arq.readline().replace("\r","").replace("\n","").split(",")
		# return fieldList
		return fieldList
		# close
		arq.close()


	# set fields list for the table 
	def setFieldsList(self,dictval):
		self.dictOfFields[self.tableOrder[dictval]] = self.getFieldNames(dictval)


	# set list of holes from the "Hole" file 
	def defineHoleList(self):
		# temp list with "Hole" file content as lists also
		tempList = []
		# parse file to tempList
		arq = open(self.dictOfTables[self.tableOrder["Hole"]],'r')
		for eachLine in arq:
			tempList.append(eachLine.replace("\r\n","").split(","))
		# find index for HOLEID field
		idxhole = tempList[0].index("HOLEID")
		# load the content of this field into holeList
		for linha in tempList[1:]:
			self.holeList.append(linha[idxhole])
		# close
		arq.close()
		# sort list
		self.holeList.sort()
		

	# define the contents based on selected source files (or source tables)
	def setAvailableContent(self):
		for k, v in self.dictOfTables.iteritems():
			if v:
				pass
			else: 
				del self.contentList[k] 











