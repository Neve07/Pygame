#Name: Nevedhaa Ayyappan
#Date: June 11th, 2019
#Course: Computer Science
#Assignment: Culminating Game


#Import Packages
import pygame, sys
from pygame.locals import *

#Initialize Package
pygame.init()
win = pygame.display.set_mode ((640,600))
pygame.display.set_caption("EduCAUTION")

#Colours init
crushed = (142, 71, 71)
white = (250, 250, 250)

#Background Music##################################################
#Music
file = 'music.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()

#Math Game 1 variables
xcar = 10
ycar = 455
check = 0
opt = 60
#Math Game 2 variables
xbox = 140
ybox = 240
woah = 10
counter = 0
#Hardware Game 1 Constants
xarrow= 320
yarrow = 300
xcar = 10
ycar = 455
xr1 = 150
xr2 = 400
yr1 = 455
yr2 = 455
#Hardware Game 2 Variables
rk1x = 100
rk1y = -10
rk2x = 300
rk2y = - 50
rk3x = 500
rk3y = 100
bucketx = 270
buckety= 380
Hardanswer = 0

game1 = 0
game2 = 0
game3 = 0
game4 = 0
comtro= False
mathtro = False
mult = False
div = False
com1 = False
com2 = False
math2 = False
Home = True

#Text init
pygame.font.init()
myfont = pygame.font.SysFont('Arial', 50)
subtitle = pygame.font.SysFont('Arial', 25)
normal = pygame.font.SysFont('comicsans', 20)
#Intro Page tet
introTitle = myfont.render('EduCAUTION', False, (crushed))
suspense = subtitle.render('The Building Game of Survival', False,(crushed))
mButton = myfont.render('Math', False, (75,75,75))
csButton1 = subtitle.render('Computer', False, (75,75,75))
csButton2 = subtitle.render('Science', False, (75,75,75))
mathgames = subtitle.render('Math Games', False, (white))
comscigames = subtitle.render('Computer Hardware Games', False, (white))
choose = subtitle. render('Choose one to play', False, (210,210,210))
#Math Game 1 text
multipliCAUTION = myfont.render('MultipliCAUTION: The Game', False, (crushed))
multiplyrules = subtitle.render('Answer the questions to keep the driver from hitting the obstacles', False, (75,75,75))
multrules2 = subtitle.render('Click the up or down box to change your answer', False, (75,75,75))
multrules3 = subtitle.render('Click the up arrow to submit your answer', False,(75,75,75))
multQ1= myfont.render ('8  x  7  = ', False, (crushed))
multQ2 = myfont.render('6  x  9  = ', False, (crushed))
correct = myfont.render('Correct answer', False, (crushed))
tryagain = myfont.render('Try Again', False, (crushed))
Mopt1 = myfont.render(str(opt), False, (75,75,75))
#Division Game text
divtitle = myfont.render('CAUTION with Division', False, (crushed))
divrules = subtitle.render('Click on the right answer to help the worker come down the building', False, (75,75,75))
divQ1 = subtitle.render('Divide 42 by me and you will get 7. I am..', False, (crushed))
divQ2 = subtitle.render('If you divide 30 by me, the answer is 3 doubled. I am..', False, (crushed))
congrats = myfont.render('Congrats!! Thats correct!', False, (white))
again = myfont.render('Try again!', False, (white))
gameOver = myfont.render('Game Over', False, (white))
home = subtitle.render('Home', False, (crushed))
opt1 = myfont.render('6', False, (75,75,75))
opt2 = myfont.render('5', False, (75,75,75))
opt3 = myfont.render('1', False, (75,75,75))
#Hardware Game 1 Text
hardtitle = myfont.render('Beware Hardware!', False, (crushed))
hardrules = subtitle.render('Use arrows to move the arrow to the right answer to clear the path.', False, (75,75,75))
hardQ1 = myfont.render('RAM stands for...', False, (100,100,100))
Hopt1 = subtitle.render('Random Access Memory', False, (75,75,75))
Hopt2 = subtitle.render('Rotten Apple Monkey', False, (75,75,75))
hardQ2 = myfont.render('Which of these is an input device?', False, (100,100,100))
Hopt3= subtitle.render('Moniter', False, (75,75,75))
Hopt4 = subtitle.render('Keyboard', False, (75,75,75))
correct = myfont.render('Correct Answer', False, (75,75,75))
wrong = myfont.render('Try again', False, (75,75,75))
#Hardware Game 2 Text
hardtit2 = myfont.render('Caution with Computers!', False, (crushed))
hrules2 = subtitle.render('Catch the falling rocks to fill in the answer.', False, (75,75,75))
H2Q1 = subtitle.render('Python is a ________________ level programming language.', False, (white))
high = subtitle.render('HIGH', False, (white))
low = subtitle.render('LOW', False, (white))
fast = subtitle.render('FAST', False, (white))
H2Q2 = subtitle.render('A capacitor __________ electicity and releases it all at once.', False, (white))
needs = subtitle.render('NEEDS', False, (white))
throws = subtitle.render('THROWS', False, (white))
stores = subtitle.render('STORES', False, (white))
attempt2 = subtitle.render('Try Again', False, (white))
Next = subtitle.render('Correct, Next level', False, (75,75,75))

