allowed_input = [
    "\\",
    "\n",
    ".",
    ",",
    " ",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

class foramt_input:
    def __init__(self, text):
        self.output = ""
        self.text = text
        self.dict = allowed_input

        self.replacer()

    def replacer(self):
        for c in self.text:
            if c in self.dict:
                self.output += c

if __name__ == "__main__":
    text = "Text with invalid Chars like !?}"

    fi = foramt_input(text)

    print(fi.output)
