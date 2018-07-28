import requests
import json
import re
from collections import defaultdict
headers={'Content-Type':'application/json'}
role_check_dict={}
#for prod
#response=requests.get("http://192.168.226.235:55006/api/sensu_checks",headers=headers)
#for stage
response=requests.get("http://192.168.226.235:55005/api/sensu_checks",headers=headers)

#checks_to_fetch = ["check_sdp2_port_9543","check_sdp2_jvm_9543","check_sdp2_serverlog_9543","check_sdp2_port_9243","check_sdp2_jvm_9243","check_sdp2_serverlog_9243","check_sdp2_port_10143","check_sdp2_jvm_10143","check_sdp2_serverlog_10143","check_sdp2_port_9843","check_sdp2_jvm_9843","check_sdp2_serverlog_9843","check_sdp2_port_9943","check_sdp2_jvm_9943","check_sdp2_serverlog_9943","check_sdp2_port_9443","check_sdp2_jvm_9443","check_sdp2_serverlog_9443","check_sdp2_port_10043","check_sdp2_jvm_10043","check_sdp2_serverlog_10043","check_sdp2_port_9343","check_sdp2_jvm_9343","check_sdp2_serverlog_9343","check_sdp2_port_22541","check_sdp2_jvm_22541","check_sdp2_serverlog_22541","check_sdp2_port_8743","check_sdp2_jvm_8743","check_sdp2_serverlog_8743","check_sdp2_port_9043","check_sdp2_jvm_9043","check_sdp2_serverlog_9043","check_sdp2_port_8543","check_sdp2_jvm_8543","check_sdp2_serverlog_8543"]
#checks_to_fetch = ["check_sdp2_port_7051","check_sdp2_port_8051"]
checks_to_fetch = ["check_sdp2_port_50020",	"check_sdp2_port_8041"]

file_out=open("D:\\Scripts\\python scripts\\jsonfiles\\Fetched_checks_striim_stage.txt","w")

for checkname in checks_to_fetch:
	if(response.status_code == 200):	
		input_dict=json.loads(response.text) 
		#print(json.dumps(input_dict,indent=2))
		for element in input_dict:
			if(element['name'] == checkname):
				print(element)
				file_out.write(json.dumps(element,indent=3))
			#print(element['subscribers'])
			#print(element['name'])
			#for subscriber_elem in element['subscribers']:
			#		subscriber_arr=subscriber_elem.split("_")
			#		subscriber_role_name = subscriber_elem
			#		if subscriber_role_name in role_check_dict.keys():
			#			role_check_dict[subscriber_role_name].append(element['name'])
			#		else:
			#			role_check_dict.update({ subscriber_role_name : []})
			#			role_check_dict[subscriber_role_name].append(element['name'])
			#role_check_dict[subscriber_elem].append(subscriber_elem['name'])
	#for element2 in input_dict:
		#for subscriber_elem2 in element['subscribers']:
		#	role_check_dict[subscriber_elem2].append(element['name'])
#print(json.dumps(role_check_dict,indent=3))


file_out.close()