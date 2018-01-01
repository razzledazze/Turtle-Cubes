#cubes

from turtle import Turtle
colours = ['#ff0000','#ffa500','#ffff00','#003300','#000033','#11051b','#2a2a2a'] #each of the three arrays is a shade of the
colours2 = ['#cc0000','#cc8400','#cccc00','#006600','#000066','#220a37','#545454'] #relevant colour (6 rainbow colours with a shade
colours3 = ['#990000','#996300','#999900','#009900','#000099','#330f53','#7e7e7e'] #for each, and three shades of grey)

while True: #runs until a valid option is chosen
    try:
        temp = input("Enter R for rainbow of G for grey: ")[0].lower() #takes choice
    except:
        temp = "b" #arbitrary value to set it to
    if temp == "r":
        rainbow = True
        break
    elif temp == "g":
        rainbow = False
        break

def cube(startx,starty,colno): #takes in start coords and the colour number
    c = Turtle() #makes turtle
    c.hideturtle() #hides it
    c.penup()
    c.goto(startx,starty) #goes to aforementioned start coords
    c.speed(0) #no animation
    c.right(30)
    

    c.color(colours[colno]) #first shade (index from first array)
    c.begin_fill() #starts filling
    for i in range(6): #main 'honeycomb' shape outline
        c.left(60)
        c.forward(50)
    c.end_fill()
        
    c.left(120)
    c.forward(100)

    c.color(colours2[colno]) #second shade for second visible face
    c.begin_fill()
    c.right(180)
    c.forward(50)
    c.left(120)
    c.forward(50)
    c.end_fill()


    c.backward(50)
    c.left(60)
    c.forward(50)
    c.begin_fill()
    c.left(180)
    c.forward(50)
    c.right(120)
    c.forward(50)
    c.end_fill()

    c.color(colours3[colno]) #third shade for final face
    c.begin_fill()
    c.backward(50)
    c.left(120)
    c.forward(50)
    c.right(120)
    c.forward(50)
    c.end_fill()

def cubeB(startx,starty,colno): #different one for going down as otherwise the top will cover the above cube
    c = Turtle()
    c.penup()
    c.hideturtle()
    c.goto(startx,starty)
    c.speed(0)
    c.left(30)

    c.color(colours[colno])
    c.begin_fill()
    c.forward(50)
    c.left(60)
    c.forward(50)
    c.left(120)
    c.forward(50)
    c.left(60)
    c.forward(50)
    c.end_fill()

    c.color(colours3[colno])
    c.begin_fill()
    c.right(120)
    c.forward(50)
    c.right(60)
    c.forward(50)
    c.right(120)
    c.forward(50)
    c.right(60)
    c.forward(50)
    c.end_fill()
    

x = 0 #start coords begin at the origin 
y = 0
if rainbow == True: #if the user wants it multicoloured:
    colno = 0 #first index in the colour arrays
else:
    colno = 6 #otherwise, last index (grey shades)
cube(x,y,colno) #draws inital cube of the first colour (or grey) at the origin

while True:
    if rainbow == True:
        colno += 1 #goes to next available colour
        if colno == 6: #goes to the start of the colour array if it's at the end
            colno = 0
    else:
        colno = 6 #if grey is chosen the index is always 6 as this is the shades of grey
    
    option = input("[U for up] [D for down] [L for left] [R for right]: ") #user choice of direction to place next cube
    try:
        if option[0].lower() == "u":
            y += 50 #adjusts the coordinates accordingly
            cube(x,y,colno) #draws cube with new coords and colour
        elif option[0].lower() == "d":
            y -= 50
            cubeB(x,y,colno)
        elif option[0].lower() == "l":
            y -= 25
            x -= 42.5
            cube(x,y,colno)
        elif option[0].lower() == "r":
            y -= 25
            x += 42.5
            cube(x,y,colno)
        else:
            print("\nEnter a valid option\n") #if the user hasn't chosen an option from the list
    except:
        print("\nEnter a valid option\n") #or they have entered something that would throw up an error (e.g. a number which would error at .lower())

        
        
    
    
    
