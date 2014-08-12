get_image.py is a python script created for downloading images from webpages.
* * *

Problem statement :
----------------- 
To create a script which recursively crawl all the links from the input url.
And download images from there.

Instructions:
------------
The script is convinient to run from command prompt.
It requires standard input.
First input is the url of the page from where to start.
Second input is the path of directory, in which to save the images.

Standard modules used:
---------------------
OS module is used.
It provides the script with some facilities of os, such as executing commands.
In the script, it is used for listing files in directories, and checking existence of directories.
For more information on OS, read the [documentation of OS][] .

urllib provides a high level interface for fetching data across the world wide web.
For more information on OS, read the [documentation of urllib][]

Rest and required information is provided in the script itself.

[documentation of OS]: https://docs.python.org/2/library/os.html

[documentation of urllib]: https://docs.python.org/2/library/urllib.html