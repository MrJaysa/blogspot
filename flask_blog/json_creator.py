#creating json file

import json
import io

data = {
	"data":["api is working so far like crazy now", "still testing d api", "how do i do", "alamin"]
}

def writes():
	try:
		with io.open('data.json', "w+", encoding ="utf8") as outfile:
			stuff = json.dumps(data, indent=4, sort_keys=True, separators=(",", ":"), ensure_ascii= False)
			outfile.write(stuff)
	except IOError:
		return "error"
#this is to read the json file
with open('data.json') as data:
		maindata = json.load(data)
		update = maindata["data"]
		update.append("msg")
		print(update)
		maindata["data"] = update
		print(maindata)