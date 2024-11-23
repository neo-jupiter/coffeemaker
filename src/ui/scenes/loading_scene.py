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
        self.weight += 0.001
        if self.weight >= 0.7:
            self.weight = 0.0

        # Calculate lerp values for scaling
        scale_x = int(self.x * (1.0 + self.weight))
        scale_y = int(self.y * (1.0 + self.weight))
        print(f"lerp x: {scale_x}, lerp y: {scale_y}")

        # Scale the image
        scaled_image = pygame.transform.scale(self.press_to_play, (scale_x, scale_y))

        # Load and scale the background
        background = pygame.image.load(settings.main_menu_path).convert()
        background = pygame.transform.scale(background, (1280, 720))
        self._surface.blit(background, background.get_rect(center=self._surface.get_rect().center))

        # Calculate the rect of the scaled image to ensure it's centered
        scaled_rect = scaled_image.get_rect(midbottom=self._surface.get_rect().midbottom)
        scaled_rect.bottom -= 25  # Offset the position slightly from the bottom

        # Blit the scaled image
        self._surface.blit(scaled_image, scaled_rect)