#!/bin/env python
 
from SOAPpy  import SOAPProxy
 
username , password , instance  = 'hotfix' , 'Hotfix' , 'yodlee'
namespace  = 'https://username:password@www.service-now.com/'+instance+ '/incident.do?SOAP' , 'http://www.service-now.com/'
 
server  = SOAPProxy (namespace)
response  = server. getRecords ()

for record  in response:
	for item  in record:
		print(item)