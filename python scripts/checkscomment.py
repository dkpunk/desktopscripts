import os
filelist = os.listdir("D:\\files\\avijit\\avijit\\")
checklist = ["check_load_linux","Check_disk_IO","Check_SAR","Check_FreeMemory","Check_Disk"]
import re
for filename in filelist:
		Data = open("D:\\files\\avijit\\avijit\\"+filename).read()
		list1 = Data.split("\n")
		list1="\n#".join(list1)
		filenametemp=open("D:\\files\\avijit\\changedfile\\"+filename,"w+")
		filenametemp.writelines(list1)
		filenametemp.close()
		

for filename in filelist:
	count=0
	Data = open("D:\\files\\avijit\\changedfile\\"+filename,).read()
	list1 = Data.split("\n")
	for ncpa_check_list_item in checklist:	
		ncpa_check_list_commented = "#"+ncpa_check_list_item
		my_regex=re.compile("#check_load_linux|#check_disk_IO|#check_SAR|#check_FreeMemory|#check_Disk",re.IGNORECASE)
		for var in list1:
			#if(count >=10):
				var1 = re.sub(my_regex,ncpa_check_list_item,var)
				print(var1)
			#count=count+1
			
			