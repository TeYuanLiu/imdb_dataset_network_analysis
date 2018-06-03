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
for key, value in movies.items():
    movie_list.writelines(key+','+value+'\n')
file_merge.close()
movie_list.close()

movie_list = open("movie_list.txt", "r",encoding='ISO-8859-1')
movie_clean = open("movie_utf-8.txt", "w+",encoding='utf-8')

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


def edgelist(fname):
    with open("movie_network_edgelist.txt", "w", encoding="utf-8") as outfile:
        cast_movie_dict = {}
        movie_cast_dict = {}
        with open(fname, encoding="ISO-8859-1") as fin:
            for line in fin:    
                obj_list = line.split(',')
                strip_list = []
                for obj in obj_list:
                    strip_list.append(obj.strip("\n").strip())
                strip_list = list(filter(None, strip_list))
                obj_count = 0
                movie_name = strip_list[0]
                new_cast_list = []
                movie_cast_dict[movie_name] = new_cast_list
                for obj in strip_list:
                    obj_count += 1
                    if obj_count >= 2:
                        movie_cast_dict[movie_name].append(obj)
                        if cast_movie_dict.get(obj) == None:
                            new_movie_list = []
                            new_movie_list.append(movie_name)
                            cast_movie_dict[obj] = new_movie_list
                        else:
                            cast_movie_dict[obj].append(movie_name)
            edgelist_dict = {}
            for m1, cl in movie_cast_dict.items():
                for c in cl:
                    for m2 in cast_movie_dict[c]:
                        if m1 is not m2:
                            keylist = [m1, m2]
                            keylist.sort()
                            #print(keylist)
                            key = keylist[0] + "," + keylist[1]
                            if edgelist_dict.get(key) == None:
                                edgelist_dict[key] = 1/len(list(set(m1).union(m2)))
                            else:
                                edgelist_dict[key] += 1/len(list(set(m1).union(m2)))
            for k, v in edgelist_dict.items():
                c1, c2 = k.split(",")
                line = ",".join([c1, c2, str(v/2)]) + "\n"
                outfile.write(line)

edgelist("movie_clean.txt")
with open("movie_rating_utf8.txt", "w", encoding="utf-8") as outfile:
    with open("movie_rating.txt", "r", encoding="ISO-8859-1") as fin:
        for line in fin:
            outfile.write(line)






