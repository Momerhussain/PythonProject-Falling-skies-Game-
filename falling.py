import pygame
import turtle
import random
import time

pygame.init()
score=0
lives=3
over=""

wn=turtle.Screen()
wn.title("falling skies by omer")
wn.bgcolor("white")
wn.bgpic("space.gif")
wn.setup(width=800,height=600)
wn.tracer(0)

wn.register_shape("crab.gif")
wn.register_shape("ironman.gif")
clock = pygame.time.Clock()
carImg = pygame.image.load("car1.png") #load the car image



svs = pygame.image.load("svs.png")

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

display_width = 800
display_height = 600
carImg = pygame.image.load("car1.png")
gameDisplay = pygame.display.set_mode((display_width,display_height))
##############################################
def intro():
	#pygame.mixr.Sound.play(start_music)
	intro = True
	menu1_x = 200
	menu1_y = 400
	menu2_x = 500
	menu2_y = 400
	menu_width = 100
	menu_height = 50
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		pygame.display.set_icon(carImg)
		
		pygame.draw.rect(gameDisplay,black,(200,400,100,50))
		pygame.draw.rect(gameDisplay,black,(500,400,100,50))
			
		gameDisplay.fill(white)
		message_display("HASH GALICTIC COLLECTOR",50,display_width/2,display_height/2)
		gameDisplay.blit(svs,((display_width/2)-100,10))	
		pygame.draw.rect(gameDisplay,green,(200,400,100,50))
		pygame.draw.rect(gameDisplay,red,(500,400,100,50))
		
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		
		
		if menu1_x < mouse[0] < menu1_x+menu_width and menu1_y < mouse[1] < menu1_y+menu_height:
			pygame.draw.rect(gameDisplay,blue,(200,400,100,50))
			if click[0] == 1:
				intro = False
		if menu2_x < mouse[0] < menu2_x+menu_width and menu2_y < mouse[1] < menu2_y+menu_height:
			pygame.draw.rect(gameDisplay,blue,(500,400,100,50))
			if click[0] == 1:
				pygame.quit()
				
	
		message_display("Go",40,menu1_x+menu_width/2,menu1_y+menu_height/2)
		message_display("Exit",40,menu2_x+menu_width/2,menu2_y+menu_height/2)
		
		pygame.display.update()
		clock.tick(50)
		pygame.quit
		

def text_objects(text,font):
	textSurface = font.render(text,True,black)
	return textSurface,textSurface.get_rect()

def message_display(text,size,x,y):
	font = pygame.font.Font("freesansbold.ttf",size)
	text_surface , text_rectangle = text_objects(text,font)
	text_rectangle.center =(x,y)
	gameDisplay.blit(text_surface,text_rectangle)


intro()



#add the player
player = turtle.Turtle()
player.speed(0)
player.shape("ironman.gif")
player.color("white")
player.penup()
player.goto(0, -250)
player.direction = "stop"


#create list of good guys
good_guys=[]





#add the goodplayer
for x in range(20):
    
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("circle")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(-100, 250)
    good_guys.append(good_guy)
    good_guy.speed=random.randint(1,2)#randomspeed


#create list of bad guys
bad_guys=[]





#add the badplayer
for x in range(20):
    
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("crab.gif")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(100, 250)
    bad_guys.append(bad_guy)
    bad_guy.speed=random.randint(1,2)#randomspeed


#make the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("triangle")
pen.color("white")
pen.penup()
pen.goto(0, 260)
font=("Courier",24,"normal")
pen.write("Score : {}  Lives: {}".format(score,lives),align="center",font=font)


#function
def go_left():
    player.direction="left"

def go_right():
    player.direction="right"

#keyboard binding
wn.listen()
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")


#main game loop

gameExit = False
	


while True:
    #udate screen
    wn.update()
    
    
    #move the player
    if player.direction== "left":
        x=player.xcor()
        x-=0.5
        player.setx(x)

    if player.direction=="right":
        x=player.xcor()
        x+=0.5
        player.setx(x)

    #for game over
    if lives==0:
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.shape("triangle")
        pen.color("red")
        pen.penup()
        pen.goto(0, 50)
        font=("Courier",50,"normal")
        pen.write("GAME OVER".format(over),align="center",font=font)
        wn.mainloop()
        

    #move the goodguys
    for good_guy in good_guys:
        
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)

        #check if off the screen
        if y < -300:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            good_guy.goto(x,y)

        #check for a collision with the player
        if good_guy.distance(player)<20:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            good_guy.goto(x,y)
            score+=10
            pen.clear()
            pen.write("Score : {}  Lives: {}".format(score,lives),align="center",font=font)
        
    

    #move the badguys
    for bad_guy in bad_guys:
        
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)

        #check if off the screen
        if y < -300:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            bad_guy.goto(x,y)

        #check for a collision with the player
        if bad_guy.distance(player)<20:
            x=random.randint(-380,380)
            y=random.randint(300,400)
            bad_guy.goto(x,y)
            score-=10
            lives-=1
            pen.clear()
            pen.write("Score : {}  Lives: {}".format(score,lives),align="center",font=font)








wn.mainloop()
