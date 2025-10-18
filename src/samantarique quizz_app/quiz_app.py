def ask_question(q):

    print(f"\n{q['question']}")
    for i, option in enumerate(q['options'], start=1):
        print(f"{i}) {option}")

    # First attempt
    answer = int(input("Enter the correct option number: "))
    if answer == q['correct']:
        print(" Correct Answer!")
        return 1
    else:
        print(" Wrong Answer!")
        
        retry = input("Do you want to try again? (yes/no): ").lower()
        if retry == "yes":
            answer = int(input("Enter again: "))
            if answer == q['correct']:
                print("Correct this time!")
                return 1
            else:
                print(f" Wrong again! The correct answer was '{q['options'][q['correct'] - 1]}'.")
                return 0
        else:
            print(f" The correct answer was '{q['options'][q['correct'] - 1]}'.")
            return 0



quiz = [
    {
        "question": "Q1. What is your name?",
        "options": ["Saman", "Atsham", "Alina"],
        "correct": 1
    },
    {
        "question": "Q2. Which programming language are we using?",
        "options": ["C++", "Python", "Java"],
        "correct": 2
    },
    {
        "question": "Q3. What symbol is used to start a comment in Python?",
        "options": ["//", "#", "/* */"],
        "correct": 2
    }
]

# ---------------------- QUIZ LOOP ----------------------
print(" Welcome to the Python Quiz App ")
score = 0

for q in quiz:
    score += ask_question(q)

# ---------------------- RESULTS ----------------------
total = len(quiz)
print("\n Quiz Completed!")
print(f" Correct Answers: {score}")
print(f" Wrong Answers: {total - score}")
print(f"Final Score: {score}/{total}")

if score == total:
    print(" Excellent! You nailed it!")
elif score >= total / 2:
    print(" Good job! Keep practicing.")
else:
    print(" Better luck next time!")

