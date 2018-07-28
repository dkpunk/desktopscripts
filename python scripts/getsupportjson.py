# this script does a get request over seyren alerts api and check
#the ops DL and prints it over the screen



import requests
import json
import re
from collections import defaultdict
headers={'Content-Type':'application/json'}
input_dict={}
input_dict2={}
role_check_dict={}
response=requests.get("http://192.168.226.235:55001/api/seyren_alerts",headers=headers)
#print(response.text)
file_out=open("D:\\Scripts\\python scripts\\jsonfiles\\Ops-Alert-Seyren.txt","w")

if(response.status_code == 200):
	input_dict=json.loads(response.text) 
	for element in input_dict:
		for subscriber_elem in element["subscriptions"]:
			#print(subscriber_elem["target"])
			if(subscriber_elem["target"]=="ops-alerts@yodlee.com"):
				#print(element)
				subscriber_elem["target"]="devops-alerts@yodlee.com"
				print(json.dumps(element,indent=3))
				file_out.write(json.dumps(element,indent=3))
file_out.close()