# -*- coding: utf-8 -*-
import re

def clean_merge(filename):
    for i, line in enumerate(filename):
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
        file_merge.writelines(string+'\n')
""""
file_merge = open("merge_test.txt", "w+",encoding='ISO-8859-1')
file_actor = open("actor_movies.txt", "r",encoding='ISO-8859-1')
file_actress = open("actress_movies.txt", "r",encoding='ISO-8859-1') 

clean_merge(file_actress)
clean_merge(file_actor)

file_merge.close()
file_actress.close()
file_actor.close()
"""

file_merge = open("merge_test.txt", "r",encoding='ISO-8859-1') 

for i, line in enumerate(file_merge):
    newline = line.rstrip('\n')
    newline = line.split(",")
    for obj in newline:
        print(obj.strip("\n").strip())
    if i > 2:
       break
   
file_merge.close()