#Intro Page Images
introBG = pygame.image.load('introBG.jpg')
multiply = pygame.image.load ('multiplication.png')
divide = pygame.image.load('division.png')
mathBG = pygame.image.load ('bg.jpeg')
mouse2 = pygame.image.load('mouse 2.0.png')
rock3 =  pygame.image.load('rock3.png')
#Math Game 1 Images
introBG = pygame.image.load('introBG.jpg')
math1BG = pygame.image.load('mathlvl1BG.jpg')
rock = pygame.image.load('pylon.jfif')
car = pygame.image.load('car.png')
#Math Game 2 Images
math1BG = pygame.image.load('mathlvl1BG.jpg')
building = pygame.image.load('building.png')
skybox = pygame.image.load('skybox.png')
#Hardware game 1 Images Init
hardBG = pygame.image.load('comsciBG.jpg')
arrow = pygame.image.load('mouse.png')
car = pygame.image.load('car.png')
rock = pygame.image.load('rock.png')
#Hardware game 2 Images Init
hardBG = pygame.image.load('comsciBG.jpg')
rock2 = pygame.image.load('rock2.png')
bucket = pygame.image.load('bucket.png')

####################################################################################################
def mathGame1():
    global game1
    global opt
    global Mopt1
    global xcar
    global ycar
    global check
    global Home
    win.blit(math1BG, (0,0))
    win.blit (multipliCAUTION, (55, 15))
    win.blit (multiplyrules, (20, 80))
    win.blit(multrules2, (100,105))
    win.blit(multrules3, (130, 130))
    win.blit(rock, (140,470))
    win.blit(rock, (380, 520))
    win.blit(car, (xcar,ycar))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if game1 == 0:
        win.blit(multQ1, (200,250))
        #Down button
        if 400+100 > mouse[0] > 400 and 300+50 > mouse[1] > 300:
                pygame.draw.rect(win, white,(400,300,50,50))   
                win.blit(Mopt1, (400,250))
                if click[0] == 1 and click != None:
                    opt -= 1
                    check = 0
                    Mopt1 = myfont.render(str(opt), False, (75,75,75))
                    win.blit(Mopt1, (400,250))
        #To change colour of button
        else:
            pygame.draw.rect(win, crushed,(400,300,50,50))
            win.blit(Mopt1, (400,250))
        #Up button
        if 400+100 > mouse[0] > 400 and 200+50 > mouse[1] > 200:
                pygame.draw.rect(win, white,(400,200,50,50))   
                win.blit(Mopt1, (400,250))
                if click[0] == 1 and click != None:
                    opt += 1
                    check = 0
                    Mopt1 = myfont.render(str(opt), False, (75,75,75))
                    win.blit(Mopt1, (390,250))
        else:
            pygame.draw.rect(win, crushed,(400,200,50,50))
            win.blit(Mopt1, (400,250))

        #If answer is right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            check = 1
        if check == 1:
            if opt == 56:
                win.blit(correct, (100, 300))
                if ycar< 520:
                    ycar += 3
                    pygame.display.update()
                if xcar <280:
                    xcar +=3
                    pygame.display.update()
            else:
                win.blit(tryagain, (100, 300))
        if xcar == 280 and ycar == 521:
            game1 = 2
    #Level 2 ###########################################
    if game1 == 2:
        win.blit(multQ2, (200,250))
        #Down button
        if 400+100 > mouse[0] > 400 and 300+50 > mouse[1] > 300:
                pygame.draw.rect(win, white,(400,300,50,50))   
                win.blit(Mopt1, (390,250))
                if click[0] == 1 and click != None:
                    opt -= 1
                    check = 0
                    Mopt1 = myfont.render(str(opt), False, (75,75,75))
                    win.blit(Mopt1, (390,250))
        else:
            pygame.draw.rect(win, crushed,(400,300,50,50))
            win.blit(Mopt1, (390,250))
        #Up button
        if 400+100 > mouse[0] > 400 and 200+50 > mouse[1] > 200:
                pygame.draw.rect(win, white,(400,200,50,50))   
                win.blit(Mopt1, (390,250))
                if click[0] == 1 and click != None:
                    opt += 1
                    check = 0
                    Mopt1 = myfont.render(str(opt), False, (75,75,75))
                    win.blit(Mopt1, (390,250))
        else:
            pygame.draw.rect(win, crushed,(400,200,50,50))
            win.blit(Mopt1, (390,250))
        #If answer is right
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            check = 2
        if check == 2:
            if opt == 54:
                win.blit(correct, (100, 300))
                if ycar > 470:
                    ycar -= 3
                    pygame.display.update()
                if xcar < 680:
                    xcar +=3
                    pygame.display.update()
                if xcar >= 680:
                    Home = True
                    xcar = 10
            else:
                win.blit(tryagain, (100, 300))
    pygame.display.update()
