import texture_parser
import board
import neopixel

parser = texture_parser.TextureParser()

strip, brightness = parser.parse()
led_count = len(strip)
pixels = neopixel.NeoPixel(board.D18, led_count, brightness=brightness, auto_write=False)
