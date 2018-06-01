###############################
# Author: Te-Yuan Liu
###############################

###############################
# Import Library
###############################
library("igraph")
library(data.table)

###############################
# Define Function
###############################
plot_dd = function(g){
    d = degree(g, mode="in")
    dd = degree.distribution(g, mode="in", cumulative=F)
    degree = 1:max(d)
    probability = dd[-1]
    nonzero.position = which(probability != 0)
    probability = probability[nonzero.position]
    degree = degree[nonzero.position]
    plot(probability ~ degree, xlab="Degree", ylab="Probability", col=1, main="Degree Distribution")
}
pairing = function(g, nl){
    for(i in 1:length(nl)){
        v_n = nl[i]
        v_id = which(V(g)$name==v_n)
        e_incid = incident(g, v_id, mode="out")
        max_w = max(e_incid$V3)
        max_w_ids = which(e_incid$V3==max_w)
        print(e_incid[max_w_ids])
        print(e_incid[max_w_ids]$V3)
    }
}
get_page_rank = function(g, nl){
    d = degree(g, mode="in")
    E(g)$weight = E(g)$V3
    print("start page rank calculation...")
    pr = page_rank(g)$vector
    print("complete page rank calculation...")
    k = 10
    top_ten_ids = get_top_ten_ids(pr,k)
    for(i in 1:k){
        idx = top_ten_ids[i]
        print(V(g)[idx]$name)
        print(pr[idx])
        print(d[idx])
    }
    for(i in 1:length(nl)){
        v_n = nl[i]
        v_id = which(V(g)$name==v_n)
        print(v_n)
        print(pr[v_id])
        print(d[v_id])
    }

}
get_top_ten_ids = function(x, k){
    n = length(x)
    p = n - k
    xp = sort(x, partial=p)[p]
    which(x > xp)
}

###############################
# Main Function
###############################
main = function(){
    dt = fread("cast_network_edgelist.txt", encoding="UTF-8", header=F, sep=",", fill=T)
    g = graph.data.frame(dt, directed=T) 
    plot_dd(g)
    nl = c("Cruise Tom","Watson Emma (II)", "Clooney George", "Hanks Tom", "Johnson Dwayne (I)", "Depp Johnny", "Smith Will (I)", "Streep Meryl", "DiCaprio Leonardo", "Pitt Brad")
    pairing(g, nl)
    get_page_rank(g, nl)
}
main()
