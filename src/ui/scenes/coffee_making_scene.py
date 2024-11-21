from ..interfaces.scene import Scene
import pygame
from ... import settings
class CoffeeMakingScene(Scene):
    
    def __init__(self,surface:pygame.Surface):
        super().__init__(surface)
        
    def handleEvent(self,event):
        return super().handleEvent()
  

    def update(self):
        self._surface.fill('white') 
        ks = settings.kitchen_settings
 
        base_cup = pygame.image.load(ks.base_cup_path).convert_alpha()
        coffee_fill = pygame.image.load(ks.cup_black_coffee_path).convert_alpha()
        base_cup.blit(coffee_fill, coffee_fill.get_rect(centerx=base_cup.get_rect().centerx - 50,centery = base_cup.get_rect().centery - 70))
        self._surface.blit(base_cup, base_cup.get_rect(center=self._surface.get_rect().center))
        