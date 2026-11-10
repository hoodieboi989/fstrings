def greet():
    name = input("what is your name? ")
    food = input("whats your favorite food? ")
    print(f"hey {name} i heard you like {food}")

def calculations():
    num1 = int(input("give me a number: "))
    num2 = int(input("give me on more:")) 
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")

def caps(name):
    a_name = name.title()
    b_name = name.upper()
    print(f"name in title: {a_name}")
    print(f"name in upper: {b_name}")

def format(num):
    print(f"formatted: {num:.2f}")

def main():
    greet()
    calculations()
    caps("matt")
    format(3.286562837856345)

if __name__ == "__main__":
    main()