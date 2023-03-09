from PIL import Image
import numpy as np

class image_encode:
    def __init__(self, array, c, r, path):
        self.img = None
        self.error = None
        self.alen = len(array)
        self.cn = c
        self.rn = r
        self.pn = self.cn * self.rn

        if self.alen > self.pn - 12:
            self.error = "Insufficent pixels."

        else:
            self.array_to_image(array, self.rn, self.cn)
            self.img.save(path, format="PNG")

    def array_to_image(self, string, r, c):
        string = str(string)
        string = string.ljust(self.pn, "0")
        array = np.array(list(string)).reshape(self.rn, self.cn)
        array = array.astype(int)
        scale_arr = (255*array).astype(np.uint8)
        self.img = Image.fromarray(scale_arr, mode="L")

class image_decode:
    def __init__(self, path):
        self.output = ""
        self.path = path
        
        self.immage_to_array()

    def immage_to_array(self):
        img = Image.open(self.path)
        width, height = img.size
        bin_str = ""

        for y in range(height):
            for x in range(width):
                pixel = img.getpixel((x, y))
                bin_str += "0" if pixel == 0 else "1"

        self.output = bin_str

if __name__ == "__main__":
    # Demo usage

    x = "0111000010010011"

    p = image_encode(x, 720, 1080, "output.png")

    y = image_decode("output.png")
    print(y.output)