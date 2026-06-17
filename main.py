from toyControl import *
import tkinter as tk

button_text = "Spin Arm"


def on_button_click(btn):
    # Change the text property of the button dynamically
    btn.config(text="Moving...")

    # Optional: Disable the button so the user cannot spam click it
    btn.config(state="disabled")

def main():
    print("Application Started")
    print("""
========================================================
Welcome to the Motivation Software graphical interface!

    This is the interface for "motivation" in your 
    coding activities!
    
========================================================
""")
    root = tk.Tk()
    root.geometry("500x700")


    # The button triggers the synchronous wrapper function
    btn = tk.Button(root, text=button_text, command=lambda: on_button_click(btn))
    btn.pack(pady=1)
    btn1 = tk.Button(root, text="Exit", command=root.destroy)
    btn1.pack(pady=1)

    root.mainloop()


if __name__ == "__main__":
    main()