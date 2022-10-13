def ips(listOfDictsIP):
	return {dictValue for dictinary in listOfDictsIP for dictKey,dictValue in dictinary.items()}

print(ips([{"ip": "192.168.3.1"}, {"ip": "10.0.0.0"}, {"ip": "127.0.0.0"}, {"ip": "192.168.3.1"}]))
print(ips([{"ip": "192.138.3.1"}, {"ip": "127.0.0.1"}, {"ip": "10.0.0.0"}]))
