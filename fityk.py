import os

def full_algo(str_matching_files_names):
	files = finding_matching_files_to_str(str_matching_files_names)
	list_of_commands = making_list_of_commands_from_filenames(files)
	#just for 1 command
	streams = exec_commands(list_of_commands)
	return streams

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

def making_list_of_commands_from_filenames(filenames):
	list_of_commands = []
	for filename in filenames:
		list_of_commands.append(makimg_command_from_string(filename))
	return list_of_commands

def makimg_command_from_string(string):
	return "cfityk -I -q "+string+" '=->exec open_2peak_guess.fit'"
	
def exec_commands(list_of_commands):
	return_streams =[]
	for command in list_of_commands:
		return_stream = executing_command(command)
		return_streams.append(return_stream)
	return return_streams

def executing_command(command):
	stream = os.popen(command).read()
	return stream

def analise_stream(stream):
	print stream



print full_algo("10ppm")

# print finding_matching_files_to_str("")
# print makimg_command_from_string("file")



fout = open("results.dat","w")
f = open('3-100ppb.txt')

# stream = os.popen("cfityk -I -q 3-100ppb.txt '=->exec open_2peak_guess.fit'").read()
# print stream