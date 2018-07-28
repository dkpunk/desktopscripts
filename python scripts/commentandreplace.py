from tempfile import mkstemp
from shutil import move
from os import fdopen, remove
import os
import re

#This script removes all the checks within the keyword_list and replace the text in check_descriptions at the end

keyword_list = ["check_load_linux","Check_disk_IO","Check_SAR","Check_FreeMemory","Check_Disk"]

check_description = '''Check_Disk[1]_Enable = "ON"
Check_Disk[1]_Service = "nsca_check_disk" 
Check_Disk[1]_Command = "check_disk"
Check_Disk[1]_Parm_--warning = "15%"
Check_Disk[1]_Parm_--critical = "10%"

Check_FreeMemory[1]_Enable = "ON"  
Check_FreeMemory[1]_Service = "nsca_check_FreeMemory"
Check_FreeMemory[1]_Command = "check_FreeMemory"    
Check_FreeMemory[1]_Parm_-m = "1000000"
Check_FreeMemory[1]_Parm_-s = "500000"

Check_SAR[1]_Enable = "ON"
Check_SAR[1]_Command = "check_sar"
Check_SAR[1]_Parm_-n = Monitor_Server[1],Monitor_Server[2],Monitor_Server[3]
Check_SAR[1]_Parm_-c = "nsca_check_cpu"          
Check_SAR[1]_Parm_-m = "nsca_check_memory"
Check_SAR[1]_Parm_-s = "nsca_check_swap" 
Check_SAR[1]_Parm_-d = "55"             
Check_SAR[1]_Parm_-e = "50"   
Check_SAR[1]_Parm_-o = "-1" 
Check_SAR[1]_Parm_-p = "-1"   
Check_SAR[1]_Parm_-t = "90"  
Check_SAR[1]_Parm_-u = "80"

Check_disk_IO[1]_Enable = "ON"  
Check_disk_IO[1]_Service = "nsca_check_disk_io" 
Check_disk_IO[1]_Command = "check_dmesg"    
Check_disk_IO[1]_Parm_-t = "/tmp/dmesg.log"
Check_disk_IO[1]_Parm_-q = "'I/O error'"

check_load_linux[1]_Enable = "ON" 
check_load_linux[1]_Service = "nsca_check_load_linux"
check_load_linux[1]_Command = "check_load_linux"
'''

def remove_check(file_path, pattern):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern,""))
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

def add_check(file_path, check_description):
    #Create temp file
    with open(file_path,'a') as new_file:
        new_file.writelines(check_description)

def comment(file_path):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        count=0
        with open(file_path) as old_file:
            for line in old_file:
                if(count>=17):
                    newline="#"+line
                    new_file.write(line.replace(line,newline))
                else:
                    new_file.write(line)
                count=count+1
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)
filelist=os.listdir("D:\\files\\avijit\\test")

for file in filelist:
    comment("D:\\files\\avijit\\test\\"+file)
    for check_item in keyword_list:
        remove_check("D:\\files\\avijit\\test\\"+file,check_item)
    add_check("D:\\files\\avijit\\test\\"+file,check_description)
print(check_description)