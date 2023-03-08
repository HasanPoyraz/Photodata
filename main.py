from matplotlib import pyplot
from matplotlib import colors

DICTIONARY = {
    "\\": 0,
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "o": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 52,
    "Z": 53,
    "0": 54,
    "1": 55,
    "2": 56,
    "3": 57,
    "4": 58,
    "5": 59,
    "6": 60,
    "7": 61,
    "8": 62,
    "9": 63,
}

# Sub functions

def format_ascii(input):
    output = input.replace(" ", "\s")
    output = output.replace(".", "\d")
    output = output.replace(",", "\c")
    output = output.replace("ı", "i")
    output = output.replace("ç", "c")
    output = output.replace("ö", "o")
    output = output.replace("ğ", "g")
    output = output.replace("ş", "s")
    output = output.replace("ü", "u")

    output += "\e"

    return output

def ascii_to_code(input, dictionary):
    output = []

    for i in input:
        output.append(dictionary[i])

    return output

def get_binary(d):
    #5, 4, 3, 2, 1, 0
    #32, 16, 8, 4, 2, 1
    #63, 31, 15, 7, 3, 1
    
    output = "" # 6 * 0/1
    
    if d >= 32:
        output += "1"
        d -= 32
    else:
        output += "0"
    
    if d >= 16:
        output += "1"
        d -= 16
    else:
        output += "0"

    if d >= 8:
        output += "1"
        d -= 8
    else:
        output += "0"

    if d >= 4:
        output += "1"
        d -= 4
    else:
        output += "0"

    if d >= 2:
        output += "1"
        d -= 2
    else:
        output += "0"

    if d >= 1:
        output += "1"
        d -= 1
    else:
        output += "0"

    return output

def code_to_binary(input):
    output = []

    for i in input:
        output.append(get_binary(i))

    return output

def list_to_string(input):
    output = ""
    
    for i in input:
        output += i

    return output

def binary_to_code(input):
    #5, 4, 3, 2, 1, 0
    #32, 16, 8, 4, 2, 1
    #63, 31, 15, 7, 3, 1

    output = []

    for text in input:
        cache = 0

        if text[0] == "1":
            cache += 32
        
        if text[1] == "1":
            cache += 16
        
        if text[2] == "1":
            cache += 8

        if text[3] == "1":
            cache += 4

        if text[4] == "1":
            cache += 2

        if text[5] == "1":
            cache += 1

        output.append(cache)

        try:
            if output[-2] == 0 and output[-1] == 5:
                del output[-1]
                del output[-1]

                return output
        except:
            pass

    return output

def reverse_dictionary(dictionary):
    rDict = dict()

    for key in dictionary:
        val = dictionary[key]
        rDict[val] = key

    return rDict

def code_to_ascii(text, dictionary):
    output = []

    for i in text:
        output.append(dictionary[i])

    return output

def rformat_ascii(text):
    text = text.replace("\s", " ")
    text = text.replace("\d", ".")
    text = text.replace("\c", ",")

    return text

def text_to_immage_array(text, cx, rx): 
    array = [[0]*rx for _ in range(cx)]
    i = 0

    for c in range(cx):
        for r in range(rx):
            try:
                array[c][r] = int(text[i])

            except:
                array[c][r] = 0
            
            i += 1

    return array

def array_to_image(array):
    pyplot.figure(figsize=(5,5))
    colormap = colors.ListedColormap(["white", "black"])
    pyplot.title("Data Matrix")

    pyplot.imshow(array, cmap=colormap)
    pyplot.show()

# Main functions

def ascii_input(text, dictionary):
    text = format_ascii(text)
    text = ascii_to_code(text, dictionary)
    text = code_to_binary(text)
    text = list_to_string(text)

    return text

def binary_input(text, dictionary):
    text = [text[ind:ind+6] for ind in range(0, len(text), 6)]

    dictionary = reverse_dictionary(dictionary)
    
    text = binary_to_code(text)
    text = code_to_ascii(text, dictionary)
    text = list_to_string(text)
    text = rformat_ascii(text)

    return text

def image_encode(array, c, r):
    x = len(array)
    if x > (c * r):
        print("Insufficent pixels.")
        print("Should be at least '", x, "' cells.")
        print("Currently '", c*r, "'.")

    else:
        array = text_to_immage_array(array, c, r)
        array_to_image(array)

# Demo Usage

f = open("text.txt", "r")
text = f.read()
f.close()

x1 = ascii_input(text, DICTIONARY) # Ascii to binary

x2 = image_encode(x1, 720, 1080) # Binary to image

x3 = binary_input(x1, DICTIONARY) # Binarry to ascii