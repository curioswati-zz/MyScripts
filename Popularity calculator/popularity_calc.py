''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''This script reads a csv file and performs some data based calculations.
It creates a dictionary of unique names found in file.
but not includes names in first column of each row.
It then scores the names by their positions columnwise.
Finally it sorts the names in order of their score.'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''Required modules.'''
import csv

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''Scores the input name.
It multiplies the name with a integer according to its index
Then updates the dic dictionary with new value.'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def score(name,dic,index):
    score = [15,10,5]
    dic[name]+=score[index-1]

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''    
'''Checks the input name , if that exist in dic dictionary.
If exist then calls score to update it's score.
else adds it with a score of 0 and then scores it by calling score().'''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def add_entry(name,dic,index):
    if name in dic:
        score(name,dic,index)
        return True
    elif name != "":
        dic[name] = 0
        score(name,dic,index)
        return False
    
'''Main Module.'''
def main():
    filename = raw_input("Enter the filename: ")
    reader = csv.reader(open(filename))                           #The reader object of the csv file.
    if not reader:
        print "Failed to open "+filename
    c=True
    big_buddies = {}
    for row in reader:
        if c:                                                     #To ignore the header row.
           c=False
        else:
            for i, col in enumerate(row):                         #iterating over the rows in reader object.
                if i != 0:
                    add_entry(col,big_buddies,i)
                    
    return sorted(big_buddies.items(),key=lambda x:x[1],reverse = True) #sorted in order of values

big_buddies = main()
for names in big_buddies:
    print names[0]+" : "+ str(names[1])
