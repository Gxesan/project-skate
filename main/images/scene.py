from .utils import SceneBase, draw_rounded_rect, half_of
import pygame, json, random, time, webbrowser

font = "./font/dense-letters.otf"

class StartScene(SceneBase):
    def __init__(self, screen):
        SceneBase.__init__(self)
        self.screen = screen

        self.interactingbutton = None
        self.init(self.screen)

    def init(self, screen):
        self.buttons = []

        self.frame = pygame.Rect(100, 100, screen.get_width() - 200, screen.get_height() - 200)

        self.button1 = pygame.Rect(half_of(screen.get_width()) - 137.5, half_of(screen.get_height()), 275, 70)
        self.buttons.append(self.button1)
        self.button1text = pygame.font.Font(font, 32).render("New Game", True, (255, 255, 255))

        self.button2 = pygame.Rect(half_of(screen.get_width()) - 137.5, half_of(screen.get_height()) + 100, 275, 70)
        self.buttons.append(self.button2)
        self.button2text = pygame.font.Font(font, 32).render("Load Game", True, (255, 255, 255))

        self.button3 = pygame.Rect(half_of(screen.get_width()) - 137.5, half_of(screen.get_height()) + 200, 275, 70)
        self.buttons.append(self.button3)
        self.button3text = pygame.font.Font(font, 32).render("Quit Game", True, (255, 255, 255))

        self.socialbutton1 = pygame.Rect(half_of(screen.get_width()) - 112, half_of(screen.get_height()) + 285, 70, 70)
        self.buttons.append(self.socialbutton1)
        self.github_image = pygame.image.load("./images/rsz_25231.png")

        self.socialbutton2 = pygame.Rect(half_of(screen.get_width()) - 35, half_of(screen.get_height()) + 285, 70, 70)
        self.buttons.append(self.socialbutton2)
        self.discord_image = pygame.image.load("./images/rsz_discord.png")

        self.socialbutton3 = pygame.Rect(half_of(screen.get_width()) + 42, half_of(screen.get_height()) + 285, 70, 70)
        self.buttons.append(self.socialbutton3)

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if self.button3.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()
                if self.socialbutton1.collidepoint(mouse_pos):
                    webbrowser.open("https://github.com/banjo-studios/project-skate")
                    pygame.quit()
                    exit()
                if self.socialbutton2.collidepoint(mouse_pos):
                    webbrowser.open("https://discord.gg/6v4GR23cqs")
                    pygame.quit()
                    exit()

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

        screen.blit(self.github_image, (half_of(screen.get_width()) - 107, half_of(screen.get_height()) + 290))
        screen.blit(self.discord_image, (half_of(screen.get_width()) - 30, half_of(screen.get_height()) + 290))
        screen.blit(self.button1text, (half_of(screen.get_width()) - 95.5, half_of(screen.get_height()) + 19))
        screen.blit(self.button2text, (half_of(screen.get_width()) - 101.5, half_of(screen.get_height()) + 119))
        screen.blit(self.button3text, (half_of(screen.get_width()) - 98.5, half_of(screen.get_height()) + 219))
        pygame.display.flip()
