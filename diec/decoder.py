def decode():
    def read_key():
        with open("key.diec", 'r', encoding='utf-8') as file:
            content = file.read()
        return content

    def read_encoded():
        with open("encoded.diec", 'r', encoding='utf-8') as file:
            content = file.read()
        return content

    key = read_key()
    encoded = read_encoded()
    
    key = key.replace("diec///", "")
    
    initial_random_number, random_numbers_string = key.split("--", 1)
    random_numbers = random_numbers_string.split("-")[1:]
    
    encoded_list = encoded.split()
    
    decoded_binary_list = []
    for encoded_char, random_number_char in zip(encoded_list, random_numbers):
        original_binary = encoded_char[:-len(random_number_char)]
        original_binary = original_binary[:-len(initial_random_number)]
        decoded_binary_list.append(original_binary)
    
    decoded_binary = ''.join(decoded_binary_list)
    
    binary_values = [decoded_binary[i:i+8] for i in range(0, len(decoded_binary), 8)]
    
    try:
        decoded_text = ''.join([chr(int(bv, 2)) for bv in binary_values])
    except OverflowError as e:
        print(f"Error converting binary to text: {e}")
        return None
    
    return decoded_text

if __name__ == "__main__":
    decoded_text = decode()
    if decoded_text:
        print(f"Decoded text: {decoded_text}")
    else:
        print("Decoding failed.")
