import json
f=open("task.json","r")
text=f.read()
a=json.loads(text)
print(a['Subscriptions'])