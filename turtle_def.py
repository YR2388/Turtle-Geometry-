from turtle import *
import math
import random

#samples
      
def arcl(r, deg):
    """ something"""
    for i in range(deg):
        speed(100)
        if i % 2 == 0:
            color('blue')
        else:
            color('red')
            forward(r)
            left(1)

def arcr(r, deg):
    for i in range(deg):
        forward(r)
        right(1)

def moveforward():
    forward(100)
    right(90)
    forward(150)
    left(45)
    back(100)

def house1(size):
    square(size)
    triangle(size)


def turnright():
    right(90)
        

def inspi(side, angle, inc):
    forward(side)
    right(angle)
    inspi(side, (angle + inc) % 360 , inc)

#Chapter one

def triangle(size):
    """We can use this function to draw a triangle. The for loops help us repeat a block of code multiple times. In this function, we are repeating the forward and right procedurs three times. Since the angle is 120 degree, it will end up with an equilateral triangle. """
    for i in range (3):
        forward(size)
        right(120)
        """The right function let the turtle turn to the right in a certain degree. You might ask that, for a equilateral triangle, the angle should be 60 degree instead of 120 degree. The reason is that whenever you turn x degrees, the internal angle of the triangle will be 180-x degree"""
        
def square(size):
    """We can call this function to draw a square for us. """
    """Square is the name of this function and size is the only parameter in this function."""
    """ The trick used in this function is called iteration, which is the for loop showed in the code"""
    for i in range(4):
        forward(size)
        right(90)

def squarepiece(size):
    forward(size)
    right(90)

def squaretrick2(size):
    for i in range (4):
        squarepiece(size)

def house(size):
    """The house function can help us draw a house figure. The size is the only parameter of this function. """
    square(size)
    """We use the square function, which is coded above, to simplify our procedures. """
    forward(size)
    """The value of size should be assigned while calling the function"""
    right(30)
    triangle(size)
    """This is the triangle function we've coded before. You don't need to worry about the parameter if you have assigned a value while calling the function"""

def Thing():
    """This program will create a doodle so that we can use it to create more complex figures."""
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(100)
    right(90)
    forward(25)
    right(90)
    forward(25)
    right(90)
    forward(50)

def Thing1():
    """This is our first attempt to draw a relatively complex figure by using the Thing() function. """
    for i in range(4):
        """It will execute the Thing() function four times. """
        Thing()



def Thing2():
    """This is our second attempt to draw a relatively complex figure by using the Thing() function. The while loop here help the create a infinite loop. Specifically, since the boolean parameter is true, the while loop will never come to an end. """
    while True:
        Thing()
        right(10)
        forward(50)

def Thing3():
    """This is our third attempt to draw a relatively complex figure by using the Thing() function. Similarly, the while loop functions as an infinite loop. """
    while True:
        Thing()
        left(45)
        forward(100)

def tryangle(size):
    for i in range (3):
        forward(size)
        right(60)

def circle():
    """Inspired by the Thing() function above, we can draw a circle with a turtle by moving one step each time. Additionally, this function gives us a 360-side polygon with 64440 degrees. """
    while True:
        forward(1)
        right(1)

def circleoption():
    """An alternative way of drawing a circle. While playing with the turtle, we find out that the turtle will close after it turns 360 degrees. So if we set up a for loop function with range of 360, the turtle will close after 360 times of computation. """
    for i in range(360):
        forward(1)
        right(1)
  
def carditianrectangle (width, height):
    """This is an alternative way of drawing a rectangle. We can use the setpos method to move the turtle to any carditian point in the plane. The width stands for the units on x-axis and height stands for the units on y-axis."""
    setpos(width, 0)
    setpos(width, height)
    setpos(0, height)
    setpos(0, 0)

def circles():
    """Use the arcr function above to draw multiple circles"""
    for i in range(9):
        arcr(1, 360)
        right(40)

def petal(size):
    arcr(size, 60)
    right(120)
    arcr(size, 60)
    right(120)

def flower(size):
    arcr(size, 60)
    right(120)
    arcr(size, 60)
    right(120)

def ray(r):
    for i in range(2): 
        arcl(r, 90)
        arcr(r, 90)

def sun(size):
    for i in range(9):
        ray(size)
        right(160)

def newpoly(side, angle):
    """poly that changes its angle in time"""
    while True:
        forward(side)
        right(angle)
        forward(side)
        right(2 * angle)
        

def poly(side, angle):
    """process for constructing a poly"""
    while True:
        forward(side)
        right(angle)
    

def polyspi(side, angle):
    """poly examples for recursion"""
    forward(side)
    right(angle)
    polyspi(side + 1, angle)

def polyspi2(side, angle, inc):
    """recursion example that changes its input continuously""" 
    forward(side)
    right(angle)
    polyspi2(side + inc, angle, inc)

def inspi(side, angle, inc):
    """this function provides us a curve of increasing curvature"""
    while True:
        forward(side)
        right(angle)
        angle = angle + inc
       
    


