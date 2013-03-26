import os

def finding_matching_files_to_str(string):
	files = []
	for dirname, dirnames, filenames in os.walk('.'):
	    # print path to all subdirectories first.
	    for subdirname in dirnames:
	        print os.path.join(dirname, subdirname)

	    # print path to all filenames.
	    for filename in filenames:
	        # print os.path.join(dirname, filename)
	        # print filename
	        if string in filename:
	        	files.append(filename)

	    # Advanced usage:
	    # editing the 'dirnames' list will stop os.walk() from recursing into there.
	    if '.git' in dirnames:
	        # don't go into any .git directories.
	        dirnames.remove('.git')
	return files

def makimg_command_from_string(string):
	return "cfityk -I -q "+string+" '=->exec open_2peak_guess.fit'"
	

print finding_matching_files_to_str("")
print makimg_command_from_string("file")



fout = open("results.dat","w")
f = open('3-100ppb.txt')

# stream = os.popen("cfityk -I -q 3-100ppb.txt '=->exec open_2peak_guess.fit'").read()
# print stream