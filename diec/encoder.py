import random
from binaryconvert import convert

def encode(text):
    key_string = "diec///" 
    random_number = random.randint(10**31, 10**32 - 1)
    key_string += str(random_number)
    key_string += ("--")
    text_binary = convert.ToBinary(text)
    binary_list = []

    for char in text_binary:
        binary_text_numbers = char + str(random_number)
        random_number_char = random.randint(10**31, 10**32 - 1)
        encoded_char = binary_text_numbers + str(random_number_char)
        key_string += f"-{random_number_char}" 
        binary_list.append(encoded_char)

    with open("key.diec", 'w', encoding='utf-8') as file:
        file.write(key_string)

    print(binary_list)
    return ' '.join(binary_list), key_string

if __name__ == "__main__":
    encode("I love python and I love to learn new things here too! <3")