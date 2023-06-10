import subprocess
import sys
import time
########################################################################################## Libaries

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])


time.sleep(1)
print("Welcome to the game / Oyuna hoş geldiniz")
time.sleep(1)
print("Checking required libraries / Gerekli kütüphaneler kontrol ediliyor")
time.sleep(1)
print("Required libraries are [tkinter,Pillow,playsound] / gerekli kütüphaneler [tkinter,Pillow,playsound]")
time.sleep(1)

try:
    print("[GAME] Trying to import pygame ")
    import pygame
except:
    print("[EXCEPTION] pygame not installed")
    try:
        print("[GAME] Trying to install pygame via pip")
        import pip
        install("pygame")
        print("[GAME] pygame has been installed")
    except:
        print("[EXCEPTION] Pip not installed on system")




        
import pygame
from level_rect import *



pygame.init()
win=pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
main_font=pygame.font.SysFont("conicsans",35)
bg=pygame.image.load('img/Katman.png').convert_alpha()
plr=pygame.image.load('img/plr.png').convert_alpha()
finish=pygame.image.load('img/level1_end.png')

def track1():
    pygame.mixer.music.load("sound/arcade.mp3")
    pygame.mixer.music.play(loops=99)

def die():
    pygame.mixer.music.load("sound/expo3.wav")
    pygame.mixer.music.play(loops=0)

level=1
timer=True
dead=False
win.fill('white')


pygame.mouse.set_pos(60,60)
plar=pygame.draw.rect(win,'red',(50,50,30,30))

win.blit(plr,(50,50))

def count3():
    global timer
    pygame.time.delay(1000)
    pygame.mouse.set_pos(60,60)
    print('1')
    pygame.time.delay(1000)
    pygame.mouse.set_pos(60,60)
    print('2')
    pygame.time.delay(1000)
    pygame.mouse.set_pos(60,60)
    print('3')
    timer=False
    track1()

def draw():
    global run,dead
    win.blit(bg,(0,0))
    win.blit(finish,(45,500))
   # start=main_font.render('START',1,'green')
   # win.blit(start,(50,60))
    pygame.display.update()
    if timer==True:
        count3()
    
    if dead!=True:
        plar=pygame.draw.rect(win,'red',(mouse_pos[0]-15,mouse_pos[1]-15,30,30))
        win.blit(plr,(mouse_pos[0]-15,mouse_pos[1]-15))
    if dead==False:
        for i in rectlist:
            if i.colliderect(plar):
                die()
                print('dead')
                dead=True
    pygame.display.update()
    win.fill('white')
run=True
while run:
    mouse_pos=pygame.mouse.get_pos()
    
    draw()
    
    pygame.time.delay(100)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                run=False
    
    
    clock.tick(60)

    
pygame.quit()
 