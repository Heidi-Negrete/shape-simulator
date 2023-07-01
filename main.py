from __future__ import annotations
import arcade
from random import choice

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

COLOR_PALETTE = [
    arcade.color.BLACK,
    arcade.color.LIGHT_GRAY,
    arcade.color.LIGHT_CRIMSON,
    arcade.color.LIGHT_BLUE,
    arcade.color.LIGHT_CORAL,
    arcade.color.LIGHT_CYAN,
    arcade.color.LIGHT_GREEN,
    arcade.color.LIGHT_YELLOW,
    arcade.color.LIGHT_PASTEL_PURPLE,
    arcade.color.LIGHT_SALMON,
    arcade.color.LIGHT_TAUPE,
    arcade.color.LIGHT_SLATE_GRAY,
]


class Shape:
    """ This class defines a simple shape """

    def __init__(
            self,
            x: int,
            y: int,
            width: int,
            height: int,
            pen_color: tuple = COLOR_PALETTE[0],
            fill_color: tuple = COLOR_PALETTE[1],
            dir_x: int = 1,
            dir_y: int = 1,
            speed_x: int = 1,
            speed_y: int = 1
    ):
        self._x = x
        self._y = y
        self.width = width
        self.height = height
        self.pen_color = pen_color
        self.fill_color = fill_color
        self.dir_x = 1 if dir_x > 0 else -1
        self.dir_y = 1 if dir_y > 0 else -1
        self.speed_x = speed_x
        self.speed_y = speed_y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value: int):
        if not (0 < value < SCREEN_WIDTH - self.width):
            self.dir_x = -self.dir_x
        self._x += abs(self._x - value) * self.dir_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value: int):
        if not (0 < value < SCREEN_HEIGHT - self.height):
            self.dir_y = -self.dir_y
        self._y += abs(self._y - value) * self.dir_y

    def set_pen_color(self, color: tuple) -> Rectangle:
        self.pen_color = color
        return self

    def set_fill_color(self, color: tuple) -> Rectangle:
        self.fill_color = color
        return self

    def draw(self):
        """ Inheriting classes will override this method """
        pass


class Rectangle(Shape):

    def draw(self):
        """ Draw the rectangle based on the current state """
        arcade.draw_xywh_rectangle_filled(
            self.x, self.y, self.width, self.height, self.fill_color
        )
        arcade.draw_xywh_rectangle_outline(
            self.x, self.y, self.width, self.height, self.pen_color, 3
        )


class Circle(Shape):
    def __init__(
            self,
            x: int,
            y: int,
            radius: int,
            pen_color: tuple = COLOR_PALETTE[0],
            fill_color: tuple = COLOR_PALETTE[1],
            dir_x: int = 1,
            dir_y: int = 1,
            speed_x: int = 1,
            speed_y: int = 1,
    ):
        super().__init__(
            x,
            y,
            radius * 2,
            radius * 2,
            pen_color,
            fill_color,
            dir_x,
            dir_y,
            speed_x,
            speed_y,
        )

    def draw(self):
        radius = self.width / 2
        center_x = self.x + radius
        center_y = self.y + radius
        arcade.draw_circle_filled(
            center_x,
            center_y,
            radius,
            self.fill_color
        )
        arcade.draw_circle_outline(
            center_x,
            center_y,
            radius,
            self.pen_color
        )


class Display(arcade.Window):
    """ Main display window """
    interval = 0

    def __init__(self, screen_title):
        """ Initialize the window """
        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, screen_title)

        # Create the rectangles collection
        self.shapes = []

        # Set the window's background color
        arcade.set_background_color(arcade.color.WHITE)

    def append(self, shape: Shape):
        """ Appends an instance of a rectangle to the list of rectangles """
        self.shapes.append(shape)

    def on_update(self, delta_time):
        " Update the position of the rectangles in the display "
        for shape in self.shapes:
            shape.x += shape.speed_x
            shape.y += shape.speed_y

    def on_draw(self):
        """ Called whenever you need to draw your window """

        # Clear the screen and start drawing
        arcade.start_render()

        # Draw the rectangles
        for shape in self.shapes:
            shape.draw()

    def change_colors(self, interval):
        """ This function is called once a second to change the colors of all the rectangles to a random selection from COLOR_PALETTE

        Arguments:
            interval {int} -- interval passed in from the arcade schedule function
        """
        for shape in self.shapes:
            shape.set_pen_color(choice(COLOR_PALETTE)).set_fill_color(
                choice(COLOR_PALETTE))


def main():
    # Create the display instance
    display = Display("Shape Simulator")

    # Create a rectangle instance
    rectangle = Rectangle(20, 20, 100, 200)

    # Append the rectangle to the display rectangles list
    display.append(rectangle)

    # Change the shape colors on a schedule
    arcade.schedule(display.change_colors, 1)

    # Run the application
    arcade.run()


if __name__ == "__main__":
    main()
