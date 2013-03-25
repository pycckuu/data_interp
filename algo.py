
import os
# import matplotlib.pyplot


def read(file):
    """Function read the inf from file and return"""
    f = open(file)
    next(f) #skipping first line
    x = []
    for line in f:
        y = [float(value) for value in line.split()]
        x.append( y )
    f.close()
    x2 = filter(None, x)
    return x2

def baseline(data):
    """ sum positive in clockwise direction in triangles"""
    mean_time_left = ( data[0][0] + data[1][0] + data[2][0] ) / 3
    mean_value_left = ( data[0][1] + data[1][1] + data[2][1] ) / 3

    mean_time_right = ( data[-1][0] + data[-2][0] + data[-3][0] ) / 3
    mean_value_right = ( data[-1][1] + data[-2][1] + data[-3][1] ) / 3

    for value in data:
         y = value[1]
         x = value[0]
         mean_value_right - mean_value_left
         x / ( x - mean_time_left )
         y_correction = ( x - mean_time_left ) * ( mean_value_right - mean_value_left) / (
                                                        mean_time_right - mean_time_left )
         value[1] = y - y_correction
    return data

    # print mean_time_right, mean_value_right,mean_value_left,mean_time_left

x = read('3-100ppb.txt')
print x
print baseline(x)
os.system("echo 'hello world'")

# matplotlib.pyplot.show()