alphabet = ['a','b','c','d','e',
'f','g','h','i','j','k','l',
'm','n','o','p','q','r','s',
't','u','v','w','x','y','z']



#Part 1
# initial attempt/solution
def encrypt(plain_text,shift_amount):
    message_list = []
    for letter in plain_text:
        message_list += letter
    print(message_list)
    shifted_alphabet = []
    for position in range(shift_amount, len(alphabet)):
        shifted_alphabet += alphabet[position]
    print(shifted_alphabet)
    encrypted_message = ""
    for position in range(len(alphabet)):
        for letter in plain_text: #for positions in range(len(message_list)):
            if letter == alphabet[position]: #if message_list[positions] == alphabet[position]:
                encrypted_message += shifted_alphabet[position]
    # print(f" Your encrypted message is {encrypted_message}") 

    #The code bellow shows the same method of encrypting the user word, but this time using python methods
    encoded_text =""
    for letter in plain_text:
        index_letter =alphabet.index(letter)
        # print(f"The letter is {letter} and the index is {index_letter}")
        new_index = index_letter + shift_amount
        # print(f"The new index is {new_index}")
        # new_letter = alphabet[new_index]
        encoded_text += alphabet[new_index]
    print(f"The encoded text is {encoded_text}")

def decrypt(plain_text,shift_amount):
    decoded_text = ""
    for letter in plain_text:
        index_of_letter = alphabet.index(letter)
        # print(index_of_letter)
        new_index = (index_of_letter + 26)-shift_amount
        # print(alphabet[new_index])
        decoded_text += alphabet[new_index]
    print(f"the decoded text is {decoded_text}")


#Part 2
#bellow is a simplification of the whole program

def caesar(start_text,shift_amount, cipher_direction):
    new_text =""
    for letter in start_text:
        index_letter =alphabet.index(letter)
        if cipher_direction =="encode":
            new_index = index_letter + shift_amount
            new_text += alphabet[new_index]
            message = "encoded"
        elif cipher_direction =="decode":
            new_index = index_letter - shift_amount
            new_text += alphabet[new_index]
            message = "decoded"
    print(f"The {message} text is {new_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt ")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))


caesar(start_text = text,shift_amount =shift, cipher_direction = direction)