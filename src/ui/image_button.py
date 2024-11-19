
from pygame import Surface
import pygame
# from interfaces.clickable import Clickable
from .interfaces.clickable import Clickable

class ImageButton(Clickable):
    
    def __init__(self,on_click,x,y,path,screen:Surface):
        self.on_click = on_click
        self.x = x
        self.y = y
        self.path = path
        self.screen = screen
        image = pygame.image.load(self.path)
        self.image2 = pygame.transform.scale(image,(image.get_width(),image.get_height())).convert_alpha()
        self.rect = self.image2.get_rect(x = x,y = y)
        
    def get_rect(self):
        return self.rect
    
    def draw(self):

        self.screen.blit(self.image2,(self.x,self.y))
        
    def on_clicked(self,event):
        self.on_click(event)        