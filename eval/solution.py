# Write your solution in this file

import re

def replace(match):
    calc = match.group(1)
    if '+' in calc:
        numbers = calc.split('+')
        a = int(numbers[0].strip())
        b = int(numbers[1].strip())
        return rf"{a+b}"
    else:
        numbers = calc.split('*')
        a = int(numbers[0].strip())
        b = int(numbers[1].strip())
        return rf"{a*b}"
        
with open("input.txt",'r') as f:
    with open("output.txt",'w') as g:
        contents = f.read()
        contents = re.sub(r'\$\{(.*?)\}(\$)?',replace,contents) 
        g.write(contents)
