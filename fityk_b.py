import os
import re
import datetime

def full_algo(str_matching_files_names):
	files = finding_matching_files_to_str(str_matching_files_names)
	# list_of_commands = making_list_of_commands_from_filenames(files)
	#just for 1 command
	streams = exec_commands(files)
	par_streams = parsing_streams(streams)
	output(par_streams)
	return par_streams

def finding_matching_files_to_str(string):
	files = []
	for dirname, dirnames, filenames in os.walk('.'):
	    # print path to all subdirectories first.
	    # for subdirname in dirnames:
	        # print os.path.join(dirname, subdirname)
	    # print filenames
	    # print dirname
	    # print path to all filenames.
	    for filename in filenames:
	        # print os.path.join(dirname, filename)
	        # print filename
	        
	        if string in filename:
	        	if len(dirname)==1:
	        		files.append(filename)

	    # Advanced usage:
	    # editing the 'dirnames' list will stop os.walk() from recursing into there.
	    if '.git' in dirnames:
	        # don't go into any .git directories.
	        dirnames.remove('.git')
	if len(files)<1:
		print "There is no files with this mask"
	print "Matched files: "
	for file in files:
		print file
	return files

# def making_list_of_commands_from_filenames(filenames):
# 	list_of_commands = []
# 	for filename in filenames:
# 		list_of_commands.append(makimg_command_from_string(filename))
# 	return list_of_commands

def makimg_command_from_string(string,b=False):
	if b == False:
		return "cfityk -I -q '"+string+"' '=->exec open_2peak_guess.fit'"
	elif b == True:
		return "cfityk -I -q '"+string+"' '=->exec open_1peak_guess.fit'"

def exec_commands(filenames):
	return_streams =[]
	for filename in filenames:
		return_stream = executing_command(makimg_command_from_string(filename))
		# print return_stream
		k = parsing_stream(return_stream)
		if abs(float(k[1][1])-float(k[1][0])) < 30:
			return_stream  = executing_command(makimg_command_from_string(filename,True))
		return_streams.append(filename+": "+return_stream)
	return return_streams

def parsing_streams(streams):
	parsing_streams = []
	for stream in streams:
		parsing_streams.append(parsing_stream(stream))
	return parsing_streams

def executing_command(command):
	# print "executing ",command
	stream = os.popen(command).read()
	return stream

def parsing_stream(string):
	sp = string.split()
	# print sp
	filename = [sp[i] for i,l in enumerate(sp) if 'txt' in l] 
	heights = [sp[i+1] for i,l in enumerate(sp) if l=='Height:']
	centers = [sp[i+6] for i,l in enumerate(sp) if l=='center']
	areas = [sp[i+6] for i,l in enumerate(sp) if l=='area']
	return [filename,centers,heights,areas]

def output(parsed_streams):
	fout = open("results.dat","w")
	now = datetime.datetime.now()
	fout.write('This file was created '+str(now)+'\n')
	for stream in parsed_streams:
		output = ''+str(stream[0][0]) + ' has peaks at ' +str(stream[1]) + '\nwith heights:'  +str(stream[2])

		fout.write('%s\n' %output)
	fout.close()
	print "\n", output
	print "\nThis results were saved in results.dat\n"

full_algo("pp")


# print finding_matching_files_to_str("")
# print makimg_command_from_string("file")





# stream = os.popen("cfityk -I -q 3-100ppb.txt '=->exec open_2peak_guess.fit'").read()
# print stream