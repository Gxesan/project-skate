from .utils import SceneBase
import pygame, json, random, time

font = "./font/dense-letters.otf"

class StartScene(SceneBase):
    def __init__(self, screen):
        SceneBase.__init__(self)
        self.screen = screen
        self.button1 = pygame.Rect(100, 100, screen.get_width()-200, screen.get_height()-200)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            pass

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), self.button1)
        pygame.display.flip()
