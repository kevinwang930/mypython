import json

# a Python object (dict):
x = {
  "librepath": " ",
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)   
with open('customize.json','w+') as f:
    f.write(y)
