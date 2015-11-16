Shotwell's SQLITE schema and design beg, just beg, for a REST front end, 
and this is a project to produce one using Flask-RESTless. 

Such a thing would allow anyone with some hard drives and a CPU 
to set up his own mini-Flickr. The first implementation for this project
will involve a BeagleBone Black and two network-attached drives. 

The idea is simple:

a config.py that finds the Shotwell SQLITE database
and some file path mani[ulations (if need be) to get at the photo contents.

And a views.py that lets you have your own mini-Flickr. 