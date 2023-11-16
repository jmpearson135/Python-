



#takes in x as an input and does the next lines of code to square x and add ten then returns the answer.
# def iSquaredPlusTen(x):
#     result = x ** 2 + 10
#     return result
# #which you can then print out or do whatever you want with it.
# 
# def areaOfRectangle(w, h):
#     return w * h


# def hello(name):
#     print("Welcome", name)

# def oddCount(listOfNumbers):
#     count = 0
#     for i in listOfNumbers:
#         if i % 2 == 1:
#             count += 1
#     return count
#     
             
# def FooBar(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FooBar")
#         elif i % 3 == 0:
#             print("Foo")
#         elif i % 5 == 0:
#             print("Bar")
#         else:
#             print(i)



# *****will most likely be on midterm.*******
import turtle
donny = turtle.Turtle()

def triangle(t, sideLength):
    for i in range(3):
        t .fd(sideLength)
        t.lt(120)
        
def threeTriangles(t):
    for i in range(3):
        triangle(t, 200)
        t.rt(120)
        
    
threeTriangles(donny)

