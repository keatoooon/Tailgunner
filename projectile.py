import pygame
import constants
class zeroShot(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        super().__init__()
        inAir=True
        onGround = True  
        self.image=pygame.Surface([4,10])
        self.image.fill((255,0,0))
        self.speed=8
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.angle=angle
        self.heading = constants.angleToVector(self.angle,self.speed)
    def hit(self):
        self.kill()
        return 1     
    def update(self):
        self.rect.x+=self.heading[0]
        self.rect.y+=self.heading[1]
        if abs(self.rect.x-constants.screenSize[0]/2)>50+constants.screenSize[0]/2 or abs(self.rect.y-constants.screenSize[1]/2)>50+constants.screenSize[1]/2:
            self.kill()

class shot(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        super().__init__()
        inAir=True
        onGround = True
        self.image=pygame.Surface([10,10])
        self.image.fill((0,0,0))
        pygame.draw.ellipse(self.image,(255,0,0),(0,0,10,10),0)
        self.image.set_colorkey((0,0,0))
        self.speed=4
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.angle=angle
        self.direction = constants.angleToVector(self.angle,1)
    def hit(self):
        self.kill()
        return 1
    def update(self):
        self.rect.x+=self.direction[0]*self.speed
        self.rect.y+=self.direction[1]*self.speed
        if abs(self.rect.x-constants.screenSize[0]/2)>50+constants.screenSize[0]/2 or abs(self.rect.y-constants.screenSize[1]/2)>50+constants.screenSize[1]/2:
            self.kill()

class playershot(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        super().__init__()
        inAir=True
        onGround = True
        size = [20,10]
        self.image=pygame.Surface(size)
        self.image.fill((0,0,0))
        pygame.draw.rect(self.image,(255,0,0),(0,0,3,size[1]))
        pygame.draw.rect(self.image,(255,0,0),(size[0]-3,0,3,size[1]))
        self.image.set_colorkey((0,0,0))
        self.speed=12
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.angle=angle
        self.direction = constants.angleToVector(self.angle,1)
    def hit(self):
        self.kill()
        return 1
    def update(self):
        self.rect.x+=self.direction[0]*self.speed
        self.rect.y+=self.direction[1]*self.speed
        if abs(self.rect.x-constants.screenSize[0]/2)>50+constants.screenSize[0]/2 or abs(self.rect.y-constants.screenSize[1]/2)>50+constants.screenSize[1]/2:
            self.kill()
class scaterShots(pygame.sprite.Sprite):
    def __init__(self,x,y,angle):
        super().__init__()
        inAir=True
        onGround = True
        size = [10,10]
        edge = 3
        
        shape = constants.angleToVector(angle,10)
        self.image=pygame.Surface((abs(shape[0])+1+2*edge,abs(shape[1])+1+2*edge))
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        #draw a line in the 
        if shape[1]<0:
            if shape[0]<0:
                pygame.draw.line(self.image,(255,0,0),[0+edge,0+edge],[self.rect.width-edge,self.rect.height-edge],3)
            elif shape[0]==0:
                pygame.draw.line(self.image,(255,0,0),[0+edge,0+edge],[0+edge,self.rect.height-edge],3)
            elif shape[0]>0:
                pygame.draw.line(self.image,(255,0,0),[0+edge,self.rect.height-edge],[self.rect.width-edge,0+edge],3)
        if shape[1]>0:
            if shape[0]<0:
                pygame.draw.line(self.image,(255,0,0),[self.rect.width+edge,0+edge],[0+edge,self.rect.height-edge],3)
            elif shape[0]==0:
                pygame.draw.line(self.image,(255,0,0),[0+edge,0+edge],[0+edge,self.rect.height-edge],3)
            elif shape[0]>0:
                pygame.draw.line(self.image,(255,0,0),[0+edge,0+edge],[self.rect.width-edge,self.rect.height-edge],3)
        elif shape[1]==0:
            pygame.draw.line(self.image,(255,0,0),[self.rect.width,0],[0,0],3)
        self.speed=1
        self.direction = constants.roundVector(constants.angleToVector(angle,12))
    def hit(self):
        self.kill()
        return 1
    def setheading(self,direction):
        self.direction = direction
    def getheading(self):
        return self.direction
    def update(self):
        self.rect.x+=self.direction[0]
        self.rect.y+=self.direction[1]
        if abs(self.rect.x-constants.screenSize[0]/2)>50+constants.screenSize[0]/2 or abs(self.rect.y-constants.screenSize[1]/2)>50+constants.screenSize[1]/2:
            self.kill()


class turretshot(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        super().__init__()
        inAir=True
        onGround = True
        size = [7,7]
        self.image=pygame.Surface(size)
        self.image.fill((0,0,0))
        pygame.draw.ellipse(self.image,(255,0,0),(0,0,7,7),0)
        self.image.set_colorkey((0,0,0))
        self.speed=12
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.direction = direction
    def hit(self):
        self.kill()
        return 1
    def update(self):
        self.rect.x+=self.direction[0]*self.speed
        self.rect.y-=self.direction[1]*self.speed
        if abs(self.rect.x-constants.screenSize[0]/2)>50+constants.screenSize[0]/2 or abs(self.rect.y-constants.screenSize[1]/2)>50+constants.screenSize[1]/2:
            self.kill()    
    
            
