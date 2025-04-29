import pygame, sys, pyaudio, math
import sounddevice as sd
import numpy as np
import XInput


screen_width=1080
screen_height=1920
pygame.init()
screen = pygame.display.set_mode((1080, 1920))
pygame.display.set_caption("Hello World")



def g_update(button,bButton,coord,image):
    match button:
        case True:
            if button==bButton:
                
                screen.blit(image, coord)
            else:
                print("active")
                screen.blit(image, coord)
                
        case False:
            if button==bButton:
                return None
            else:
                print("inactive")
                


bg_img = pygame.image.load("drawing.png")
aOrB = pygame.image.load("AorB.png")
SeSt = pygame.image.load("SelectStart.png")
arr = pygame.image.load("arrow.png")

bA=''
bB=''
bX=''
bY=''

bUP=''
bDN=''
bLF=''
bRI=''
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

   screen.blit(bg_img, (0, 0))


   state = XInput.get_state(0)
   dib=XInput.get_button_values(state)

   g_update(dib['A'],bA,(800,1430),aOrB)
   g_update(dib['B'],bB,(600,1430),aOrB)
   g_update(dib['X'],bX,(650,1280),SeSt)
   g_update(dib['Y'],bY,(800,1280),SeSt)

   g_update(dib['DPAD_DOWN'],bDN,(213,1450),arr)
   g_update(dib['DPAD_LEFT'],bLF,(107,1345),arr)
   g_update(dib['DPAD_RIGHT'],bRI,(320,1345),arr)
   g_update(dib['DPAD_UP'],bUP,(213,1239),arr)

   bA=dib['A']
   bB=dib['B']
   bX=dib['X']
   bY=dib['Y']
   bUP=dib['DPAD_UP']
   bDN=dib['DPAD_DOWN']
   bLF=dib['DPAD_LEFT']
   bRI=dib['DPAD_RIGHT']

   
   
   pygame.display.update()



   