import pandas as pd

data = pd.read_csv('movie_network_edgelist.txt', sep=",", encoding='utf-8', header=None)
data.columns = ["m1", "m2", "weight"]
df = pd.DataFrame(data)
movies1 = df.m1.unique()
movies2 = df.m2.unique()

import numpy
movies = numpy.concatenate([movies1,movies2])
movies = numpy.unique(movies)

print(movies)


f = open('movie_list.txt', "w", encoding="utf-8")
for i in range(len(movies)):
    f.write("%s\n" % (movies[i]))
f.close()

# data = pd.read_csv('movie_list.txt', sep="\n", encoding='utf-8', header=None)
# data.columns = ["movie"]
# df1 = pd.DataFrame(data)

# genre_data = pd.read_csv('movie_genre.txt', sep="\t", encoding='utf-8', header=None)
# print genre_data
# genre_data.columns = ["movie", "nan", "genre"]
# df2 = pd.DataFrame(genre_data)
# del df2['nan']

# genre_clean = pd.merge(df1, df2, how='inner')
# print genre_clean
# genre_clean.to_csv('movie_genre_clean.txt', encoding='utf-8', sep="\t", index=False, header=None)