def polystop(side, angle):
     """poly function that have stop rule"""
     turn = 0
     while turn % 360 == 0:
         forward(side)
         right(angle)
         turn = turn + angle

def inspistop(side, startangle, endangle, inc):
    """an increasing curvatur with stop sign"""
    while startang == endang:
        forward(side)
        left(startang)
        startang = startang + inc


def polyarc(side, bottom, top):
    while True:
        inspistop(side, bottom, top, 1)
        inspistop(side, top, bottom, -1)

def lcm(a, b):
    """This formula shows us the symmetry of a poly"""
    n = 0
    multiple = a
    while multiple % b != 0:
        n = n + 1
        multiple = n * a
    return multiple

def randommovement (a, b, c, d):
    while True:
        value1 = random.randint(a, b)
        value2 = random.randint(c, d)
        left(value1)
        forward(value2)

        
 
    
    
    

def outofbounds(turtle):
    if turtle.xcor() >= window_width()/2 or turtle.ycor() >= window_height()/2:
        return True
    else:
        return False

def checkforward(distance, turtle):
    turtle.hideturtle()
    a = turtle.pos()
    turtle.penup()
    turtle.forward (distance)
    if (outofbounds(turtle) == True):
        turtle.setpos(a)
    else:
        turtle.pendown()
        turtle.forward(distance)
"""boolean that describe whether the turtle has hitted the wall or not"""
def stuck(turtle):
    
    if turtle.xcor() >= window_width()/2 or turtle.ycor() >= window_height()/2:
        return True
    else:
        return False
    
def randommove2(a, b, c, d, turtle):
    while True:
        turtle.left (random.randint(a, b))
        distance = random.randint(c, d)
        checkforward(distance, turtle)
        if stuck(turtle):
            turtle.left (180)

def size(turtle):
    print(window_width())
    print(turtle.xcor())
    print(window_height())
    turtle.forward(340)
    print(turtle.xcor())
    print(turtle.ycor())
    print(turtle.pos())


def wriggle():
    while stuck:
        turtle.right(1)
        checkforward(1)



def smell(turtle, lastdistance, currentdistance):
    if (lastdistance > currentdistance):
        return False
    else:
        return True
    

def findbysmell1(foodx, foody, turtle):
    while True:
        k = turtle.pos()
        turtle.forward(10)
        lastdistance = turtle.distance(k)
        currentdistance = turtle.distance(foodx, foody)
        if smell(turtle, lastdistance, currentdistance) == True:
            turtle.right(10)

def findbysmell2(foodx, foody, turtle, turn):
    while True:
        lastdistance = turtle.distance(foodx, foody)
        turtle.forward(1)
        currentdistance = turtle.distance(foodx,foody)
        if smell(turtle, lastdistance, currentdistance) == True:
            turtle.right(turn)

def findbysmell3(randomx, randomy, randomturn, smellturn, foodx, foody, turtle):
    while True:
        lastdistance = turtle.distance(foodx, foody)
        turtle.left(random.randint(-randomturn, randomturn))
        turtle.forward(random.randint(randomx, randomy))
        currentdistance = turtle.distance(foodx, foody)
        if smell(turtle, lastdistance, currentdistance) == True:
            turtle.right(smellturn)

def factor(turtle, foodx, foody):
    return 1/turtle.distance(foodx, foody)

def varystep(side, angle, turtle, foodx, foody):
    turtle.speed(10000)
    while True:
        turtle.forward(factor(turtle, foodx, foody) * side)
        left(angle)

def varyturn(side, angle, turtle, foodx, foody):
    turtle.speed(10000)
    while True:
        turtle.forward(side)
        turtle.left(factor(turtle, foodx, foody)*anlge)

def toward(turtle , foodx, foody):
    a = foodx - turtle.xcor()
    b = foody - turtle.ycor()
    if a > 0:
        return math.atan(b/a)
    elif a < 0:
        return math.radians(180) + math.atan(b/a)
    else:
        return math.radians(90) * b/abs(b)

def bearing(turtle, foodx, foody):
    return toward(turtle, foodx, foody) - math.radians(turtle.heading())



def righteye(turtle, foodx, foody):
    if bearing(turtle, foodx, foody) > 5.23599:
        return True
    elif bearing(turtle, foodx, foody) < 0.174533:
        return True
    else:
        return False

def lefteye(turtle, foodx, foody):
    if bearing(turtle, foodx, foody) > 6.10865:
        return True
    elif bearing(turtle, foodx, foody) < 1.0472:
        return True
    else:
        return False


def headforpoint(turtle, foodx, foody):
    while True:
        if lefteye(turtle, foodx, foody) or righteye(turtle, foodx, foody):
            turtle.forward(1)
        else:
            turtle.left(10)


def intensity(turtle, stronglevel, foodx, foody):
    return math.cos(bearing(turtle, foodx, foody))*(stronglevel/math.pow(turtle.distance(foodx, foody),2))

def intensitylefteye(turtle, stronglevel, foodx, foody):
    if (lefteye(turtle, foodx, foody)) == False:
        return 0
    else:
        factor = stronglevel/math.pow(turtle.distance(foodx, foody),2)
        angle = bearing(turtle, foodx, foody) - 45
        return (factor * math.cos(angle))

