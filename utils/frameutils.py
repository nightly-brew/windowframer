import math
import cairo

def hex_to_rgba(hex_color: str):
  stripped_str = hex_color.lstrip('#')

  if len(stripped_str) == 6:
    # Do not remove the trailing comma in the tuple at the end, otherwise python
    # recognises the parenthesis as mathematical elements, not collection delimiters.
    return tuple(round(int(stripped_str[i:i+2], 16) / 255, 3) for i in (0, 2, 4)) + (1.0, )
  if len(stripped_str) == 8:
    return tuple(round(int(stripped_str[i:i+2], 16) / 255, 3) for i in (0, 2, 4, 6))
  else:
    raise Exception("The hex color string has an invalid length (it's not 6 nor 8 chars, # excluded")

def draw_shape_gradient(
    ctx: object,
    center_x: int,
    center_y: int,
    shape: object,
    offset: int,
    spread: int,
    inner_color: tuple,
    outer_color: tuple
):

  # The filling adds color in the offset zone.
  shape.add_path(ctx, center_x, center_y, offset)
  ctx.set_source(cairo.SolidPattern(*inner_color))
  ctx.set_fill_rule(cairo.FillRule.WINDING)
  ctx.fill()

  # The additional stroke on the start of the fade area helps uniforming color changes on the offset border,
  # otherwise with some shapes, some pixels do not mix well. 
  shape.add_path(ctx, center_x, center_y, offset)
  ctx.set_source(cairo.SolidPattern(*inner_color))
  ctx.set_line_width(1)
  ctx.stroke()

  red_step   = (inner_color[0] - outer_color[0]) / spread
  green_step = (inner_color[1] - outer_color[1]) / spread
  blue_step  = (inner_color[2] - outer_color[2]) / spread
  alpha_step = (inner_color[3] - outer_color[3]) / spread

  for i in range(0, spread, 1):
    # First adds the frame path to the context, then adds an encapsulating path.
    shape.add_path(ctx, center_x, center_y, offset + i)
    shape.add_path(ctx, center_x, center_y, offset + i + 1)

    red   = inner_color[0] - red_step * i
    green = inner_color[1] - green_step * i
    blue  = inner_color[2] - blue_step * i
    alpha = inner_color[3] - alpha_step * i

    ctx.set_source(cairo.SolidPattern(red, green, blue, alpha))
    ctx.set_fill_rule(cairo.FillRule.EVEN_ODD)
    ctx.set_line_width(1)
    ctx.stroke()
