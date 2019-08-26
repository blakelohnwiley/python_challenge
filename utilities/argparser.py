import argparse

#defined functions 
def input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', action='store', dest='debug',default=False,
            help='Store the value for debug, default set to false.')
    parser.add_argument("-f",action='store', dest='filename',default="filename.txt",
            help='Store the input name of text file.')
    result = parser.parse_args()
    return result
