# x = 10
# nameOfClass = "Roadmap to computing"
# def reverseString(message):
#     
#     return message[::-1]
#         
# print(reverseString(nameOfClass))
#Slice is string [start:end:step]
#by doing this it takes the whole string and returns incriments by 1 which reverses the string.
#-----------------------------------------------------------------------------------------------------
import turtle
passMe = turtle.Turtle()
def drawColoredTriangle(t, length, color):
    t.color(color)
    for i in range(3): 
        t.fd(length)
        t.lt(120)
        
        
drawColoredTriangle(passMe, 100, "purple")

#range(how many times you want it to loop)
# i can be called anything it is just there for interations
#------------------------------------------------------------------------------------------------------