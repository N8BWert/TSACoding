def absolute_value(x: int):
    if x < 0:
        return -x
    else:
        return x

if __name__ == "__main__":
    num_people = int(input("How many people: "))   # Recieve from the user the integer corresponding to the number of people in the hallway
    num_switches = int(input("How many switches: ")) # Recieves from the user the integer corresopnding to the number of switches in the hallway
    switches = [0] * num_switches   # Create a list representing the states of the switches (0 = off, 1 = on)
    # Iterate through the numbered people and reverse the status of a switch if the switch number is divisible by the person's number
    for i in range(1, num_people + 1):
        for j in range(0, num_switches):
            if (j + 1) % i == 0:
                switches[j] = absolute_value(switches[j] - 1)
    print(sum(switches))    # Because all on switches are represented as 1s the sum of the switches list will be the number of switches turned on
