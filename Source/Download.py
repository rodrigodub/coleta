#################################################
## Download
## Routine to get Data to Work on
## 
## v0.1.2
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

	# parse file / parseFile
	def parseFile(self,dictkey):
		# open
		arq = open(self.dictOfTables[dictkey],'r')
		# iterate
		for eachLine in arq:
			print eachLine
		# close
		arq.close()


	# define tables source / setTableSource
	def setTableSource(self,dictkey,fileName):
		self.dictOfTables[dictkey] = fileName

		
	# get field names / getFieldNames
	def getFieldNames(self,dictkey):
		# open
		arq = open(self.dictOfTables[dictkey],'r')
		# get first line
		fieldList = arq.readline().replace("\r\n","").split(",")
		# return fieldList
		return fieldList
		# close
		arq.close()


	# set fields list for the table / setFieldsList
	def setFieldsList(self,dictkey):
		self.dictOfFields[dictkey] = self.getFieldNames(dictkey)


