## this script is used to get details either from prod/stage and search port checks with "Custom" roles and add one more role
## called sdp2_role_others_<port> to the existing subscribers/roles and write to respective files

import requests
import json
import re
from collections import defaultdict
headers={'Content-Type':'application/json'}
role_check_dict={}
http_port_list = [8443,8543,8643,8743,8843,8943,9043,9143,9243,9343,9443,9543,9643,9743,9843,9943,10043,10143,10243,10343,10443,10543,10643,10743,10843,10943,11043,11143,11243,11343,11443,11543,11643,11743,11843,11943,12043,12143,12243]
#for prod
response=requests.get("http://192.168.226.235:55006/api/sensu_checks",headers=headers)
#for stage
#response=requests.get("http://192.168.226.235:55005/api/sensu_checks",headers=headers)

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

#my_regex=re.escape("sdp2_role_OAUTHCLIENT")+"*"

checkname_list=["check_sdp2_serverlog_", "check_sdp2_telnet_", "check_sdp2_jvm_","check_sdp2_accesslog_","check_sdp2_firemem_jvm_","check_sdp2_corelog_","check_sdp2_port_"]
#file_out=open("D:\\Scripts\\python scripts\\jsonfiles\\Custom2OThersChecksprod.txt","w")
file_out=open("D:\\Scripts\\python scripts\\jsonfiles\\OAUTHCHECKSHTTPS.txt","w")

if(response.status_code == 200):
	
	input_dict=json.loads(response.text) 
	
	#print(json.dumps(input_dict,indent=2))
	for element in input_dict:
		for portnumber in http_port_list:
			for checkname in checkname_list:
				my_regex1=re.escape(checkname)+str(portnumber)
				if((re.search(my_regex1,element['name'],re.IGNORECASE))):
						'''new_role_name = "sdp2_role_OAUTHCLIENT_"+str(portnumber)
						element['subscribers'].append(new_role_name)
						newlist=Remove(element['subscribers'])
						element['subscribers'] = newlist
				
						print(json.dumps(element,indent=2))'''
						file_out.write(json.dumps(element,indent=3))
		
file_out.close()

				#role_check_dict[subscriber_elem].append(subscriber_elem['name'])
	#for element2 in input_dict:
		#for subscriber_elem2 in element['subscribers']:
		#	role_check_dict[subscriber_elem2].append(element['name'])
