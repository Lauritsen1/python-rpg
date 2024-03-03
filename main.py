from entities.character import Character

from controllers.game import Game

def main(App):

    player = Character('Player')
    enemy = Character('Enemy')


if __name__ == "__main__":
    app = Game()
    app.run()