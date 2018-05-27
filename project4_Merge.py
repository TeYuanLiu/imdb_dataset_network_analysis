# -*- coding: utf-8 -*-
import re

def clean_merge(input_file, output_file):
    for i, line in enumerate(input_file):
        newline = line.split("\t\t")
        if len(newline) <= 10:
            continue
        strip_list = []
        for obj in newline:
            pattern = re.search(r"\((\d{4}|\?{4})\/*I{0,}\)(.*)$", obj)
            if pattern:
                obj = obj.replace(pattern.group(2),'')
            obj = obj.replace(',','')
            strip_list.append(obj.strip("\n").strip())
        strip_list = list(filter(None, strip_list))
        string = ','.join([str(obj) for obj in strip_list])
        output_file.writelines(string+'\n')
""""
file_merge = open("merge_test.txt", "w+",encoding='ISO-8859-1')
file_actor = open("actor_movies.txt", "r",encoding='ISO-8859-1')
file_actress = open("actress_movies.txt", "r",encoding='ISO-8859-1') 

clean_merge(file_actress, file_merge)
clean_merge(file_actor, file_merg)

file_merge.close()
file_actress.close()
file_actor.close()
"""

"""
movie_list = open("movie_list.txt", "w+",encoding='ISO-8859-1')
file_merge = open("merge_test.txt", "r",encoding='ISO-8859-1') 
movies = {}
for i, line in enumerate(file_merge):
    newline = line.rstrip('\n')
    newline = line.split(",")
    character = newline[0].strip("\n").strip()
    for j in range(1,len(newline)):
        movie_name = newline[j].strip("\n").strip()
        if movie_name in movies:
            movies[movie_name] += ","+character
        else:
            movies[movie_name] = character
    #if i > 2000:
       #break
for key, value in movies.items():
    movie_list.writelines(key+','+value+'\n')
file_merge.close()
movie_list.close()
"""


movie_list = open("movie_list.txt", "r",encoding='ISO-8859-1')
movie_clean = open("movie_clean.txt", "w+",encoding='ISO-8859-1')

for i, line in enumerate(movie_list):
    newline = line.split(',')
    if len(newline) <= 5:
        continue
    strip_list = []
    for obj in newline:
        strip_list.append(obj.strip("\n").strip())
    strip_list = list(filter(None, strip_list))
    string = ','.join([str(obj) for obj in strip_list])
    movie_clean.writelines(string+'\n')

movie_clean.close()
movie_list.close()

