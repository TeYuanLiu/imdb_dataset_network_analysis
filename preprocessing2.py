# -*- coding: iso-8859-1 -*-
##############################
# Author: Te-Yuan Liu
##############################

##############################
# Import library
##############################
import numpy as np
import re
import time
##############################
# Define function
##############################
def mergetxt(fnames):
    with open("merged.txt", "w", encoding="ISO-8859-1") as outfile:
        for fname in fnames:
            with open(fname, encoding="ISO-8859-1") as infile:
                for line in infile:
                    outfile.write(line)
def readtxt_write_edgelist(fname, cast_names):
    movies = ["Booze Culture (2012)", "Call of Babylon (2012)", "Inner Joy of a Broken Heart (2011)", "Is This It? (2012)", "Life of a Spy (2012)", "Losers in Love (2011)", "Love House (2011)", "Street Fight (2012)", "The Book of Life (2013/I)", "The Shadow of Death (2011)", "Boycie (2011)", "Legion of Evil (2010)", "Be My Valentine (2011)", "A Schoolboy Error Production (2009)", "The Hope Within (2009)", "Fear of the Park (2010)", "White Cobra (2014)"]                 
    start = time.time()
    cast_movie_dict = {}
    movie_cast_dict = {}
    line_count = 0
    cast_count = 0
    with open(fname, encoding="ISO-8859-1") as fin:
        for line in fin:
            line_count += 1
            obj_list = re.split(r"\t+", line) ############# change to \t
            if len(obj_list) < 11: ############### change to 11 later
                continue
            cast_count += 1
            strip_list = []
            for obj in obj_list:
                strip_list.append(obj.strip("\n").strip().replace(",", ""))
            strip_list = list(filter(None, strip_list))
            obj_count = 0
            cast_name = strip_list[0]
            new_movie_list = []
            cast_movie_dict[cast_name] = new_movie_list
            for obj in strip_list:
                obj_count += 1
                if obj_count >= 2:
                    p1 = re.search(r"\((\d{4}|\?{4})[^()]*\)(.+)", obj)
                    if p1:
                        obj = obj.replace(p1.group(2),"")
                        ## movie 2 cast dict update
                        if movie_cast_dict.get(obj) == None:
                            new_cast_list = []
                            new_cast_list.append(cast_name)
                            movie_cast_dict[obj] = new_cast_list
                        else:
                            movie_cast_dict[obj].append(cast_name)
                        ## cast 2 movie dict update
                        cast_movie_dict[cast_name].append(obj)
                    else:
                        p2 = re.search(r"\((\d{4}|\?{4})[^()]*\)", obj)
                        if not p2:
                            obj = obj + " (????)"
                        # movie 2 cast dict update
                        if movie_cast_dict.get(obj) == None:
                            new_cast_list = []
                            new_cast_list.append(cast_name)
                            movie_cast_dict[obj] = new_cast_list
                        else:
                            movie_cast_dict[obj].append(cast_name)
                        ## cast 2 movie dict update
                        cast_movie_dict[cast_name].append(obj)
    print("There are ",len(cast_movie_dict)," actors/actresses and ",len(movie_cast_dict)," unique movies...")
    for cast_name in cast_names:
        print("Actor/Actress: ",cast_name," and number of movies: ",len(cast_movie_dict[cast_name]))
    with open("movie2actor.txt", "w", encoding="utf-8") as outfile:
        for k, v in movie_cast_dict.items():
            outfile.write("%s,%s\n" %(k, v))    

    with open("bipartite_edgelist.txt", "w", encoding="utf-8") as outfile:
        for k, v in movie_cast_dict.items():
            if(k in movies):
                for actor in v:
                    outfile.write("%s,%s,1\n" %(k, actor))

    # ## create edge list for actor/actress network
    # dic = {}
    # edgelist_dict = {}
    # for c1, ml in cast_movie_dict.items():
    #     for m in ml:
    #         for c2 in movie_cast_dict[m]:
    #             if c1 != c2:
    #                 dic[c1] = 1
    #                 dic[c2] = 1
    #                 key = c1 + "\n" + c2
    #                 if edgelist_dict.get(key) == None:
    #                     edgelist_dict[key] = 1.0/len(ml)
    #                 else:
    #                     edgelist_dict[key] += 1.0/len(ml)
    # print("There are ",len(dic)," nodes in the cast network...")
    
    # with open("cast_network_edgelist.txt", "w", encoding="utf-8") as outfile:
    #     for k, v in edgelist_dict.items():
    #         c1, c2 = k.split("\n")
    #         line = ",".join([c1.replace(",", ""), c2.replace(",", ""), str(v)]) + "\n"
    #         outfile.write(line)
    
    # ## create edge list for movie network
    # trim_movie_cast_dict = {}
    # trim_cast_movie_dict = {}
    # edgelist_dict = {}
    # for m, cl in movie_cast_dict.items():
    #     if len(cl) < 5: ############## change to 5
    #         continue
    #     trim_movie_cast_dict[m] = cl
    # for m, cl in trim_movie_cast_dict.items():
    #     for c in cl:
    #         if trim_cast_movie_dict.get(c) == None:
    #             new_movie_list = []
    #             new_movie_list.append(m)
    #             trim_cast_movie_dict[c] = new_movie_list
    #         else:
    #             trim_cast_movie_dict[c].append(m)
    # print("There are ",len(trim_cast_movie_dict)," actors/actresses and ",len(trim_movie_cast_dict)," unique movies left after trimming...")
    # dic = {}
    # for m1, cl1 in trim_movie_cast_dict.items():
    #     for c in cl1:
    #         for m2 in trim_cast_movie_dict[c]:
    #             if m1 != m2:
    #                 dic[m1] = 1
    #                 dic[m2] = 1
    #                 cl2 = movie_cast_dict[m2]
    #                 cast_union_count = len(list(set(cl1) | set(cl2)))
    #                 key1 = m1 + "\n" + m2
    #                 key2 = m2 + "\n" + m1
    #                 if edgelist_dict.get(key1) == None and edgelist_dict.get(key2) == None:
    #                     edgelist_dict[key1] = 1.0/cast_union_count
    #                 elif edgelist_dict.get(key1) != None and edgelist_dict.get(key2) == None:
    #                     edgelist_dict[key1] += 1.0/cast_union_count
    #                 elif edgelist_dict.get(key1) == None and edgelist_dict.get(key2) != None:
    #                     edgelist_dict[key2] += 1.0/cast_union_count
    #                 else:
    #                     print("*******error: ",edgelist_dict)
    #                     return
    # print("There are ",len(dic)," nodes in the movie network..." )
    
    # with open("movie_network_edgelist.txt", "w", encoding="utf-8") as outfile:
    #     for k, v in edgelist_dict.items():
    #         m1, m2 = k.split("\n")
    #         line = ",".join([m1.replace(",", ""), m2.replace(",", ""), str(v/2)]) + "\n"
    #         outfile.write(line)
    
    end = time.time()
    print("runtime: " + str(end - start))

##############################
# Main function
##############################
def main():
    # run the two below lines of code for creation of merged.txt
    file_names = ["actor_movies.txt", "actress_movies.txt"]
    cast_names = ["O'Connor Frank (I)", "Harris Sam (II)", "Downes Robin Atkin", "Miller Harold (I)", "Blum Steve (IX)", "Flowers Bess", "Jeremy Ron", "Tatasciore Fred", "Phelps Lee (I)", "Lowenthal Yuri", "Cruise Tom", "Watson Emma (II)", "Clooney George", "Hanks Tom", "Johnson Dwayne (I)", "Depp Johnny", "Smith Will (I)", "Streep Meryl", "DiCaprio Leonardo", "Pitt Brad"] 
    # mergetxt(file_names)

    print("hello" + " world...")
    readtxt_write_edgelist("merged.txt", cast_names)
if __name__ == "__main__":
    main()
