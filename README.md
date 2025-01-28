# Greeting Reward Program
This Python program takes a user input as a greeting and determines a reward based on the content of the greeting. The program checks whether the greeting starts with "hello" or the letter "h", and assigns a reward accordingly.

Requirements:
Python 3.x
How to Use:
Run the script.
When prompted, enter a greeting.
The program will check if the greeting starts with "hello" or "h".

Based on the input, the program will output one of the following rewards:
"$0" if the greeting starts with "hello".
"$20" if the greeting starts with the letter "h" (but not "hello").
"$100" if the greeting does not start with "h" or "hello".

Example:
Input:
Enter a greeting: hello there
Output:
$0

Input:
Enter a greeting: hi
Output:
$20

Input:
Enter a greeting: good morning
Output:
$100

How It Works:
The program asks the user to enter a greeting.
It strips any surrounding spaces and converts the greeting to lowercase for uniformity.
The program checks if the greeting starts with "hello" or just "h".
Depending on the input, it prints the appropriate reward: $0, $20, or $100.
