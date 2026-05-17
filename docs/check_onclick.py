import re, sys

with open(r'C:\Users\HP\AppData\Local\Temp\reyee-deploy\compare.html', 'r', encoding='utf-8') as f:
    c = f.read()

onclicks = re.findall(r'onclick="[^"]*"', c)
for oc in onclicks:
    print(oc[:120])
