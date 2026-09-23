import numpy as np
import csv

insta_minutes=[]
study_min=[]

with open("001_digital_behaviour_analystic_lab/digital_behaviour.csv","r",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        insta_minutes.append(int(row["Instagram_Minutes"]))
        study_min.append(int(row["Study_Minutes"]))

insta_minutes=insta_minutes[:7]
study_min=study_min[:7]

Instagram=np.array(insta_minutes)
Study=np.array(study_min)

print(Instagram,Study)

#total=np.sum(Instagram)
insta_total=Instagram.sum()
insta_average=Instagram.mean()
insta_maximum=Instagram.max()
insta_minimum=Instagram.min()
insta_days=len(Instagram)

study_total=Study.sum()
study_average=Study.mean()
study_maximum=Study.max()
study_minimum=Study.min()
study_days=len(Study)

print(f"Instagram Total {insta_total},Instagram Average {insta_average},Instagram Maximum {insta_maximum},Instagram Minimum {insta_minimum},Instagram Days {insta_days}")
print(f"Study Total {study_total},Study Average {study_average},Study Maximum {study_maximum},Study Minimum {study_minimum},Study Days {study_days}")

print(Instagram[0],Instagram[-1],Instagram[2])

print(Instagram[:3],Instagram[-2:],Instagram[1:4],Instagram[::2])

i_hours=Instagram/60

print(i_hours)

i_hours=i_hours.round(2)

difference = Study-Instagram

'''greater=[val for val in difference if val>100]
for val in difference:
    if val>100
        greater.append(val)'''

boolean=Instagram>100

#print(greater)

#greater=[bool_ for bool_ in boolean if bool_]

#greater=filter(lamda bool:bool_,boolean)

greater_insta=Instagram[Instagram>100]
count_insta=(Instagram>100).sum()

greater_study=Study[Study>100]
count_study=(Study>100).sum()

value_insta=Instagram[Instagram>insta_average]
value_study=Study[Study>study_average]
