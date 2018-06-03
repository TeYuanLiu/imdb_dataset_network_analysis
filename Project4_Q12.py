import pandas as pd
import os, pickle
import string
import re
import numpy as np
from sklearn import linear_model
import sklearn.metrics as mcs
from collections import defaultdict
import time

fname = "movie_rating.txt"

start = time.time()
movie_rating_dict = {}
line_count = 0

with open(fname, encoding="ISO-8859-1") as fin:
    for line in fin:
        line_count += 1
        obj_list = re.split(r"\t+", line) ############# change to \t        

        obj = obj_list[0]

        p1 = re.search(r"\((\d{4}|\?{4})[^()]*\)(.+)", obj)
        if p1:
            obj = obj.replace(p1.group(2),"")
            movie_rating_dict[obj]=obj_list[1]
        else:
            p2 = re.search(r"\((\d{4}|\?{4})[^()]*\)", obj)
            if not p2:
                obj = obj + " (????)"
            movie_rating_dict[obj]=obj_list[1]


with open("movie_rating_clean.txt", "w", encoding="utf-8") as outfile:
    for k, v in movie_rating_dict.items():
        outfile.write("%s\t%s" %(k, v)) 


fname = "director_movies.txt"

start = time.time()
movie_director_dict = {}
line_count = 0

with open(fname, encoding="ISO-8859-1") as fin:
    for line in fin:
        line_count += 1
        obj_list = re.split(r"\t+", line) ############# change to \t        

        obj = obj_list[0]

        p1 = re.search(r"\((\d{4}|\?{4})[^()]*\)(.+)", obj)
        if p1:
            obj = obj.replace(p1.group(2),"")
            movie_director_dict[obj_list[1]]=obj
        else:
            p2 = re.search(r"\((\d{4}|\?{4})[^()]*\)", obj)
            if not p2:
                obj = obj + " (????)"
            movie_director_dict[obj_list[1]]=obj


with open("movie_director_clean.txt", "w", encoding="utf-8") as outfile:
    for k, v in movie_director_dict.items():
        outfile.write("%s\t%s" %(k, v)) 