from cryptography.fernet import Fernet
from tkinter import filedialog, ttk
import tkinter as tk
from tkinter.simpledialog import askstring
import pyperclip  # Import pyperclip module

def generate_key(file_paths):
    key = Fernet.generate_key()
    # Copy the key to the clipboard
    pyperclip.copy(key.decode())
    with open('key.txt', 'a') as key_file:
        for file_path in file_paths:
            key_file.write(f"File: {file_path}, Key: {key.decode()}\n")
    
    return key

def encrypt_file(file_path, encryption_key, error_label):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        cipher_suite = Fernet(encryption_key)
        encrypted_data = cipher_suite.encrypt(data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
        return True
    except Exception as e:
        update_error_label(error_label, f"Error: {str(e)}")
        return False

def decrypt_file(file_path, encryption_key, error_label):
    try:
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        cipher_suite = Fernet(encryption_key)
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)
        return True
    except Exception as e:
        update_error_label(error_label, f"Error: {str(e)}")
        return False

def update_error_label(error_label, message):
    error_label.config(state=tk.NORMAL)  # Enable editing
    error_label.delete(1.0, tk.END)  # Clear previous messages
    error_label.insert(tk.END, message)
    error_label.config(state=tk.DISABLED)  # Disable editing

def main():
    root = tk.Tk()
    root.title("FileGuard - File Encryption/Decryption")

    # Set the window icon
    #root.iconbitmap('FileGuard.png')

    # Increase the window size
    root.geometry("500x400")  # Increased width for better layout

    # Create a style to enhance the appearance
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12))
    style.configure("TLabel", font=("Helvetica", 10, "italic"))

    def select_files():
        global file_paths, encryption_key
        file_paths = filedialog.askopenfilenames(title="Select files", filetypes=[("All Files", "*.*")])
        if file_paths:
            encryption_key = generate_key(file_paths)  # Generate a single key for all selected files
            file_text.config(state=tk.NORMAL)  # Enable editing
            file_text.delete(1.0, tk.END)  # Clear previous text
            file_text.insert(tk.END, "Selected Files:\n")
            for file_path in file_paths:
                file_text.insert(tk.END, f"{file_path}\n")
            file_text.config(state=tk.DISABLED)  # Disable editing
            update_error_label(error_label, "")  # Clear previous error messages

    def encrypt_selected_files():
        global file_paths, encryption_key
        if file_paths:
            for file_path in file_paths:
                success = encrypt_file(file_path, encryption_key, error_label)
                if success:
                    update_error_label(error_label, "Files encrypted successfully.")
                else:
                    print("Error encrypting the files.")
        else:
            update_error_label(error_label, "No files selected.")

    def decrypt_selected_files():
        global file_paths, encryption_key
        if file_paths:
            # Ask for decryption key
            decryption_key = askstring("Decryption Key", "Enter decryption key:")
            if decryption_key:
                for file_path in file_paths:
                    success = decrypt_file(file_path, decryption_key.encode(), error_label)
                    if success:
                        update_error_label(error_label, "Files decrypted successfully.")
                    else:
                        print("Error decrypting the files.")
            else:
                update_error_label(error_label, "Decryption canceled.")
        else:
            update_error_label(error_label, "No files selected.")

    select_button = ttk.Button(root, text="Select files", command=select_files)
    encrypt_button = ttk.Button(root, text="Encrypt files", command=encrypt_selected_files)
    decrypt_button = ttk.Button(root, text="Decrypt files", command=decrypt_selected_files)

    file_text = tk.Text(root, wrap=tk.WORD, height=8, font=("Helvetica", 12), state=tk.DISABLED)
    error_label = tk.Text(root, wrap=tk.WORD, height=4, fg="red", font=("Helvetica", 10, "bold"), state=tk.DISABLED)

    select_button.pack(pady=10)
    encrypt_button.pack(pady=10)
    decrypt_button.pack(pady=10)
    file_text.pack(pady=10)
    error_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
