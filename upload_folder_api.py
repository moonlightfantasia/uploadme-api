#import required libraries
from requests import request
from os import listdir
from os.path import isfile, join, isdir

#setting allowed file extension as PDF
ALLOWED_EXTENSIONS = set(['pdf','png', 'jpg', 'jpeg'])

#defining function to validate file type
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_files(url="http://127.0.0.1:5000/", input_folder=""):
  #checking existence of the directory and making it formatting
  if isdir(input_folder):
    if not input_folder[-1] == "/":
      input_folder = input_folder+"/"

  #getting file path list
  filepath_list = [input_folder+filen for filen in listdir(input_folder) if isfile(join(input_folder, filen)) and allowed_file(filen)]

  #initializing files list
  files_data = []

  # updating data to be uploaded to list
  for file_temp in filepath_list:
    file_ext = file_temp.rsplit('.', 1)[1].lower()
    if file_ext == 'pdf':
      file_type = "application/"+file_ext
    if file_ext in ['png','jpg','jpeg']:
      file_type = "image/"+file_ext
    with open(file_temp,'rb') as fobj:
      fdata = fobj.read()
    fname = file_temp.split('/')[-1]
    #adding data
    files_data.append(('file',(fname, fdata, file_type)))

  #passing empty headers
  headers = {}
  #passing empty payload
  payload={}
  #calling api
  response = request("POST", url, headers=headers, data=payload, files=files_data)
  print(response.text)

#passing input folder
source_folder = "C:/Users/littinrajan/projects/nextgen/sample"
#api call function
upload_files(url="http://127.0.0.1:5000/", input_folder=source_folder)
