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

filename='D:\\files\\Nagios_Check.csv'
fields = []
rows = []

required_sensu_checks=[]
with open(filename, 'r') as csvfile:
	csvreader=csv.reader(csvfile,delimiter=',')
	for row in csvreader:
			flag=0
			row=row[1].lower()
			for ncpa_check_list_item in ncpa_check_list:
				#print(ncpa_check_list_item)
				if(row.find(ncpa_check_list_item) > -1):
					#print(row[1])
					flag=flag+1
			if(flag == 0):
				required_sensu_checks.append(row)

print("Final Sensu Checks:"+str(required_sensu_checks))



