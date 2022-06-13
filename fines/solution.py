# Write your solution in this file
"""date,license_plate,speed,address
2020-03-01 05:40:25,HGQ 845,136,"16210 Daniel Trace
West Josephshire, OK 94582"""

import csv


with open('violations.csv','r') as c:
    with open('output.txt','w') as out:
        cs = csv.DictReader(c)
        d = dict()
        for row in cs:
            plate = row["license_plate"]
            speed = row["speed"]
            d[row["license_plate"]] = d.get(row["license_plate"],0) + int(speed)-120
        d = dict(sorted(d.items(),key=lambda x : (x[1],x[0])))
        for plate,fines in d.items():
            out.write(f"{plate} {fines}\n")
        
            
    