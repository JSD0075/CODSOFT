import random
import string

def generate_random_string(length):
    try:
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string
    except ValueError:
        return None

while True:
    try:
        length = int(input("Enter the Length of Password: "))
        if length > 0:
            random_string = generate_random_string(length)
            if random_string:
                print(f'Your Password of length {length} is {random_string}')
                break
            else:
                print("Invalid input. Please enter a positive integer.")
        else:
            print("Invalid input. Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")