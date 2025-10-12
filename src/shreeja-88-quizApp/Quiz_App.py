import tkinter as tk
from tkinter import messagebox
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# -----------------------------
# Question Bank
# -----------------------------
QUESTION_BANK = [
    {
        "q": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Power Unit",
            "Central Performance Utility",
            "Compute Process Utility",
        ],
        "answer": 0,
    },
    {
        "q": "Which data structure uses FIFO order?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": 1,
    },
    {
        "q": "What is the output of 2 ** 3 in Python?",
        "options": ["5", "6", "8", "9"],
        "answer": 2,
    },
    {
        "q": "HTTP status 404 means?",
        "options": ["OK", "Created", "Not Found", "Forbidden"],
        "answer": 2,
    },
    {
        "q": "Which of these is NOT a programming paradigm?",
        "options": ["Object-Oriented", "Functional", "Procedural", "Hypothetical"],
        "answer": 3,
    },
]

SHUFFLE_QUESTIONS = True
SHUFFLE_OPTIONS = True

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        

        self.questions = [self.prepare_question(q) for q in QUESTION_BANK]
        if SHUFFLE_QUESTIONS:
            random.shuffle(self.questions)

        self.current_q = 0
        self.score = 0
        self.user_answers = []  # store user selections

        self.q_label = tk.Label(root, text="", wraplength=400, justify="left", font=("Arial", 12), bg="#EDCBD2")
        self.q_label.pack(pady=20)

        self.var = tk.IntVar(value=-1)
        self.opts = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.var, value=i, font=("Arial", 11),)
            rb.pack(anchor="w", padx=20, pady=2)
            self.opts.append(rb)

        self.submit_btn = tk.Button(root, text="Submit", command=self.check_answer,bg="#80C4B7")
        self.submit_btn.pack(pady=20)

        self.load_question()

    def prepare_question(self, item):
        options = list(item["options"])
        mapping = list(range(len(options)))
        if SHUFFLE_OPTIONS:
            random.shuffle(mapping)
            options = [options[i] for i in mapping]
            correct_new_index = mapping.index(item["answer"])
        else:
            correct_new_index = item["answer"]
        return {"q": item["q"], "options": options, "answer": correct_new_index}

    def load_question(self):
        if self.current_q < len(self.questions):
            q = self.questions[self.current_q]
            self.q_label.config(text=f"Q{self.current_q+1}. {q['q']}")
            self.var.set(-1)
            for i, opt in enumerate(q["options"]):
                self.opts[i].config(text=opt)
        else:
            self.show_results()

    def check_answer(self):
        sel = self.var.get()
        if sel == -1:
            messagebox.showwarning("No selection", "Please select an answer.")
            return

        q = self.questions[self.current_q]
        self.user_answers.append(sel)

        if sel == q["answer"]:
            self.score += 1

        self.current_q += 1
        self.load_question()

    def show_results(self):
        result_window = tk.Toplevel(self.root)
        result_window.title("Quiz Results")

        score_label = tk.Label(result_window, text=f"Your Score: {self.score}/{len(self.questions)}", font=("Arial", 14),bg="#EDCBD2")
        score_label.pack(pady=20)

        # Pie chart
        fig, ax = plt.subplots(figsize=(2, 2))
        labels = ["Correct", "Wrong"]
        sizes = [self.score, len(self.questions) - self.score]
        colors = ["#4CAF50", "#F44336"]
        ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")

        canvas = FigureCanvasTkAgg(fig, master=result_window)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10)

        # Review Section
        review_label = tk.Label(result_window, text="Review:", font=("Arial", 12, "bold"),bg="#EDCBD2")
        review_label.pack(pady=10)

        for i, q in enumerate(self.questions):
            frame = tk.Frame(result_window)
            frame.pack(anchor="w", padx=10, pady=5, fill="x")

            q_text = tk.Label(frame, text=f"Q{i+1}. {q['q']}", wraplength=400, justify="left", font=("Arial", 11, "bold"))
            q_text.pack(anchor="w")

            user_ans = self.user_answers[i]
            correct_ans = q["answer"]

            user_text = q["options"][user_ans] if user_ans != -1 else "Not answered"
            correct_text = q["options"][correct_ans]

            ans_label = tk.Label(frame, text=f"Your Answer: {user_text}", fg=("green" if user_ans == correct_ans else "red"), font=("Arial", 10))
            ans_label.pack(anchor="w")

            if user_ans != correct_ans:
                corr_label = tk.Label(frame, text=f"Correct Answer: {correct_text}", fg="green", font=("Arial", 10, "italic"))
                corr_label.pack(anchor="w")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


