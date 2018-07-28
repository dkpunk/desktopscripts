import requests
import time
import json
import re
import csv
timestr = time.strftime("%Y%m%d")
filename="./prod.json"
filenamecsv="./allroles.csv"
nonsdp2file="./nonsdp2checks.csv"
#my_regex=re.escape("sdp2_role_")+"*"
my_regex="*"

outfile=open(filename,'w')
outfile1=open(filenamecsv,'w')
outfile2=open(nonsdp2file,'rb')
nonsdp2_role_list=[]
reader=csv.reader(outfile2)
for row in reader:
        if(row[0]):
                print row[0]
                nonsdp2_role_list.append(str(row[0]))

response = requests.get('http://192.168.226.235:55006/api/sensu_checks')
print(response.text)
data=json.loads(response.text)
for element in data:
        print element["name"]
        print element["subscribers"]
outfile.write(str(json.dumps(response.text,indent=2)))
outfile.close()
input_dict=json.loads(response.text)
role_check_dict={}
#print(json.dumps(input_dict,indent=2))
for element in input_dict:
                #print(element['subscribers'])
                #print(element['name'])
        for subscriber_elem in element['subscribers']:
                if((re.search(my_regex,subscriber_elem,re.IGNORECASE)) or (subscriber_elem in nonsdp2_role_list)):
                        subscriber_role_name = subscriber_elem
                        if subscriber_role_name in role_check_dict.keys():
                                role_check_dict[subscriber_role_name].append(element['name'])
                        else:
                                role_check_dict.update({ subscriber_role_name : []})
                                role_check_dict[subscriber_role_name].append(element['name'])
temp=""
print json.dumps(role_check_dict,indent=2)
for key,val in role_check_dict.items():
        temp=temp+key+","
        templist=val
        print "key"+key+" val"+str(val)
        for item in templist:
                temp=temp+item+","
        #print temp+"\n"
        outfile1.write(temp+"\n")
        temp=""

