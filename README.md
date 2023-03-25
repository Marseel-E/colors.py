# colors.py
Python functions that output styialized input to the terminal

# Some shells don't support colorized text, or follow diffrernt foramts.
This was tested on: `fish`, `bash`

# how to use
All functions take 1 parameter `text` which is the desired text to be formatted, and return the same value which is the formatted string.
Example:
```py
from colors import red

if __name__ == '__main__':
  print(red("This is red text"))
```

# available functions
#### these functions have 9 similar style functions that follow this format (`color_style`, ex: `red_blinking`).
**Styles:** `bold`, `dim`, `italic`, `underlined`, `blinking`, `highlighted`, `invisible`, `linethrough`  
- `black`
- `red`
- `green`
- `yellow`
- `blue`
- `magenta`
- `cyan`
- `white`
