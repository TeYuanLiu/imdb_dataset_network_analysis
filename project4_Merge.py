# -*- coding: utf-8 -*-
import re

file_merge = open("merge_movies.txt", "r+",encoding='ISO-8859-1') 
file_actor = open("actor_movies.txt", "r",encoding='ISO-8859-1')
file_actress = open("actress_movies.txt", "r",encoding='ISO-8859-1') 

def clean_merge(filename):
    for i, line in enumerate(filename):
        newline = line.split("\t\t")
        for j in range(len(newline)):
            pattern = re.search(r"\((\d{4}|\?{4})\/*I{0,}\)(.*)$", newline[j])
            if pattern:
                newline[j] = newline[j].replace(pattern.group(2),'')
        if len(newline) > 10:
            file_merge.write(str(newline)+'\n')

clean_merge(file_actress)
clean_merge(file_actor)

file_actress.close()
file_actor.close()
file_merge.close()