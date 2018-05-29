# -*- coding: utf-8 -*-
import re

def clean_merge(input_file, output_file):
    for i, line in enumerate(input_file):
        newline = line.split("\t\t")
        if len(newline) <= 10:
            continue
        strip_list = []
        for obj in newline:
            pattern = re.search(r"\((\d{4}|\?{4})\/.*\)(.*)$", obj)
            if pattern:
                obj = obj.replace(pattern.group(2),'')
            obj = obj.replace(',','')
            strip_list.append(obj.strip("\n").strip())
        strip_list = list(filter(None, strip_list))
        string = ','.join([str(obj) for obj in strip_list])
        output_file.writelines(string+'\n')

file_merge = open("merge_test.txt", "w+",encoding='ISO-8859-1')
file_actor = open("actor_movies.txt", "r",encoding='ISO-8859-1')
file_actress = open("actress_movies.txt", "r",encoding='ISO-8859-1') 

clean_merge(file_actress, file_merge)
clean_merge(file_actor, file_merge)

file_merge.close()
file_actress.close()
file_actor.close()

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


"""
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

movie_clean = open("movie_clean.txt", "r",encoding='ISO-8859-1')
edge_list = open("edge_list.txt", "w+",encoding='ISO-8859-1')
matrix = []
for i, line in enumerate(movie_clean):
    newline = line.split(',')
    strip_list = []
    for obj in newline:
        strip_list.append(obj.strip("\n").strip())
    strip_list = list(filter(None, strip_list))
    matrix.append(strip_list)
for i in range(len(matrix)-1):
    print(i)
    for j in range(i+1, len(matrix)):
        intersect = len(intersection(matrix[i],matrix[j]))
        union = len(matrix[i])+len(matrix[j])-2
        if intersect > 0:
            weight = intersect/union
            edge_list.writelines(matrix[i][0]+','+matrix[j][0]+','+str(weight)+'\n')
            #print(matrix[i][0], matrix[j][0], weight)
print(len(matrix))
movie_clean.close()
edge_list.close()
"""