# Day 1 - Python basics starter

def greet(name):
    return f"Hello, {name}! Welcome to Python."


def main():
    name = input("What's your name? ")
    print(greet(name))

    # try a few basics
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    print(f"Sum of {numbers} = {total}")


if __name__ == "__main__":
    main()
