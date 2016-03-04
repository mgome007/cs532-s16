library(igraph)
#Reads the Karate Data from a seprate GML file from the link:
# http://networkdata.ics.uci.edu/data/karate/karate.gml
# http://www-personal.umich.edu/~mejn/netdata/
g <- read.graph("karate.gml", format="gml")

print('Edges will be deleted in the following order : ')
	
repeat{
	#Edges are beign calcualted below...
	edges_betweenness <- edge.betweenness(g)
	#Seperation of Edges are codnucted with the maximum value of edges
	max_value <- max(edges_betweenness)
	#Edges are deleted as followed.
	edge_to_delete <- match(c(max_value),edges_betweenness)
	#Graph is updated after each seperation
	print(paste(paste(paste(get.edgelist(g)[edge_to_delete,1]," -> "),get.edgelist(g)[edge_to_delete,2]),paste("  -- Betweenness = ",max_value)))
	g <- delete.edges(g, E(g, P=c(get.edgelist(g)[edge_to_delete,1],get.edgelist(g)[edge_to_delete,2])))
	cluster_no <- clusters(g)['no']

	#Number of clusters to be undone are declared here
	if(cluster_no == 2)
	{
		break
	}

	cs <- leading.eigenvector.community(g, steps=1)
	#Colors given to each node is designed here
	V(g)$color <- ifelse(cs$membership==1, "brown1", "olivedrab4")
	scale <- function(v, a, b) {
  	v <- v-min(v) ; v <- v/max(v) ; v <- v * (b-a) ; v+a
	}
	E(g)$color <- "grey"
	E(g)[ V(g)[ color=="brown1" ] %--% V(g)[ color=="olivedrab4" ] ]$color <- "red"
	tkplot(g, layout=layout.kamada.kawai, vertex.label.font=2)
}
#Majority of this code was refrence from sources that I had to find to
# help strengthen my understanding of this paper.
#http://spaghetti-os.blogspot.com/2014/05/zacharys-karate-club.html
cs <- leading.eigenvector.community(g, steps=1)
V(g)$color <- ifelse(cs$membership==1, "brown1", "olivedrab4")
scale <- function(v, a, b) {
v <- v-min(v) ; v <- v/max(v) ; v <- v * (b-a) ; v+a
}
V(g)$size <- scale(abs(cs$eigenvectors[[1]]), 10, 20)
E(g)$color <- "grey"
E(g)[ V(g)[ color=="brown1" ] %--% V(g)[ color=="olivedrab4" ] ]$color <- "red"
tkplot(g, layout=layout.kamada.kawai, vertex.label.font=2)

