#Need to install requests package for python
#easy_install requests
import requests

# Set the request parameters
url = 'https://yodlee.service-now.com/api/now/table/incident?'
url = 'https://yodlee.service-now.com/api/now/table/incident?https://yodlee.service-now.com/api/now/table/incident?sysparm_query%3Dsys_created_on%3Ejavascript:gs.daysAgoEnd(1)%5Eincident_state%3D1%5EORincident_state%3D26'
# Eg. User name="admin", Password="admin" for this code sample.
user = 'hotfix'
pwd = 'Hotfix'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
print(response.text)
data = response.json()
print(data['number'])
print(data['sys_created_on'])
print(data['incident_state'])