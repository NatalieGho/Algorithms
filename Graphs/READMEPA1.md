The visualization of the graph is a bunch of coordinates that determine the points on the 2D cartesian coordinate that is being created with the points. The algorithm follows the logic of using side roads, main roads, highways, main roads, then side roads in order to find the shortest path from one start point to the end point. Between points there are edges, and these are assigned a weight. At each point, the algorithm should give the shortest point and follow the logic of transitioning from different types of roads. 

The input for this code will be written as such: 
The first line includes how many side road, main road, and highway edges there are.
The second line includes all the edges that are side roads.
The third line includes all edges that are main roads.
The fourth line includes all edges that are highway roads.
The fifth line will say how many test cases there are.
The remaining lines will have four numbers each, which compose of the starting coordinate and the ending coordinate respectively. 

The output will first print out the total distance of the path, then the number of nodes travelled, then the path taken will be printed out in order. 


This algorithm is a variation of dijkstras algorithm which is modified for this program.