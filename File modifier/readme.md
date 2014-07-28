File modifier.py is a python script created for specific modification in a text file.
* * *

Problem statement :
----------------- 
To create a script which can insert some text in between a file.
The modification should be done at a specific place.
All files in the current directory and its subdirectories should modify, where the script reside.

Instructions:
------------
The script is convinient to run from command prompt.
It requires standard input.
First input is the text, after which, insertion need take place.
Second input is the text to insert.

Standard modules used:
---------------------
OS module is used.
It provides the script with some facilities of os, such as executing commands.
In the script, it is used for listing files in directories, and checking existence of directories.
For more information on OS, read the [documentation of OS][]

Restrictions:
------------
The script is somewhat specific for a kind of files, it was written for.
But with a little modification, it can be used for any file.
The modification needs to be done in the module named *"modify_line"*.
It just needs to change the *add_the_text_at* variable so as to provide suitable location after the first input.
**Caution** : Never run the script for the same directory or file again. It does not overwrite, but insert again after the previous modification.

Rest and required information is provided in the script itself.

[documentation of OS]:[https://docs.python.org/2/library/os.html]
