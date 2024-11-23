import pygame
from .. import settings
from enum import Enum
import time
        
class SpoonContents(Enum):
    EMPTY = "empty"
    SUGAR = "sugar"
    COFFEE_POWDER = "coffee_powder"

class Spoon(pygame.sprite.Sprite):
    def __init__(self, pos :tuple,contents:SpoonContents,*groups):
        super().__init__(*groups)
        
        self.ks = settings.kitchen_settings
        self.contents = contents
        match contents:
            case SpoonContents.SUGAR:
                self.image = pygame.image.load(self.ks.spoon_sugar_path).convert_alpha()
            case SpoonContents.COFFEE_POWDER:
                self.image = pygame.image.load(self.ks.spoon_coffee_path).convert_alpha()
            case _:
                self.image = pygame.image.load(self.ks.base_spoon_path).convert_alpha()
                
                
        self._transform_scale()
        self.rect = self.image.get_rect(center = pos)
        self.will_move = False
        
    def update(self,surface:pygame.Surface):
        # print(self.rect)
        surface.blit(self.image,self.rect)
        
    def move(self,pos:tuple):
        self.rect = self.image.get_rect(center = pos)
        
    def handle_events(self,event:pygame.event.Event):
        match event.type:
            case pygame.MOUSEBUTTONDOWN:
  
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    if self.will_move is True:
                        self.change_will_move(False)
                    else: 
                        self.change_will_move(True)
                
            case pygame.MOUSEMOTION:
                if self.will_move:
                    self.move(pygame.mouse.get_pos())
            case pygame.MOUSEBUTTONUP:
                # self.will_move = False
                pass
    def change_will_move(self,value:bool):
        self.will_move = value
        print(f"WILL MOVE CHANGED {self.will_move}")
        

        
 
    def _transform_scale(self):
        new_cup = pygame.transform.scale(self.image,(0.5 * self.image.get_width(),0.5 * self.image.get_height()))
        self.image = new_cup

        
                
        
        
    