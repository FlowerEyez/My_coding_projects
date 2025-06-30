from PIL import Image
import subprocess
import sys
from colorama import Fore, Style

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_PIXEL = 255

def get_pixel_matrix(img, new_width=100):
    w, h = img.size
    new_height = int(h * new_width / w)
    img = img.resize((new_width, new_height))
    pixels = list(img.getdata())
    return [pixels[i:i + new_width] for i in range(0, len(pixels), new_width)]

def rgb_to_intensity(matrix, algo="average"):
    out = []
    for row in matrix:
        newr = []
        for r, g, b in row:
            if algo == "average":
                val = (r + g + b) / 3
            elif algo == "luminosity":
                val = 0.21 * r + 0.72 * g + 0.07 * b
            elif algo == "min_max":
                val = (max(r, g, b) + min(r, g, b)) / 2
            newr.append(val)
        out.append(newr)
    return out

def normalize(matrix):
    flat = [v for row in matrix for v in row]
    mn, mx = min(flat), max(flat)
    r = mx - mn if mx != mn else 1
    return [[(v - mn) / r * MAX_PIXEL for v in row] for row in matrix]

def intensity_to_acsii(matrix):
    length = len(ASCII_CHARS)
    return [
        [ASCII_CHARS[int(v / MAX_PIXEL * (length - 1))] for v in row]
        for row in matrix
    ]

def print_ascii(ascii_matrix, color=Fore.WHITE):
    for row in ascii_matrix:
        line = "".join(ch * 2 for ch in row)
        print(color + line)
    print(Style.RESET_ALL)

def main(image_path, width=100, algo="average", invert=False, color=Fore.WHITE):
    img = Image.open(image_path).convert("RGB")
    pm = get_pixel_matrix(img, width)
    im = rgb_to_intensity(pm, algo)
    im = normalize(im)
    if invert:
        im = [[MAX_PIXEL - v for v in row] for row in im]
    am = intensity_to_acsii(im)
    print_ascii(am, color)

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Usage: ascii.py IMAGE [width] [algo] [invert]")
    else:
        img, *rest = args
        w = int(rest[0]) if rest else 100
        algo = rest[1] if len(rest) > 1 else "average"
        inv = rest[2].lower() == "invert" if len(rest) > 2 else False
        main(img, width=w, algo=algo, invert=inv, color=Fore.GREEN)