from .utils import SceneBase, draw_rounded_rect, half_of
import pygame, json, random, time

font = "./font/dense-letters.otf"

class StartScene(SceneBase):
    def __init__(self, screen):
        SceneBase.__init__(self)
        self.screen = screen

        self.init(self.screen)

    def init(self, screen):
        self.buttons = []
        self.interactingbutton = None

        self.frame = pygame.Rect(100, 100, screen.get_width() - 200, screen.get_height() - 200)

        self.button1 = pygame.Rect(half_of(screen.get_width()) - 137.5, half_of(screen.get_height()) - 100, 275, 70)
        self.buttons.append(self.button1)
        self.button2 = pygame.Rect(half_of(screen.get_width()) - 137.5, half_of(screen.get_height()), 275, 70)
        self.buttons.append(self.button2)
        self.button3 = pygame.Rect(half_of(screen.get_width()) - 137.5, half_of(screen.get_height()) + 100, 275, 70)
        self.buttons.append(self.button3)

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

    def Update(self):
        pass

    def Render(self, screen):
        self.init(screen)

        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), self.frame)

        for button in self.buttons:
            if button == self.interactingbutton:
                draw_rounded_rect(screen, button, (0, 255, 0), 18)
            else:
                draw_rounded_rect(screen, button, (255, 0, 0), 18)

        pygame.display.flip()
