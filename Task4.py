def list_to_string(input_list):
    # Takes a list and iterates over it to convert it to a string
    string = ""
    for element in input_list:
        string += element
    return string

if __name__ == "__main__":
    encoded_string = str(input("Enter Encrypted String: ")) # Takes the encoded_string as input from the user (ex: ZEZLPRNWDDKVAWLCXAYAYWORINKLADYPRNDKZZAFDXDNRGE)
    key_string = str(input("Enter Key String: "))   # Takes the key_string from user input (ex: QWERTYUIOPQWERTYUIOPQWERTYUIOPQWERTYUIOPQWERTYU)
    distance_apart = [ord(character) - ord("A") for character in key_string] # Calculates the distance each character of the key_string is from the start of the alphabet
    for i in range(0, len(encoded_string)):
        # Assuming that N, the 13th letter of the alphabet, is the center point the distance from "A" is converted into a bidirectional form
        if distance_apart[i] > 13:
            distance_apart[i] = -distance_apart[i] + 26
    decoded_string_list = []
    for j in range(0, len(encoded_string)):
        # Each letter in the encoded_string is now shifted its associated distance apart to the left, wrapping the alphabet if the new order is less than that of "A"
        if ord(encoded_string[j]) - distance_apart[j] >= ord("A"):
            decoded_string_list.append(chr(ord(encoded_string[j]) - distance_apart[j]))
        else:
            decoded_string_list.append(chr(ord(encoded_string[j]) - distance_apart[j] + 26))
    decoded_string = list_to_string(decoded_string_list)    # Convets the decoded_string_list into a printable string
    print(decoded_string)   # displays the decoded string (ex: PAVCIPHORSARWNEARSMPOSKIBLEDOSOLNEWITROUTTZEKEY = Pad ciphers are near impossible to solve without a key)
    