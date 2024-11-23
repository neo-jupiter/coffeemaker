from ...ui.interfaces.scene import Scene 
import pygame
from ... import settings
from ...models.scene_change_event import SceneChangeEvent,SceneType
class LoadingScene(Scene):
    
    def __init__(self,surface:pygame.Surface):
        super().__init__(surface)
        self.press_to_play = pygame.image.load(settings.press_anywhere_path).convert_alpha()
        self.x = self.press_to_play.get_width()
        self.y = self.press_to_play.get_height()
        self.weight = 0.0
        self.EVENT_SCENE_CHANGE = pygame.USEREVENT + 1
        
        
        
    def handleEvent(self,event:pygame.event.Event):
        
        match event.type:
            case pygame.MOUSEBUTTONDOWN:
                scene_change_event = SceneChangeEvent(sceneType= SceneType.COFFEEMAKING_SCENE)
                scene_change_event.post()
                # pygame.event.post(pygame.event.Event(custom_event.CustomEvent.SCENE_CHANGE_EVENT,scene_name ="COFFEEMAKINGSCENE"))
                
                
    def update(self):
        self.weight  = self.weight + 0.01
        if self.weight >= 1:
            self.weight = 0.0 
        lerp_value_x = pygame.math.lerp(self.x,self.x + 50,self.weight)
        lerp_value_y = pygame.math.lerp(self.y,self.y + 50,self.weight)
        # print(f"lerp x : {lerp_value_x} , lerp y : {lerp_value_y}")
        self.press_to_play =  pygame.transform.scale(self.press_to_play,(lerp_value_x,lerp_value_y))
        background = pygame.image.load(settings.main_menu_path).convert()
        background = pygame.transform.scale(background,(1280,720))
        self._surface.blit(background,background.get_rect(center = self._surface.get_rect().center))
        press_to_play_rect = self.press_to_play.get_rect(midbottom = self._surface.get_rect().midbottom)
        press_to_play_rect.bottom = press_to_play_rect.bottom - 25

        
        self._surface.blit(self.press_to_play,press_to_play_rect)