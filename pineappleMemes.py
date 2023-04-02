# Screen Properties
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Arcade Game"


# Actual Meme class
class Meme(Window):
    """Meme"""

    def __init__(self):
        """Init"""

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.spongebobMeme = "Who lives in a pineapple under the sea."
        self.spongebobMemeAnswer = "Spongebob Squarepants. As they say in the song."
        self.whoEatsPineapple = "Who only eats pineapples"
        self.whoEatsPineappleAnswer = "Pine & Apple Addicts. LOL"
        self.howToGrowAPineapple = "One Thing:"
        self.howToGrowAPineappleAnswer = "Put it in water."

        pass

    def setup(self):
        """Setup"""

        arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)

        pass


if __name__ == "__main__":
    window = Game()
    window.setup()
    arcade.run()
