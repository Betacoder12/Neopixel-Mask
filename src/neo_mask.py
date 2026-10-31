import board
import neopixel
import texture_parser

NUM_LEDS = 99
MAX_BRIGHTNESS = 0.2

parser = texture_parser.TextureParser()
strip, brightness = parser.parse()

# Make the color list exactly NUM_LEDS long: trim extras, pad the rest with black,
# so every pixel on the strip receives data.
colors = [tuple(c) for c in strip][:NUM_LEDS]
colors += [(0, 0, 0)] * (NUM_LEDS - len(colors))

# Never let a texture ask for more brightness than the power budget allows.
brightness = max(0.0, min(float(brightness), MAX_BRIGHTNESS))

pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, brightness=brightness, auto_write=False)

for i, color in enumerate(colors):
    pixels[i] = color
pixels.show()

# Keep the program running so the data line stays driven.
# Press Enter (or Ctrl+C) to turn the strip off and exit.
try:
    input("Pattern is showing. Ctrl+C to turn off.\n")
except KeyboardInterrupt:
    pass

pixels.fill((0, 0, 0))
pixels.show()
