#!/usr/bin/python

import os
import re
import datetime
import sys
from subprocess import *


# stdin,stdout = os.popen2('"C:\Program Files\Fityk\cfityk.exe" -I -q "10-1ppm.txt" "=->exec open_2peak_guess.fit"')



# p.stdout.close()


def full_algo(str_matching_files_names,string2="txt"):
	files = finding_matching_files_to_str(str_matching_files_names,string2)
	# list_of_commands = making_list_of_commands_from_filenames(files)
	#just for 1 command
	streams = exec_commands(files)
	par_streams = parsing_streams(streams)
	output(par_streams)
	return par_streams

def finding_matching_files_to_str(string,string2):
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
	        
	        if string in filename and string2 in filename and len(dirname)==1:
	        	files.append(filename)

	    # Advanced usage:
	    # editing the 'dirnames' list will stop os.walk() from recursing into there.
	    if '.git' in dirnames:
	        # don't go into any .git directories.
	        dirnames.remove('.git')
	if len(files)<1:
		return sys.exit("There is no files with this mask. \nHint: cases, spaces, etc. are important.")
	else:
		print "\nMatched files: "
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
		return '"C:\Program Files\Fityk\cfityk.exe" -I -q "'+string+'" "=->exec open_2peak_guess.fit"'
	elif b == True:
		return '"C:\Program Files\Fityk\cfityk.exe" -I -q "'+string+'" "=->exec open_1peak_guess.fit"'

def exec_commands(filenames):
	return_streams =[]
	for filename in filenames:
		return_stream = executing_command(makimg_command_from_string(filename))
		# print return_stream
		k = parsing_stream(return_stream)
		# print k
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
	stream = os.popen(command).read()
	p = Popen(command, shell=True, bufsize=1024, stdin=PIPE,stdout=PIPE)
	# p.stdin.write("google.com\n")
	p.stdin.close()
	return p.stdout.read()

def parsing_stream(string):
	r1 = string.split('.txt')
	if ".txt:" in string:
		filename = r1[0]
	else:
		filename = []
	sp = string.split()
	# print sp
	# filename = [sp[i] for i,l in enumerate(sp) if 'txt' in l] 
	heights = [sp[i+1] for i,l in enumerate(sp) if l=='Height:']
	centers = [sp[i+6] for i,l in enumerate(sp) if l=='center']
	areas = [sp[i+6] for i,l in enumerate(sp) if l=='area']
	return [filename,centers,heights,areas]

def output(parsed_streams):
	fout = open("results.dat","w")
	now = datetime.datetime.now()
	# fout.write('This file was created '+str(now)+'\n\n')
	temp1 ='=====================||=============Peak 1===========||=============Peak 2=========||\n'
	temp = 'File name   || peaks ||  centre ||  height ||  area  || centre ||  height ||  area ||'
	fout.write(temp1)
	fout.write(temp)
	print temp1,temp
	for stream in parsed_streams:
		output =  '{0:15s} {1:7s} {2:10s} {3:10s} {4:10s}'.format(str(stream[0]), str(len(stream[1])), str(stream[1][0]),str(stream[2][0]),str(stream[3][0]))
		if len(stream[1])==2:
			output += '{0:10s} {1:10s} {2:10s}'.format(str(stream[1][1]), str(stream[2][1]), str(stream[3][1]))
		else:
			output += '{0:10s} {1:10s} {2:10s}'.format('NA','NA','NA')
		fout.write('\n%s' %output)
		print output
	fout.close()
	print "\nThis results were saved in results.dat\n"

x = "=" * (65 +len(str(sys.argv[1])))
print x
print 'We are trying to find the files with the following mask: = ', str(sys.argv[1]), "   ="
print x


if len(sys.argv)==2:
	full_algo(str(sys.argv[1]))
elif len(sys.argv)==3:
	full_algo(str(sys.argv[1]),str(sys.argv[2]))

# print finding_matching_files_to_str("")
# print makimg_command_from_string("file")





# stream = os.popen("cfityk -I -q 3-100ppb.txt '=->exec open_2peak_guess.fit'").read()
# print stream
