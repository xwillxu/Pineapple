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
        self.spongebobMemeAnswer = "Spongebob Squarepants"

        pass

    def setup(self):
        """Setup"""

        arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)

        pass

    def on_key_press(self, key, modifiers):
        """Key Press"""

        pass

    def on_key_release(self, key, modifiers):
        """Key Press"""

        pass

    def on_draw(self):
        """Draw"""

        arcade.start_render()

        pass

    def on_update(self, delta_time):
        """Update"""

        pass


if __name__ == "__main__":
    window = Game()
    window.setup()
    arcade.run()
