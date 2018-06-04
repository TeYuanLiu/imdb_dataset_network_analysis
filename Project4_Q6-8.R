library(igraph)
#install.packages("data.table")
#install.packages("SciViews")
library(data.table)
library(SciViews)
getwd()
setwd("/Users/mandyfu/Documents/GitHub/imdb_dataset_network_analysis")
getwd()

#system.time(dt <- fread(file="movie_network_edgelist.txt", encoding='UTF-8', header = F, sep = ",", fill = T))
#head(dt)
#g <- graph.data.frame(dt, directed=F)
g = readRDS("graph.rds")
vcount(g)
ecount(g)

pdf('/Users/mandyfu/Documents/GitHub/imdb_dataset_network_analysis/Q6.pdf')
plot(degree.distribution(g),main="Degree distribution of the movie network",xlab="Degree",ylab="Frequency")
dev.off()
#saveRDS(g, "graph.rds")

#c = fastgreedy.community(g)
#saveRDS(c, "community.rds")
c = readRDS("community.rds")

modularity(c)
sizes(c)

movie_genres = fread(file="movie_genre_clean.txt", header=FALSE, sep='\t')
head(movie_genres)
V(g)$genre=as.character(movie_genres$V2[match(V(g)$name,movie_genres$V1)]) 
V(g)$community.id = c$membership

for(i in 1:10){
  V2 = V(g)[community.id == i]
  #g2 = induced_subgraph(g, V2)
  counts = table(V2$genre)
  barplot(counts, main=paste("Community", i, "Genre Distribution"), ylab="Number of Movies", las=2)
  # pdf('Q7_',i,'.pdf')
  # barplot(counts, main=paste("Community", i, "Genre Distribution"), ylab="Number of Movies", las=2)
  # dev.off()
}

##Question 8(a): In each community determine the most dominant genre based simply on frequency counts.
for(i in 1:10){
  V2 = V(g)[community.id == i]
  counts = table(V2$genre)
  index = which(counts %in% max(counts))
  print(rownames(counts)[index])
}

##Question 8(b)

all_counts = table(V(g)$genre)
all_genres = as.vector(all_counts)
q = all_genres/sum(all_genres)
names(q) = names(all_counts)

for(i in 1:10){
  V2 = V(g)[community.id == i]
  counts = table(V2$genre)
  c = as.vector(counts)
  lnc = ln(c)
  p = c/sum(c)
  scores=numeric(length(c))
  
  for(j in 1:length(c)){
    genre_name = names(counts)[j]
    scores[j] = lnc[j]*(p[j]/q[genre_name])
  }
  
  index = which(scores %in% max(scores))
  print(rownames(counts)[index])
}

##Question 8(c) community 8
V2 = V(g)[community.id == 8]
counts = table(V2$genre)
system.time(dt2 <- fread(file="bipartite_edgelist.txt", encoding='UTF-8', header = F, sep = ",", fill = T))
bg <- graph.data.frame(dt2, directed=F)
V(bg)$genre=as.character(movie_genres$V2[match(V(bg)$name,movie_genres$V1)]) 
V(bg)$type <- V(bg)$name %in% V2$name
V(bg)$color <- ifelse(V(bg)$type, "lightblue", "orange")
V(bg)$label.degree = ifelse(V(bg)$type, pi, 0)
label_degree = ifelse(V(bg)$type, pi, 0)
nodesize=degree(bg)
l <- layout.bipartite(bg) 
plot(bg, layout = l[, c(2,1)],vertex.label.cex = 0.8, vertex.size=nodesize, vertex.label.degree = -pi/2, vertex.label.dist = 1)
degrees = degree(bg)
for(id in 1:vcount(bg)){
  if (! V(bg)$type[id]){
    print(id)
    print(degrees[id])
  }
}

actor_ids = c(19, 20, 25)
for(id in actor_ids){
  counts = table(neighbors(bg, V(bg)[id])$genre)
  barplot(counts, main=paste(V(bg)[id]$name, "movie genre"), ylab="Number of Movies", las=2)
}


