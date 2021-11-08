import math
import cairo

class RoundedSquare:
  def __init__(self, corner_radius: float):
    self.corner_radius = corner_radius

  def add_path(
      self,
      ctx: object,
      center_x: int,
      center_y: int,
      width: int
  ):
    straight_length = width - width * self.corner_radius

    ctx.move_to(center_x - width, center_y - straight_length)

    # top-left
    ctx.curve_to(
      center_x - width,
      center_y - straight_length,
      center_x - width,
      center_y - width,
      center_x - straight_length,
      center_y - width
    )
    # top
    ctx.line_to(center_x + 1 + straight_length, center_y - width)
    # top-right
    ctx.curve_to(
      center_x + 1 + straight_length,
      center_y - width,
      center_x + 1 + width,
      center_y - width,
      center_x + 1 + width,
      center_y - straight_length
    )
    # right
    ctx.line_to(center_x + 1 + width, center_y + 1 + straight_length)
    # bottom-right
    ctx.curve_to(
      center_x + 1 + width,
      center_y + 1 + straight_length,
      center_x + 1 + width,
      center_y + 1 + width,
      center_x + 1 + straight_length,
      center_y + 1 + width
    )
    # bottom
    ctx.line_to(center_x - straight_length, center_y + 1 + width)
    # bottom-left
    ctx.curve_to(
      center_x - straight_length,
      center_y + 1 + width,
      center_x - width,
      center_y + 1 + width,
      center_x - width,
      center_y + 1 + straight_length
    )
    # left
    ctx.line_to(center_x - width, center_y - straight_length)
