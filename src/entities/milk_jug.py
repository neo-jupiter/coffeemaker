import pygame
from .. import settings

class MilkJug(pygame.sprite.Sprite):
    
    def __init__(self,pos : tuple, *groups):
        super().__init__(*groups)
        
        self.initial_pos = pos
        self.ks = settings.kitchen_settings
        self.image = pygame.image.load(self.ks.milk_jug_path).convert_alpha()
        self._transform_scale()
        self.rect = self.image.get_rect(center = self.initial_pos)
        
        self.will_move = False
    
    def update(self, surface:pygame.Surface):
        surface.blit(self.image,self.rect)
        
    def handle_events(self,event):
        match event.type:
            case pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.will_move = True
                    # self.image = pygame.transform.rotate(self.image,45)
            case pygame.MOUSEMOTION:
                if self.will_move:
                    self.move(pygame.mouse.get_pos())
            case pygame.MOUSEBUTTONUP:
                self.will_move = False
                # self.image = pygame.transform.rotate(self.image,-45)
    def move(self,pos:tuple):
        self.rect = self.image.get_rect(center = pos)
        
    def snap_back(self):
        self.move(self.initial_pos)
                    
            
    def _transform_scale(self):
        new_cup = pygame.transform.scale(self.image,(0.4 * self.image.get_width(),0.4 * self.image.get_height()))
        self.image = new_cup
