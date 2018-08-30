import pysnow
from datetime import date,timedelta
import datetime
import json
yesterday=datetime.datetime.today()-datetime.timedelta(1)
today=datetime.datetime.today()
print(yesterday)
cobrand_to_incidents={}
qb=(
	pysnow.QueryBuilder().field('sys_created_on').between(yesterday,today).AND().field('incident_state').equals('1')
	)
c=pysnow.Client(instance='yodlee',user='evagent',password='Evagent')
incident=c.resource(api_path='/table/incident')
response=incident.get(query=qb)
for record in response.all():
	if(record['sys_created_on']):
		print(record['number'])
		print(record['incident_state'])
		print(record['u_cobrand_id_nonedit'])
		print(record['sys_created_on'])
		sys_ids=record['u_cobrand_id']
		sys_id_list=sys_ids.split(",")
		for cobrand_id in sys_id_list:
			if cobrand_id in cobrand_to_incidents.keys():
					cobrand_to_incidents[cobrand_id].append(record['number'])
			else:
					cobrand_to_incidents.update({ cobrand_id : []})
					cobrand_to_incidents[cobrand_id].append(record['number'])

print(json.dumps(cobrand_to_incidents,indent=2))