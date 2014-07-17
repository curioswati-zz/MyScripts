import csv

def score(name,dic,index):
    score = [15,10,5]
    dic[name]+=score[index-1]
    
def add_entry(name,dic,index):
    if name in dic:
        score(name,dic,index)
        return True
    elif name != "":
        dic[name] = 0
        score(name,dic,index)
        return False
def main():
    reader = csv.reader(open("C:\Python27\Choose Your Big Buddy - Sheet1.csv"))
    c=True
    big_buddies = {}
    for row in reader:
        if c:
           c=False
        else:
            for i, col in enumerate(row):
                if i != 0:
                    add_entry(col,big_buddies,i)
    return big_buddies                
print main()
