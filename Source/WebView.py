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
	def createHolePages(self, contentList, holeList):
		# iterate between holes
		for h in holeList:
			# define file name
			fileName = 'html/Hole%s.html' % h
			# open file
			arq = open(fileName, 'w')
			# write file, first static part
			arq.write('<!DOCTYPE html>\n')
			arq.write('<html lang="en">\n')
			arq.write('  <head>\n')
			arq.write('    <meta charset="utf-8">\n')
			arq.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
			arq.write('    <meta name="description" content="">\n')
			arq.write('    <meta name="author" content="">\n')
			arq.write('    <link rel="shortcut icon" href="../Bootstrap/assets/ico/favicon.png">\n')

			arq.write('    <title>Coleta : Offline data collection</title>\n')

			arq.write('    <!-- Bootstrap core CSS -->\n')
			arq.write('    <link href="../Bootstrap/dist/css/bootstrap.css" rel="stylesheet">\n')
			arq.write('    <!-- Bootstrap theme -->\n')
			arq.write('    <link href="../Bootstrap/dist/css/bootstrap-theme.min.css" rel="stylesheet">\n')

			arq.write('    <!-- Custom styles for this template -->\n')
			arq.write('    <link href="theme.css" rel="stylesheet">\n')

			arq.write('    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->\n')
			arq.write('    <!--[if lt IE 9]>\n')
			arq.write('      <script src="../Bootstrap/assets/js/html5shiv.js"></script>\n')
			arq.write('      <script src="../Bootstrap/assets/js/respond.min.js"></script>\n')
			arq.write('    <![endif]-->\n')
			arq.write('  </head>\n')

			arq.write('  <body>\n')

			arq.write('    <!-- Fixed navbar -->\n')
			arq.write('    <div class="navbar navbar-inverse navbar-fixed-top">\n')
			arq.write('      <div class="container">\n')
			arq.write('        <div class="navbar-header">\n')
			arq.write('          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n')
			arq.write('            <span class="icon-bar"></span>\n')
			arq.write('            <span class="icon-bar"></span>\n')
			arq.write('            <span class="icon-bar"></span>\n')
			arq.write('          </button>\n')
			arq.write('          <a class="navbar-brand" href="#">Coleta</a>\n')
			arq.write('        </div>\n')
			arq.write('        <div class="navbar-collapse collapse">\n')
			arq.write('          <ul class="nav navbar-nav">\n')
			arq.write('            <li class="active"><a href="#">Collar</a></li>\n')
			arq.write('            <li><a href="#about">Survey</a></li>\n')
			arq.write('            <li class="dropdown">\n')
			arq.write('              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Geology <b class="caret"></b></a>\n')
			arq.write('              <ul class="dropdown-menu">\n')
			arq.write('                <li><a href="#">Lithology</a></li>\n')
			arq.write('                <li><a href="#">Alteration</a></li>\n')
			arq.write('              </ul>\n')
			arq.write('            </li>\n')
			arq.write('            <li><a href="#contact">Samples and Checks</a></li>\n')
			arq.write('          </ul>\n')
			arq.write('        </div><!--/.nav-collapse -->\n')
			arq.write('      </div>\n')
			arq.write('    </div>\n')

			arq.write('    <div class="container theme-showcase">\n')

			arq.write('      <!-- Main jumbotron for a primary marketing message or call to action -->\n')
			arq.write('      <div class="jumbotron">\n')
			arq.write('        <h1>Collar</h1>\n')
			arq.write('        <p>The place to edit prospect, gridname & coordinates, hole depth, start & end dates, and make comments about a hole.</p>\n')
			arq.write('        <p><a class="btn btn-primary btn-lg">Learn more &raquo;</a></p>\n')
			arq.write('      </div>\n')

			arq.write('      <!-- DRILLHOLE SELECTOR -->\n')
			arq.write('      <div class="page-header">\n')
			arq.write('        <h1>Drillhole</h1>\n')
			arq.write('      </div>\n')
			arq.write('      <ul class="nav nav-pills nav-justified">\n')
			arq.write('        <li class="active"><a href="#">RPN123</a></li>\n')
			arq.write('        <li><a href="#">RPN124</a></li>\n')
			arq.write('        <li><a href="#">SRC122</a></li>\n')
			arq.write('        <li><a href="#">SRC123</a></li>\n')
			arq.write('      </ul>\n')



			arq.write('      <!-- DRILLHOLE DETAILS -->\n')
			arq.write('      <div class="page-header">\n')
			arq.write('        <h1>Details</h1>\n')
			arq.write('      </div>\n')



			arq.write('      <form class="form-inline" role="form">\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="PROJECTCODE">PROJECTCODE</label>\n')
			arq.write('          <select id="PROJECTCODE" class="form-control" disabled>\n')
			arq.write('            <option>Merlot</option>\n')
			arq.write('          </select>\n')
			arq.write('        </div>\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="TENEMENTID">TENEMENTID</label>\n')
			arq.write('          <select id="TENEMENTID" class="form-control">\n')
			arq.write('            <option>E446</option>\n')
			arq.write('            <option>E447</option>\n')
			arq.write('            <option>F256</option>\n')
			arq.write('            <option>W3328</option>\n')
			arq.write('          </select>\n')
			arq.write('        </div>\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="GRIDNAME">GRIDNAME</label>\n')
			arq.write('          <select id="GRIDNAME" class="form-control">\n')
			arq.write('            <option>Merlot</option>\n')
			arq.write('            <option>Cabernet</option>\n')
			arq.write('            <option>Shiraz</option>\n')
			arq.write('            <option>Carmenere</option>\n')
			arq.write('          </select>\n')
			arq.write('        </div>\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="HOLETYPE">HOLETYPE</label>\n')
			arq.write('          <select id="HOLETYPE" class="form-control" disabled>\n')
			arq.write('            <option>DRILLHOLE</option>\n')
			arq.write('          </select>\n')
			arq.write('        </div>\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="EAST">EAST</label>\n')
			arq.write('          <input type="number" class="form-control" id="EAST" placeholder="EAST">\n')
			arq.write('        </div>\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="NORTH">NORTH</label>\n')
			arq.write('          <input type="number" class="form-control" id="NORTH" placeholder="NORTH">\n')
			arq.write('        </div>\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="RL">RL</label>\n')
			arq.write('          <input type="number" class="form-control" id="RL" placeholder="RL">\n')
			arq.write('        </div>\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="DEPTH">DEPTH</label>\n')
			arq.write('          <input type="number" class="form-control" id="DEPTH" placeholder="DEPTH">\n')
			arq.write('        </div>\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="PROSPECT">PROSPECT</label>\n')
			arq.write('          <select id="PROSPECT" class="form-control">\n')
			arq.write('            <option>Merlot</option>\n')
			arq.write('            <option>Cabernet</option>\n')
			arq.write('            <option>Shiraz</option>\n')
			arq.write('            <option>Carmenere</option>\n')
			arq.write('          </select>\n')
			arq.write('        </div>\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="STARTDATE">STARTDATE</label>\n')
			arq.write('          <input type="date" class="form-control" id="STARTDATE" placeholder="STARTDATE">\n')
			arq.write('        </div>\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="ENDDATE">ENDDATE</label>\n')
			arq.write('          <input type="date" class="form-control" id="ENDDATE" placeholder="ENDDATE">\n')
			arq.write('        </div> \n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="Grid_Original">Grid_Original</label>\n')
			arq.write('          <select id="Grid_Original" class="form-control">\n')
			arq.write('            <option>Merlot</option>\n')
			arq.write('            <option>Cabernet</option>\n')
			arq.write('            <option>Shiraz</option>\n')
			arq.write('            <option>Carmenere</option>\n')
			arq.write('          </select>\n')
			arq.write('        </div>\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="Logged_By">Logged_By</label>\n')
			arq.write('          <select id="Logged_By" class="form-control">\n')
			arq.write('            <option>Merlot</option>\n')
			arq.write('            <option>Cabernet</option>\n')
			arq.write('            <option>Shiraz</option>\n')
			arq.write('            <option>Carmenere</option>\n')
			arq.write('          </select>\n')
			arq.write('        </div>\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="DrillCompany">DrillCompany</label>\n')
			arq.write('          <select id="DrillCompany" class="form-control">\n')
			arq.write('            <option>Merlot</option>\n')
			arq.write('            <option>Cabernet</option>\n')
			arq.write('            <option>Shiraz</option>\n')
			arq.write('            <option>Carmenere</option>\n')
			arq.write('          </select>\n')
			arq.write('        </div>\n')                
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="Rig">Rig</label>\n')
			arq.write('          <select id="Rig" class="form-control">\n')
			arq.write('            <option>Merlot</option>\n')
			arq.write('            <option>Cabernet</option>\n')
			arq.write('            <option>Shiraz</option>\n')
			arq.write('            <option>Carmenere</option>\n')
			arq.write('          </select>\n')
			arq.write('        </div>\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="Status">Status</label>\n')
			arq.write('          <select id="Status" class="form-control">\n')
			arq.write('            <option>Merlot</option>\n')
			arq.write('            <option>Cabernet</option>\n')
			arq.write('            <option>Shiraz</option>\n')
			arq.write('            <option>Carmenere</option>\n')
			arq.write('          </select>\n')
			arq.write('        </div>\n')
			arq.write('        <div class="form-group">\n')
			arq.write('          <label for="HoleComments">HoleComments</label>\n')
			arq.write('          <textarea class="form-control" id="HoleComments"placeholder="HoleComments" rows="3"></textarea>\n')
			arq.write('        </div>\n')                         
			arq.write('      </form>\n')


			arq.write('      <p></p>\n')


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



	


	


