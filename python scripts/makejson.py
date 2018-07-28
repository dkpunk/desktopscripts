import re

my_regex=re.compile('\"client\"',re.M)
my_regex2=re.compile('\"command\"',re.M)
my_regex3=re.compile('\"name\"',re.M)

file1="D:\\files\\test_sensu\\SensuChecksmod.json"
file2="D:\\files\\test_sensu\\SensuFile.json"

with open(file1,'w') as new_file:
        with open(file2) as old_file:
            for line in old_file:
            	if(re.search(my_regex,line)):
            		new_file.write(line)
            	if(re.search(my_regex2,line)):
            		new_file.write(line)
            	if(re.search(my_regex3,line)):
            		new_file.write(line)