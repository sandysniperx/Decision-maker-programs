import tkinter as tk
import random

def wheel():
    chosen_item = random.choice(options)
    result_label.config(text=f"The wheel landed on: {chosen_item}")

root = tk.Tk()
root.title("Picker")

options = input("Enter elements to be picked from: ").split()
print("\n",options)

clicker = tk.Button(root, text="Spin the Wheel", command=wheel, font=("Bahnschrift", 18))
clicker.pack(pady=50)

result_label = tk.Label(root, text="", font=("Bahnschrift", 16))
result_label.pack(pady=50)

root.mainloop()