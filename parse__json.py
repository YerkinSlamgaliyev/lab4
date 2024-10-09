import json

with open('C:/Users/slamg/OneDrive/Рабочий стол/pp2/lab4/sample-data.json') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<6}")
print("-" * 80)

for item in data['imdata']:
    if 'l1PhysIf' in item:
        attributes = item['l1PhysIf']['attributes']
        dn = attributes['dn']
        description = attributes.get('descr', 'inherit')
        speed = attributes.get('speed', '')
        mtu = attributes.get('mtu', '')

        print(f"{dn:<50} {description:<20} {speed:<6} {mtu:<6}")
