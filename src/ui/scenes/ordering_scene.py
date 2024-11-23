from ..interfaces.scene import  Scene

class OrderingScene(Scene):
    def __init__(self, surface):
        super().__init__(surface)
        
    def update(self):
        self._surface.fill("white")
        # self._group.draw()
    
    def handleEvent(self,event):
        '''Handle event for the scene'''
        pass