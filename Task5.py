if __name__ == "__main__":
    max_num = int(input("Input Ceiling: ")) # Ask the user for the ceiling to sum beneath
    sum_of_mod_one = sum(x for x in range(1, max_num) if max_num % x == 1)  # Take the sum of all numbers between 1 and the maximum number (not inclusive) that satisfy maxnum % x == 1
    print(sum_of_mod_one)   # display the sum of all numbers between 1 and max_num, such that max_num % x == 1