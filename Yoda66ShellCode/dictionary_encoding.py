## Encodes any text file into a much much larger text file
## Keys are randomly generated in an insecure way in the initialization step of each DictionaryEncoder
import random

from pprint import pprint

BYTE_VALUES = 256   # Number of permutations possible within one byte

class DictionaryEncoder():
    

    def __init__(self):
        print("init" + __name__)
        full_word_list = ["word" + str(x) for x in range(100000)]
        
        self.word_key = random.sample(full_word_list, k=BYTE_VALUES)
        print(len(set(self.word_key)))

    def encode_file(self, ciphertext_file_path):
        print("CIPHER FILE :: " + ciphertext_file_path)
        with open(ciphertext_file_path) as f:
            data = f.read()
            pprint(data)
            for i in range(len(data)):
                print(str(data[i]) + " == " + self.decode_line(self.encode_line(data[i])))

    def encode_line(self, character) -> str:
        #print("ENCODING :: " + str(character))
        return self.word_key[ord(character)]
    
    def decode_line(self, line) -> bytes:
        #print("DECODING :: " + line)
        return chr(self.word_key.index(line))





if __name__ == "__main__":
    encoder = DictionaryEncoder()
    encoder.encode_file("ciphertext.txt")