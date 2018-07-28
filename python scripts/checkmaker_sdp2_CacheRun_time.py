
#portlist=[1034,1235,12356,1231]
## ./checkmaker_port_sdp2_telnet.py <comma seperated ports> <comma seperated roles>
## seperate check will be created for each port and the subscribers will be added to the all the checks

import sys
portlist=sys.argv[1].split(",")
subscriberlist=sys.argv[2].split(",")
','.join(map(lambda x: '"'+x+'"',subscriberlist))
def makecheck(portlist,subscriberlist):
	for port in portlist:
		jsonstring='''{
   "name": "check_sdp2_CacheRun_time_'''+str(port)+'''",
    "command": "export PATH=$PATH:/opt/sensu/embedded/bin:/opt/sensu/embedded/bin/scripts_ypa && check_cache_time -i '''+str(port)+''' 2> /dev/null",
    "category": "Application",
    "handlers": [
      "default"
    ],
    "subscribers": '''+str(subscriberlist)+''',
    "userdefined1": "http://sot.yodlee.com",
    "instance": "'''+str(port)+'''",
    "check_type": "status",
    "interval": 300
  	},'''
		print(jsonstring)
	return(jsonstring)
makecheck(portlist,subscriberlist)



