"""Simple demo script for printing and a small function."""

def greet(person):
    return "Hello " + person


def main():
    # Hello World in Python
    print("Hello, Tsetse!")

    # Variables
    age = 18
    name = "Tsetse"
    print("My name is", name, "and I am", age, "years old.")

    # Loop
    for i in range(5):
        print("Loop number:", i)

    # Function usage
    print(greet("Gegeenee"))


if __name__ == "__main__":
    main()
