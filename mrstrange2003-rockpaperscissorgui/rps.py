import tkinter as tk
import random

CHOICES = ["Rock", "Paper", "Scissors"]
WIN_TARGET = 3

def winner(player, computer):
    if player == computer:
        return "Tie"
    if (player == "Rock" and computer == "Scissors") or \
       (player == "Paper" and computer == "Rock") or \
       (player == "Scissors" and computer == "Paper"):
        return "Player"
    return "Computer"

def updatelabel():
    player_score_label.config(text=f"Player: {player_score.get()}")
    computer_score_label.config(text=f"Computer: {computer_score.get()}")
    rounds_label.config(text=f"Rounds played: {rounds_played.get()}")

def disablebuttons():
    rock_btn.config(state="disabled")
    paper_btn.config(state="disabled")
    scissors_btn.config(state="disabled")

def enablebuttons():
    rock_btn.config(state="normal")
    paper_btn.config(state="normal")
    scissors_btn.config(state="normal")

def displayresult():
    if player_score.get() > computer_score.get():
        result_msg = "You won the match!"
    elif player_score.get() < computer_score.get():
        result_msg = "Computer won the match!"
    else:
        result_msg = "Match ended in a tie!"
    final_label.config(text=result_msg)
    disablebuttons()

def play(player_choice):
    if player_score.get() >= WIN_TARGET or computer_score.get() >= WIN_TARGET:
        return
    comp_choice = random.choice(CHOICES)
    computer_choice_label.config(text=f"Computer chose: {comp_choice}")
    result = winner(player_choice, comp_choice)
    if result == "Tie":
        round_result_label.config(text="It's a tie!")
    elif result == "Player":
        round_result_label.config(text="You win this round!")
        player_score.set(player_score.get() + 1)
    else:
        round_result_label.config(text="Computer wins this round!")
        computer_score.set(computer_score.get() + 1)
    rounds_played.set(rounds_played.get() + 1)
    updatelabel()
    if player_score.get() >= WIN_TARGET or computer_score.get() >= WIN_TARGET:
        displayresult()

def reeset():
    player_score.set(0)
    computer_score.set(0)
    rounds_played.set(0)
    computer_choice_label.config(text="Computer chose: —")
    round_result_label.config(text="Make your move!")
    final_label.config(text="")
    enablebuttons()
    updatelabel()

root = tk.Tk()
root.title("Rock • Paper • Scissors — Best of 5")
root.geometry("420x340")
root.resizable(False, False)
root.configure(padx=12, pady=12)

title = tk.Label(root, text="Rock • Paper • Scissors", font=("Helvetica", 16, "bold"))
title.pack(pady=(0, 10))

frame_scores = tk.Frame(root)
frame_scores.pack(pady=(0, 8))

player_score = tk.IntVar(value=0)
computer_score = tk.IntVar(value=0)
rounds_played = tk.IntVar(value=0)

player_score_label = tk.Label(frame_scores, text=f"Player: {player_score.get()}", font=("Helvetica", 12))
player_score_label.grid(row=0, column=0, padx=10)

computer_score_label = tk.Label(frame_scores, text=f"Computer: {computer_score.get()}", font=("Helvetica", 12))
computer_score_label.grid(row=0, column=1, padx=10)

rounds_label = tk.Label(frame_scores, text=f"Rounds played: {rounds_played.get()}", font=("Helvetica", 11))
rounds_label.grid(row=1, column=0, columnspan=2, pady=(6,0))

divider = tk.Frame(root, height=2, bd=1, relief="sunken")
divider.pack(fill="x", pady=8)

info_frame = tk.Frame(root)
info_frame.pack(pady=(0, 8))

computer_choice_label = tk.Label(info_frame, text="Computer chose: —", font=("Helvetica", 12))
computer_choice_label.pack()

round_result_label = tk.Label(info_frame, text="Make your move!", font=("Helvetica", 12, "italic"))
round_result_label.pack(pady=(4,0))

final_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"))
final_label.pack(pady=(6, 6))

btn_frame = tk.Frame(root)
btn_frame.pack(pady=(4, 10))

rock_btn = tk.Button(btn_frame, text="Rock", width=12, height=2, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=6)

paper_btn = tk.Button(btn_frame, text="Paper", width=12, height=2, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=6)

scissors_btn = tk.Button(btn_frame, text="Scissors", width=12, height=2, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=6)

control_frame = tk.Frame(root)
control_frame.pack(pady=(8,0))

reset_btn = tk.Button(control_frame, text="Reset Match", width=12, command=reeset)
reset_btn.grid(row=0, column=0, padx=8)

exit_btn = tk.Button(control_frame, text="Exit", width=12, command=root.destroy)
exit_btn.grid(row=0, column=1, padx=8)

updatelabel()
root.mainloop()
