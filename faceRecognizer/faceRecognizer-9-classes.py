class Rectangle: 
    def __init__(self,c, w, l): # a method
        self.width = w
        self.length = l
        self.color = c 
    
    def area(self):
        self.area = self.width * self.length
        return self.area

c1 = 'red'
w1 = 3
l1 = 6
rec1 = Rectangle(c1, w1, l1)
areaRec = rec1.area()
print('Rec1 = ', rec1.color, rec1.length, areaRec)
