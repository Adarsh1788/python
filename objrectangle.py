class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    def perimeter(self):
        p=2*(self.l+self.b)
        print("perimeter of rectangle is:",p)
    def compare(self,obj2):
        try:
            if obj1.area()==obj2.area():
                print("Both areas are equal")
            elif onj1.area()>obj2.area():
                print("Area of rectangle1 is greater than Rectangle2")
            elif obj1.area()<obj2.area():
                print("area of rectangle1 is less than rectangle 2")
        except:
            print("cant be compared")
l1=int(input("Enter the length of first rectangle:"))
b1=int(input("Enter the breadth of first rectangle:"))
l2=int(input("Enter the length of second rectangle:"))
b2=int(input("Enter the breadth of second rectangle:"))
obj1=rectangle(l1,b1)
obj2=rectangle(l2,b2)
print("Area of Rectangle1",obj1.area())
print("Area of Rectangle2",obj2.area())
obj1.compare(obj2)
