import json

infname = '2330.json'
with open(infname,'r',encoding="utf-8") as inf:
    data = json.load(inf)
print(data['MainData'].keys())