import pygame
from . import settings
from .ui.image_button import ImageButton
from .ui.scenes.coffee_making_scene import CoffeeMakingScene
from .ui.scenes.ordering_scene import OrderingScene
from .ui.scenes.loading_scene import LoadingScene
from .models.custom_event import CustomEvent
from .models.scene_change_event import SceneChangeEvent,SceneType
class Game:
    def _init(self):
        pygame.init()
        self._objArray = []
        self.clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT))
        self._current_scene = LoadingScene(self._screen)
        
        
        
                
        # def on_button_clicked(event):
        #     print(event)
        # background = pygame.image.load(settings.loading_screen_path)
        # screen = pygame.display.set_mode((settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT))
        # screen.blit(background,background.get_rect(center = screen.get_rect().center))
        # image_button = ImageButton(x = 1280/2,y = 720/2,screen=screen,path=settings.play_button_path,on_click=on_button_clicked)
        # self._objArray.append(image_button)
        # image_button.draw()

            
        
    def _mouseButtonPressHandler(self,event):
        for obj in self._objArray:
            if obj.get_rect().collidepoint(pygame.mouse.get_pos()):
                obj.on_clicked("button clicked")
        
    def _proccess_events(self):
        for event in pygame.event.get():
            self._current_scene.handleEvent(event)
            match event.type:
                case pygame.QUIT:
                     pygame.quit()
                     exit()
                case CustomEvent.SCENE_CHANGE_EVENT:
                    self._change_scene(event.event)
    def _change_scene(self,event:SceneChangeEvent):
        match event.sceneType:
            case SceneType.COFFEEMAKING_SCENE:
                self._current_scene = CoffeeMakingScene(self._screen)
            case SceneType.ORDERING_SCENE:
                self._current_scene = OrderingScene(self._screen)
                    
    def _update(self):
        self.clock.tick(settings.FPS)
        self._current_scene.update()
    def _render(self):
        pygame.display.flip()
    def run(self):
        self._init()
        while True:
            self._proccess_events()
            self._update()
            self._render()
            