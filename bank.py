def value(greeting):
    # Convert the greeting to lowercase for case-insensitivity
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

def main():
    greeting = input("Enter a greeting: ").strip()
    result = value(greeting)
    print(f"{result}")

if __name__ == "__main__":
    main()

