from game import Game
from menu import Menu

g = Game()  
m = Menu()  

# main menu loop

while True:
    while m.running:
        m.event()
        m.update()
        m.render()

  
    if m.start_game:
        g.start()
        while g.running:
            g.event()
            g.update()
            g.render()

        g.clean()

    elif m.quit:
        m.running = False

    m.clean()
