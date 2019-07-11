import requests
import sys
import json
lats = str(sys.argv[1])
logs = str(sys.argv[2])
latd = str(sys.argv[3]) 
logd = str(sys.argv[4])



route = requests.get("https://api.tomtom.com/routing/1/calculateRoute/"+lats+","+logs+":"+latd+","+logd+"/json?avoid=unpavedRoads&key=ewAx62lxGhRva3JTNfheAFmW7veM65p8")

# f = open("js","w")
parsed_route = route.json();
# print("Kill yourself Biatch")
# f.write(json.dumps(route.json()))
# print(parsed_route)
elat = str(parsed_route["routes"][0]["legs"][0]["points"][0]["latitude"])
elog = str(parsed_route["routes"][0]["legs"][0]["points"][0]["longitude"])

l = len(parsed_route["routes"][0]["legs"][0]["points"])
tmp = int(l/100);
i = tmp
if tmp==0:
	tmp = tmp + 1


f = open("data.csv","w")
f.write("")
f.close()
f = open("data.csv", "a+")
# f.write(str(lats)+" "+str(logs)+" "+str(latd)+" "+str(logd)+"\n") 
# f.write(lats+" "+logs+" "+latd+" "+logd+"\n")
t = 0
while(i<l):
	slat = elat
	slog = elog
	elat = str(parsed_route["routes"][0]["legs"][0]["points"][i]["latitude"])
	elog = str(parsed_route["routes"][0]["legs"][0]["points"][i]["longitude"])
	troute = requests.get("https://api.tomtom.com/routing/1/calculateRoute/"+slat+","+slog+":"+elat+","+elog+"/json?avoid=unpavedRoads&key=ewAx62lxGhRva3JTNfheAFmW7veM65p8");
	tparsed_route = troute.json();
	t = t+int(tparsed_route["routes"][0]["summary"]["travelTimeInSeconds"])
	f.write(str(t)+" ")
	troute = requests.get("https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point="+slat+"%2C"+slog+"&key=ewAx62lxGhRva3JTNfheAFmW7veM65p8")
	tparsed_route = troute.json()
	# print(str(t)+" "+str(tparsed_route["flowSegmentData"]["freeFlowSpeed"]))
	f.write(str(tparsed_route["flowSegmentData"]["freeFlowSpeed"])+"\n")
	# speed.append(tparsed_route["flowSegmentData"]["freeFlowSpeed"])

	i=i+tmp
	
# f.close()
