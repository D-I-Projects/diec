import re

def decode():
    with open("encoded.diec", 'r', encoding='utf-8') as file:
        encoded_string = file.read()

    with open("key.diec", 'r', encoding='utf-8') as file:
        key_string = file.read()

    initial_random_number = int(re.search(r'diec///(\d+)--', key_string).group(1))

    random_numbers = [int(num) for num in re.findall(r'-(\d+)', key_string)]

    binary_list = encoded_string.split()

    decoded_binary = []

    for idx, encoded_char in enumerate(binary_list):
        binary_text_numbers = int(encoded_char) - random_numbers[idx]

        original_number = binary_text_numbers - initial_random_number

        decoded_binary.append(str(original_number))

    decoded_binary_string = ''.join(decoded_binary)

    binary_values = [decoded_binary_string[i:i+8] for i in range(0, len(decoded_binary_string), 8)]
    
    decoded_text = ''.join([chr(int(bv, 2)) for bv in binary_values if len(bv) == 8])

    return decoded_text

if __name__ == "__main__":
    decoded_text = decode()
    print(decoded_text)
