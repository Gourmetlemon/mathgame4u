import random

# Function to generate a random math question
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"
    answer = eval(question)
    return question, answer

def main():
    while True:
        question, correct_answer = generate_question()
        print(f"Solve: {question}")
        
        # Get the user's answer
        user_answer = input("Your answer: ")
        
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print("Game Over")
            break

if __name__ == "__main__":
    main()