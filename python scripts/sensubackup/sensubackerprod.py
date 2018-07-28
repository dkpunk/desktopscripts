#! python
import requests
import time
import json
timestr = time.strftime("%Y%m%d")
filename="D:\\Scripts\\python scripts\\sensubackup\\prod\\prod_"+timestr+".json"

outfile=open(filename,'w') 


response = requests.get('http://192.168.226.235:55006/api/sensu_checks')
print(response.text)
outfile.write(str(json.dumps(response.text,indent=2)))
outfile.close()