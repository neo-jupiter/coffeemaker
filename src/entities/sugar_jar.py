import pygame
from .. import settings

class SugarJar(pygame.sprite.Sprite):
    
    def __init__(self,pos : tuple, *groups):
        super().__init__(*groups)
        
        self.ks = settings.kitchen_settings
        self.image = pygame.image.load(self.ks.sugar_jar_path).convert_alpha()
        self._transform_scale()
        self.rect = self.image.get_rect(center = pos)
        
    def update(self,surface: pygame.Surface):
        surface.blit(self.image,self.rect)
    def handle_events(self,event):
        pass
        
    def _transform_scale(self):
        new_cup = pygame.transform.scale(self.image,(0.5 * self.image.get_width(),0.5 * self.image.get_height()))
        self.image = new_cup
