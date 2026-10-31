import time
import board
import neopixel

NUM_LEDS = 8
BRIGHTNESS = 0.3

pixels = neopixel.NeoPixel(board.D18, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)


def fill(color, delay=0.5):
    pixels.fill(color)
    pixels.show()
    time.sleep(delay)


def chase(color, delay=0.02):
    """One lit pixel runs from the first LED to the last."""
    for i in range(NUM_LEDS):
        pixels.fill((0, 0, 0))
        pixels[i] = color
        pixels.show()
        time.sleep(delay)


try:
    for color in [(255, 0, 0), (0, 255, 0), (0, 0, 255)]:
        fill(color)
    chase((0, 255, 0))
finally:
    pixels.fill((0, 0, 0))   # always turn everything off, even if you Ctrl+C
    pixels.show()
