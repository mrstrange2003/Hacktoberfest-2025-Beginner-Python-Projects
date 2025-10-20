

def check_answer(question, answer, user_answer):
    """Check if user's answer is correct."""
    if user_answer.lower() == answer.lower():
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer is: {answer}\n")
        return False

def play_quiz():
    print(" Welcome to the Quiz Game!\n")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's get started.\n")

    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
            "answer": "A"
        },
        {
            "question": "Which programming language is known as the 'Language of AI'?",
            "options": ["A. Java", "B. Python", "C. C++", "D. JavaScript"],
            "answer": "B"
        },
        {
            "question": "Who developed the theory of relativity?",
            "options": ["A. Newton", "B. Galileo", "C. Einstein", "D. Tesla"],
            "answer": "C"
        },
        {
            "question": "What does HTML stand for?",
            "options": [
                "A. HyperText Markup Language",
                "B. HighText Machine Language",
                "C. Hyperloop Transfer Machine Language",
                "D. Hyperlink and Text Markup Language"
            ],
            "answer": "A"
        }
    ]

    score = 0

    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        for opt in q["options"]:
            print(opt)
        user_answer = input("Your answer (A/B/C/D): ")
        if check_answer(q["question"], q["answer"], user_answer):
            score += 1

    print(f" Quiz Over! You scored {score}/{len(questions)} points.")
    if score == len(questions):
        print(" Excellent! You're a quiz master!")
    elif score >= len(questions) // 2:
        print(" Good job! Keep learning!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    play_quiz()
