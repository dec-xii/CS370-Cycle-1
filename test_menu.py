import unittest
import menu
import pygame

class TestMenu(unittest.TestCase):
    def test_start_button(self):
        pygame.init()
        pygame.font.init()
        m = menu.Menu()
        menu.game_start(m)
        self.assertEqual(m.start_game, True)

    def test_quit_button(self):
        with self.assertRaises(SystemExit) as ex:
            menu.game_quit()
        self.assertEqual(ex.exception.code, None)

if __name__ == '__main__':
    unittest.main()
