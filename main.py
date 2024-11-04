from game import Game
from menu import Menu

g = Game()
m = Menu()

# main menu loop
while True:
    m.start()
    while m.running:
        m.event()
        m.update()
        m.render()


    # check the game start
    if m.start_game:
        g.start()
        while g.running:
            g.event()
            g.update()
            g.render()

        g.clean()

    m.clean()
