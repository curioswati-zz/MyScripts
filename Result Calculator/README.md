best_2_of_3_calc.py is a python script that calculates the sums of best two of three numbers which are internal marks.
* * *

Problem statement :
----------------- 
To create a script which can read a csv file structured as *example.csv*.
It has *n* rows and 4 columns. First column is names of students.
The remaining three columns are the internal marks respectively for internal 1, 2 and 3.
The script has to calculate the sum of best two internal for each student.
Then create another csv file with the calculated data having 2 columns, one with student name
and second with its marks.

Instructions:
------------
The script is convinient to run from command prompt.
It takes standard input as the name of the file.
Type *best_2_of_3 example.csv* from command prompt in your current directory.

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
The modification can be done in the calculate_sum module by providing logic in accordance with the need.

Rest and required information is provided in the script itself.

[documentation of csv]: https://docs.python.org/2/library/csv.html