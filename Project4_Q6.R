library(igraph)
#install.packages("data.table")
library(data.table)
getwd()
setwd("/Users/mandyfu/Documents/GitHub/imdb_dataset_network_analysis")
getwd()

system.time(dt <- fread(file="movie_network_edgelist.txt", encoding='UTF-8', header = F, sep = ",", fill = T))
head(dt)
g <- graph.data.frame(dt, directed=F)
vcount(g)
ecount(g)
plot(degree.distribution(g),main="Degree distribution of the movie network",xlab="Degree",ylab="Frequency")
saveRDS(g, "graph.rds")


c = fastgreedy.community(g)
saveRDS(c, "community.rds")