#################################################
## WebView
## Routine to create the HTML files
## 
## v0.1.0
## for ticket ID42
## 
## Rodrigo Nobrega
## 20130917-20130918
#################################################


# class WebView
class WebView(object):
	"""
	Class to crete the HTML pages
	based tables and fields list
	from the source database.
	"""

	# constructor with attributes
	def __init__(self):
		super(WebView, self).__init__()
		# self.arg = arg
		self.pageSet = {1:"Hole", 2:"Survey", 3:"Interval1", 4:"Interval2", 5:"Interval3", 6:"Interval4", 7:"Interval5", 8:"Samples"}
		self.fileList = ["index.html"]


	# create HTML files list. 
	# Parameters: 
	# contentList : dictionary of available files/tables
	# holeList : the list of selected holes
	def createFileList(self,contentList,holeList):
		for k,v in contentList.iteritems():
			for h in holeList:
				self.fileList.append(v + h + ".html")


	# create web pages
	# index.html
	def createIndexPage():
		pass
	

	


	


