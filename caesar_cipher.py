alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

exit_status = ""

while exit_status != True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    def caesar(plain_text, shift_amount):
        if direction == "encode":
            cipher_text = ""
            for letter in plain_text:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                cipher_text += alphabet[new_position % 26]
            print(f"The encoded text is {cipher_text}")
        elif direction == "decode":
            cipher_text = ""
            for letter in plain_text:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                cipher_text += alphabet[new_position % 26]
            print(f"The decoded text is {cipher_text}")

    caesar(plain_text=text, shift_amount=shift)
    exit_status = int(input("Type 1 to exit, type 0 to continue:\n"))
    if exit_status == 1:
        exit_status = True
    else:
        exit_status = False