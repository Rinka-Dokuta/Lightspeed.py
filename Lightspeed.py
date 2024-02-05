import pygame
import random
import math

#Boilerplate
pygame.init()
gamescreen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Single Particle Movement")
clock = pygame.time.Clock()

#Particle setup
xpos = [] #X position of the particle
ypos = [] #Y postition of the particle
xVel = [] #X velocity of the particle
yVel = [] #Y velocity of the particle
speed = 2 #Constant speed for all particles

#Create particles
for i in range(100):
    xpos.append(450) #Start X at center
    ypos.append(450) #Start Y at center
    
    #Generate random velocities
    velX = random.uniform(-1, 1)
    velY = random.uniform(-1, 1)
    
    #Calculate the magnitude of the velocity vector
    magnitude = math.sqrt(velX**2 + velY**2)
    
    #Normalize the velocity vector to have a constant speed
    if magnitude != 0:
        normalizedVelX = speed * velX / magnitude
        normalizedVelY = speed * velY / magnitude
    else:
        normalizedVelX = 0
        normalizedVelY = 0
    
    xVel.append(normalizedVelX)
    yVel.append(normalizedVelY)

#Game loop!------------------------------------------------
while True:
    clock.tick(60)
    
    #Event handling-----------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        
    #Physics--------------------------------------------------
    for i in range(100):
       #Update position
        xpos[i] += xVel[i]
        ypos[i] += yVel[i]
    
        #Boundary checking
        if xpos[i] < 0 or xpos[i] > 900 or ypos[i] < 0 or ypos[i] > 900: #Check if hitting left or right wall
            xpos[i] = 450 #Reset X to center
            ypos[i] = 450 #Reset Y to center
            
            #Generate new random velocities
            velX = random.uniform(-1, 1)
            velY = random.uniform(-1, 1)
            
            #Calculate the magnitude of the velocity vector
            magnitude = math.sqrt(velX**2 + velY**2)
    #Render section---------------------------------------------
    gamescreen.fill((0, 0, 0))
    for i in range(100):
        pygame.draw.circle(gamescreen, (255, 255, 255), (xpos[i], ypos[i]), 5)
    pygame.display.flip()
    
#End of game loop----------------------------------------------------------------
pygame.quit()    
