import json
filename2='D:\\Scripts\\python scripts\\AuditScriptsforZameer\\TeChecks.json'
filename3='D:\\Scripts\\python scripts\\AuditScriptsforZameer\\TeChecksOut.json'
check_list={}
with open(filename2, 'r') as txtfile:
	data=json.load(txtfile)
for element in data:
	print(data[element]['checks'])
	if(data[element]['checks']):
			for check_name in data[element]['checks']:
				try:
					check_list[check_name]=check_list[check_name]+1
				except KeyError as e:
					check_list[check_name]=1

print(json.dumps(sorted(check_list),indent=3))

for element2 in data:
	print(data[element2]['checks'])
	if(data[element2]['checks']):
			data[element2]['checks']=sorted(check_list.keys())


outfile=open(filename3,'w') 

#for servername in out_list:
	#cronstring='*/5 * * * * . /home/nthumma/.bash_profile;/home/nthumma/dinesh_scripts/check_nagios_critical.sh '+str(servername)+' &>/home/nthumma/dinesh_scripts/logs/check_nagios_'+str(servername)+'.log'
	#print(cronstring)
outfile.write(str(json.dumps(data,indent=2)))
outfile.close()