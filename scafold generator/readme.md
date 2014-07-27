scafold_gen is a python script that generates a project scafold.
* * *

Problem statement :
----------------- 
To create a script which can create the whole directory structure mentioned in *sample.pdf*.

Instructions:
------------
The script is convinient to run from command prompt.
It takes standard input as the name of the directory, in which scafold needs to generate.
Type *Generate_scafold.py <project>* from command prompt.
Provide absolute path if you don't want it to generate the scafold in current directory.

Standard modules used:
---------------------
OS and sys modules are used.
OS provides a portable way of using operating system dependent functionality, such as executing commands.
In the script, it is used for creating directories, and checking existence of directories.

sys provides access to some variables used or maintained by the interpreter and functions that interact strongly with the interpreter.
In the script, it is used for reading command line args.
For more information on OS, read the [documentation of OS][]
For more information on sys, read the [documentation of sys][]

Restrictions:
------------
The script is specific for the structure mentioned in sample.pdf.

Rest and required information is provided in the script itself.

[documentation of OS]:https://docs.python.org/2/library/os.html
[documentation of sys]:https://docs.python.org/2/library/sys.html