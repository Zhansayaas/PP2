import json
with open(r"c:Users/karbozzhansaya/Desktop/Принципы программирования/4lab/sample-data.json") as mx:
    json_data = mx.read()
data = json.loads(json_data)
print("Interface Status")
print("=" * 80)
print("DN" + ' '*46 + "Description" + ' '*10 + "Speed   MTU  ")
print('-'*47 + " " + '-'*20 + ' ' + "-"*7 + ' ' + "-"*4)
for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    speed = item["l1PhysIf"]["attributes"]["speed"]
    mtu = item["l1PhysIf"]["attributes"]["mtu"]
    print(f"{dn:<50} {speed:>8} {mtu:>6}")