def intensityrighteye(turtle, stronglevel, foodx, foody):
    if righteye(turtle, foodx, foody) == False:
        return 0
    else:
        factor = stronglevel/math.pow(turtle.distance(foodx, foody),2)
        angle = bearing(turtle, foodx, foody)-45
        return (factor * math.cos(angle))
    
def findbysource(turtle, stronglevel, foodx, foody):
    while True:
        turtle.forward(1)
        if intensitylefteye(turtle, stronglevel, foodx, foody) > intensityrighteye(turtle, stronglevel, foodx, foody):
            turtle.left(10)
        else:
            turtle.right(10)
def prey(turtle1, speed, turn):
    turtle1.forward(speed)
    turtle1.right(turn)

def predator(turtle2, speed, turn):
    turtle2.forward(speed)
    if smell(turtle2, lastdistance, currentdistance) == True:
        turtle2.right(turn)

def predatorandprey(turtle1, speed1, turn1, turtle2, speed2, turn2, preyx, preyy, ):
    while True:
        prey(turtle1, speed1, turn1)
        preyx = turtle1.xcor()
        preyy = turtle1.ycor()
        lastdistance = turtle2.distance(preyx, preyy)
        turtle2.forward(speed2)
        currentdistance = turtle2.distance(turtle1.pos())
        if smell(turtle2, lastdistance, currentdistance) == True:
            turtle2.right(turn2)
        


       
def okok(turtle1, turtle2):
    turtle1.forward(10)
    print(turtle2.distance(turtle1))
    turtle1.forward(100)
    turtle1.right(30)
    turtle1.forward(50)
    turtle2.setheading(turtle2)
   
def face(turtle1, turtle2):
    turtle1.right(math.radians(bearing(turtle1, turtle2.xcor(), turtle2.ycor()))+90)


         
def follow(turtle1, turtle2):
    face(turtle1, turtle2)
    turtle1.forward(1)



    
def eqspi(turtle1, side, angle, scale):
    turtle1.forward(side)
    turtle1.left(angle)
    eqspi(side * scale, angle, scale)

def chamber(base, s1, s2, a1, a2, turtle1):
    lowerleft = turtle1.position()
    turtle1.forward(base)
    turtle1.left(a2)
    turtle1.forward(s2)
    upperright = turtle1.position()
    upperright1 = turtle1.heading()
    turtle1.penup()
    turtle1.setpos(lowerleft)
    turtle1.pendown()
    turtle1.left(a1)
    turtle1.forward(s1)
    
def spiralgrowth(base, s1, s2, a1, a2, turtle1):
    lowerleft = turtle1.position()
    turtle1.forward(base)
    turtle1.left(a2)
    turtle1.forward(s2)
    upperright = turtle1.position()
    upperright1 = turtle1.heading()
    turtle1.penup()
    turtle1.setpos(lowerleft)
    turtle1.pendown()
    turtle1.left(a1)
    turtle1.forward(s1)
    turtle1.setheading(upperright1)
    nextbase = turtle1.distance(upperright)
    r = nextbase/base
    spiralgrowth(nextbase, s1*r, s2*r, a1, a2,turtle1)
    
def branch(length, turtle1):
    turtle1.forward(length)
    turtle1.left(45)
    branch(length/2, turtle1)
    turtle1.right(90)
    branch(length/2, turtle1)

def branch1(length, level, turtle1):
    if level > 0:
        turtle1.forward(length)
        turtle1.left(45)
        branch1(length/2, level-1, turtle1)
        turtle1.right(90)
        branch1(length/2, level-1, turtle1)

def node(length, anlge, level, turtle1):
    turtle1.left(angle)
    lbranch(length, angle, level-1, turtle1)
    turtle1.right(2 * angle)
    rbranch(length, angle, level-1, turtle1)
    turtle1.left(angle)

def lbranch(length, angle, level, turtle1):
    turtle1.forward(2 * length)
    node(length, angle, level, turtle1)
    turtle1.back(2 * length)

def rbranch(length, angle, level, turtle1):
    turtle1.forward(length)
    node(length, angle, level, turtle1)
    turtle1.back(length)
    
def nestedtriangle(size, turtle1):
    i = 0
    if size > 10:
        while i < 3:
            nestedtriangle(size/2, turtle1)
            turtle1.forward(size)
            turtle1.right(120)
            i = i + 1

def cornertri(size, turtle1):
    i = 0
    if size > 10:
        while i < 3:
            turtle1.forward(size)
            cornertri(size/2, turtle1)
            turtle1.right(120)
            i = i+1

def insert(size, turtle1):
    turtle1.left(120)
    outwardtri(size/2, turtle1)
    turtle1.right(120)



def outwardtri(size, turtle1):
    i = 0
    if size>10:
        while i < 3:
           turtle1.forward(size/2)
           insert(size, turtle1)
           turtle1.forward(size/2)
           turtle1.right(120)
           i = i + 1

        







