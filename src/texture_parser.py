import json
import os

class TextureParser:
    def load_texture(self, name):
            TEXTURES_DIR = os.path.join(os.path.dirname(__file__), "..", "textures")
            path = os.path.join(TEXTURES_DIR, name)
            with open(path, "r") as f:
                return json.load(f)
    def load_json(self, name):
            with open(name, "r") as f:
                return json.load(f)
    def __init__(self):
        self.settings = self.load_json("settings.json")
        self.texture_file = self.load_texture(self.settings["texture"])

    def parse(self):
        texture = self.texture_file["texture"]
        pallette = self.texture_file["pallette"]
        brightness = self.texture_file["brightness"]
        strip = []

        for y in range(len(texture) - 1, -1, -1):
                strip_cache = []
                if y > len(texture) - 1:
                    strip.append([0,0,0])
                if (len(texture) - y) % 2 == 0:
                    for x in texture[y]:
                        color = pallette[str(x)]
                        strip_cache.append(color)
                else:
                    for x in texture[y]:
                        color = pallette[str(x)]
                        strip_cache.insert(0, color)
                strip.append(strip_cache)
        return strip, brightness

if __name__ == "__main__":
    parser = TextureParser()
    strip, brightness = parser.parse()
    print("Strip:", strip)
    print("Brightness:", brightness)
    