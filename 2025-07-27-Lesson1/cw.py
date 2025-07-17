class Fruit:
    def __init__(self,name,taste,color):
        self.name = name
        self.taste = taste
        self.color = color
    
    def info(self):
        print("{} is {} and {}".format(self.name,self.color,self.taste))

apple = Fruit("apple","fresh","red")
apple.info()

banana = Fruit("banana","yummy","yellow")
banana.info()