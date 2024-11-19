from abc import ABC, abstractmethod

class Clickable(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def on_clicked(self,event):
        """Handle click event."""
        
