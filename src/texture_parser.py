import json
import os


class TextureParser:
    def load_texture(self, name):
        textures_dir = os.path.join(os.path.dirname(__file__), "..", "textures")
        path = os.path.join(textures_dir, name)
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
        palette = self.texture_file["pallette"]   # key spelled as in your JSON files
        brightness = self.texture_file["brightness"]
        strip = []

        # Read rows from the bottom up, and reverse every other row, so the
        # colors come out in the order a snaking strip is physically wired.
        # extend() adds the row's colors one by one, giving one flat list of
        # pixels (append() would add each whole row as a single item).
        # Every row is preceded by one unlit spacer LED, [0, 0, 0].
        for y in range(len(texture) - 1, -1, -1):
            row = [palette[str(x)] for x in texture[y]]
            if (len(texture) - y) % 2 == 1:
                row.reverse()
            strip.append([0, 0, 0])
            strip.extend(row)

        return strip, brightness


if __name__ == "__main__":
    parser = TextureParser()
    strip, brightness = parser.parse()
    # 1 = any lit color, 0 = black. With an all-lit texture, a 9x10 picture
    # should print 01111111111 repeated 9 times (99 pixels).
    layout = "".join("0" if tuple(c) == (0, 0, 0) else "1" for c in strip)
    print("Pixels:", len(strip))
    print("Layout:", layout)
    print("Brightness:", brightness)