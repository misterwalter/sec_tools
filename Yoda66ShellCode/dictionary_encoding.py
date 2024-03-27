## Encodes any text file into a much much larger text file
## Keys are randomly generated in an insecure way in the initialization step of each DictionaryEncoder
import random   ## Source of randomness, `secrets`` would probably be better for production, but this is a quick little thing.

from pprint import pprint   ## Makes everything more readable and beautiful.

BYTE_VALUES = 256   # Number of permutations possible within one byte

## class that can encode data into words and then decode it again
class DictionaryEncoder():
    ## Set up word list for this iteration
    def __init__(self):
        print("init" + __name__)
        full_word_list = ["word" + str(x) for x in range(100000)]   # Not bothering with a word list right now, this is just a concept
        
        self.word_key = random.sample(full_word_list, k=BYTE_VALUES)
        assert len(set(self.word_key)) == BYTE_VALUES               # Earlier on, this caught that duplicate keys were being used, corrupting data

    ## Encodes and then decodes an entire file.
    def encode_file(self, ciphertext_file_path):
        print("CIPHER FILE :: " + ciphertext_file_path)
        with open(ciphertext_file_path) as f:
            data = f.read()
            pprint(data)
            for i in range(len(data)):
                print(str(data[i]) + " == " + self.decode_word(self.encode_byte(data[i])))

    ## Converts a single byte into a codeword
    def encode_byte(self, character) -> str:
        #print("ENCODING :: " + str(character))
        return self.word_key[ord(character)]
    
    ## Converts a single codeword back to a byte
    def decode_word(self, line) -> bytes:
        #print("DECODING :: " + line)
        return chr(self.word_key.index(line))





if __name__ == "__main__":
    encoder = DictionaryEncoder()
    encoder.encode_file("ciphertext.txt")