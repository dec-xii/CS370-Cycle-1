
from game import Game

g = Game()

g.start()

while g.running:
    g.event()
    g.update()
    g.render()

g.clean()
