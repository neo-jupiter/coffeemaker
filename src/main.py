

import pygame
import json
from models.game_configuration import GameConfiguration
import assets
from models.image_button import ImageButton


def main():
    objarray = []
    pygame.init()
    background = pygame.image.load(assets.loading_screen_path)
    configuration =  GameConfiguration(get_conf_json())
    
    screen = pygame.display.set_mode((configuration.screenWidth,configuration.screenHeight))
    # screen.fill("white")
    screen.blit(background,background.get_rect(center = screen.get_rect().center))
    image_button = ImageButton(x = 1280/2,y = 720/2,screen=screen,path=assets.play_button_path,onClicked=onClicked)
    objarray.append(image_button)
    image_button.draw()
    clock = pygame.time.Clock()    
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(f"MOUSE DOWN {pos}")
                
                for button in objarray:
                    if(checkIsClicked(button,pos)):
                        print("CLICKED")
                        button.onClicked(button,event)
                        
        pygame.display.flip()

def get_conf_json():
    with open("./conf.json","r") as confFile:
        return json.load(confFile)
def onClicked(button:ImageButton,event):
    print(f"BUTTON CLICKED  at x : {button.x} & y : {button.y}")
    
def checkIsClicked(button:ImageButton,mouse_pos):
    return button.get_rect().collidepoint(mouse_pos)
    
    

if __name__ == "__main__":
    main()