##################################################################################
def mathGame2():
    global woah
    global xbox
    global ybox
    global game2
    global counter
    global Home
    win.blit(math1BG, (0,0))
    win.blit(divtitle, (80, 15))
    win.blit(divrules, (20,80))
    win.blit(building, (-220,80))
    win.blit(skybox, (xbox, ybox))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #Level 1 ##########################################################
    if game2 == 0:
        win.blit(divQ1, (200, 200))
        #Choice 1 Button
        if 200+100 > mouse[0] > 200 and 270+50 > mouse[1] > 270:
            pygame.draw.rect(win, white,(200,270,100,50))
            win.blit(opt2, (210, 270))
            if click[0] == 1 and click != None:
                woah = 0
        else:
            pygame.draw.rect(win, crushed,(200,270,100,50))
            win.blit(opt2, (210, 270))
        #Choice 2 Button
        if 350+100 > mouse[0] > 350 and 270+50 > mouse[1] > 270:
            pygame.draw.rect(win, white,(350,270,100,50))
            win.blit(opt1, (360, 270))
            if click[0] == 1 and click != None:
                woah = 1 
        else:
            pygame.draw.rect(win, crushed,(350,270,100,50))
            win.blit(opt1, (360, 270))
        #Choice 3 Button
        if 500+100 > mouse[0] > 500 and 270+50 > mouse[1] > 270:
            pygame.draw.rect(win, white,(500,270,100,50))
            win.blit(opt3, (510, 270))
            if click[0] == 1 and click != None:
                woah = 0
        else:
            pygame.draw.rect(win, crushed,(500,270,100,50))
            win.blit(opt3, (510, 270))
        
        #For actions when button is clicked
        #Correct Answer
        if woah == 1:
            win.blit(congrats, (200, 500))
            if ybox <= 350:
                while counter < 100:
                    ybox += 1
                    win.blit(skybox, (xbox, ybox))
                    counter += 1
                    pygame.display.update()
                game2 = 2 #Second Level
                counter = 0
        #Wrong answer
        if woah == 0:
            win.blit(again, (200, 500))

    #LEVEL 2 #########################################################
    if game2 != 0:
        win.blit(divQ2, (200, 200))
        #Choice 1
        if 200+100 > mouse[0] > 200 and 270+50 > mouse[1] > 270:
            pygame.draw.rect(win, white,(200,270,100,50))
            win.blit(opt2, (210, 270))
            if click[0] == 1 and click != None:
                woah = 1
        else:
            pygame.draw.rect(win, crushed,(200,270,100,50))
            win.blit(opt2, (210, 270))
        #Choice 2
        if 350+100 > mouse[0] > 350 and 270+50 > mouse[1] > 270:
            pygame.draw.rect(win, white,(350,270,100,50))
            win.blit(opt1, (360, 270))
            if click[0] == 1 and click != None:
                woah = 2
        else:
            pygame.draw.rect(win, crushed,(350,270,100,50))
            win.blit(opt1, (360, 270))
        #Choice 3
        if 500+100 > mouse[0] > 500 and 270+50 > mouse[1] > 270:
            pygame.draw.rect(win, white,(500,270,100,50))
            win.blit(opt3, (510, 270))
            if click[0] == 1 and click != None:
                woah = 0

        else:
            pygame.draw.rect(win, crushed,(500,270,100,50))
            win.blit(opt3, (510, 270))
    #If correct
    if woah == 1:
        win.blit(congrats, (200, 500))
        if ybox <= 350:
            while counter < 200:
                ybox += 1
                win.blit(skybox, (xbox, ybox))
                counter += 1
                pygame.display.update()
        if ybox >= 350:
            woah = 3
    if woah == 0:
        win.blit(again, (200, 500))
    #To return to home
    if woah == 3:
        win.blit(gameOver, (200, 500))
        Home = True
    pygame.display.update()
