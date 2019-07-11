import requests 
import json
API_ENDPOINT = "https://api.open-elevation.com/api/v1/lookup"

f = open("data.csv", "r")
if f.mode == 'r':
	data =f.read()

x = data.split(" ")

d = {
	"locations":[]
}

k = 0
lat=0
log = 0
# while k<len(x):
# 	if(k%2==0):
# 		lat = x[k]
# 		k=k+1
# 	if(k%2==1):
# 		log = x[k]
# 		k=k+1
# 	tmp = {"latitude": 10,
# 			"longitude": 10}

# 	tmp["latitude"] = lat
# 	tmp["longitude"] = log
# 	d["locations"].append(tmp)


# print(d)
d = {
	"locations":
	[
		{
			"latitude": 10,
			"longitude": 10
		},
		{
			"latitude":20,
			"longitude": 20
		},
		{
			"latitude":41.161758,
			"longitude":-8.583933
		}
	]

}

headers = {'Accept': 'application/json','Content-Type': 'application/json'}
r = requests.post(API_ENDPOINT, data=json.dumps(d), headers=headers)
print(r.text)