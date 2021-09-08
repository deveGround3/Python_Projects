from tkinter import *

GreenTr = None
RedTr = None
PinkTr = None
OrangeTr = None

root = Tk()
root.title("Color Corners")
ColorC = Canvas(root, height = 175, width = 175, bg = "white")
ColorC.grid(column = 1, row = 1)

Green_button = Button(root, text = "Insert green in this direction")
Green_button.grid(column = 1, row = 0, padx = 4, pady = 5)
Green_button.bind("<Button-1>", lambda x: draw(0, 0, "green"))

Red_button = Button(root, text = "Insert red in this direction")
Red_button.grid(column = 2, row = 1, padx = 8, pady = 2)
Red_button.bind("<Button-1>", lambda x: draw(175, 0, "red"))

Pink_button = Button(root, text = "Insert pink in this direction")
Pink_button.grid(column = 1, row = 2, padx = 4, pady = 5)
Pink_button.bind("<Button-1>", lambda x: draw(175, 175, "pink"))

Orange_button = Button(root, text = "Insert orange in this direction")
Orange_button.grid(column = 0, row = 1, padx = 8, pady = 2)
Orange_button.bind("<Button-1>", lambda x: draw(0, 175, "orange"))

def draw(coordX, coordY, color):
    global GreenTr
    global RedTr
    global OrangeTr
    global PinkTr
    
    if (color == "green"):
        if GreenTr is None:
            GreenTr = ColorC.create_polygon(coordX, coordY, coordX + 175, coordY, 87.5, 87.5,
                            fill = color)            
        else:
            ColorC.delete(GreenTr)
            GreenTr = None
        
    elif (color == "red"):
        if RedTr is None:
            RedTr = ColorC.create_polygon(coordX, coordY, coordX, coordY + 175, 87.5, 87.5,
                            fill = color)
        else:
            ColorC.delete(RedTr)
            RedTr = None    
            
    elif (color == "pink"):
        if PinkTr is None:
            PinkTr = ColorC.create_polygon(coordX, coordY, coordX - 175, coordY, 87.5, 87.5,
                            fill = color)
        else:
            ColorC.delete(PinkTr)
            PinkTr = None 
            
    elif (color == "orange"):
        if OrangeTr is None:
            OrangeTr = ColorC.create_polygon(coordX, coordY, coordX, coordY - 175, 87.5, 87.5,
                            fill = color)  
        else:
            ColorC.delete(OrangeTr)
            OrangeTr = None     
    
root.mainloop()

