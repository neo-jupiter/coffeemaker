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
        table = pygame.image.load(settings.table_path).convert()
        mug = pygame.image.load(settings.mug_path).convert_alpha()
        table_rect = table.get_rect(center = self._surface.get_rect().center)
        self._surface.blit(table,table_rect)
        self._surface.blit(mug,mug.get_rect(center=table_rect.midtop))