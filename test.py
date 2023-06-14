import time

def print_slowly(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_user_input(prompt):
    return input(prompt)

def main():
    print_slowly("Welcome to the Impressive CLI Program!")
    name = get_user_input("What's your name? ")
    print_slowly(f"Hello, {name}!")
    age = get_user_input("How old are you? ")
    print_slowly(f"Wow, {age} years old!")
    favorite_color = get_user_input("What's your favorite color? ")
    print_slowly(f"{favorite_color} is a fantastic choice!")
    print_slowly("Thank you for using the Impressive CLI Program. Goodbye!")

if __name__ == '__main__':
    main()

