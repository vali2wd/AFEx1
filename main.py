class LabTwo:
#sa bag un cod
#si alt comment
#third comment
#fourth comment
    def __init__(self):
        self.myFile = open("grafpond.in")
        self.vert, self.edges = self.findEV()
        self.dic ={}
        self.dic = self.readForm(self.dic)

    def findEV(self):
        line = self.myFile.readline().split()
        return int(line[0]), int(line[1])


    def readForm(self, myDict = {}):
        myDict = {c:[] for c in range(1, self.vert + 1)}
        for i in range(self.edges):
            line = self.myFile.readline().split()
            a,b,c = int(line[0]), int(line[1]), int(line[2])
            myDict[a].append([b,c])

        return myDict

X = LabTwo()
print(X.dic)
