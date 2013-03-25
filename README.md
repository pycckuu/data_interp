Here are a couple of example files of the type of data I'm looking at (.txt) and a link to the software webpage:

http://fityk.nieto.pl/

Ideally I would like a short script which will call fityk, perform a background correction, auto-identify the peaks (up to 5), autofit a LogNormalA peak to each identified peak, then export the key properties of the peaks (Center, Area and Height) to a text file along with the file name. i.e. the first linees would look like (the numbers are just made up):

610ppm.txt peak1
40.67 93196
7591
610ppm.txt peak2
90.31
101962
5300
500ppm.txt
peak1 39.56
900980 3909

The peaks correspond in this case to different species of arsenic (arsenite and arsenate).  The first column corresponds to the time in seconds and the second column to the intensity measured at the detector (the intensity is then converted to a concentration after calibration).

I have never used the command line version of the software or tried any scripting with it, so I'm not sure how user friendly it is....if you look into it and think it would be difficult or take a lot of time to write something, don't worry about it.  We can just do it file by file with the GUI if necessary (I was just hoping you might find a more efficient way to do it!).