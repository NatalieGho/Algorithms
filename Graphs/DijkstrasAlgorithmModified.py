# PA1 Skeleton Code
# DSA2, spring 2025
# Natalie Ghofrany, krv3xx
import heapq

# This code will read in the input, and put the values into lists.  It is up
# to you to properly represent this as a graph -- this code only reads in the
# input properly.

# Read in the values for the number of side roads, main roads, and highways
[s,m,h] = [int(x) for x in input().split(" ")]
# Read in the side road edges
tmp = input().split(" ")
side_road_edges =sorted([(int(tmp[i]),int(tmp[i+1]),int(tmp[i+2]),int(tmp[i+3]),int(tmp[i+4])) for i in range(0,5*s,5)])
# Read in the main road edges
tmp = input().split(" ")
main_road_edges =sorted([(int(tmp[i]),int(tmp[i+1]),int(tmp[i+2]),int(tmp[i+3]),int(tmp[i+4])) for i in range(0,5*m,5)])
# Read in the highway edges
tmp = input().split(" ")
highway_edges = sorted([(int(tmp[i]),int(tmp[i+1]),int(tmp[i+2]),int(tmp[i+3]),int(tmp[i+4])) for i in range(0,5*h,5)])
# Read in how many test cases there will be
num_test_cases = int(input())
# Read in each test case
test_cases = []
for _ in range(num_test_cases):
	tmp = input().split(" ")
	test_cases.append((int(tmp[0]),int(tmp[1]),int(tmp[2]),int(tmp[3])))

# Generate a list of the nodes from the edges read in
side_road_nodes = []
main_road_nodes = []
highway_nodes = []
all_nodes = []
for (x1,y1,x2,y2,w) in side_road_edges:
	side_road_nodes.append((x1,y1))
	side_road_nodes.append((x2,y2))
side_road_nodes = sorted(list(set(side_road_nodes))) # remove duplicates
for (x1,y1,x2,y2,w) in main_road_edges:
	main_road_nodes.append((x1,y1))
	main_road_nodes.append((x2,y2))
main_road_nodes = sorted(list(set(main_road_nodes))) # remove duplicates
for (x1,y1,x2,y2,w) in highway_edges:
	highway_nodes.append((x1,y1))
	highway_nodes.append((x2,y2))
highway_nodes = sorted(list(set(highway_nodes))) # remove duplicates
all_nodes = sorted(list(set(side_road_nodes+main_road_nodes+highway_nodes))) # combine and remove duplicates

# At this point, the data structures are as follows.  You may not need all of
# these in your code.
#
# - `s`, `m`, and `h` contain the (integer) number of side road edges, main
#   road edges, and highway edges, respectively
#
# - Edge data structures:
#   - `side_road_edges` contains a list of 5-tuples that represent the edges
#     of the side roads.  Example: [(0, 0, 0, 1, 1), (0, 0, 1, 0, 1), ...].
#     The 5-tuple is (x1,y1,x2,y2,2), where (x1,y1) is one end of the edge,
#     (x2,y2) is the other end, and w is the weight of the edge.  All values
#     are integers.  This list is sorted.  Note that this only has the edges
#     in one direction, but they are bi-directional edges.
#   - `main_road_edges` has the edges for the main roads, in the same form as
#     the edges for the side roads
#   - `highway_edges` has the edges for the main roads, in the same form as
#     the edges for the side roads
#
# - Node data structures:
#   - `side_road_nodes` contain all the nodes that connect to a side road as a
#     list of 2-tuples; this list is sorted
#   - `main_road_nodes` contain all the nodes that connect to a main road as a
#     list of 2-tuples; this list is sorted
#   - `highway_nodes` contain all the nodes that connect to a highway as a
#     list of 2-tuples; this list is sorted
#   - `all_nodes` contain all the nodes in the graph as a list of 2-tuples;
#     this list is sorted
#
# - Test case data structures:
#   - `num_test_cases` is how many test cases there are
#   - `test_cases` is the test cases themselves, as a list of 4-tuples.
#     Example: [(4, 0, 3, 8), (1, 1, 3, 7), (5, 1, 8, 3)].  Each tuple is of
#     the form (x1,y1,x2,y2), which means that the test case is to find the
#     route from (x1,y1) to (x2,y2).  The tuples in this list are in the
#     order they occur in the input file.


