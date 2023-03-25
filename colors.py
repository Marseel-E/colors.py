"""
MIT License

Copyright (c) 2023 Marseel-E

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


__all__ = []


COLORS = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
STYLES = ['bold', 'dim', 'italic', 'underlined', 'blinking', 'unidentified', 'highlighted', 'invisible', 'linethrough']


def _format_name(color: str, style: str) -> str:
	"""
		Generates the name for the styalized color functions.

		Parameters:
			color <str> - The name of the color.
			style <str> - The name of the style.

		Returns:
			String: The formatted function name.
	"""
	return color + "_" + style


for color in COLORS:
	__all__.append(color)
	for style in STYLES:
		__all__.append(_format_name(color, style))


def _get_remainder(number: float) -> int:
	"""
		Returns the remainder of the given number.

		Parameters:
			number <float> - The number to extract its remainder.

		Returns:
			Float: the remainder of the given number.
	"""
	return int((number % int(number)) * 10)

def _format(style: float, text: str) -> str:
	"""
		Wraps the given text in the given style.

		Parameters:
			style <float> - The style to be formatted in (number is the color, remainder is the style).
			text <str> - The text to be styalized.

		Returns:
			String: The formatted string.
	"""
	return f"\033[{str(_get_remainder(style))};{str(int(style))}m {text}\033[0m"


from functools import partial

for color_code, color in enumerate(COLORS):
	globals()[color] = partial(_format, float(30 + color_code))
	for style_code, style in enumerate(STYLES):
		globals()[_format_name(color, style)] = partial(_format, float(30 + color_code) + ((style_code + 1) / 10))


if __name__ == '__main__':
	[print(k) for k, v in globals().items() if not k.startswith('__')]


# 1 bold
# 2 dim
# 3 italic
# 4 underlined
# 5 blinking
# 6 also blinking ?
# 7 highlighted
# 8 invisible
# 9 linethrough
# 30 black
# 31 red
# 32 green
# 33 yellow
# 34 blue
# 35 magenta
# 36 cyan
# 37 white
