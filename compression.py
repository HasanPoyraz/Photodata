DECODE = [" ", "the", "e", "t", "a", "of", "o", "and", "i", "n", "s", "e ", "r", " th",
          " t", "in", "he", "th", "h", "he ", "to", "\r\n", "l", "s ", "d", " a", "an",
          "er", "c", " o", "d ", "on", " of", "re", "of ", "t ", ", ", "is", "u", "at",
          "   ", "n ", "or", "which", "f", "m", "as", "it", "that", "\n", "was", "en",
          "  ", " w", "es", " an", " i", "\r", "f ", "g", "p", "nd", " s", "nd ", "ed ",
          "w", "ed", "http://", "for", "te", "ing", "y ", "The", " c", "ti", "r ", "his",
          "st", " in", "ar", "nt", ",", " to", "y", "ng", " h", "with", "le", "al", "to ",
          "b", "ou", "be", "were", " b", "se", "o ", "ent", "ha", "ng ", "their", "\"",
          "hi", "from", " f", "in ", "de", "ion", "me", "v", ".", "ve", "all", "re ",
          "ri", "ro", "is ", "co", "f t", "are", "ea", ". ", "her", " m", "er ", " p",
          "es ", "by", "they", "di", "ra", "ic", "not", "s, ", "d t", "at ", "ce", "la",
          "h ", "ne", "as ", "tio", "on ", "n t", "io", "we", " a ", "om", ", a", "s o",
          "ur", "li", "ll", "ch", "had", "this", "e t", "g ", "e\r\n", " wh", "ere",
          " co", "e o", "a ", "us", " d", "ss", "\n\r\n", "\r\n\r", "=\"", " be", " e",
          "s a", "ma", "one", "t t", "or ", "but", "el", "so", "l ", "e s", "s,", "no",
          "ter", " wa", "iv", "ho", "e a", " r", "hat", "s t", "ns", "ch ", "wh", "tr",
          "ut", "/", "have", "ly ", "ta", " ha", " on", "tha", "-", " l", "ati", "en ",
          "pe", " re", "there", "ass", "si", " fo", "wa", "ec", "our", "who", "its", "z",
          "fo", "rs", ">", "ot", "un", "<", "im", "th ", "nc", "ate", "><", "ver", "ad",
          " we", "ly", "ee", " n", "id", " cl", "ac", "il", "</", "rt", " wi", "div",
          "e, ", " it", "whi", " ma", "ge", "x", "e c", "men", ".com"]

def encapsulate(input_list):
    output = []
    output_append = output.append
    output_extend = output.extend

    for chunk in (input_list[i:i+255] for i in range(0, len(input_list), 255)):
        if 1 == len(chunk):
            output_append(chr(255))
            output_extend(chunk)

        else:
            output_extend((chr(255), chr(len(chunk) - 1)))
            output_extend(chunk)
    return output

def trie(decode_table):
    empty_node = list(None for _ in range(0, 256))
    root_node = list(empty_node)
    if not decode_table:
        raise ValueError('Empty data passed to make_tree')
    elif len(decode_table) > 254:
        raise ValueError('Too long list in make tree: %d' % len(decode_table))
    else:
        for enc_byte, sstr in enumerate(decode_table):
            node_ptr = root_node
            for str_pos, ch in enumerate(sstr):
                if node_ptr[ord(ch)]:  
                    terminal_byte, children = node_ptr[ord(ch)]
                    if len(sstr) == str_pos + 1: 
                        if not terminal_byte:
                            node_ptr[ord(ch)] = [chr(enc_byte), children]
                            break
                        else:
                            raise ValueError('Unexpected terminal: duplicates in data (%s) (%s) (%s)' %
                                             (sstr, ch, node_ptr))
                    node_ptr = children
                else:  
                    if len(sstr) == str_pos + 1: 
                        node_ptr[ord(ch)] = [chr(enc_byte), list(empty_node)]
                    else:
                        node_ptr[ord(ch)] = [None, list(empty_node)]
                        _, node_ptr = node_ptr[ord(ch)]
    stack = list(root_node)
    while stack:
        node_ptr = stack.pop()
        if node_ptr:
            _, children = node_ptr
            if children == empty_node:
                node_ptr[1] = None  
            else:
                stack.extend(children)
    return root_node

def compress(input):
    tree_node = (None, None)
    output = []
    unmatched = []

    SMAZ_TREE = trie(DECODE)

    output_extend = output.extend
    output_append = output.append

    pos = 0

    while pos < len(input):
        tree_ptr = SMAZ_TREE
        enc_byte = None
        j = 0
        while j < len(input) - pos:
            byte_val, tree_ptr = tree_ptr[ord(input[pos + j])] or tree_node
            j += 1
            if byte_val is not None:
                enc_byte = byte_val
                enc_len = j
            if not tree_ptr:
                break

        if enc_byte is None:
            unmatched.append(input[pos])
            pos += 1
        else:
            pos += enc_len
            if unmatched:
                output_extend(encapsulate(unmatched))
                unmatched = []
            output_append(enc_byte)
    if unmatched:
        output_extend(encapsulate(unmatched))

    return "".join(output)

if __name__ == "__main__":
    x = "Demo for text Hello world 12 times!"

    c = compress(x)

    print(c)

    for i in c:
        print(ord(i), end="")