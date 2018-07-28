import requests
import json
import re
from collections import defaultdict
headers={'Content-Type':'application/json'}
role_check_dict={}
response=requests.get("http://192.168.226.235:55006/api/sensu_checks",headers=headers)

if(response.status_code == 200):
	input_dict=json.loads(response.text) 
	#print(json.dumps(input_dict,indent=2))
	for element in input_dict:
		#print(element['subscribers'])
		#print(element['name'])
		for subscriber_elem in element['subscribers']:
				subscriber_arr=subscriber_elem.split("_")
				subscriber_role_name = subscriber_elem
				if subscriber_role_name in role_check_dict.keys():
					role_check_dict[subscriber_role_name].append(element['name'])
				else:
					role_check_dict.update({ subscriber_role_name : []})
					role_check_dict[subscriber_role_name].append(element['name'])
			#role_check_dict[subscriber_elem].append(subscriber_elem['name'])
	#for element2 in input_dict:
		#for subscriber_elem2 in element['subscribers']:
		#	role_check_dict[subscriber_elem2].append(element['name'])
print(json.dumps(role_check_dict,indent=3))
file_out=open("D:\\Scripts\\python scripts\\jsonfiles\\RolestoCheck_Prod.txt","w")
file_out.write(json.dumps(role_check_dict,indent=3))
file_out.close()