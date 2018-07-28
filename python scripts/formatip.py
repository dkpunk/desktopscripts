filename = "D:\\files\\SensuFile.json"
#import json;
import ujson as json;
filename2 = "D://files/ip-list-beautified.txt"
jsondata=json.load(open(filename))
print(jsondata['client'])