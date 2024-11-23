from ..interfaces.scene import Scene
from ...models.scene_change_event import SceneType,SceneChangeEvent
import pygame
from ... import settings
from ...entities.coffee_cup import CoffeeCup,CoffeeContents
from ...entities.sugar_jar import SugarJar
from ...entities.coffee_jar import CoffeeJar
from ...entities.spoon import SpoonContents,Spoon
from ...entities.milk_jug import MilkJug
from ...entities.water_jug import WaterJug
class CoffeeMakingScene(Scene):
    
    def __init__(self,surface:pygame.Surface):
        super().__init__(surface)
        self.group = pygame.sprite.Group()
        screen_size = self._surface.get_rect().size
        self.sugar_jar = SugarJar((screen_size[0]/6,screen_size[1]/5),self.group)
        self.coffee_jar = CoffeeJar((screen_size[0]/6 + self.sugar_jar.rect.size[0],screen_size[1]/5),self.group)
        self.coffee_cup = CoffeeCup(self._surface.get_rect().center,CoffeeContents.EMPTY,self.group)
        self.spoon = Spoon((screen_size[0]/6 + self.sugar_jar.rect.size[0] + self.coffee_jar.rect.size[0] + 100,screen_size[1]/5),SpoonContents.EMPTY,self.group)
        self.milk_jug = MilkJug((screen_size[0]/6 + self.sugar_jar.rect.size[0] + self.coffee_jar.rect.size[0] + 100 + self.spoon.rect.size[0] + 40,screen_size[1]/5),self.group)
        self.water_jug = WaterJug((screen_size[0]/6 + self.sugar_jar.rect.size[0] + self.coffee_jar.rect.size[0] + 100 + self.spoon.rect.size[0] + 40 + self.milk_jug.rect.size[0] + 40,screen_size[1]/5),self.group)
        
        self.will_move = False
        self.go_to_ordering = None

        
        
    def handleEvent(self,event:pygame.event.Event):
        super().handleEvent(event)
        for sprite in self.group.sprites():
            sprite.handle_events(event)
        match event.type:
            case pygame.MOUSEBUTTONDOWN:
                self._change_coffee_contents(event)
                self._change_spoon_contents(event)
                self._add_spoon_coffee_cup(event)
                
            case pygame.MOUSEBUTTONUP:
                self._milk_water_jug_add_move(event)
                if not self.go_to_ordering :
                    return
                if self.go_to_ordering.colliderect(self.coffee_cup.rect):
                    
                    event = SceneChangeEvent(SceneType.ORDERING_SCENE)
                    event.post()                                            
                    print("change scene")
                else:
                    self.coffee_cup.move(self._surface.get_rect().center)
    def _add_spoon_coffee_cup(self,event:pygame.event.Event):
        screen_size = self._surface.get_rect().size
        if self.spoon.rect.colliderect(self.coffee_cup.rect):
            match self.spoon.contents:
                case SpoonContents.SUGAR:
                    self._change_coffee_cup(CoffeeContents.SUGAR)
                case SpoonContents.COFFEE_POWDER:
                    self._change_coffee_cup(CoffeeContents.COFFEE_POWDER)
            self.group.remove(self.spoon)
            self.spoon = Spoon((screen_size[0]/6 + self.sugar_jar.rect.size[0] + self.coffee_jar.rect.size[0] + 109,screen_size[1]/5),SpoonContents.EMPTY,self.group)
    def _milk_water_jug_add_move(self,event):
        if self.milk_jug.rect.colliderect(self.coffee_cup.rect):
            self.group.remove(self.coffee_cup)
            match self.coffee_cup.contents:
                case CoffeeContents.EMPTY:
                    self.coffee_cup = CoffeeCup(self.coffee_cup.rect.center,CoffeeContents.MILK,self.group)
                case CoffeeContents.COFFEE_POWDER:
                    self.coffee_cup = CoffeeCup(self.coffee_cup.rect.center,CoffeeContents.MILK_COFFEE,self.group)
                case CoffeeContents.BLACK_COFFEE:
                    self.coffee_cup = CoffeeCup(self.coffee_cup.rect.center,CoffeeContents.MILK_COFFEE,self.group)
                  
        self.milk_jug.snap_back()
        if self.water_jug.rect.colliderect(self.coffee_cup.rect):
            if self.coffee_cup.contents == CoffeeContents.COFFEE_POWDER:
                self.group.remove(self.coffee_cup)
                self.coffee_cup = CoffeeCup(self.coffee_cup.rect.center,CoffeeContents.BLACK_COFFEE,self.group)
        self.water_jug.snap_back()
    def _change_spoon_contents(self,event:pygame.event.Event):
        if self.spoon.rect.colliderect(self.sugar_jar.rect):
            self.group.remove(self.spoon)
            self.spoon = Spoon(self.spoon.rect.center,SpoonContents.SUGAR,self.group)
            self.spoon.will_move = True
        elif self.spoon.rect.colliderect(self.coffee_jar.rect):
            self.group.remove(self.spoon)
            self.spoon = Spoon(self.spoon.rect.center,SpoonContents.COFFEE_POWDER,self.group)
            self.spoon.will_move = True
    def _change_coffee_contents(self,event:pygame.event.Event):
            if self.black_coffee_selector.collidepoint(pygame.mouse.get_pos()):
                self._change_coffee_cup(CoffeeContents.BLACK_COFFEE)
            elif self.sugar.collidepoint(pygame.mouse.get_pos()):
                self._change_coffee_cup(CoffeeContents.SUGAR)
            elif self.milk_coffee_selector.collidepoint(pygame.mouse.get_pos()):
                self._change_coffee_cup(CoffeeContents.MILK)
    
    def _change_coffee_cup(self,coffee_contents: CoffeeContents) -> CoffeeCup:
        self.group.remove(self.coffee_cup)
        self.coffee_cup = CoffeeCup(self.coffee_cup.rect.center,coffee_contents,self.group)
        return self.coffee_cup
                
  

    def update(self):
        self._surface.fill('red') 
        self.go_to_ordering = pygame.draw.rect(self._surface,"grey",pygame.rect.Rect(30,30,60,60))
        
        self.black_coffee_selector = pygame.draw.rect(self._surface,"black",pygame.rect.Rect(30,110,60,60))
        self.milk_coffee_selector = pygame.draw.rect(self._surface,"white",pygame.rect.Rect(30,190,60,60))
        self.sugar = pygame.draw.rect(self._surface,"purple",pygame.rect.Rect(30,270,60,60))
        self.coffee_powder = pygame.draw.rect(self._surface,"brown",pygame.rect.Rect(30,350,60,60))
            
        self.group.update(self._surface)

        