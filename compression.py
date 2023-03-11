import gzip

class compress:
    def __init__(self, input):
        self.output = ""
        self.input = input

        self.compress_str()

    def compress_str(self):
        input_bytes = self.input.encode("utf-8")
        compressed_bytes = gzip.compress(input_bytes)

        for b in compressed_bytes:
            self.output += bin(b)[2:].zfill(8)

class decompress:
    def __init__(self, input):
        self.output = ""
        self.input = input

        self.decompress_str()

    def decompress_str(self):
        c_b = [self.input[i:i+8] for i in range(0, len(self.input), 8)]
        c_b = bytes([int(b, 2) for b in c_b])

        dc_b = gzip.decompress(c_b)

        self.output = dc_b.decode("utf-8")

if __name__ == "__main__":
    text = "Demo text for compression including numbers like 1 2 3"

    c = compress(text)

    dc = decompress(c.output)

    print("[INPUT] - ", len(c.input))
    print("[COMPRESSED] - ", len(c.output))
    print("[DECOMPRESSED] - ", dc.output)