###############################################################################################
def comSci2():
    global bucketx
    global buckety
    global rk1y
    global rk2y
    global rk3y
    global Hardanswer
    global game4
    global Home
    win.blit(hardBG, (-5,-20))
    win.blit(hardtit2, (120, 15))
    win.blit(hrules2, (140, 80))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if game4 == 0:
        win.blit(H2Q1, (65, 520))
        #First Rock
        win.blit(rock2, (rk1x,rk1y))
        win.blit(high, (rk1x + 20, rk1y + 10))
        if rk1y < 450:
            rk1y += 5
            pygame.display.update()
        if rk1y >= 450:
            rk1y = -10
        #Second Rock
        win.blit(rock2, (rk2x,rk2y))
        win.blit(fast, (rk2x + 20, rk2y + 10))
        if rk2y < 450:
            rk2y += 5
            pygame.display.update()
        if rk2y >= 450:
            rk2y = -50
        #Third Rock
        win.blit(rock2, (rk3x,rk3y))
        win.blit(low, (rk3x + 20, rk3y + 10))
        if rk3y < 450:
            rk3y += 5
            pygame.display.update()
        if rk3y >= 450:
            rk3y = -10
        #Bucket
        win.blit(bucket, (bucketx, buckety))
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bucketx -= 10
                win.blit(bucket, (bucketx, buckety))
            elif event.key == pygame.K_RIGHT:
                bucketx += 10
                win.blit(bucket, (bucketx, buckety))
        #If rock lands in bucket
        if bucketx+148 >rk1x > bucketx and rk1y >= buckety:
            Hardanswer= 1
        if bucketx+148 >rk2x > bucketx and rk2y >= buckety:
            Hardanswer = 2
        if bucketx+148 >rk3x > bucketx and rk3y >= buckety:
            Hardanswer = 2
        if Hardanswer == 1:
            win.blit(high, (200, 520))
            #Next level button
            if 200+200 > mouse[0] > 200 and 270+50 > mouse[1] > 270:
                pygame.draw.rect(win, white,(200,270,200,50))
                win.blit(Next, (210, 270))
                if click[0] == 1 and click != None:
                    game4 = 2
            else:
                pygame.draw.rect(win, crushed,(200,270,200,50))
                win.blit(Next, (210, 270))
        if Hardanswer == 2:
            win.blit(attempt2, (200, 500))
    #Level 2 ##########################################################
    if game4 == 2:
        win.blit(H2Q2, (65, 520))
        #First Rock
        win.blit(rock2, (rk1x,rk1y))
        win.blit(needs, (rk1x + 20, rk1y + 10))
        if rk1y < 450:
            rk1y += 3
            pygame.display.update()
        if rk1y >= 450:
            rk1y = -10
        #Second Rock
        win.blit(rock2, (rk2x,rk2y))
        win.blit(throws, (rk2x + 20, rk2y + 10))
        if rk2y < 450:
            rk2y += 5
            pygame.display.update()
        if rk2y == 450:
            rk2y = -50
        #Third Rock
        win.blit(rock2, (rk3x,rk3y))
        win.blit(stores, (rk3x + 20, rk3y + 10))
        if rk3y < 450:
            rk3y += 5
            pygame.display.update()
        if rk3y == 450:
            rk3y = -10
        #Bucket
        win.blit(bucket, (bucketx, buckety))
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bucketx -= 10
                win.blit(bucket, (bucketx, buckety))
            elif event.key == pygame.K_RIGHT:
                bucketx += 10
                win.blit(bucket, (bucketx, buckety))
        #If rock lands in bucket
        if bucketx+148 >rk1x > bucketx and rk1y >= buckety:
            Hardanswer= 4
        if bucketx+148 >rk2x > bucketx and rk2y >= buckety:
            Hardanswer = 4
        if bucketx+148 >rk3x > bucketx and rk3y >= buckety:
            Hardanswer = 3
        if Hardanswer == 3:
            win.blit(high, (200, 520))
            #Next level button
            if 200+200 > mouse[0] > 200 and 270+50 > mouse[1] > 270:
                pygame.draw.rect(win, white,(200,270,200,50))
                win.blit(Next, (210, 270))
                if click[0] == 1 and click != None:
                    game4 = 5
            else:
                pygame.draw.rect(win, crushed,(200,270,200,50))
                win.blit(Next, (210, 270))
        if Hardanswer == 4:
            win.blit(attempt2, (200, 500))
    if game4 == 5:
        Home = True
    pygame.display.update()
