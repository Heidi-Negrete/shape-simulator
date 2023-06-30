import arcade

class Rectangle:
    def __init__(
            self,
            x: int,
            y: int,
            width: int,
            height: int,
            pen_color: str = "BLACK",
            fill_color: str = "BLUE",
            dir_x: int = 1,
            dir_y: int = 1,
            speed_x: int = 1,
            speed_y: int = 1
    ):
      self.x = x
      self.y = y
      self.width = width
      self.height = height
      self.pen_color = pen_color
      self.fill_color = fill_color
      self.dir_x = 1 if dir_x > 0 else -1
      self.dir_y = 1 if dir_y > 0 else -1
      self.speed_x = speed_x
      self.speed_y = speed_y

    def set_pen_color(self, color: tuple) -> Rectangle:
       self.pen_color = color
       return self

    def set_fill_color(self, color: tuple) -> Rectangle:
       self.fill_color = color
       return self
    
    def draw(self):
      arcade.draw_xywh_rectangle_filled(
          self.x, self.y, self.width, self.height, self.fill_color
       )
      arcade.draw_xywh_rectangle_outline(
         self.x, self.y, self.width, self.height, self.pen_color, 3
      )