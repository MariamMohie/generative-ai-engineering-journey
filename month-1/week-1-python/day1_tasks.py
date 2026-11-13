#? Function 1
def greeting(name):
    return f"Hello, {name}!"

#? Function 2
def add_numbers(x, y):
    return x + y

#? Function 3
def max(numbers):
    if not numbers:
        return None  
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

#? Function 4
def num_of_words(sentence):
    words = sentence.split()
    return len(words)

#? Function 5
def mid_of_degree(degrees):
    if not degrees:
        return None  
    mid_degree = sum(degrees) / len(degrees)
    return mid_degree

# print(greeting("Mariam"))  #? This will return the string "Hello, Alice!"
# print(add_numbers(5, 3))  #? This will return the integer 8
# print(max([1, 5, 3, 9, 2]))  #? This will return the integer 9
# print(num_of_words("Hello, my dog is cute"))  #? This will return the integer 5
# print(mid_of_degree([1, 2, 3, 4, 5]))  #? This will return the float 3.0

#? guessing game and the user has  only 5 attemps
def guessing_game():
    import random
    number = random.randint(1, 10)
    attempts = 5

    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 10.")
    print(f"You have {attempts} attempts to guess the number.")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            return
        attempts -= 1
        print(f"You have {attempts} attempts left.")

    print(f"Sorry, you've run out of attempts. The number was {number}.")

guessing_game()



