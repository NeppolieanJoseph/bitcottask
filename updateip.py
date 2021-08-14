import json
import os
import subprocess
import re

a_file = open("nodejs/config.json", "r")
json_object = json.load(a_file)
a_file.close()
print(json_object)

p = subprocess.Popen("docker inspect -f ‘{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}’ mongodb", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
mongoip = re.sub('‘' ,'',  output.decode('utf-8').strip('\n'))
mongoip = re.sub('’' ,'',  mongoip)
json_object["mongo_host"] = mongoip

p = subprocess.Popen("docker inspect -f ‘{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}’ rediscache", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
redisip = re.sub('‘' ,'',  output.decode('utf-8').strip('\n'))
redisip = re.sub('’' ,'',  redisip)
json_object["redis_host"] = redisip

a_file = open("nodejs/config.json", "w")
json.dump(json_object, a_file)
a_file.close()
print(json_object)
