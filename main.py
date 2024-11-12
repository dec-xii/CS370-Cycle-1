from game import Game
from menu import Menu

g = Game()

g.start()

while g.running:
    g.event()
    g.update()
    g.render()

        g.clean()

    elif m.quit:
        m.running = False

    m.clean()
