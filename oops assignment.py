class power():
    def __init__(self,x,n):
        self.x=x
        self.n=n
    def topower(self):
        return self.x ** self.n
obj1=power(10,2)
obj2=power(20,3)
print(obj1.topower())
print(obj2.topower())