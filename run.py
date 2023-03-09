from encryption import *
from imgprocess import *

def run():
    print("1: Encode text")
    print("2: Decode image")

    mode = input("Choice:    ")

    if mode == "1":
        encode()
    
    elif mode == "2":
        decode()

    else:
        print("Unregistered input.")

def encode():
    print("File path to text (eg: desktop/text.txt).")
    x = input("Path: ")
    print("Image save file path (eg: desktop/output.png).")
    y = input("Path: ")

    f = open(x)
    txt = f.read()
    f.close()

    p = ascii_input(txt)
    y = image_encode(p.output, 720, 1080, y)

    if y.error == "Insufficent pixels.":
        print("Insufficent pixels.")
        print("Should be at least '", y.alen, "' cells.")
        print("Currently '", y.pn, "'.")

def decode():
    print("File to decode from (eg: desktop/output.png).")
    x = input("Path: ")

    p = image_decode(x)

    y = binary_input(p.output)

    print(y.output)

run()