##################################################################################
def comSci1():
    global game3
    global xarrow
    global yarrow
    global xr1
    global xr2
    global yr1
    global yr2
    global xcar
    global ycar
    global home
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    win.blit(hardBG, (-5,-20))
    win.blit(hardtitle, (160, 15))
    win.blit(hardrules, (25,80))
    win.blit(arrow, (xarrow, yarrow))
    win.blit(car, (xcar, ycar))
    win.blit(rock, (xr1, yr1))
    win.blit(rock, (xr2, yr2))
    if game3 == 0:
        win.blit(hardQ1, (200, 200))
        pygame.draw.rect(win, white,(15,290,250,50))
        pygame.draw.rect(win, white,(405, 290, 220, 50))
        win.blit(Hopt1, (30, 300))
        win.blit(Hopt2, (420, 300))
        #Move arrow
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xarrow -= 5
                win.blit(arrow, (xarrow, yarrow))
            elif event.key == pygame.K_RIGHT:
                xarrow += 5
                win.blit(arrow, (xarrow, yarrow))
        if xarrow < 265 and xarrow > 15:
            pygame.draw.rect(win, crushed,(15,290,250,50))
            win.blit(Hopt1, (30, 300))
            win.blit(correct, (200, 400))
            #Move car
            if yr1 < 620:
                yr1 += 7
                win.blit(rock, (xr1, yr1))
            if xcar < 300:
                xcar += 10
        if xcar == 300:
            game3 = 2
        if xarrow < 420 and xarrow > 400:
            pygame.draw.rect(win, crushed,(405, 290, 220, 50))
            win.blit(Hopt2, (420, 300))
            win.blit(wrong, (250, 400))
    #Level 2 ##################################################
    if game3 == 2:
        win.blit(hardQ2, (10, 200))
        pygame.draw.rect(win, white,(15,290,250,50))
        pygame.draw.rect(win, white,(405, 290, 220, 50))
        win.blit(Hopt3, (30, 300))
        win.blit(Hopt4, (420, 300))
        #Move arrow
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xarrow -= 5
                win.blit(arrow, (xarrow, yarrow))
            elif event.key == pygame.K_RIGHT:
                xarrow += 5
                win.blit(arrow, (xarrow, yarrow))
        if xarrow+40  < 520 and xarrow+40 > 400:
            pygame.draw.rect(win, crushed,(405, 290, 220, 50))
            win.blit(Hopt4, (420, 300))
            win.blit(correct, (200, 400))
            #Move car
            if yr2 < 640:
                yr2 += 7
                win.blit(rock, (xr1, yr1))
            if xcar < 640:
                xcar += 10
        if xcar >= 600:
            #Next level button
            if 200+200 > mouse[0] > 200 and 270+50 > mouse[1] > 270:
                pygame.draw.rect(win, white,(200,270,200,50))
                win.blit(Next, (210, 270))
                if click[0] == 1 and click != None:
                    Home = True
                    game3 = 5
            else:
                pygame.draw.rect(win, crushed,(200,270,200,50))
                win.blit(Next, (210, 270))
        if xarrow < 265 and xarrow > 15:
            pygame.draw.rect(win, crushed,(15,290,250,50))
            win.blit(Hopt3, (30, 300))
    if game3 == 5:
        Home = True
        hommie()
    pygame.display.update()

def hommie():
    Home = True