# output() function -- given a list of coordinates (as 2-tuples) and the
# (integer) distance, this function will output the result in the correct
# format for the auto-grader
def output(path,dist):
	print(dist)
	print(len(path))
	for (x,y) in path:
		print(x,y)
	print()



# YOUR CODE HERE

class ProcessingNodes: #attributes of all the nodes
	def __init__(self):
		self.dist = 1000000
		self.done = False
		self.parent = None
		self.index = 0
		self.mainroad = False
		self.highroad = False
		self.coordinate = (-1,-1)
	def getDist(self):
		return self.dist
	def setDist(self,dist):
		self.dist = dist
	def getDone(self):
		return self.done
	def setDone(self):
		self.done = True
	def getParent(self):
		return self.parent
	def setParent(self, parent):
		self.parent = parent
	def getIndex(self):
		return self.index
	def setIndex(self, index):
		self.index = index
	def getMainRoad(self):
		return self.mainroad
	def setMainRoad(self,):
		self.mainroad = True
	def getHighRoad(self):
		return self.highroad
	def setHighRoad(self):
		self.highroad = True
	def getCoordinate(self):
		return self.coordinate
	def setCoordinate(self, item1, item2):
		self.coordinate = (item1, item2)
	def __lt__(self,other):
		return self.getIndex()<other.getIndex()

min_x = min(x for x, y in all_nodes)
max_x = max(x for x, y in all_nodes)
min_y = min(y for x, y in all_nodes)
max_y = max(y for x, y in all_nodes)

width = max_x + min_x + 1
def index(x1,y1): #setting up the indexing mathematics
	value = (x1-min_x) * width + (y1-min_y)
	return value
def unhash(input):
	x_value = input // width + min_x
	y_value = input % width + min_y
	return x_value,y_value

