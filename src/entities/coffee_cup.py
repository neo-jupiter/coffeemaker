import pygame
from .. import settings
from enum import Enum
        
class CoffeeContents(Enum):
    EMPTY = "empty"
    BLACK_COFFEE = "black_coffee"
    MILK_COFFEE = "milk_coffee"
    MILK = "milk"
    SUGAR = "sugar"
    COFFEE_POWDER = "coffee_powder"

class CoffeeCup(pygame.sprite.Sprite):
    def __init__(self, pos :tuple,contents:CoffeeContents,*groups):
        super().__init__(*groups)
        
        self.ks = settings.kitchen_settings
        self.contents = contents
 
        self.image = pygame.image.load(self.ks.base_cup_path).convert_alpha()
        self._create_content(self.contents)
        self._transform_scale()
        self.rect = self.image.get_rect(center = pos)
        self.will_move = False
        
    def update(self,surface:pygame.Surface):
        # print(self.rect)
        surface.blit(self.image,self.rect)
        
    def move(self,pos:tuple):
        self.rect = self.image.get_rect(center = pos)
        
    def handle_events(self,event:pygame.event.Event):
        match event.type:
            case pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.will_move = True
            case pygame.MOUSEMOTION:
                if self.will_move:
                    self.move(pygame.mouse.get_pos())
            case pygame.MOUSEBUTTONUP:
                self.will_move = False

        
    def _create_content(self,coffee_contents:CoffeeContents):
        coffee_fill = None
        match coffee_contents:
            case CoffeeContents.BLACK_COFFEE:
                coffee_fill = pygame.image.load(self.ks.cup_black_coffee_path).convert_alpha()
            case CoffeeContents.MILK_COFFEE:
                coffee_fill = pygame.image.load(self.ks.cup_milk_coffee_path).convert_alpha()
            case CoffeeContents.MILK:
                coffee_fill = pygame.image.load(self.ks.cup_milk_path).convert_alpha()
            case CoffeeContents.SUGAR:
                coffee_fill = pygame.image.load(self.ks.cup_sugar_particles_path).convert_alpha()
            case CoffeeContents.COFFEE_POWDER:
                coffee_fill = pygame.image.load(self.ks.cup_coffee_particles_path).convert_alpha()
        if coffee_fill is not None:
            self.image.blit(coffee_fill, coffee_fill.get_rect(centerx=self.image.get_rect().centerx - 50,centery = self.image.get_rect().centery - 70))
    def _transform_scale(self):
        new_cup = pygame.transform.scale(self.image,(0.5 * self.image.get_width(),0.5 * self.image.get_height()))
        self.image = new_cup

        
                
        
        
    