###################################################################################################
def mathintro():
    global mult
    global div
    win.blit(mathBG, (0,0))
    win.blit(introTitle, (10, 150))
    win.blit(mathgames, (10, 200))
    win.blit(choose, (10, 230))
    win.blit(multiply, (100, 300))
    win.blit(divide, (370, 300))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #Click multiply sign
    if 100+200 > mouse[0] > 100 and 300+200 > mouse[1] > 300:
            if click[0] == 1 and click != None:
                mult = True
    #Click divide sign
    if 370+200 > mouse[0] > 370 and 300+200 > mouse[1] > 300:
            if click[0] == 1 and click != None:
                div = True
    pygame.display.update()
###################################################################################################
def comsciIntro():
    global com1
    global com2
    win.blit(mathBG, (0,0))
    win.blit(introTitle, (10, 150))
    win.blit(comscigames, (10, 200))
    win.blit(choose, (10, 230))
    win.blit(mouse2, (100, 300))
    win.blit(rock3, (370, 300))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #Click arrow game
    if 100+200 > mouse[0] > 100 and 300+200 > mouse[1] > 300:
            if click[0] == 1 and click != None:
                com1 = True
    #Click rock game
    if 370+200 > mouse[0] > 370 and 300+200 > mouse[1] > 300:
            if click[0] == 1 and click != None:
                com2 = True
    pygame.display.update()
    pygame.display.update()
###################################################################################################
def introduction():
    global comtro
    global mathtro
    #Draw 
    win.blit(introBG, (0,0))
    win.blit(introTitle, (200, 150))
    win.blit(suspense, (190, 210))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #Computer Science Button
    if 380+110 > mouse[0] > 380 and 280+50 > mouse[1] > 280:
            pygame.draw.rect(win, white,(380,280,110,50))
            win.blit(csButton1, (390, 280))
            win.blit(csButton2, (400, 300))
            if click[0] == 1 and click != None:
                comtro = True
    else:
        pygame.draw.rect(win, crushed,(380,280,110,50))
        win.blit(csButton1, (390, 280))
        win.blit(csButton2, (400, 300))
    #Math Button
    if 160+110 > mouse[0] > 160 and 280+50 > mouse[1] > 280:
            pygame.draw.rect(win, white,(160,280,110,50))
            win.blit(mButton, (170, 280))
            if click[0] == 1 and click != None:
                mathtro = True
    else:
        pygame.draw.rect(win, crushed,(160,280,110,50))
        win.blit(mButton, (170, 280))
    pygame.display.update()

###########################################################################################################
#Main game Loop
run = True
while run:
    #Quit game
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Transitions (I USED BOOLEANS RATHER THAN COUNTERS :))
    #Prevents spagetti code
    if comtro == True:
        comsciIntro()
        mathtro = False
        mult = False
        div = False
        Home = False
    if mathtro == True:
        mathintro()
        comtro = False
        com2 = False
        com1 = False
        Home = False
    if com1 == True:
        comSci1()
        com2 = False
        comtro = False
        mathtro = False
        mult = False
        div = False
    if com2 == True:
        comSci2()
        com1 = False
        comtro = False
        mathtro = False
        mult = False
        div = False
    if mult == True:
        mathGame1()
        div = False
        mathtro = False
        comtro= False
        com1 = False
        com2 = False
        math2 = False
    if div == True:
        mathGame2()
        mult = False
        mathtro = False
        comtro= False
        com1 = False
        com2 = False
    if Home == True:
        introduction()
        mult = False
        div = False
        com2 = False
        math2 = False
        #So we can play the game multiple times
        #Math Game 1 variables
        xcar = 10
        ycar = 455
        check = 0
        opt = 60
        #Math Game 2 variables
        xbox = 140
        ybox = 240
        woah = 10
        counter = 0
        #Hardware Game 1 Constants
        xarrow= 320
        yarrow = 300
        xcar = 10
        ycar = 455
        xr1 = 150
        xr2 = 400
        yr1 = 455
        yr2 = 455
        #Hardware Game 2 Variables
        rk1x = 100
        rk1y = -10
        rk2x = 300
        rk2y = - 50
        rk3x = 500
        rk3y = 100
        bucketx = 270
        buckety= 380
        Hardanswer = 0
        game1 = 0
        game2 = 0
        game3 = 0
        game4 = 0

#End Game
pygame.quit()
