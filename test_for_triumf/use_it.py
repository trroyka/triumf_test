import simple_draw as sd
import cycle as c

sd.resolution = (900, 700)
sd.background_color = (135, 206, 235)


while True:
    sd.clear_screen()
    c.fitness()
    if sd.user_want_exit():
        break

sd.pause()
