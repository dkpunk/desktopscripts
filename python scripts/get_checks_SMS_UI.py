## this script is used to get details either from prod/stage and search port checks with "Custom" roles and add one more role
## called sdp2_role_others_<port> to the existing subscribers/roles and write to respective files

import requests
import json
import re
from collections import defaultdict
headers={'Content-Type':'application/json'}
role_check_dict={}
http_port_list = [9000,8888,9006,9007,8080,8899,8888,9008]
#for prod
#response=requests.get("http://192.168.226.235:55006/api/sensu_checks",headers=headers)
#for stage
response=requests.get("http://192.168.226.235:55005/api/sensu_checks",headers=headers)

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

#my_regex=re.escape("sdp2_role_OAUTHCLIENT")+"*"

checkname_list=["check_sdp2_custom_SMS_telnet_","check_sdp2_custom_SMS_UI_telnet_","check_sdp2_custom_ErrorSegment_Service_telnet_","check_sdp2_custom_ErrorSegment_Audit_telnet_","check_sdp2_custom_YUVA_service_telnet_","check_sdp2_custom_PreSR_UI_telnet_","check_sdp2_custom_BugR_service_telnet_","check_sdp2_custom_JN_Analysis_service_telnet_"]
#file_out=open("D:\\Scripts\\python scripts\\jsonfiles\\Custom2OThersChecksprod.txt","w")
file_out=open("D:\\Scripts\\python scripts\\jsonfiles\\SMSUICHECKS.txt","w")

if(response.status_code == 200):
	
	input_dict=json.loads(response.text) 
	
	#print(json.dumps(input_dict,indent=2))
	for element in input_dict:
		for portnumber in http_port_list:
			for checkname in checkname_list:
				my_regex1=re.escape(checkname)+str(portnumber)
				if((re.search(my_regex1,element['name'],re.IGNORECASE))):
						print(json.dumps(element,indent=2))
						file_out.write(json.dumps(element,indent=3))
		
file_out.close()

				#role_check_dict[subscriber_elem].append(subscriber_elem['name'])
	#for element2 in input_dict:
		#for subscriber_elem2 in element['subscribers']:
		#	role_check_dict[subscriber_elem2].append(element['name'])
