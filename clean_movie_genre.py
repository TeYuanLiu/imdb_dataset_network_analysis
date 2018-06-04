import pandas as pd
import re
import time
# data = pd.read_csv('movie2actor.txt', sep=",", encoding='utf-8', header=None)
# data.columns = ["m", "a"]
# df = pd.DataFrame(data)
# movies = df.m.unique()

# import numpy

# f = open('movie_list.txt', "w", encoding="utf-8")
# for i in range(len(movies)):
#     f.write("%s\n" % (movies[i]))
# f.close()

# data = pd.read_csv('movie_list.txt', sep="\n", header=None)
# data.columns = ["movie"]
# df1 = pd.DataFrame(data)

fname = "movie_genre.txt"

start = time.time()
movie_genre_dict = {}
line_count = 0

with open(fname, encoding="ISO-8859-1") as fin:
    for line in fin:
        line_count += 1
        obj_list = re.split(r"\t+", line) ############# change to \t        

        obj = obj_list[0]

        p1 = re.search(r"\((\d{4}|\?{4})[^()]*\)(.+)", obj)
        if p1:
            obj = obj.replace(p1.group(2),"")
            movie_genre_dict[obj]=obj_list[1]
        else:
            p2 = re.search(r"\((\d{4}|\?{4})[^()]*\)", obj)
            if not p2:
                obj = obj + " (????)"
            movie_genre_dict[obj]=obj_list[1]


with open("movie_genre_clean.txt", "w", encoding="utf-8") as outfile:
    for k, v in movie_genre_dict.items():
        outfile.write("%s\t%s" %(k, v))    


# genre_data = pd.read_csv('movie_genre.txt', sep="\t", header=None)
# print(genre_data)
# genre_data.columns = ["movie", "nan", "genre"]
# df2 = pd.DataFrame(genre_data)
# del df2['nan']

# genre_clean = pd.merge(df1, df2, how='inner')
# print(genre_clean)
# genre_clean.to_csv('movie_genre_clean.txt', encoding='utf-8', sep="\t", index=False, header=None)

    

