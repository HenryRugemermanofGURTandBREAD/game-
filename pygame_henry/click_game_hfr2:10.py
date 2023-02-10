import time

WIDTH = 500
HEIGHT = 300

urmum = Actor('character')
urmum.pos = 100,50

def draw():
    screen.fill((0, 255, 0))
    urmum.draw()

def update():
    urmum.left = urmum.left + 2
    if urmum.left > WIDTH:
        urmum.right = 0



def on_mouse_down(pos):
    if urmum.collidepoint(pos):
        set_character_hurt()

def set_character_normal():
    urmum.image = 'character'

def set_character_hurt():
    urmum.image = 'character_clicked'
    sounds.eep.play()
    clock.schedule_unique(set_character_normal, 1.0)

