popularity_calc.py is a python script that calculates popularity of names in a csv file.
* * *

Problem statement :
----------------- 
To create a script which can read a csv file structured as *example.csv*.
It has *n* rows and 4 columns. First column is names of newbies that choose its big buddy.
The remaining three columns are the names of big buddies, in the preference order as chosen by newbie.
The script has to calculate the popularity, by multiplying the occurence of a name by its position weight.
The position weight is 15 for first, 10 for second and 5 for third.
Finally sum up the score for the name.
Do the above for all big buddy names.
Then print the sorted names in descending order of their scores.

Instructions:
------------
The script is convinient to run from command prompt.
It takes standard input as the name of the file.
Type *popularity_calc example.csv* from command prompt in your current directory.

Standard modules used:
---------------------
csv module is used.
It provides reading and manipulations on csv (comma saperated value) files.
In the script, it is used for reading the input file.
For more information on csv, read the [documentation of csv][]

Restrictions:
------------
The script is somewhat specific for a kind of file, it was written for.
But with a little modification, it can be used for any file.
The modification can be done in the *score()* module, by providing a different score list.

Rest and required information is provided in the script itself.

[documentation of csv]: https://docs.python.org/2/library/csv.html