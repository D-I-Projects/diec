import random
from binaryconvert import convert

def encode(text):
    key_string = ["diec///"]
    random_number = random.randint(10**7, 10**8 - 1)
    key_string.append(str(random_number))
    key_string.append("--")
    
    bit = 8
    text_binary = convert.ToBinary(text, bit)
    binary_list = []

    for char in text_binary:
        if char.isdigit():
            binary_text_number = int(char) + random_number
            random_number_char = random.randint(10**7, 10**8 - 1)
            encoded_char = str(binary_text_number + random_number_char)
            key_string.append(f"-{random_number_char}")
            binary_list.append(encoded_char)

    encoded_string = ' '.join(binary_list)
    key_string = ''.join(key_string)

    with open("encoded.diec", 'w', encoding='utf-8') as file_encoded, open("key.diec", 'w', encoding='utf-8') as file_key:
        file_encoded.write(encoded_string)
        file_key.write(key_string)

    return encoded_string, key_string

if __name__ == "__main__":
    encode("I love python and I love to learn new things here too! <3")
