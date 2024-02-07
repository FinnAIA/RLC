import random
import tkinter as tk

def random_capitalize(sentence):
    result = [letter.upper() if random.choice([True, False]) else letter.lower() for letter in sentence]
    return ''.join(result)

def on_convert():
    input_text = entry.get()
    capitalized_sentence = random_capitalize(input_text)
    output_text.delete(1.0, 'end')
    output_text.insert(1.0, capitalized_sentence)

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get('1.0', 'end-1c'))

# Create the main window
root = tk.Tk()
root.title("RLC GUI")

root.geometry("600x300")
root.configure(bg="black")

# Create input field
label = tk.Label(root, text="Enter text: ", bg="black", fg="white")
label.pack()
entry = tk.Entry(root, width=40, bg="white", font=("Arial", 12))
entry.pack()

# Create convert button
convert_button = tk.Button(root, text="Convert", bg="blue", fg="white", command=on_convert)
convert_button.pack(pady=2)

# Create output field
#output_var = tk.StringVar()
output_label = tk.Label(root, text="Result:", bg="black", fg="white")
output_label.pack()
output_text = tk.Text(root, height=1, width=40, bg="white", fg="black", font=("Arial", 12))
output_text.pack()

copy_button = tk.Button(root, text="Copy", command=copy_text, bg="red", fg="white")
copy_button.pack()

# Start the GUI event loop
root.mainloop()