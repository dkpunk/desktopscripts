import docx
def getText(filename):
 		doc=docx.Document(filename)
 		fullText=[]
 		for para in doc.paragraphs:
 			fullText.append(para.text)
 		return(fullText)
#print(getText('D:\\files\\NamingConvension.docx'))

FileOut=getText('D:\\files\\NamingConvension.docx')
ncpa_check_list=[]
for element in FileOut:
	if (('=' in element) and (']' in element)):
			print(element)

			temp=element.split('=')
			#print(temp[1])
			temp2=temp[1].split('[')
			#print(temp2[0])
			#ncpa_check_list.append(temp[1].lower())
			ncpa_check_list.append(temp2[0].lower())

#print(str(ncpa_check_list))
import csv
import re


filename2="D:\\files\\conventionalcheckfilter.txt"
cclist=[]
with open(filename2,'r') as fh2:
	temp = fh2.readlines()
	for temp1 in temp:
		temp2=temp1.split("=")
		cclist.append(temp2[1].rstrip().lower())
#print(cclist);






filename='D:\\files\\Nagios_Check.csv'
fields = []
rows = []
required_sensu_checks_dictionary={}
required_sensu_checks=[]
with open(filename, 'r') as csvfile:
	csvreader=csv.reader(csvfile,delimiter=',')
	for row in csvreader:
			#print(row[1])

			if(row[0]):
				ip=row[0]
				required_sensu_checks_dictionary.update({ip : []})
			flag=0
			row1=row[1].lower()
			if(row1 in cclist):
					flag=flag+1
			#print(row1)
			for ncpa_check_list_item in ncpa_check_list:
				#print("ncpa_check_list_item"+ncpa_check_list_item)
				#my_regex=r"\b"+re.escape(ncpa_check_list_item)+r"[0-9]+\b"
				my_regex=re.compile(r'('+re.escape(ncpa_check_list_item)+r')'+r'\d+')
				#if(ncpa_check_list_item.endswith('_')):
				#	print(ncpa_check_list_item)
				#	my_regex=re.escape(ncpa_check_list_item)+"[0-9]."
				#else:
				#	my_regex=re.escape(ncpa_check_list_item)+"*"
				#print("row1------->"+row1)
				if(my_regex.search(row1)):
					flag=flag+1
				
			if((flag == 0) and (row[1])):
				#required_sensu_checks.append(row[1])
				required_sensu_checks_dictionary[ip].append(row[1])



#print("Final Sensu Checks:"+str(required_sensu_checks_dictionary))
import json
print(json.dumps(required_sensu_checks_dictionary,indent=1))
file_out=open("D:\\files\\ScriptOut.txt","w")
file_out.write(json.dumps(required_sensu_checks_dictionary,indent=1))
file_out.close()

#import pprint
#pprint.pprint(str(required_sensu_checks_dictionary))

