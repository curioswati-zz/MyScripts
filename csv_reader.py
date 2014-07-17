import csv
reader = csv.reader(open("Choose Your Big Buddy - Sheet1.csv"))
bList = {}
c=True
big_buddies = {'Ankit Kulkarni':0,'Ajeet Khan':0,'Akanksha Rathore':0,'Rahul Sagore':0,'Shaifali Agrawal':0,'Chitrank Dixit':0,'Nitesh Mishra':0,'Komal Rathore':0,'Bedi Singh Yadav':0,'Sunny Raikwar':0,'Gaurav Parmar':0}
for row in reader:
    if c:
        for i in range(0,len(row)):
            bList[row[i]] = []
        c=False
    else:
        i=0
        for key in bList:
            bList[key].append(row[i])
            i+=1
cnt=20
for key in bList:
    for name in big_buddies:
        if key != 'NewBies':
            score = bList[key].count(name) * cnt
            #print cnt
            big_buddies[name]+=score
    cnt-=5
print bList#big_buddies
