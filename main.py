import pygame
import json
from src import settings

from src.game import Game
import assets
from src.ui.image_button import ImageButton



def main():
    coffeemaker = Game()
    coffeemaker.run()
    # objarray = []
    # pygame.init()
    # background = pygame.image.load(assets.loading_screen_path)
 
    
    # screen = pygame.display.set_mode((settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT))
    # # screen.fill("white")
    # screen.blit(background,background.get_rect(center = screen.get_rect().center))
    # image_button = ImageButton(x = 1280/2,y = 720/2,screen=screen,path=assets.play_button_path,on_click=onClicked)
    # objarray.append(image_button)
    # image_button.draw()
    # clock = pygame.time.Clock()    
    # while True:
    #     clock.tick(60)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             exit()
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             pos = pygame.mouse.get_pos()
    #             print(f"MOUSE DOWN {pos}")
                
    #             for button in objarray:
    #                 if(checkIsClicked(button,pos)):
    #                     print("CLICKED")
    #                     button.on_clicked(pos)
                        
    #     pygame.display.flip()

def get_conf_json():
    with open("./conf.json","r") as confFile:
        return json.load(confFile)
def onClicked(event):
    print(f"BUTTON CLICKED : {event}")
    
def checkIsClicked(button:ImageButton,mouse_pos):
    return button.get_rect().collidepoint(mouse_pos)
    
    

if __name__ == "__main__":
    main()