from bottle import *
import ftplib, io

server = "example.org"

def check(user, password):
	link = ftplib.FTP(server)
	
	try:
		link.login(user, password)
	except:
		return False
	
	return True

@route("/")
@auth_basic(check)
def callback():
	try:
		path = request.query["p"]
	except KeyError:
		path = "/"
	
	if path == "": path = "/"
	
	link = ftplib.FTP(server)
	link.login(request.auth[0], request.auth[1])
	
	try: link.cwd(path)
	except: return "Access denied"
	
	files = list(link.mlsd())
	
	return template("tpl/browse", path=path, files=files)

@route("/download")
@auth_basic(check)
def callback():
	filename = request.query["f"]
	
	link = ftplib.FTP(server)
	link.login(request.auth[0], request.auth[1])
	
	data = []
	link.retrbinary("RETR " + filename, data.append)

	return data

@route("/upload", method="POST")
@auth_basic(check)
def callback():
	path = request.forms.get("path")
	upload = request.files.get("file")
	#upload.save("/tmp/" + upload.filename)
	if True: # TODO check is a file select
		#link = ftplib.FTP(server)
		#link.login(request.auth[0], request.auth[1])
		#link.storbinary("STOR "+ upload.filename, upload.file)
		#https://stackoverflow.com/questions/15050064/how-to-upload-and-save-a-file-using-bottle-framework
		return request.files
	else:
		return "No file selected"

@route("/newdir", method="POST")
@auth_basic(check)
def callback():
	path = request.forms.get('path')
	dirname = request.forms.get('name')

	if path != "" and dirname != "":
		link = ftplib.FTP(server)
		link.login(request.auth[0], request.auth[1])
		link.cwd(path)
		link.mkd(dirname)
	
		return dirname + " created"
		
	else:
		return "Enter a directory name"

# Move, copy, delete
@route("/mcd", method="POST")
@auth_basic(check)
def callback():
	path = request.forms.get("path")
	action = request.forms.get("path")
	# TODO
	
	return "Done"

@route("/static/<p>")
def callback(p):
	return static_file(p, "./static/")

@route("/robots.txt")
def callback():
	return static_file("robots.txt", "./static/")

run(host="localhost", port=8081, reloader=True, debug=True, threaded=True)
