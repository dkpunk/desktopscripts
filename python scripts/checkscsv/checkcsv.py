import requests
import json
import re
from collections import defaultdict
headers={'Content-Type':'application/json'}
role_check_dict={}
response=requests.get("http://192.168.226.235:55006/api/sensu_checks",headers=headers)
file_out=open(".//RolestoCheck_Prod.txt","w")
if(response.status_code == 200):
	input_dict=json.loads(response.text) 
	for element in input_dict:
		file_out.write(element['name']+"\n")

file_out.close()