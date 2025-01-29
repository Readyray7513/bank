def main():
    # Prompt for greeting input
    greeting = input("Enter a greeting: ").strip().lower()

    # Check the greeting's condition
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

# Call the main function to run the program
main()
