import pygame
from abc import ABC,abstractmethod
class Scene(ABC):
    def __init__(self,surface:pygame.Surface):
        self._group = pygame.sprite.Group()
        self._surface = surface
    
    @abstractmethod
    def update(self,event):
        self._surface.fill("white")
        self._group.draw()
    
    @abstractmethod
    def handleEvent(self):
        '''Handle event for the scene'''
        pass