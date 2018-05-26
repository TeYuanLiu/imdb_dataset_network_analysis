# -*- coding: utf-8 -*-
import re

file_merge = open("merge_movies.txt", "r+",encoding='ISO-8859-1') 
file_actor = open("actor_movies.txt", "r",encoding='ISO-8859-1')
file_actress = open("actress_movies.txt", "r",encoding='ISO-8859-1') 

for i, line in enumerate(file_actress):
    newline = line.split("\t\t")
    for j in range(len(newline)):
        print(newline[j])
        newline[j] = re.sub(r"(?<=\(\d{4}\)).*$",'',str(newline[j]))
        print(newline[j])
    if len(newline) > 10:
        file_merge.write(str(newline)+'\n')
    if i >= 3:
        break
"""
for i, line in enumerate(file_actor):
    newline = line.split("\t\t")
    if len(newline) > 10:
        file_merge.write(str(newline)+'\n')
"""
file_actress.close()
file_actor.close()
file_merge.close()