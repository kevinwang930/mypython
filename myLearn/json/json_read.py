import json
with open('customize.json','r') as f:
    data = json.load(f)

print(data)
print(type(data))

