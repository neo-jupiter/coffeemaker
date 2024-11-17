class GameConfiguration:
    def __init__(self,confJson:dict):
        self.screenWidth = confJson["screenWidth"]
        self.screenHeight = confJson["screenHeight"]
        self.fps = confJson["fps"]  
        