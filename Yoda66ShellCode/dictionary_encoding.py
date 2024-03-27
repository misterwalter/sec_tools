## Encodes any text file into a much much larger text file
## Keys are randomly generated in an insecure way in the initialization step of each DictionaryEncoder
import random

from pprint import pprint

BYTE_VALUES = 256   # Number of permutations possible within one byte

class DictionaryEncoder():
    full_word_list = ["word" + str(x) for x in range(10000)]

    def __init__(self):
        print("init" + __name__)
        
        self.word_key = random.choices(self.full_word_list, k=BYTE_VALUES)
        pprint(self.word_key)

    def encode_file(self, ciphertext_file_path):
        print("CIPHER FILE :: " + ciphertext_file_path)
        with open(ciphertext_file_path) as f:
            lines = f.readlines()
            pprint(lines)
            for line in lines:
                print(line + " == " + self.decode_line(self.encode_line(line)))

    def encode_line(self, line) -> str:
        print("ENCODING :: " + line)
        return line
    
    def decode_line(self, line) -> str:
        print("DECODING :: " + line)
        return line





if __name__ == "__main__":
    encoder = DictionaryEncoder()
    encoder.encode_file("ciphertext.txt")