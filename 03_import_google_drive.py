from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth) 

upload_file_list = ['formulario.html']
for upload_file in upload_file_list:

	gfile = drive.CreateFile({'parents': [{'id': '1NT-hmDFaK6XmUhQv4b74ASdOmBxVuRsE'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.