#################################################
## WebView
## Routine to create the HTML files
## 
## v0.1.0
## for ticket ID42
## 
## Rodrigo Nobrega
## 20130917-20130926
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
	# contentList : dictionary of available files/tables
	# holeList : the list of selected holes
	def createIndexPage(self, contentList, holeList):
		# define file name
		fileName = 'html/index.html'
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
		arq.write('              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Intervals <b class="caret"></b></a>\n')
		arq.write('              <ul class="dropdown-menu">\n')
		# write file, first dynamic part
		for k, v in contentList.iteritems():
			if (k > 2 and k < 8):
				arq.write('                <li class="disabled"><a href="#">%s</a></li>\n' % v)
		# write file, second static part
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
		# write file, second dynamic part
		for h in holeList:
			arq.write('        <li><a href="Hole%s.html">%s</a></li>\n' % (h, h))
		# write file, third static part
		arq.write('      </ul>\n')
		arq.write('      <br></br>\n')
		arq.write('      <br></br>\n')
		arq.write('      <br></br>\n')
		arq.write('      <div class="well">\n')
		arq.write('        <p class="text-right"><small>&copy;2013 ::: Version 0.1</small></p>\n')
		arq.write('      </div>\n')
		arq.write('    </div>\n')
		arq.write('    <script src="../Bootstrap/assets/js/jquery.js"></script>\n')
		arq.write('    <script src="../Bootstrap/dist/js/bootstrap.min.js"></script>\n')
		arq.write('    <script src="../Bootstrap/assets/js/holder.js"></script>\n')
		arq.write('  </body>\n')
		arq.write('</html>\n')
		# close file
		arq.close()


	# create web pages : Hole%.html
	# Parameters:
	# contentList : dictionary of available files/tables
	# holeList : the list of selected holes	
	# fieldList : list of fields for the file/table
	def createHolePages(self, contentList, holeList, fieldList):
		# iterate between holes
		for h in holeList:
			# define file name
			fileName = 'html/Hole%s.html' % h
			# open file
			arq = open(fileName, 'w')
			# write file, STATIC
			arq.write('<!DOCTYPE html>\n')
			arq.write('<html lang="en">\n')
			arq.write('  <head>\n')
			arq.write('    <meta charset="utf-8">\n')
			arq.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
			arq.write('    <meta name="description" content="">\n')
			arq.write('    <meta name="author" content="">\n')
			arq.write('    <link rel="shortcut icon" href="../Bootstrap/assets/ico/favicon.png">\n')
			# write file, DYNAMIC
			arq.write('    <title>Coleta : %s Collar</title>\n' % h) 
			# write file, STATIC
			arq.write('    <link href="../Bootstrap/dist/css/bootstrap.css" rel="stylesheet">\n')
			arq.write('    <link href="../Bootstrap/dist/css/bootstrap-theme.min.css" rel="stylesheet">\n')
			arq.write('    <link href="theme.css" rel="stylesheet">\n')
			arq.write('      <script src="../Bootstrap/assets/js/html5shiv.js"></script>\n')
			arq.write('      <script src="../Bootstrap/assets/js/respond.min.js"></script>\n')
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
			# write file, DYNAMIC
			arq.write('            <li class="active"><a href="Hole%s.html">Collar</a></li>\n' % h)
			arq.write('            <li><a href="Survey%s.html">Survey</a></li>\n' % h)
			arq.write('            <li class="dropdown">\n')
			arq.write('              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Intervals <b class="caret"></b></a>\n')
			arq.write('              <ul class="dropdown-menu">\n')
			for k, v in contentList.iteritems():
				if (k > 2 and k < 8):
					arq.write('                <li><a href="%s%s.html">%s</a></li>\n' % (v,h,v))
			arq.write('              </ul>\n')
			arq.write('            </li>\n')
			arq.write('            <li><a href="Samples%s.html">Samples and Checks</a></li>\n' % h)
			arq.write('          </ul>\n')
			arq.write('        </div><!--/.nav-collapse -->\n')
			arq.write('      </div>\n')
			arq.write('    </div>\n')

			arq.write('    <div class="container theme-showcase">\n')

			arq.write('      <!-- Main jumbotron for a primary marketing message or call to action -->\n')
			arq.write('      <div class="jumbotron">\n')
			arq.write('        <h1>%s</h1>\n' % h)
			arq.write('        <p>Edit drillhole collar details.</p>\n')
			arq.write('        <p><a class="btn btn-primary btn-lg">Learn more &raquo;</a></p>\n')
			arq.write('      </div>\n')


			# drillhole details
			arq.write('      <!-- DRILLHOLE DETAILS -->\n')
			arq.write('      <div class="page-header">\n')
			arq.write('        <h1>Collar Details</h1>\n')
			arq.write('      </div>\n')
			# start details
			arq.write('      <form class="form-inline" role="form">\n')
			# controls
			for field in fieldList:
				if field <> 'HOLEID':
					arq.write('        <div class="form-group">\n')
					arq.write('          <label for="%s">%s</label>\n' % (field,field))
					arq.write('          <input type="text" class="form-control" id="%s" placeholder="%s">\n' % (field,field))
					arq.write('        </div>\n')

			#arq.write('        <div class="form-group">\n')
			#arq.write('          <label for="TENEMENTID">TENEMENTID</label>\n')
			#arq.write('          <select id="TENEMENTID" class="form-control">\n')
			#arq.write('            <option>E446</option>\n')
			#arq.write('            <option>E447</option>\n')
			#arq.write('            <option>F256</option>\n')
			#arq.write('            <option>W3328</option>\n')
			#arq.write('          </select>\n')
			#arq.write('        </div>\n')

			#arq.write('        <div class="form-group">\n')
			#arq.write('          <label for="HOLETYPE">HOLETYPE</label>\n')
			#arq.write('          <select id="HOLETYPE" class="form-control" disabled>\n')
			#arq.write('            <option>DRILLHOLE</option>\n')
			#arq.write('          </select>\n')
			#arq.write('        </div>\n')
			
			#arq.write('        <div class="form-group">\n')
			#arq.write('          <label for="EAST">EAST</label>\n')
			#arq.write('          <input type="number" class="form-control" id="EAST" placeholder="EAST">\n')
			#arq.write('        </div>\n')
			
			#arq.write('        <div class="form-group">\n')
			#arq.write('          <label for="HoleComments">HoleComments</label>\n')
			#arq.write('          <textarea class="form-control" id="HoleComments"placeholder="HoleComments" rows="3"></textarea>\n')
			#arq.write('        </div>\n')    

			# end details                     
			arq.write('      </form>\n')

			# select holes
			arq.write('      <!-- DRILLHOLE SELECTOR -->\n')
			arq.write('      <div class="page-header">\n')
			arq.write('        <h3>Change drillhole</h3>\n')
			arq.write('      </div>\n')
			arq.write('      <ul class="nav nav-pills nav-justified">\n')
			for dh in holeList:
				if dh == h:
					arq.write('        <li class="active disabled"><a href="Hole%s.html">%s</a></li>\n' % (dh,dh))
				else:
					arq.write('        <li><a href="Hole%s.html">%s</a></li>\n' % (dh,dh))			
			arq.write('      </ul>\n')


			# well
			arq.write('      <br></br>\n')

			arq.write('      <div class="well">\n')
			arq.write('        <p class="text-right"><small>&copy;2013 ::: Version 0.1</small></p>\n')
			arq.write('      </div>\n')


			arq.write('    </div> <!-- /container -->\n')


			arq.write('    <!-- Bootstrap core JavaScript\n')
			arq.write('    ================================================== -->\n')
			arq.write('    <!-- Placed at the end of the document so the pages load faster -->\n')
			arq.write('    <script src="../Bootstrap/assets/js/jquery.js"></script>\n')
			arq.write('    <script src="../Bootstrap/dist/js/bootstrap.min.js"></script>\n')
			arq.write('    <script src="../Bootstrap/assets/js/holder.js"></script>\n')
			arq.write('  </body>\n')
			arq.write('</html>\n')


			# close file
			arq.close()



	
	# create web pages : Survey%.html
	# Parameters:
	# contentList : dictionary of available files/tables
	# holeList : the list of selected holes	
	# fieldList : list of fields for the file/table
	def createSurveyPages(self, contentList, holeList, fieldList):
		# iterate between holes
		for h in holeList:
			# define file name
			fileName = 'html/Survey%s.html' % h
			# open file
			arq = open(fileName, 'w')
			# write file, STATIC
			arq.write('<!DOCTYPE html>\n')
			arq.write('<html lang="en">\n')
			arq.write('  <head>\n')
			arq.write('    <meta charset="utf-8">\n')
			arq.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
			arq.write('    <meta name="description" content="">\n')
			arq.write('    <meta name="author" content="">\n')
			arq.write('    <link rel="shortcut icon" href="../Bootstrap/assets/ico/favicon.png">\n')
			# write file, DYNAMIC
			arq.write('    <title>Coleta : %s Survey</title>\n' % h) 
			# write file, STATIC
			arq.write('    <link href="../Bootstrap/dist/css/bootstrap.css" rel="stylesheet">\n')
			arq.write('    <link href="../Bootstrap/dist/css/bootstrap-theme.min.css" rel="stylesheet">\n')
			arq.write('    <link href="theme.css" rel="stylesheet">\n')
			arq.write('      <script src="../Bootstrap/assets/js/html5shiv.js"></script>\n')
			arq.write('      <script src="../Bootstrap/assets/js/respond.min.js"></script>\n')
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
			# write file, DYNAMIC
			arq.write('            <li><a href="Hole%s.html">Collar</a></li>\n' % h)
			arq.write('            <li class="active"><a href="Survey%s.html">Survey</a></li>\n' % h)
			arq.write('            <li class="dropdown">\n')
			arq.write('              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Intervals <b class="caret"></b></a>\n')
			arq.write('              <ul class="dropdown-menu">\n')
			for k, v in contentList.iteritems():
				if (k > 2 and k < 8):
					arq.write('                <li><a href="%s%s.html">%s</a></li>\n' % (v,h,v))
			arq.write('              </ul>\n')
			arq.write('            </li>\n')
			arq.write('            <li><a href="Samples%s.html">Samples and Checks</a></li>\n' % h)
			arq.write('          </ul>\n')
			arq.write('        </div><!--/.nav-collapse -->\n')
			arq.write('      </div>\n')
			arq.write('    </div>\n')

			arq.write('    <div class="container theme-showcase">\n')

			arq.write('      <!-- Main jumbotron for a primary marketing message or call to action -->\n')
			arq.write('      <div class="jumbotron">\n')
			arq.write('        <h1>%s</h1>\n' % h)
			arq.write('        <p>Edit downhole survey.</p>\n')
			arq.write('        <p><a class="btn btn-primary btn-lg">Learn more &raquo;</a></p>\n')
			arq.write('      </div>\n')


			# survey details
			arq.write('      <!-- SURVEY DETAILS -->\n')
			arq.write('      <div class="page-header">\n')
			arq.write('        <h1>Survey</h1>\n')
			arq.write('      </div>\n')
			# start details
			arq.write('      <form class="form-inline" role="form">\n')
			# controls
			for field in fieldList:
				if field <> 'HOLEID':
					arq.write('        <div class="form-group">\n')
					arq.write('          <label for="%s">%s</label>\n' % (field,field))
					arq.write('          <input type="text" class="form-control" id="%s" placeholder="%s">\n' % (field,field))
					arq.write('        </div>\n')
			# end details                     
			arq.write('      </form>\n')

			# select holes
			arq.write('      <!-- DRILLHOLE SELECTOR -->\n')
			arq.write('      <div class="page-header">\n')
			arq.write('        <h3>Change drillhole</h3>\n')
			arq.write('      </div>\n')
			arq.write('      <ul class="nav nav-pills nav-justified">\n')
			for dh in holeList:
				if dh == h:
					arq.write('        <li class="active disabled"><a href="Survey%s.html">%s</a></li>\n' % (dh,dh))
				else:
					arq.write('        <li><a href="Survey%s.html">%s</a></li>\n' % (dh,dh))			
			arq.write('      </ul>\n')


			# well
			arq.write('      <br></br>\n')

			arq.write('      <div class="well">\n')
			arq.write('        <p class="text-right"><small>&copy;2013 ::: Version 0.1</small></p>\n')
			arq.write('      </div>\n')


			arq.write('    </div> <!-- /container -->\n')


			arq.write('    <!-- Bootstrap core JavaScript\n')
			arq.write('    ================================================== -->\n')
			arq.write('    <!-- Placed at the end of the document so the pages load faster -->\n')
			arq.write('    <script src="../Bootstrap/assets/js/jquery.js"></script>\n')
			arq.write('    <script src="../Bootstrap/dist/js/bootstrap.min.js"></script>\n')
			arq.write('    <script src="../Bootstrap/assets/js/holder.js"></script>\n')
			arq.write('  </body>\n')
			arq.write('</html>\n')


			# close file
			arq.close()




	# create web pages : Interval%.html
	# Parameters:
	# contentList : dictionary of available files/tables
	# holeList : the list of selected holes	
	# fieldList : list of fields for the file/table
	def createIntervalPages(self, contentList, holeList, fieldList):
		# iterate between Interval source
		for ch, va in contentList.iteritems():
			if (ch > 2 and ch < 8):
				# iterate between holes
				for h in holeList:
					# define file name
					fileName = 'html/%s%s.html' % (va, h)
					# open file
					arq = open(fileName, 'w')
					# write file, STATIC
					arq.write('<!DOCTYPE html>\n')
					arq.write('<html lang="en">\n')
					arq.write('  <head>\n')
					arq.write('    <meta charset="utf-8">\n')
					arq.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
					arq.write('    <meta name="description" content="">\n')
					arq.write('    <meta name="author" content="">\n')
					arq.write('    <link rel="shortcut icon" href="../Bootstrap/assets/ico/favicon.png">\n')
					# write file, DYNAMIC
					arq.write('    <title>Coleta : %s %s</title>\n' % (h, va)) 
					# write file, STATIC
					arq.write('    <link href="../Bootstrap/dist/css/bootstrap.css" rel="stylesheet">\n')
					arq.write('    <link href="../Bootstrap/dist/css/bootstrap-theme.min.css" rel="stylesheet">\n')
					arq.write('    <link href="theme.css" rel="stylesheet">\n')
					arq.write('      <script src="../Bootstrap/assets/js/html5shiv.js"></script>\n')
					arq.write('      <script src="../Bootstrap/assets/js/respond.min.js"></script>\n')
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
					# write file, DYNAMIC
					arq.write('            <li><a href="Hole%s.html">Collar</a></li>\n' % h)
					arq.write('            <li><a href="Survey%s.html">Survey</a></li>\n' % h)
					arq.write('            <li class="dropdown active">\n')
					arq.write('              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Intervals <b class="caret"></b></a>\n')
					arq.write('              <ul class="dropdown-menu">\n')
					for k, v in contentList.iteritems():
						if (k > 2 and k < 8):
							arq.write('                <li><a href="%s%s.html">%s</a></li>\n' % (v,h,v))
					arq.write('              </ul>\n')
					arq.write('            </li>\n')
					arq.write('            <li><a href="Samples%s.html">Samples and Checks</a></li>\n' % h)
					arq.write('          </ul>\n')
					arq.write('        </div><!--/.nav-collapse -->\n')
					arq.write('      </div>\n')
					arq.write('    </div>\n')

					arq.write('    <div class="container theme-showcase">\n')

					arq.write('      <!-- Main jumbotron for a primary marketing message or call to action -->\n')
					arq.write('      <div class="jumbotron">\n')
					arq.write('        <h1>%s</h1>\n' % h)
					arq.write('        <p>Edit Geology intervals.</p>\n')
					arq.write('        <p><a class="btn btn-primary btn-lg">Learn more &raquo;</a></p>\n')
					arq.write('      </div>\n')


					# interval details
					arq.write('      <!-- INTERVAL DETAILS -->\n')
					arq.write('      <div class="page-header">\n')
					arq.write('        <h1>%s</h1>\n' % va)
					arq.write('      </div>\n')
					# start details
					arq.write('      <form class="form-inline" role="form">\n')
					# controls
					for field in fieldList[ch]:
						if field <> 'HOLEID':
							arq.write('        <div class="form-group">\n')
							arq.write('          <label for="%s">%s</label>\n' % (field,field))
							arq.write('          <input type="text" class="form-control" id="%s" placeholder="%s">\n' % (field,field))
							arq.write('        </div>\n')
					# end details                     
					arq.write('      </form>\n')

					# select holes
					arq.write('      <!-- DRILLHOLE SELECTOR -->\n')
					arq.write('      <div class="page-header">\n')
					arq.write('        <h3>Change drillhole</h3>\n')
					arq.write('      </div>\n')
					arq.write('      <ul class="nav nav-pills nav-justified">\n')
					for dh in holeList:
						if dh == h:
							arq.write('        <li class="active disabled"><a href="%s%s.html">%s</a></li>\n' % (va,dh,dh))
						else:
							arq.write('        <li><a href="%s%s.html">%s</a></li>\n' % (va,dh,dh))			
					arq.write('      </ul>\n')


					# well
					arq.write('      <br></br>\n')

					arq.write('      <div class="well">\n')
					arq.write('        <p class="text-right"><small>&copy;2013 ::: Version 0.1</small></p>\n')
					arq.write('      </div>\n')


					arq.write('    </div> <!-- /container -->\n')


					arq.write('    <!-- Bootstrap core JavaScript\n')
					arq.write('    ================================================== -->\n')
					arq.write('    <!-- Placed at the end of the document so the pages load faster -->\n')
					arq.write('    <script src="../Bootstrap/assets/js/jquery.js"></script>\n')
					arq.write('    <script src="../Bootstrap/dist/js/bootstrap.min.js"></script>\n')
					arq.write('    <script src="../Bootstrap/assets/js/holder.js"></script>\n')
					arq.write('  </body>\n')
					arq.write('</html>\n')


					# close file
					arq.close()




	




