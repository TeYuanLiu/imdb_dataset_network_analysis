import pandas as pd

data = pd.read_csv('movie_network_edgelist.txt', sep=",", header=None)
data.columns = ["m1", "m2", "weight"]
df = pd.DataFrame(data)
movies = df.m1.unique()

f = open('movie_list.txt', 'wb')
for i in range(len(movies)):
    f.write("%s\n" % (movies[i]))
f.close()

data = pd.read_csv('movie_list.txt', sep="\n", header=None)
data.columns = ["movie"]
df1 = pd.DataFrame(data)

genre_data = pd.read_csv('movie_genre.txt', sep="\t", header=None)
print genre_data
genre_data.columns = ["movie", "nan", "genre"]
df2 = pd.DataFrame(genre_data)
del df2['nan']

genre_clean = pd.merge(df1, df2, how='inner')
print genre_clean
genre_clean.to_csv('movie_genre_clean.txt', encoding='utf-8', sep="\t",index=False)



