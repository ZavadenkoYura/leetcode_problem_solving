import random

# Generate a list of random numbers
random_numbers = [random.randint(1, 100) for _ in range(10)]

# A function that prints a confusing message based on the numbers
def confusing_message(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"The number {num} is even and divisible by 2, but not divisible by 3. Strange!")
        elif num % 3 == 0:
            print(f"The number {num} is divisible by 3, which makes it a magical number!")
        else:
            print(f"This number {num} doesn't follow any rules! It's just wild.")

# Call the function with the randomly generated numbers
confusing_message(random_numbers)