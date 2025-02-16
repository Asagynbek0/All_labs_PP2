import json

with open(r"C:\Users\alinu\Documents\new_folder\labs\lab4\json\sample-data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    
print("Interface Status")
print("=" * 74)
print(f"{'DN':<46} {'Description':<20} {'Speed':<6} {'MTU':<6}")
print("-" * 46 + " " + "-" * 20 + " " + "-" * 6 + " " + "-" * 6)

for i in data["imdata"]:
    properties = i["l1PhysIf"]["attributes"]
    DN = properties["dn"]
    Description = properties["descr"]
    Speed = properties["speed"]
    MTU = properties["mtu"]
    

    print(f"{DN:<46} {Description:<20} {Speed:<6} {MTU:<6}")