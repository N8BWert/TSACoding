def create_perfect_square_list(max_num: int):
    # incriment from 1 to the highest number such that that number squared is less than 1000 and add each numbers square to a list
    squares, index = [], 1
    while index ** 2 < max_num:
        squares.append(index ** 2)
        index += 1
    return squares

if __name__ == "__main__":
    max_num = int(input())  # Recieve the user's input as an integer
    perfect_squares = create_perfect_square_list(max_num)   # Craft a list of the perfect squares between 1 and the input number
    sum_of_perfect_squares = sum(perfect_squares)   # Take the sum of the elements in the perfect_sqaures list and store them as a new variable
    print(sum_of_perfect_squares)   # Display the sum of the perfect squares between 1 and the maximum number
