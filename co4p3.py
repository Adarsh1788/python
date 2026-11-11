#create a class rectangle with private attributes length and width. overload"<"operator compare the area of the rectangle
class rectangle:
    def __init__(self):
        self.__length = int(input("enter the length of rectangle: "))
        self.__breadth= int(input("enter the breadth of the rectangle: "))
    def __lt__(ob1,ob2):
       area1=ob1.__length*ob1.__breadth
       area2=ob2.__length*ob2.__breadth
       print("area of the rectangle is : ",area1)
       print("area of the rectangle is : ",area2)
       return area1>area2
print("enter the length and breadth of first object: ")
ob1 = rectangle()
print("enter the length and breadth of second object: ")
ob2 = rectangle()
if(ob1<ob2):
    print("rectangle1  is less then rectangle2 ")
else:
    print("rectangle1  is less than or equal to rectangle2")