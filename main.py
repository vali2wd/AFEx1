class LabTwo:
#solving first lab
    def __init__(self):
        print("here")
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

    # def KruskalSlow(self):
    #     self.dic.

X = LabTwo()
print(X.graph)
