


# rps_gui.py
import tkinter as tk
from tkinter import ttk, messagebox
import random
import os

# ==============================
# 1. Main Window
# ==============================
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("800x400")
root.configure(bg="#2c3e50")  # dark blue-gray
root.resizable(False, False)

# ==============================
# 2. Title
# ==============================
title = ttk.Label(
    root,
    text=" Rock Paper Scissors",
    font=("Helvetica", 20, "bold"),
    foreground="#ecf0f1",
    background="#2c3e50"
)
title.pack(pady=20)

# ==============================
# 3. Choice Frame (Radio Buttons)
# ==============================
choice_frame = ttk.Frame(root)
choice_frame.pack(pady=10)

# Radio button variable
choice_var = tk.StringVar(value="Rock")

# Create 3 radio buttons
ttk.Radiobutton(choice_frame, text="Rock", variable=choice_var, value="Rock").pack(side="left", padx=20)
ttk.Radiobutton(choice_frame, text="Paper", variable=choice_var, value="Paper").pack(side="left", padx=20)
ttk.Radiobutton(choice_frame, text="Scissors", variable=choice_var, value="Scissors").pack(side="left", padx=20)

# ==============================
# 4. Play Button
# ==============================
play_btn = ttk.Button(root, text="Play", style="Play.TButton")
play_btn.pack(pady=15)

# ==============================
# 5. Result Display
# ==============================

# Frame to hold result labels
result_frame = ttk.Frame(root)
result_frame.pack(pady=10, fill="x", padx=30)

user_label = ttk.Label(result_frame, text="", font=("Arial", 12), foreground="#000000")
user_label.pack(anchor="w")

comp_label = ttk.Label(result_frame, text="", font=("Arial", 12), foreground="#e74c3c")
comp_label.pack(anchor="w")

winner_label = ttk.Label(result_frame, text="", font=("Arial", 14, "bold"), foreground="#27ae60")
winner_label.pack(pady=10)

#anchor="w" = left-align

# ==============================
# 6. Bottom Buttons
# ==============================
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=20)

again_btn = ttk.Button(btn_frame, text="Play Again")
again_btn.pack(side="left", padx=10)

quit_btn = ttk.Button(btn_frame, text="Quit", style="Quit.TButton")
quit_btn.pack(side="left", padx=10)

# ==============================
# 7. Styling
# ==============================
style = ttk.Style()
style.theme_use('clam')

# Play button - green
style.configure("Play.TButton", font=("Helvetica", 12, "bold"), foreground="white")
style.map("Play.TButton", background=[('active', '#2ecc71')], foreground=[('active', 'white')])
style.configure("Play.TButton", background="#27ae60")

# Quit button - red
style.configure("Quit.TButton", font=("Helvetica", 12, "bold"), foreground="white")
style.map("Quit.TButton", background=[('active', '#e74c3c')])
style.configure("Quit.TButton", background="#c0392b")



# ==============================
# 8. Helper: Clear results
# ==============================
def clear_results():
    user_label.config(text="")
    comp_label.config(text="")
    winner_label.config(text="")



# ==============================
# 9. Game Logic
# ==============================
def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user, comp):
    if user == comp:
        return "Wow!, It's a tie"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Scissors" and comp == "Paper") or \
         (user == "Paper" and comp == "Rock"):
        return "You Win!!"
    else:
        return "Computer Win!"

# ==============================
# 10. Play Function (clear → play)
# ==============================
def play():
    clear_results()

    # Get choices & decide winner                     
    user = choice_var.get()
    comp = get_computer_choice()
    result = determine_winner(user, comp)

    #Show new results
    user_label.config(text=f"You chose: {user}")
    comp_label.config(text=f"Computer chose: {comp}")
    winner_label.config(text=f">>> {result} <<<")

# ==============================
# 11. Button Commands
# ==============================
play_btn.config(command=play)
again_btn.config(command=lambda: [clear_results()])
quit_btn.config(command=root.quit)

# ==============================
# 12. Start App
# ==============================
root.mainloop()





#+-------------------------------------------+
#|          Rock Paper Scissors              |
#+-------------------------------------------+
#|  [O] Rock    [O] Paper    [O] Scissors    |
#|                                           |
#|  [ Play ]                                 |
#|                                           |
#|  You chose: Rock                          |
#|  Computer chose: Scissors                 |
#|  >>> You Win!! <<<                        |
#|                                           |
#|  [ Play Again ]    [ Quit ]               |
#+-------------------------------------------+

# Play Again button is there just to clear the screen...

