import csv
data=[]
with open('/Users/abhishek/Downloads/test/Dataset/house.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    count=1
    for row in reader:
        if count==1:
            count+=1
            continue
        data.append(row)
        count+=1
    pass1=[]
    pass2=[]
    for i in data:
        if (int(float(i[2])) - (541.1243*int(float(i[5]))) + (14926.04)) <= 0:
            pass1.append(i)
        
    for j in pass1:
        if (int(float(j[2])) - (327.685*int(float(j[5]))) - (46971.36)) >=0:
            pass2.append(j)
with open('house_clean.csv', 'w') as out:
    writer = csv.writer(out)
    for row in pass2:
            writer.writerow(row)