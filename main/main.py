import pygame, os, sys
from scene import scene

if int(sys.version[0]) < 3:
    print("Error detected. Wrong python version.")

#project skate
nameOfGame = "Project Skate"
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption(nameOfGame)
# pygame.display.set_icon(pygame.image.load('./images/hiking.png'))
active_scene = scene.StartScene(screen)

while active_scene != None:
    pressed_keys = pygame.key.get_pressed()

    filtered_events = []
    for event in pygame.event.get():
        quit_attempt = False
        if event.type == pygame.QUIT:
            quit_attempt = True
        elif event.type == pygame.KEYDOWN:
            alt_pressed = pressed_keys[pygame.K_LALT] or \
                          pressed_keys[pygame.K_RALT]
            if event.key == pygame.K_F4 and alt_pressed:
                quit_attempt = True

        if quit_attempt:
            active_scene.Terminate()
        else:
            filtered_events.append(event)

    active_scene.ProcessInput(filtered_events, pressed_keys)
    active_scene.Update()
    active_scene.Render(screen)
    active_scene = active_scene.next

    pygame.display.flip()