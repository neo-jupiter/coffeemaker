from enum import Enum
import pygame
from .custom_event import CustomEvent
class SceneType(Enum):
    COFFEEMAKING_SCENE = "COFFEMAKING_SCENE"
    ORDERING_SCENE = "ORDERING_SCENE"
    
class SceneChangeEvent:
    def __init__(self,sceneType : SceneType):
        self.sceneType = sceneType
        
    def post(self):
        pygame.event.post(pygame.event.Event(CustomEvent.SCENE_CHANGE_EVENT,event = self))
        