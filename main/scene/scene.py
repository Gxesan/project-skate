from .utils import SceneBase, draw_rounded_rect, half_of
import pygame, json, random, time

font = "./font/dense-letters.otf"

class StartScene(SceneBase):
    def __init__(self, screen):
        SceneBase.__init__(self)
        self.screen = screen
        self.frame = pygame.Rect(100, 100, screen.get_width()-200, screen.get_height()-200)
        self.button1 = pygame.Rect(half_of(screen.get_width())-137.5, half_of(screen.get_height())-20, 275, 70)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            pass

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), self.frame)
        draw_rounded_rect(screen, self.button1, (255, 0, 0), 18)
        pygame.display.flip()
