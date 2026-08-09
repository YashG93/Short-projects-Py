
class shape():

    def area(self):
        return 0
    
class square(shape):

    def __init__(self,n):
        self.n=n

    def area(self):
        return self.n**2

sh=shape()
sq=square(5)
print(sq.area())
print(sh.area())