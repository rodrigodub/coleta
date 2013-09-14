#################################################
## Download
## Routine to get Data to Work on
## 
## v0.1.0
## for ticket ID43
## 
## Rodrigo Nobrega
## 20130914-
#################################################


# class Download
class Download(object):
	"""Define the Download dta to go offline"""

	# constructor with attributes
	def __init__(self, fileNameTest):
		super(Download, self).__init__()
		self.fileNameTest = fileNameTest

	# parseFile / parseFileTest
	def parseFileTest(self):
		# open
		arq = open(self.fileNameTest,'r')
		# iterate
		for eachLine in arq:
			print eachLine
		# close
		arq.close()
		


