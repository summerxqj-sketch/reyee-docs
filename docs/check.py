import json, re

with open(r'C:\Users\HP\AppData\Local\Temp\reyee-deploy\tasks.html', 'r', encoding='utf-8') as f:
    c = f.read()

match = re.search(r'var RAW = (.+?);', c, re.DOTALL)
if match:
    data = json.loads(match.group(1))
    print(f'Tasks data: {len(data)} records')
    for d in data:
        print(f'  #{d["seq"]} {d["pri"]} {d["title"]}')
else:
    print('ERROR: No RAW data found!')

# Also check compare.html
with open(r'C:\Users\HP\AppData\Local\Temp\reyee-deploy\compare.html', 'r', encoding='utf-8') as f:
    c2 = f.read()

match2 = re.search(r'var RAW = (.+?);', c2, re.DOTALL)
if match2:
    data2 = json.loads(match2.group(1))
    print(f'\nCompare data: {len(data2)} records')
    print(f'First: {data2[0]["feature"]}')
    print(f'Last: {data2[-1]["feature"]}')
