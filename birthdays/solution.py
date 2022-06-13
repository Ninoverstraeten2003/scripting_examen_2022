# Write your solution in this file

import json
from datetime import datetime

with open("data.json",'r') as f:
    with open("output.txt",'w') as g:
        d = json.load(f)
        s = dict()
        for person in d:
            s[person["birthday"]["month"]] = s.get(person["birthday"]["month"],0) + 1
        s = list(s.items())
        list1 = []
        for month,aantal in s:
            month_str = str(month)
            month = datetime.strptime(month_str,'%m')
            month = month.strftime('%B')
            list1.append((month,'*'*aantal))
        list1.sort(key = lambda x: datetime.strptime(x[0],'%B'))
        for combination in list1:
            g.write(f"{combination[0].rjust(10)} {combination[1]}\n")
        
        
    