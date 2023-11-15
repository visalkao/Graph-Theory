import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_input = text.get("1.0", "end-1c")  # Get text from the Text widget
    print(type(user_input))
    list_of_lists = [list(map(int, sublist.split(','))) for sublist in user_input.split('],')]

# Convert the last element separately due to the lack of trailing comma
    list_of_lists[-1] = list(map(int, list_of_lists[-1].replace('[','').replace(']','').split(',')))


    messagebox.showinfo("Message", "Hello:\n" + user_input)

# Create the main window
root = tk.Tk()
root.title("Graph Theory")

# Create a label
label = tk.Label(root, text="Enter your the graph:")
label.pack(pady=10)

# Create a Text widget for multiline input
text = tk.Text(root, height=5, width=40)
text.pack(pady=10)

# Create a button
button = tk.Button(root, text="Say Hello", command=on_button_click)
button.pack(pady=10)

# Run the main loop
root.mainloop()
