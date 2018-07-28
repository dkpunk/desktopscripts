'''import pycurl, json

c = pycurl.Curl()
c.setopt(pycurl.URL,'http://192.168.226.235:55005/api/sensu_checks')
c.setopt(pycurl.HTTPHEADER, ['Accept:application/json'])

c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, data)
c.setopt(pycurl.VERBOSE, 1)
c.perform()
print(curl_agent.getinfo(pycurl.RESPONSE_CODE))
c.close()
'''
import json
with open('D:\Scripts\python scripts\jsonfiles\checkstopatch.txt','r') as fw:
  lines=fw.read()
  print(lines)
  jsonlist=json.loads(lines)
#print(lines)
#jsonlist=lines.split('##@@##')
#print(jsonlist) 
'''data = {
    "name": "check_sdp2_CacheRun_time_38541",
    "command": "export PATH=$PATH:/opt/sensu/embedded/bin:/opt/sensu/embedded/bin/scripts_ypa && check_cache_time -i 38541 2> /dev/null",
    "category": "Application",
    "handlers": [
      "default"
    ],
    "subscribers": [
      "sdp2_role_CacheRun_time_38541"
    ],
    "userdefined1": "http://sot.yodlee.com",
    "instance": "38541",
    "check_type": "status",
    "interval": 300
  }'''
headers={'Content-Type':'application/json'}
import requests
#data = {"name": "abc", "path": "def", "target": ["ghi"]}
for data in jsonlist:
  #for stage 
  print(data["id"])
  temp=data["id"]
  data.pop('id',None)
  #for stage
  response = requests.patch('http://192.168.226.235:55005/api/sensu_checks/'+temp, json=data,headers=headers)
  #for prod
 # response = requests.patch('http://192.168.226.235:55006/api/sensu_checks/'+temp, json=data,headers=headers)
  
  print(response.status_code)
  print(response.text)

