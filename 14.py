import json

x='{"name":"John","age":24,"city":"Berlin"}'

y=json.loads(x)

print(y["age"])
print(y["city"])
print(y["name"])
print(y)