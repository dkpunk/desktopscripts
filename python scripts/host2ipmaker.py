import re
ipdictionary={}
with open("D:\\files\\test_sensu\\ip-list.txt","r") as rfile:
	lines=rfile.readlines()
	for line in lines:
		arr=line.split(",")
		#print("Hostname :"+arr[1])
		#print("Ip : "+arr[0])
		ipdictionary[arr[1].rstrip()]=arr[0].rstrip()
#print(ipdictionary)
my_regex=re.compile('\"client\"',re.M)
my_regex2=re.compile('\"command\"',re.M)
my_regex3=re.compile('\"name\"',re.M)
with open("D:\\files\\test_sensu\\SensuChecksmodiphost.json","w") as new_file1:
	with open("D:\\files\\test_sensu\\SensuFile.json",'r') as new_file:
		for line in new_file:
			if(re.search(my_regex,line)):
				linearr=line.split("\"")
				print(linearr[3])
				for keyval in ipdictionary.keys():
					if(linearr[3] == keyval):
						new_file1.write(line.rstrip()+ipdictionary[keyval])
			if(re.search(my_regex2,line)):
				new_file1.write(line)
			if(re.search(my_regex3,line)):
				new_file1.write(line)
				#replacetext=key+","+ipdictionary[key]
				#print(replacetext)
				#my_regex=re.compile(r"*"+re.escape(key)+r"*")
				#if(re.search(my_regex,line,re.I)):
				#	newline=line+replacetext
				#	print(newline)
            	#print(replacetext)
		

