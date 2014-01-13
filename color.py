import sys
import re

color_codes = {
    'white': 0,
    'black': 1,
    'blue': 2,
    'green': 3,
    'red': 4,
    'brown': 5,
    'purple': 6,
    'orange': 7,
    'yellow': 8,
    'lime': 9,
    'teal': 10,
    'cyan': 11,
    'royal': 12,
    'pink': 13,
    'grey': 14,
    'silver': 15,
}


def make_colorizer(color_code):
    return lambda text: '\3%s%s\3' % (color_code, text)


def colorize(text, regex, color):
    return re.sub('(%s)' % regex, lambda m: color(m.group(0)), text)

for color in color_codes:
    setattr(sys.modules[__name__], color, make_colorizer(color_codes[color]))
