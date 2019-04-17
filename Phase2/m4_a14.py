class Box:
    def getVolume(self):
        vol= self.length*self.breadth* self.height
        return vol
    def __init__(self, length, breadth,height):
        self.length = length
        self.breadth = breadth
        self.height = height
 
class BigBox(Box):
    def __init__(self, length, breadth,height):
        Box.__init__(self,length,breadth,height)
 
    def getCapacity(self, sBox):
            sVol = sBox.getVolume()
            capacity = self.getVolume()/sVol
            return int(capacity)
smallBox = Box(1,1,1)
bigBox = BigBox(4,4,4)
capacity = bigBox.getCapacity(smallBox)
print(capacity)
