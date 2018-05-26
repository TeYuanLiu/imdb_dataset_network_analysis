##############################
# Author: Te-Yuan Liu
##############################

##############################
# Import library
##############################
import numpy as np
import re
##############################
# Define function
##############################
def mergetxt(fnames):
    with open("merged.txt", "w") as outfile:
        for fname in fnames:
            with open(fname, encoding="ISO-8859-1") as infile:
                for line in infile:
                    outfile.write(line)
def readtxt(fname):
    with open(fname, encoding="ISO-8859-1") as fin:
        c = 0
        for line in fin:

            obj_list = re.split(r"\t+", line)
            strip_list = []
            for obj in obj_list:
                strip_list.append(obj.strip("\n").strip())
            strip_list = list(filter(None, strip_list))
            for obj in strip_list:
                target = obj.split("(")[0]

            print(strip_list)
            c += 1
            if c > 3:
                break
##############################
# Main function
##############################
def main():
    # run the two below lines of code for creation of merged.txt
    #file_names = ["actor_movies.txt", "actress_movies.txt"]
    #mergetxt(file_names)

    readtxt("actor_movies.txt")
    #readtxt("actress_movies.txt")
    #str1 = ["  x  \n"]
    #str1[0] = str1[0].strip("\n")
    #print(str1)

if __name__ == "__main__":
    main()
