import json
with open('file.json', 'r') as f:
    file = json.load(f)
for donut in file:
    if donut['name'] == 'Old Fashioned':
        donut['batters']['batter'].append({'type': 'Tea', 'id': '5000'})
with open('file.json', 'w') as f:
    json.dump(file, f, indent=4)
print("Updated file.json file successfully!")