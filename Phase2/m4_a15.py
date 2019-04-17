class Actor:
    def talk(self):
        print("can talk")
class TennisPlayer(Actor):
    def talk(self):
        print("Tennis Player", end=" ")
        super().talk()
class Professor(Actor):
    def talk(self):
        print("Professor", end=" ")
        super().talk() 
class Shopkeeper(Actor):
    def talk(self):
        print("Shopkeeper", end=" ")
        super().talk() 
class Carpenter(Actor):
    def talk(self):
        print("Carpenter", end=" ")
        super().talk()
a=TennisPlayer()
b=Professor()
c=Shopkeeper()
d=Carpenter()
a.talk()
b.talk()
c.talk()
d.talk()
