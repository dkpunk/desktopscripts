##Script downloads the latest json from Pilto env and saves it to a file in the jsonfiles directory 


import json
import pycurl


from subprocess import Popen
with open("D:\Scripts\python scripts\jsonfiles\curlfile.json","wb") as wfile:
	#Output=Popen(r'"curl -X GET --header "Accept: application/json" "http://192.168.226.235:55002/api/sensu_checks"')
	#print(Output)
	c=pycurl.Curl()
	c.setopt(c.URL,'http://192.168.226.235:55005/api/sensu_checks')
	#c.setopt(pycurl.HTTPHEADER,['Accept: application/json'])
	#c.setopt(pycurl.GET,1)
	c.setopt(c.WRITEDATA,wfile)
	c.perform()

with open("D:\Scripts\python scripts\jsonfiles\curlfile.json","r") as rfile:
	jsondump=json.load(rfile)
	print(json.dumps(jsondump,indent=2))

