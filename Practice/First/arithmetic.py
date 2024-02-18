user_input = input("Solve the expression: 4 * 100 - 54 = ")

correct_answer = 4 * 100 - 54

try:
    user_answer = int(user_input)
    print("Correct answer:", correct_answer)
    print("Your answer:", user_answer)
except ValueError:
    print("Invalid input! Please enter a valid integer.")