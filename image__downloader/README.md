get_image.py is a python script created for downloading pictures from web pages.
* * *

Problem statement :
----------------- 
To create a script which can download images from web pages provided one URL.
Should go through all the links mentioned on that URL and also download images from there.

Instructions:
------------
The script is convenient to run from command prompt.
It requires standard input.
First input is the URL, of the main page.
Second input is the directory name, where to save the images.

Standard modules used:
---------------------
OS module is used.
It provides the script with some facilities of os, such as executing commands.
In the script, it is used for listing files in directories, and checking existence of directories.
For more information on OS, read the [documentation of OS][] .

urllib provides a high level interface for fetching data across the world wide web.
For more information on OS, read the [documentation of urllib][]

Restrictions:
-------------
Only downloads JPG and JPEG images.

Rest and required information is provided in the script itself.

[documentation of OS]: https://docs.python.org/2/library/os.html
[documentation of urllib]:https://docs.python.org/2/library/urllib.html