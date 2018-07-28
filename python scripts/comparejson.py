import requests
import json
import re
from collections import defaultdict
headers={'Content-Type':'application/json'}
role_check_dict={}
response=requests.get("http://192.168.226.235:55006/api/sensu_checks",headers=headers)
filename = "D:\\files\\shubham json\\shubham.json"

with open(filename, 'r') as csvfile:
  lines=csvfile.read()
  input_dict2=json.loads(lines)

file_out=open("D:\\files\\shubham json\\difference.json","w")
flag=0
if(response.status_code == 200):
	input_dict=json.loads(response.text) 
	#print(json.dumps(input_dict,indent=2))
	for element2 in input_dict2:
		#print(element['subscribers'])
		#print(element['name'])
		#print("element2"+element2["name"])
		for element1 in input_dict:
			#print("element1"+element1["name"])
			if(element2["name"] == element1["name"]):
				flag=flag+1
				if(element2["subscribers"] == element1["subscribers"]):
					flag=flag+1
				if(element2["command"] == element1["command"]):
					flag=flag+1

				break
			else:
				flag=0
		if( (flag > 0) and (flag<3)):
			print(json.dumps(element2,indent=3))
			'''
		for subscriber_elem in element['subscribers']:
				subscriber_arr=subscriber_elem.split("_")
				subscriber_role_name = subscriber_elem
				if subscriber_role_name in role_check_dict.keys():
					role_check_dict[subscriber_role_name].append(element['name'])
				else:SS
					role_check_dict.update({ subscriber_role_name : []})
					role_check_dict[subscriber_role_name].append(element['name'])
			#role_check_dict[subscriber_elem].append(subscriber_elem['name'])

			'''
	#for element2 in input_dict:
		#for subscriber_elem2 in element['subscribers']:
		#	role_check_dict[subscriber_elem2].append(element['name'])
#print(json.dumps(role_check_dict,indent=3))


file_out.close()
