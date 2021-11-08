import math
import cairo

from shapes.rounded_square import RoundedSquare
import utils.frameutils as frameutils

class RoundedFrame:

  @staticmethod
  def register_argparser(subparsers: object):
    parser = subparsers.add_parser(
      "rounded",
      description  = "simple frame with rounded edges",
      allow_abbrev = False
    )
    parser.add_argument(
      "frame_width",
      type = int,
      help = "size in pixels of the frame border"
    )
    parser.add_argument(
      "corner_radius",
      type = float,
      help = "roundness of the corners."
             " A value of 1 means totally round, while 0 produces perfectly squared corners"
    )
    parser.add_argument(
      "frame_color",
      type = str,
      help = "background color of the frame."
             " Accepts hex with and without alpha."
    )
    parser.add_argument(
      "--shadow_spread",
      type    = int,
      default = 0,
      help    = "spread in pixels of the frame's shadow"
    )
    parser.add_argument(
      "--shadow_color",
      type    = str,
      default = "#000000FF",
      help    = "color of the shadow."
                " Accepts hex with and without alpha."
    )
    parser.add_argument(
      "--indicator_width",
      type    = int,
      default = 0,
      help    = "width in pixels of the indicator line"
    )
    parser.add_argument(
      "--indicator_offset",
      type    = int,
      default = 0,
      help    = "distance of the indicator line from the window's side, in pixels"
    )
    parser.add_argument(
      "--indicator_color",
      type    = str,
      default = "#FFFFFFFF",
      help    = "color of the indicator line."
                " Accepts hex with and without alpha."
    )

  def __init__(self, args: object):
    self.shape = RoundedSquare(args.corner_radius)

    self.frame_width = args.frame_width
    self.frame_color = frameutils.hex_to_rgba(args.frame_color)

    self.shadow_spread = args.shadow_spread
    self.shadow_color  = frameutils.hex_to_rgba(args.shadow_color)

    self.indicator_width  = args.indicator_width
    self.indicator_offset = args.indicator_offset
    self.indicator_color  = frameutils.hex_to_rgba(args.indicator_color)

  def get_calculated_size(self) -> tuple:
    shadow_size    = self.frame_width + self.shadow_spread + 1 if self.shadow_spread > 0 else 0
    indicator_size = self.indicator_offset + self.indicator_width if self.indicator_width > 0 else 0

    size = 2 * max(self.frame_width, shadow_size, indicator_size) + 1

    return (size, size)

  def draw(self, surface: object, center_x: int, center_y: int):
    ctx = cairo.Context(surface)

    if self.shadow_spread > 0:
      self._draw_shadow(ctx, center_x, center_y)

    self._draw_frame(ctx, center_x, center_y)

    if self.indicator_width > 0:
      self._draw_indicator(ctx, center_x, center_y)

  def _draw_frame(self, ctx: object, center_x: int, center_y: int):
    ctx.set_fill_rule(cairo.FillRule.WINDING)

    self.shape.add_path(ctx, center_x, center_y, self.frame_width)
    
    ctx.set_source_rgba(*self.frame_color)
    ctx.fill()

  def _draw_indicator(self, ctx: object, center_x: int, center_y: int):
    ctx.set_fill_rule(cairo.FillRule.EVEN_ODD)

    self.shape.add_path(ctx, center_x, center_y, self.indicator_offset)
    self.shape.add_path(ctx, center_x, center_y, self.indicator_offset + self.indicator_width)

    ctx.set_source_rgba(*self.indicator_color)
    ctx.fill()

  def _draw_shadow(self, ctx: object, center_x: int, center_y: int):
    frameutils.draw_shape_gradient(
      ctx,
      center_x,
      center_y,
      self.shape,
      self.frame_width,
      self.shadow_spread,
      self.shadow_color,
      (0, 0, 0, 0)
    )
