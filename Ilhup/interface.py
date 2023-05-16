import tkinter as tk

def choice1():
    print("You selected Choice 1")

def choice2():
    print("You selected Choice 2")

def choice3():
    print("You selected Choice 3")

def close():
    root.destroy()

root = tk.Tk()
root.title("Program Menu")

# Set the window size
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = int((screen_width / 2) - (window_width / 2))
y_position = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

choice1_button = tk.Button(button_frame, text="Choice 1", command=choice1)
choice1_button.pack(pady=5)

choice2_button = tk.Button(button_frame, text="Choice 2", command=choice2)
choice2_button.pack(pady=5)

choice3_button = tk.Button(button_frame, text="Choice 3", command=choice3)
choice3_button.pack(pady=5)

close_button = tk.Button(root, text="Close", command=close)
close_button.pack(pady=10)

root.mainloop()
