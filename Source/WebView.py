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


	# create web pages : index.html
	# Parameters:
	# holeList : the list of selected holes
	def createIndexPage(self, holeList):
		# define file name
		fileName = "html/index.html"
		# open file
		arq = open(fileName, 'w')
		# write file, first static part
		arq.write('<!DOCTYPE html>\n')
		arq.write('<html lang="en">\n')
		arq.write('  <head>\n')
		arq.write('    <meta charset="utf-8">\n')
		arq.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
		arq.write('    <meta name="description" content="Data Collection">\n')
		arq.write('    <meta name="author" content="Rodrigo Nobrega">\n')
		arq.write('    <link rel="shortcut icon" href="../Bootstrap/assets/ico/favicon.png">\n')
		arq.write('    <title>Coleta : Offline data collection</title>\n')
		arq.write('    <link href="../Bootstrap/dist/css/bootstrap.css" rel="stylesheet">\n')
		arq.write('    <link href="../Bootstrap/dist/css/bootstrap-theme.min.css" rel="stylesheet">\n')
		arq.write('    <link href="theme.css" rel="stylesheet">\n')
		arq.write('  </head>\n')
		arq.write('  <body>\n')
		arq.write('    <div class="navbar navbar-inverse navbar-fixed-top">\n')
		arq.write('      <div class="container">\n')
		arq.write('        <div class="navbar-header">\n')
		arq.write('          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n')
		arq.write('            <span class="icon-bar"></span>\n')
		arq.write('            <span class="icon-bar"></span>\n')
		arq.write('            <span class="icon-bar"></span>\n')
		arq.write('          </button>\n')
		arq.write('          <a class="navbar-brand" href="index.html">Coleta</a>\n')
		arq.write('        </div>\n')
		arq.write('        <div class="navbar-collapse collapse">\n')
		arq.write('          <ul class="nav navbar-nav">\n')
		arq.write('            <li class="disabled"><a href="#">Collar</a></li>\n')
		arq.write('            <li class="disabled"><a href="#">Survey</a></li>\n')
		arq.write('            <li class="dropdown disabled">\n')
		arq.write('              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Geology <b class="caret"></b></a>\n')
		arq.write('              <ul class="dropdown-menu">\n')
		arq.write('                <li class="disabled"><a href="#">Lithology</a></li>\n')
		arq.write('                <li class="disabled"><a href="#">Alteration</a></li>\n')
		arq.write('              </ul>\n')
		arq.write('            </li>\n')
		arq.write('            <li class="disabled"><a href="#">Samples and Checks</a></li>\n')
		arq.write('          </ul>\n')
		arq.write('        </div>\n')
		arq.write('      </div>\n')
		arq.write('    </div>\n')
		arq.write('    <div class="container theme-showcase">\n')
		arq.write('      <div class="jumbotron">\n')
		arq.write('        <h1>Coleta</h1>\n')
		arq.write('        <p>This is the index page to select the drillhole you are going to log.</p>\n')
		arq.write('        <p><a class="btn btn-primary btn-lg disabled">Learn more &raquo;</a></p>\n')
		arq.write('      </div>\n')
		arq.write('      <div class="page-header">\n')
		arq.write('        <h1>Drillhole</h1>\n')
		arq.write('      </div>\n')
		arq.write('      <ul class="nav nav-pills nav-justified">\n')
		# write file, first dynamic part
		for h in holeList:
			arq.write('        <li><a href="Hole' + h + '.html">' + h + '</a></li>\n')
		# write file, second static part
		arq.write('      </ul>\n')
		arq.write('      <br></br>\n')
		arq.write('      <br></br>\n')
		arq.write('      <br></br>\n')
		arq.write('      <div class="well">\n')
		arq.write('        <p class="text-right"><small>&copy;2013 Rodrigo Nobrega ::: Version 0.1</small></p>\n')
		arq.write('      </div>\n')
		arq.write('    </div>\n')
		arq.write('    <script src="../Bootstrap/assets/js/jquery.js"></script>\n')
		arq.write('    <script src="../Bootstrap/dist/js/bootstrap.min.js"></script>\n')
		arq.write('    <script src="../Bootstrap/assets/js/holder.js"></script>\n')
		arq.write('  </body>\n')
		arq.write('</html>\n')
		# close file
		arq.close()


	

	


	


