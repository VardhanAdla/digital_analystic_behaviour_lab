import csv
APP="Instagram"
minutes=[]
with open("digital_behaviour.csv", "r", newline="", encoding="utf-8") as file:
    reader=csv.DictReader(file)
    for row in reader:
        minutes.append(int(row["Instagram_Minutes"]))
minutes=minutes[0:7]
total=sum(minutes)
average=total//len(minutes)
highest=max(minutes)
lowest=min(minutes)
count=0
for i in minutes:
    if i>average:
        count+=1

print(f"The app that is used {APP} , The total minutes used{total} ,The average minutes used {average} ,The highest minutes used {highest} ,The lowest minutes used {lowest} ,The no.of minutes used above average {count}")
