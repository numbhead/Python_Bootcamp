from Caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(data, steps, dir):
    output = ""
    for char in data:
        if char in alphabet:
            position = alphabet.index(char)
            if dir == "encode":
                new_position = position + steps
                new_letter = alphabet[new_position%len(alphabet)]
            elif direction == "decode":
                new_position = position - steps
                new_letter = alphabet[new_position]
        else:
            new_letter = char
        output += new_letter
    
    print(f"The {direction}d text is {output}")
    
should_continue = "yes"
while should_continue == "yes" :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))%len(alphabet)
    caesar(text,shift,direction)
    should_continue = input("Type 'yes' if you want to go again or type 'no' to exit:\n").lower()
print("Good Bye!")
