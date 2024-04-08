import tkinter as tk
from tkinter import filedialog, messagebox
from functools import partial

def encrypt_file(filename, key):
    try:
        with open(filename, "rb") as file:
            data = bytearray(file.read())

        for index, value in enumerate(data):
            data[index] = value ^ key

        with open("CC-" + filename, "wb") as file:
            file.write(data)
        
        messagebox.showinfo("Success", "File encrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_file(filename, key):
    try:
        with open(filename, "rb") as file:
            data = bytearray(file.read())

        for index, value in enumerate(data):
            data[index] = value ^ key

        with open(filename, "wb") as file:
            file.write(data)
        
        messagebox.showinfo("Success", "File decrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file(entry):
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def execute_operation(operation_func, filename_entry, key_entry):
    filename = filename_entry.get()
    key = key_entry.get()
    if not filename or not key:
        messagebox.showerror("Error", "Please provide both filename and key!")
        return
    operation_func(filename, int(key))

def create_gui():
    root = tk.Tk()
    root.title("File Encryption and Decryption")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    filename_label = tk.Label(frame, text="Filename:")
    filename_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    filename_entry = tk.Entry(frame, width=50)
    filename_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

    browse_button = tk.Button(frame, text="Browse", command=partial(browse_file, filename_entry))
    browse_button.grid(row=0, column=2, padx=5, pady=5)

    key_label = tk.Label(frame, text="Key:")
    key_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

    key_entry = tk.Entry(frame)
    key_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

    encrypt_button = tk.Button(frame, text="Encrypt", command=partial(execute_operation, encrypt_file, filename_entry, key_entry))
    encrypt_button.grid(row=2, column=0, padx=5, pady=5)

    decrypt_button = tk.Button(frame, text="Decrypt", command=partial(execute_operation, decrypt_file, filename_entry, key_entry))
    decrypt_button.grid(row=2, column=1, padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
