from .utils import SceneBase, draw_rounded_rect, half_of
import pygame, json, random, time

font = "./font/dense-letters.otf"

class StartScene(SceneBase):
    def __init__(self, screen):
        self.buttons = []
        self.interactingbutton = None
        SceneBase.__init__(self)
        self.screen = screen
        self.frame = pygame.Rect(100, 100, screen.get_width()-200, screen.get_height()-200)

        self.button1 = pygame.Rect(half_of(screen.get_width())-137.5, half_of(screen.get_height())-20, 275, 70)
        self.buttons.append(self.button1)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
                for button in self.buttons:
                    if button.collidepoint(mouse_pos):
                        self.interactingbutton = button
                        break
                    else:
                        self.interactingbutton = None

#interactive buttons

    def Update(self):
        pass

    def Render(self, screen):
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), self.frame)

        for button in self.buttons:
            if button == self.interactingbutton:
                draw_rounded_rect(screen, button, (0, 255, 0), 18)
            else:
                draw_rounded_rect(screen, button, (255, 0, 0), 18)

        pygame.display.flip()
