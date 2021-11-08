#!/usr/bin/python3

import cairo
import argparse

from frames.rounded_frame import RoundedFrame

frames = {
  "rounded": RoundedFrame
}

parser = argparse.ArgumentParser(
  description  = "border images generator compatible with sway-borders",
  allow_abbrev = False
)
parser.add_argument(
  "output_file",
  type = str,
  help = "path of the image file to generate"
)

subparsers = parser.add_subparsers(
  title = "frame_type",
  dest  = "frame_type",
  help  = "the type of frame to generate"
)

for frame in frames.values():
  frame.register_argparser(subparsers)

args = parser.parse_args()

frame = frames[args.frame_type](args)

width, height = frame.get_calculated_size()
center_x = int(width / 2)
center_y = int(height / 2)

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
frame.draw(surface, center_x, center_y)
surface.write_to_png(args.output_file)
