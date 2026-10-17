import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select a text file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def count_words():
    file_path = entry_path.get()
    if not file_path:
        messagebox.showwarning("No File", "Please select a file first.")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        words = content.split()
        word_count = len(words)
        char_count = len(content)
        line_count = content.count('\n') + 1
        
        result_label.config(
            text=f"Words: {word_count}\nCharacters: {char_count}\nLines: {line_count}"
        )
    
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
    except PermissionError:
        messagebox.showerror("Error", "Permission denied.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")


# --- Main window setup ---
root = tk.Tk()
root.title("Word Counter")
root.geometry("420x250")
root.resizable(False, False)
root.configure(bg="#f4f4f9")

style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 10), padding=6)
style.configure("TLabel", background="#f4f4f9", font=("Segoe UI", 10))

title_label = tk.Label(root, text="Word Counter", font=("Segoe UI", 16, "bold"), bg="#f4f4f9")
title_label.pack(pady=15)

frame = tk.Frame(root, bg="#f4f4f9")
frame.pack(pady=5)

entry_path = tk.Entry(frame, width=35, font=("Segoe UI", 10))
entry_path.pack(side=tk.LEFT, padx=5)

browse_btn = ttk.Button(frame, text="Browse", command=browse_file)
browse_btn.pack(side=tk.LEFT)

count_btn = ttk.Button(root, text="Count Words", command=count_words)
count_btn.pack(pady=15)

result_label = tk.Label(root, text="", font=("Segoe UI", 11), bg="#f4f4f9", justify="left")
result_label.pack(pady=10)

root.mainloop()