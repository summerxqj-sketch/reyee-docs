import re

with open(r'C:\Users\HP\AppData\Local\Temp\reyee-deploy\tasks.html', 'r', encoding='utf-8') as f:
    c = f.read()
m = re.search(r'onclick="[^"]*"', c)
if m: print('tasks.html:', m.group()[:100])

with open(r'C:\Users\HP\AppData\Local\Temp\reyee-deploy\compare.html', 'r', encoding='utf-8') as f:
    c2 = f.read()
m2 = re.search(r'onclick="[^"]*"', c2)
if m2: print('compare.html:', m2.group()[:100])
