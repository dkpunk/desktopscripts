import csv
import json
import re
import socket
my_regex=re.escape('\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
				
filename='D:\\Scripts\\python scripts\\nagiossensucompare\\Nagios_Check.csv'
filename2='D:\\Scripts\\python scripts\\nagiossensucompare\\sensudetails.json'
filename3='D:\\Scripts\\python scripts\\nagiossensucompare\\cronout.txt'
nagios_ip={}
sensu_ip={}
with open(filename, 'r') as csvfile:
	csvreader=csv.reader(csvfile,delimiter=',')
	for row in csvreader:
			print(row[0])
			try:
				socket.inet_aton(row[0])
			#if(re.search(my_regex,row[0],re.IGNORECASE)):
				try:
					nagios_ip[row[0]]=nagios_ip[row[0]]+1
				except KeyError as e:
					nagios_ip[row[0]]=1
			except socket.error:
				print("hell no")
print(json.dumps(nagios_ip,indent=2))

with open(filename2, 'r') as txtfile:
	data=json.load(txtfile)
for element in data:
	if(element["address"]):
				try:
					sensu_ip[element["address"]]=sensu_ip[element["address"]]+1
				except KeyError as e:
					sensu_ip[element["address"]]=1
print(json.dumps(sensu_ip,indent=2))
list1=nagios_ip.keys()
list2=sensu_ip.keys()
out_list=list(set(list1)-set(list2))
print("Output List"+str(out_list))

cronfile=open(filename3,'w') 

for servername in out_list:
	cronstring='*/5 * * * * . /home/nthumma/.bash_profile;/home/nthumma/dinesh_scripts/check_nagios_critical.sh '+str(servername)+' &>/home/nthumma/dinesh_scripts/logs/check_nagios_'+str(servername)+'.log'
	print(cronstring)
	cronfile.write(cronstring+"\n")
cronfile.close()