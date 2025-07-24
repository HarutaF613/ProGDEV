class Car:
    def __init__(self,name,color,size,conpany):
        self.name = name
        self.color = color
        self.size = size
        self.conpany = conpany
    
    def info(self):
        print("{} \n color : {} \n size : {} \n company : {}".format(self.name,self.color,self.size,self.conpany))
        print("")

n1 = Car("Civix","Red","Compact","Honda")
n2 = Car("Corolla","White","Compact","Toyota")
n3 = Car("ModelS","Black","Full-Size","Tesla")
n4 = Car("CX-5","Blue","Mid-Size","Mazda")
n5 = Car("Q5","Silver","Mid-Size","Audi")
n6 = Car("Mustang","Yellow","Sport","Ford")
n7 = Car("LanddCruiser","Green","Full-Size","Toyota")

n1.info()
n2.info()
n3.info()
n4.info()
n5.info()
n6.info()
n7.info()