import tkinter
from tkinter import Canvas, Label, Menu, Scale, messagebox , filedialog
from functools import partial
from tkinter.constants import ALL, CENTER, HORIZONTAL
import turtle
#import pyautogui


x = 1
fullScreen = False
bgColors = ['Black','White']
penColors = ['Violet','Blue','Green','Yellow','Red','White','Black']
FONT = ('Arial', 10, 'normal')

def drag_handler(x, y):
    locator.ondrag(None)
    marker.undo()
    marker.write((x, y),align='left',font=FONT)
    locator.setheading(locator.towards(x, y))  # head towards new location
    locator.setposition(x, y)
    locator.ondrag(drag_handler)


def openFileDialog():
    fileName = filedialog.askopenfilename(initialdir="C:/Users/Lenovo/Documents" , title="Open New Source File" , filetypes = [("python files" , "*.py")])

def setBgColor(color):
    drawingCanvas.config(bg=color)
    if color == "White":
        locator.color("black")
        marker.undo()
        marker.color("black")
        marker.write(locator.position(),align='left',font=FONT)
    else:
        locator.color("white")       
        marker.undo()
        marker.color("white")
        marker.write(locator.position(),align='left',font=FONT)

def setPenColor(color):
    t.pencolor(color)

def setPenSpeed(speed):
    t.speed(speed)

def toggleFs(*args):
    global fullScreen,fileMenu
    if(fullScreen):
        fullScreen = False
        fileMenu.entryconfigure(8,label="Enter FullScreen")
        root.attributes("-fullscreen" , fullScreen)
        root.geometry("%dx%d+0+0" % (root.winfo_screenwidth(),root.winfo_screenheight()))
    else:
        fullScreen = True
        fileMenu.entryconfigure(8,label="Exit FullScreen")
        root.attributes("-fullscreen" , fullScreen)
 
def draw(*args):
    root.unbind("<f>")
    global x
    t.circle(5*x)
    t.circle(-5*x)
    t.left(90)
    t.circle(5*x)
    t.circle(-5*x)
    t.right(90)
    x = x+1
    root.bind("<f>" , draw)

# def setPenSpeed():
#     dialogBox = tkinter.Tk()
#     dialogBox.title("Set Pen Speed")
#     dialogBox.geometry("300x125")
#     widthScale = Scale(master=dialogBox , from_=0 , to=10 , resolution=1 , orient=HORIZONTAL , length=150 ,highlightthickness=0)
#     widthScale.pack()
#     Label(master=dialogBox , text="Speed 0 is NO ANIMATION").pack()
#     Label(master=dialogBox , text="1 (Min Speed) ... 10 (Max Speed)").pack()

root  = tkinter.Tk()
root.title("Animations 6969")
root.attributes("-fullscreen" , fullScreen)
root.geometry("%dx%d+0+0" % (root.winfo_screenwidth(),root.winfo_screenheight()))

commandMenu = tkinter.Menu(root)

# FILE MENU
fileMenu = tkinter.Menu(master=commandMenu , tearoff=0)
fileMenu.add_command(label="New File")
fileMenu.add_separator()
fileMenu.add_command(label="Open File" , command = openFileDialog)
fileMenu.add_cascade(label="Open Recents")
fileMenu.add_separator()
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save As...")
fileMenu.add_separator()
fileMenu.add_command(label="Enter FullScreen" , command=toggleFs)
fileMenu.add_command(label="Exit A.6969" , command=root.destroy)

#EDIT MENU
editMenu = tkinter.Menu(master=commandMenu,tearoff=0)

colorsBgMenu = tkinter.Menu(master=editMenu , tearoff=0)
for color in bgColors:
    colorsBgMenu.add_command(label=color , command=partial(setBgColor,color))
colorsPenMenu = tkinter.Menu(master=editMenu,tearoff=0)
for color in penColors:
    colorsPenMenu.add_command(label=color,command=partial(setPenColor,color))

editMenu.add_cascade(label="Background Color" , menu=colorsBgMenu)
editMenu.add_separator()
editMenu.add_cascade(label="Pen Color" , menu=colorsPenMenu)

speed = Menu(master=editMenu , tearoff=0)
for i in range(11):
    if i == 0:
        speed.add_command(label = str(i) + " (no animation)" , command = partial(setPenSpeed , i))
        continue
    speed.add_command(label = str(i) , command = partial(setPenSpeed , i))

editMenu.add_cascade(label="Pen Speed" , menu = speed)
editMenu.add_command(label="Pen Co-ordinates")

#Help Menu
helpMenu = tkinter.Menu(master=commandMenu,tearoff=0)
helpMenu.add_command(label="Keyboard Bindings")
helpMenu.add_command(label="Demo")
helpMenu.add_command(label="About A.6969")

commandMenu.add_cascade(label="File" , menu=fileMenu)
commandMenu.add_cascade(label="Edit" , menu=editMenu)
commandMenu.add_cascade(label="Help" , menu=helpMenu)
root.config(menu=commandMenu)

drawingCanvas = tkinter.Canvas(master=root , bg="black")
drawingCanvas.place(relheight=1 , relwidth=1)

tScreen = turtle.TurtleScreen(drawingCanvas)
tScreen.bgcolor("black")
t = turtle.RawTurtle(tScreen)
t.pencolor("blue")
t.penup()
t.setx(550)
t.sety(-300)
t.pendown()
t.speed(10)
t.hideturtle()

locator = turtle.RawTurtle(tScreen)
locator.color("white")
locator.speed(0)
locator.penup()
locator.setposition(-170,80)

marker = turtle.RawTurtle(tScreen,visible=False)
marker.penup()
marker.setx(-170)
marker.sety(100)
marker.color("white")
marker.write(locator.position(),align='left',font=FONT)

locator.ondrag(drag_handler)

root.bind("<f>" , draw)
root.bind("<F11>",toggleFs)
root.mainloop()

