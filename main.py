from typing import List, Dict  # For annotations

import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

class Node:
    def __init__(self, arg_id):
        self._id = arg_id

    @property
    def id(self):
        return self._id


class LabTwo:
    # solving first lab
    def __init__(self):
        self.myFile = open("grafpond.in")
        self.vert, self.edges = self.findEV()
        self.graph = []
        self.mydict = {}
        self.graph, self.mydict = self.readForm()

    def PrimFast(self) -> int:
        # Priority queue is implemented as a dictionary with
        # key as an object of 'Node' class and value as the cost of
        # reaching the node from the source.
        # Since the priority queue can have multiple entries for the
        # same adjacent node but a different cost, we have to use objects as
        # keys so that they can be stored in a dictionary.
        # [As dictionary can't have duplicate keys so objectify the key]

        # The distance of source node from itself is 0. Add source node as the first node
        # in the priority queue
        priority_queue = {Node(1): 0}
        added = [False] * (len(self.mydict) + 10)
        min_span_tree_cost = 0

        while priority_queue:

            # Choose the adjacent node with the least edge cost
            node = min(priority_queue, key=priority_queue.get)

            cost = priority_queue[node]

            # Remove the node from the priority queue
            del priority_queue[node]

            if not added[node.id]:
                min_span_tree_cost += cost
                added[node.id] = True
                print("Added Node : " + str(node.id) + ", cost now : " + str(min_span_tree_cost))

                for item in self.mydict[node.id]:
                    adjnode = item[0]
                    adjcost = item[1]
                    if not added[adjnode]:
                        priority_queue[Node(adjnode)] = adjcost

        return min_span_tree_cost

    def findEV(self):
        line = self.myFile.readline().split()
        return int(line[0]), int(line[1])

    def readForm(self):
        r = []
        d = {i: [] for i in range(1, self.vert + 1)}

        for i in range(self.edges):
            line = self.myFile.readline().split()
            a, b, c = int(line[0]), int(line[1]), int(line[2])
            r.append([a, b, c])
            r.append([b, a, c])
            r.sort(key=lambda x: x[2])
            d[a].append((b, c))
            d[b].append((a, c))
        return r, d

    def find(self, parent, i):
        # return recursively root of roots from quick-union
        # https://www.cs.duke.edu/courses/cps100e/fall09/notes/UnionFind.pdf
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        # weighted tree of quick-union
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # attach smaller tree to bigger tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            # increment as to keep track of size
            rank[xroot] += 1

    def KruskalFast(self):
        output = []
        parent = []
        rank = []
        i, e = 0, 1

        # initialize to fit nodes in array/ rank
        for node in range(self.vert + 1):
            parent.append(node)
            rank.append(0)

        # while for all nodes to be visited
        while e < self.vert:
            # picks edges in ascending order
            a, b, weight = self.graph[i]
            i += 1
            x = self.find(parent, a)
            y = self.find(parent, b)

            # one way of saying: they won't form a cycle
            # or if they belong to different sets
            if x != y:
                e += 1
                output.append([a, b, weight])
                self.union(parent, rank, x, y)

        for u, v, weight in output:
            print(u, '-', v, '@', weight)

        return output

    def MSTprinter(self, output = [[]]):
        for u, v, weight in output:
            print(u, '-', v, '@', weight)
    def KruskalSecBest(self):
        # just CROSS OUT from big graph an EDGE, one by one, present in MST (solved w/ Krsukal at the beginning)
        mySolution = sys.maxsize
        myVec = []
        blockPrint()
        MST = self.KruskalFast()
        enablePrint()
        blockPrint()
        for MSTEdge in MST:
            node1, node2, dist = MSTEdge[0],MSTEdge[1],MSTEdge[2]
            # find first edge with given spec, second will be the one right after
            # you may use same e1 after popping to remove both of them
            e1 = self.graph.index([node1,node2,dist])

            # e2 = e1 + 1
            self.graph.pop(e1)
            self.graph.pop(e1)


            reCalcMST = self.KruskalFast()
            totalCost = [sum(i) for i in zip(*reCalcMST)]
            print("Total Cost:", totalCost[2])

            if mySolution != min(totalCost[2], mySolution):
                myVec = reCalcMST

            mySolution = min(totalCost[2], mySolution)
            print('^', '-'*20)
            self.graph.insert(e1,[node1,node2,dist])
            self.graph.insert(e1 + 1, [node2, node1, dist])
        enablePrint()
        print("1st:")
        self.MSTprinter(MST)
        print('^' * 20)
        print("2nd:")
        self.MSTprinter(myVec)
        print(mySolution)



    def KruskalFastEdgesConstrained(self, arr=[[]]):
        output = []
        parent = []
        rank = []
        i, e = 0, 1

        # initialize to fit nodes in array/ rank
        for node in range(self.vert + 1):
            parent.append(node)
            rank.append(0)

        # boiler/ just go through arr and and find/union the nodes
        for a, b in arr:
            x = self.find(parent, a)
            y = self.find(parent, b)

            # one way of saying: they won't form a cycle
            # or if they belong to different sets
            if x != y:
                e += 1
                output.append([a, b, "Unknown"])
                self.union(parent, rank, x, y)

        # while for all nodes to be visited
        while e < self.vert:
            # picks edges in ascending order
            a, b, weight = self.graph[i]
            i += 1
            x = self.find(parent, a)
            y = self.find(parent, b)

            # one way of saying: they won't form a cycle
            # or if they belong to different sets
            if x != y:
                e += 1
                output.append([a, b, weight])
                self.union(parent, rank, x, y)

        self.MSTprinter(output)

        return output


if __name__ == "__main__":
    X = LabTwo()
    # print("🦅 Prim ElogE:")
    # X.PrimFast()
    # print("🦅 Kruskal MlogN:")
    # X.KruskalFast()
    print('*', '-' * 15)
    print("🦅 Kruskal Second Best O(VE):")
    X.KruskalSecBest()
    # print('*','-'*15)
    # print("🦅 Kruskal MlogN with constrained edges:")
    # myArr = [[1,4],[2,3],[5,2]]
    # X.KruskalFastEdgesConstrained(myArr)
