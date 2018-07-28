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
	if (('=' in element)):
			#print(element)
			temp=element.split('=')
			#print(temp[1])
			ncpa_check_list.append(temp[1].lower())

#print(str(ncpa_check_list))
import csv
import re

filename='D:\\files\\Nagios_Check.csv'
fields = []
rows = []
required_sensu_checks_dictionary={}
required_sensu_checks=[]
with open(filename, 'r') as csvfile:
	csvreader=csv.reader(csvfile,delimiter=',')
	for row in csvreader:
			if(row[0]):
				ip=row[0]
				required_sensu_checks_dictionary.update({ip : []})
			flag=0
			row1=row[1].lower()
			for ncpa_check_list_item in ncpa_check_list:
				#print(ncpa_check_list_item)
				my_regex=re.escape(ncpa_check_list_item)+"*"
				if(re.search(my_regex,row[1],re.IGNORECASE)):
					#print(row[1])
					flag=flag+1
			if((flag == 0) and (row[1])):
				required_sensu_checks.append(row[1])
				required_sensu_checks_dictionary[ip].append(row[1])


#print("Final Sensu Checks:"+str(required_sensu_checks_dictionary))
import json
print(json.dumps(required_sensu_checks_dictionary,indent=1))
file_out=open("D:\\files\\ScriptOut.txt","w")
file_out.write(json.dumps(required_sensu_checks_dictionary,indent=1))
file_out.close()

#import pprint
#pprint.pprint(str(required_sensu_checks_dictionary))

