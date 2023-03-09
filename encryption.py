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
    "O": 41,
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

class ascii_input:
    def __init__(self, text, dictionary = DICTIONARY):
        self.output = ""
        self.input = text
        self.dictionary = dictionary

        self.foramt_ascii()
        self.ascii_to_code()
        self.code_to_binary()
        self.list_to_string()

    def foramt_ascii(self):
        self.output = self.input.replace(" ", "\s")
        self.output = self.output.replace(".", "\d")
        self.output = self.output.replace(",", "\c")
        self.output = self.output.replace("i", "ı")
        self.output = self.output.replace("ç", "c")
        self.output = self.output.replace("ö", "o")
        self.output = self.output.replace("ğ", "g")
        self.output = self.output.replace("ş", "s")
        self.output = self.output.replace("ü", "u")
        self.output = self.output.replace("İ", "I")
        self.output = self.output.replace("Ç", "C")
        self.output = self.output.replace("Ö", "O")
        self.output = self.output.replace("Ğ", "G")
        self.output = self.output.replace("Ş", "S")
        self.output = self.output.replace("Ü", "U")

        self.output += "\e"

    def ascii_to_code(self):
        out = []

        for i in self.output:
            out.append(self.dictionary[i])

        self.output = out

    def get_binary(self, d):
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

    def code_to_binary(self):
        out = []

        for i in self.output:
            out.append(self.get_binary(i))

        self.output = out

    def list_to_string(self):
        out = ""

        for i in self.output:
            out += i

        self.output = out

class binary_input:
    def __init__(self, text, dictionary = DICTIONARY):
        self.output = ""
        self.listed = [text[ind:ind+6] for ind in range(0, len(text), 6)]
        self.dictionary = self.reverse_dictionary(dictionary)

        self.binary_to_code()
        self.code_to_ascii()
        self.list_to_string()
        self.rformat_ascii()

    def binary_to_code(self):
        #5, 4, 3, 2, 1, 0
        #32, 16, 8, 4, 2, 1
        #63, 31, 15, 7, 3, 1

        out = []

        for text in self.listed:
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

            out.append(cache)

            try:
                if out[-2] == 0 and out[-1] == 5:
                    del out[-1]
                    del out[-1]

                    break

            except:
                pass

        self.output = out

    def code_to_ascii(self):
        out = []

        for i in self.output:
            out.append(self.dictionary[i])

        self.output = out

    def list_to_string(self):
        out = ""

        for i in self.output:
            out += i

        self.output = out

    def rformat_ascii(self):
        self.output = self.output.replace("\s", " ")
        self.output = self.output.replace("\d", ".")
        self.output = self.output.replace("\c", ",")

    def reverse_dictionary(self, dictionary):
        rDict = dict()

        for key in dictionary:
            val = dictionary[key]
            rDict[val] = key

        return rDict

if __name__ == "__main__":
    # Demo usage

    x = "Hello"
    y = "100010000101001100001100101001000000000101"

    p = ascii_input(x, DICTIONARY)
    print(p.output)

    y = binary_input(y, DICTIONARY)
    print(y.output)
