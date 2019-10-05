xpos = 0 
ypos = 0
b_height = 400;
b_width= 500;
x_dir = +4
y_dir = +4
x_racchetta=200

def setup():
    global xpos,ypos,b_width,b_height
    background(18,3,255)
    size (b_width, b_height)
    

def draw():
    global xpos,ypos,b_width,b_height,x_dir,y_dir,x_racchetta
    background(18,3,255)
    ellipse(xpos,ypos,50,50)
    xpos += x_dir
    ypos += y_dir
    
    if (xpos > width or xpos < 0):
        x_dir = x_dir * (-1)
        fill(random (0, 255),random (0, 255),random (0, 255))
        
    
        
    if (ypos > height or ypos < 0):
        y_dir = y_dir * (-1)
        fill(random (0, 255),random (0, 255),random (0, 255))
        
    rect(x_racchetta, 375, 100, 25)
        
    if ypos > b_height-50 and ypos > x_racchetta:
        y_dir = y_dir * (-1)
    

    

def keyPressed():
     global xpos,ypos,b_width,b_height,x_dir,y_dir,x_racchetta
     if keyCode == LEFT:
        x_racchetta -= 15
     if keyCode == RIGHT:
        x_racchetta += 15
    
    
    
