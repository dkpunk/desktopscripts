from elasticsearch import Elasticsearch
print(dir(elasticsearch))
client=Elasticsearch('localhost')

mappings = {
	'mappings':{
		'events':{
			'properties' : {
			'id':{'type':'string','index':'not_analysed'},
			'name':{'type':'string','analyser':'english'},
			'description' : {'type':'string','analyser':'english'},
			'city':{'type':'string','analyser':'english'},
			'start_date':{'type':'date'},
			'price':{'type':'float'}
							}
					}
				}
			}
client.indices.create(index='eventbrite',body=mappings)