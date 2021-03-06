import json


# write your code here

json_string = str(input())

json_object = json.loads(json_string)

print(type(json_object))
print(json_object)