#keep in mind that you will have to call the functions that are not in the init funciton. Might just want to
#group everythin in def so that it gets done quickly and painlessly
class Graph:
	def __init__(self): #creating the empty adjacency matrix nodes. They are set to null if do not exist
		self.SideRoads = [[0] * len(all_nodes) for _ in range(len(all_nodes))] #creating graph class for side roads
		self.MainRoads = [[0] * len(all_nodes) for _ in range(len(all_nodes))]  #creating graph class for main roads
		self.HighRoads = [[0] * len(all_nodes) for _ in range(len(all_nodes))]  #creating graph class for highways
		self.Nodes = []
	# def setup(self): #setting upt the information for the adjacency matrix
		for (x1, y1, x2, y2, w) in side_road_edges: #adjacency matrix for the side nodes
			first = index(x1, y1)
			second = index(x2, y2)
			self.SideRoads[first][second] = w
			self.SideRoads[second][first] = w
		for (x1, y1, x2, y2, w) in main_road_edges: #adjacency matrix for the main nodes
			first = index(x1, y1)
			second = index(x2, y2)
			self.MainRoads[first][second] = w
			self.MainRoads[second][first] = w

		for (x1, y1, x2, y2, w) in highway_edges: #adjacency matrix for the highway nodes
			first = index(x1, y1)
			second = index(x2, y2)
			self.HighRoads[first][second] = w
			self.HighRoads[second][first] = w
	# def constructNodes(self):
		for node in all_nodes:
			item1 = node[0]
			item2 = node[1]
			val = ProcessingNodes()
			val.setCoordinate(item1, item2)
			goshdarn = index(item1, item2)
			# print(goshdarn)
			val.setIndex(goshdarn)
			if node in main_road_nodes:
				val.setMainRoad()
			if node in highway_nodes:
				val.setHighRoad()
			self.Nodes.append(val)
	def getSideRoads(self):
		return self.SideRoads
	def getMainRoads(self):
		return self.MainRoads
	def getHighRoads(self):
		return self.HighRoads
	def findNode(self,x,y):
		tup = (x,y)
		for node in self.Nodes:
			if node.getCoordinate() == tup:
				return node
	def Dijkstra(self, typeOfGraph, start, end, number):
		PQ = []
		heapq.heapify(PQ)
		start_node = self.findNode(start[0], start[1])
		end_node = self.findNode(end[0], end[1])
		start_node.dist = 0
		heapq.heappush(PQ, (0, start_node))
		while len(PQ) > 0:
			current_distance, current_node = heapq.heappop(PQ)
			if current_node.getDone():
				continue
			current_node.setDone()
			if current_node == end_node:
				break
			if current_node.getMainRoad() and (number==1 or number==5):
				end_node = current_node
				break
			if current_node.getHighRoad() and (number==2 or number==4):
				end_node = current_node
				break

			coord = current_node.getCoordinate()
			ind = index(coord[0],coord[1])

			for indexOfNeighbor in range(len(typeOfGraph[ind])):
				if typeOfGraph[ind][indexOfNeighbor] > 0: #making sure that the weight of the edge is greater than zer
					partone, parttwo = unhash(indexOfNeighbor)
					neighbor_node = self.findNode(partone,parttwo)
					neighbor_distance = typeOfGraph[ind][indexOfNeighbor]
					new_distance = current_distance + neighbor_distance

					if new_distance < neighbor_node.getDist():
						neighbor_node.setDist(new_distance)
						neighbor_node.setParent(current_node)
						heapq.heappush(PQ, (new_distance, neighbor_node))
						if neighbor_node.getMainRoad() and (number == 1 or number == 5):
							end_node = neighbor_node
							break
						if neighbor_node.getHighRoad() and (number == 2 or number == 4):
							end_node = neighbor_node
							break
		path = []
		current = end_node
		while current:
			path.append(current.getCoordinate())
			current = current.getParent()
		path.reverse()
		return path, end_node.getDist(), end_node

def setUpDijkstra(input):  #have to validate the type of roads that are being input. The input should be the adjacency matrix based on the type of node start is
	one = input[0]
	two = input[1]
	three = input[2]
	four = input[3]
	start = (one, two)
	end = (three, four)
	graph = Graph() 
	path1, dist1, ending_node = graph.Dijkstra(graph.getSideRoads(), start, end, 1)
	path1.pop()
	# print(path1)

	graph = Graph()
	path2, dist2, ending_node2 = graph.Dijkstra(graph.getMainRoads(), ending_node.getCoordinate(), end, 2)
	path2.pop()
	# print(path2)

	graph = Graph()
	path5, dist5, node_ended_at = graph.Dijkstra(graph.getSideRoads(), end, ending_node2.getCoordinate(), 5)
	path5.pop()
	path5.reverse()
	# print(path5)

	graph = Graph()
	path4, dist4, node_ended_at2 = graph.Dijkstra(graph.getMainRoads(), node_ended_at.getCoordinate(), ending_node2.getCoordinate(), 4)
	path4.pop()
	path4.reverse()
	# print(path4)

	graph = Graph()
	path3, dist3, middle_man = graph.Dijkstra(graph.getHighRoads(), node_ended_at2.getCoordinate(), ending_node2.getCoordinate(), 3)
	path3.reverse()
	# print(path3)

	total_distance = dist1 + dist2 + dist3 + dist4 + dist5
	final_path = path1 + path2 + path3 + path4 + path5
	
	output(final_path, total_distance)
#note that the input for this is not defined well

##NEED TO SETUP HOW TO ACTUALLY CALL SETUPDIJKSTRA AND STUFF FOR INPUTS AND ENDS PONTS
def main():
	for test_case in test_cases:
		graph = Graph()
		setUpDijkstra(test_case)


if __name__ == "__main__":
	main()

#have to process the lists that are outputs of the function, will always go through the five nodes
