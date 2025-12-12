import math

def area_circle(r):
    return math.pi*r*r

def area_squre(l):
    return l*l

def area_rectangle(l, b):
    return l*b

if __name__=="__main__":
    print("area of circle=",area_circle(5))
    print("area of squre=",area_squre(4))
    print("Area of rectangle=",area_rectangle(2,3))
