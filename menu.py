from game import Game

class MainMenu:
    def __init__(self):
        self.options = ["Start Game", "Options", "Quit"]
        self.selected_option = 0

    def display(self):
        print("Main Menu")
        for index, option in enumerate(self.options):
            if index == self.selected_option:
                print(f"> {option} <")  # Highlight the selected option
            else:
                print(option)

    def navigate(self, direction):
        self.selected_option += direction
        self.selected_option %= len(self.options)  # Loop around the options

    def select(self):
        if self.selected_option == 0:  # Start Game
            return "start"
        elif self.selected_option == 1:  # Options
            return "options"
        elif self.selected_option == 2:  # Quit
            return "quit"

g = Game()

while True:
    menu = MainMenu()
    
    while True:
        menu.display()
        action = input("Use arrow keys to navigate (up/down) or Enter to select: ")

        if action == "up":
            menu.navigate(-1)
        elif action == "down":
            menu.navigate(1)
        elif action == "enter":
            selection = menu.select()
            if selection == "start":
                break  # Exit menu to start the game
            elif selection == "quit":
                g.clean()
                exit()

    g.start()

    while g.running:
        g.event()
        g.update()
        g.render()

    g.clean()
