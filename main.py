class LabTwo:
    #solving first lab
    def __init__(self):
        self.myFile = open("grafpond.in")
        self.vert, self.edges = self.findEV()
        self.graph = []
        self.graph = self.readForm()

    def findEV(self):
        line = self.myFile.readline().split()
        return int(line[0]), int(line[1])

    def readForm(self):
        r = []
        for i in range(self.edges):
            line = self.myFile.readline().split()
            a,b,c = int(line[0]), int(line[1]), int(line[2])
            r.append([a,b,c])
            r.append([b,a,c])
            r.sort(key= lambda x: x[2])
        return r

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

        #initialize to fit nodes in array/ rank
        for node in range(self.vert + 1):
            parent.append(node)
            rank.append(0)

        #while for all nodes to be visited
        while e < self.vert:
            # picks edges in ascending order
            a, b, weight = self.graph[i]
            i += 1
            x = self.find(parent, a)
            y = self.find(parent, b)

            # one way of saying: they won't form a cycle
            if x != y:
                e += 1
                output.append([a,b,weight])
                self.union(parent, rank, x, y)

        for u, v, weight in output:
            print(u, '-', v, '@', weight)

        return output


X = LabTwo()
X.KruskalFast()
