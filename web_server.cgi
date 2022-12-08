#!/usr/bin/python3

import socket
import time
import base64
import cgi, os, sys
import cgitb; cgitb.enable()

def path_to_string(path):
	with open(path, "rb") as image_file:
		return base64.b64encode(image_file.read()).decode()

def recieve_data(s):
	data=""
	try:
		while True:
			data+=s.recv(1024).decode()
			if "\n" in data:
				break
		return data
        #If loss or corruption
	except socket.timeout as e:
		return "Timed out"

#Get form data
form=cgi.FieldStorage()
fileitem= form['filename']

#If file uploaded
if fileitem.filename:
        #create temporary file
	fn = os.path.basename(fileitem.filename.replace("\\","/"))
	open('/tmp/'+fn, 'wb').write(fileitem.file.read())
	path='/tmp/'+fn
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                truth=True
                #Connect to server
                s.connect(('128.112.170.34', 1025))
                #Set timeout in case of loss or corruption
                s.settimeout(5)
                message = path_to_string(path)+'\n'
                t1=time.time()
                #Since tcp, if timed out then send again
                while truth:
                    #Send data
                    s.sendall(message.encode("utf-8"))
                    #recieve data
                    data= recieve_data(s)
                    #If data recieved from server
                    if data!="Timed out":
                        #exit loop
                        truth=False
                        t2=time.time()
        #Calculate RTT and Throughput
	print("Content-type: text/html\n\n")
	print('<h1> RTT:</h1><h2>',1000*(t2-t1), 'ms</h2>')
	print('<h1> Throughput:</h1><h2>',8*os.path.getsize(path)/(t2-t1),"bps</h2")
	print('<h1> The category is:</h1><h2>',data,'</h2>')

#If no file uploaded
else:
	print("Content-type: text/html\n\n")
	print('<h1> No file was uploaded </h1>')

