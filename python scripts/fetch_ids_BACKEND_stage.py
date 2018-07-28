## this script is used to get details either from prod/stage and search port checks with "Custom" roles and add one more role
## called sdp2_role_others_<port> to the existing subscribers/roles and write to respective files

import requests
import json
import re
from collections import defaultdict
headers={'Content-Type':'application/json'}
role_check_dict={}
filename = "D:\\Scripts\\python scripts\\jsonfiles\\OAUTHCHECKSHTTPS_filterOAUTHFIREMEMBACKEND.txt"
#http_port_list = [8443,8543,8643,8743,8843,8943,9043,9143,9243,9343,9443,9543,9643,9743,9843,9943,10043,10143,10243,10343,10443,10543,10643,10743,10843,10943,11043,11143,11243,11343,11443,11543,11643,11743,11843,11943,12043,12143,12243]
#for prod
#response=requests.get("http://192.168.226.235:55006/api/sensu_checks",headers=headers)
#for stage
response=requests.get("http://192.168.226.235:55005/api/sensu_checks",headers=headers)
with open(filename, 'r') as csvfile:
  lines=csvfile.read()

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

#my_regex=re.escape("sdp2_role_OAUTHCLIENT")+"*"
#role_name = ["sdp2_role_FRONTEND1_","sdp2_role_BACKEND1_","sdp2_role_FRONTEND2_","sdp2_role_DAPFRONTEND_","sdp2_role_DAPBACKEND_","sdp2_role_DEVFRONTEND_","sdp2_role_DEVFRONTEND2_","sdp2_role_DEVBACKEND_","sdp2_role_DC_","sdp2_role_QUERYCENTER_","sdp2_role_QUERYCENTER-REST_","sdp2_role_TOOLCENTER_"]
#checkname_list=["check_sdp2_port_","check_sdp2_jvm_","check_sdp2_serverlog_"]
#file_out=open("D:\\Scripts\\python scripts\\jsonfiles\\Custom2OThersChecksprod.txt","w")
file_out=open("D:\\Scripts\\python scripts\\jsonfiles\\stagechecks.txt","w")
input_dict2=json.loads(response.text)
if(True):
	
	input_dict=json.loads(str(lines)) 
	
	#print(json.dumps(input_dict,indent=2))
	for element in input_dict:
		for element2 in input_dict2:
				if(element["name"]==element2["name"]):
					print("name: "+element2["name"]+" id :"+element2["id"])
					file_out.write("name: "+element2["name"]+" id :"+element2["id"]+"\n")
		
file_out.close()

				#role_check_dict[subscriber_elem].append(subscriber_elem['name'])
	#for element2 in input_dict:
		#for subscriber_elem2 in element['subscribers']:
		#	role_check_dict[subscriber_elem2].append(element['name'])
