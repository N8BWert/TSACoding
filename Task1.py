def factorial(x: int):
    # Finds the factorial of a number by multiplying each number from 1 to the desired number
    product = 1
    while x > 1:
        product *= x
        x -= 1
    return product

def primes(upper_bound: int):
    # Finds the prime numbers from 1 to the upper bound
    prime_list = []
    for num in range(1, upper_bound + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)
    return prime_list

def sum_of_powers(prime_num_list, frequency_list):
    # Finds the sum of each prime factor to the power of 0 through their frequency (ex: 2^0 + 2^1 + ... + 2^10)
    sum_list = [0] * len(prime_num_list)
    for i in range(0, len(sum_list)):
        for j in range(0, frequency_list[i] + 1):
            sum_list[i] += prime_num_list[i] ** j
    return sum_list

def list_product(list):
    # Finds the product of the elements of a list
    product = 1
    for element in list:
        product *= element
    return product

if __name__ == "__main__":
    x = int(input("Input an integer: "))    # Take the user's input and convert it to an integer
    x_factorial = factorial(x)  # Calculate the factorial of x
    prime_nums = primes(x)  # Find all of the prime numbers between 1 and x
    frequency_list = [0] * len(prime_nums) # Create an empty frequency list to assist in calculating the prime factorization of x!
    for prime_num in prime_nums:
        # Create a frequency list for the prime factorization of x!
        while x_factorial % prime_num == 0:
            x_factorial /= prime_num
            frequency_list[prime_nums.index(prime_num)] += 1
    list_of_sums = sum_of_powers(prime_nums, frequency_list)    # Find the sum of each power of the prime factor
    product = list_product(list_of_sums)    # calculate the product of the prime factor powers
    print(product)  # Print the result
    