## this script is used to get details either from prod/stage and search port checks with "Custom" roles and add one more role
## called sdp2_role_others_<port> to the existing subscribers/roles and write to respective files

import requests
import json
import re
from collections import defaultdict
headers={'Content-Type':'application/json'}
role_check_dict={}
#for prod
response=requests.get("http://192.168.226.235:55006/api/sensu_checks",headers=headers)
#for stage
#response=requests.get("http://192.168.226.235:55005/api/sensu_checks",headers=headers)


my_regex=re.escape("sdp2_role_OAUTH_")+"*"
my_regex1=re.escape("check_sdp2_corelog_")+"*"

#file_out=open("D:\\Scripts\\python scripts\\jsonfiles\\Custom2OThersChecksprod.txt","w")
file_out=open("D:\\Scripts\\python scripts\\jsonfiles\\oauth_rectified.txt","w")

if(response.status_code == 200):
	input_dict=json.loads(response.text) 
	#print(json.dumps(input_dict,indent=2))
	for element in input_dict:
		flag=0
		if((re.search(my_regex1,element['name'],re.IGNORECASE))):
		#print(element['subscribers'])
		#print(element['name'])
			for subscriber_elem in element['subscribers']:
				if((re.search(my_regex,subscriber_elem,re.IGNORECASE))):
					'''subscriber_arr=subscriber_elem.split("_")
					new_role_name = "sdp2_role_others_"+subscriber_arr[3]
					element['subscribers'].append(new_role_name)
					flag=1'''
					print(json.dumps(element,indent=2))
					file_out.write(json.dumps(element,indent=3))
		
file_out.close()

				#role_check_dict[subscriber_elem].append(subscriber_elem['name'])
	#for element2 in input_dict:
		#for subscriber_elem2 in element['subscribers']:
		#	role_check_dict[subscriber_elem2].append(element['name'])
