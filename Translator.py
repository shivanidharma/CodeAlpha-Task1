import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
from datetime import datetime

# ==========================
# LANGUAGES (25+)
# ==========================
languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Urdu": "ur",
    "Hindi": "hi",
    "Punjabi (Gurmukhi)": "pa",
    "Pashto": "ps",
    "Arabic": "ar",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Turkish": "tr",
    "Dutch": "nl",
    "Greek": "el",
    "Polish": "pl",
    "Swedish": "sv",
    "Norwegian": "no",
    "Danish": "da",
    "Vietnamese": "vi",
    "Indonesian": "id"
}

# ==========================
# FUNCTIONS
# ==========================

def update_counter(event=None):
    count = len(input_text.get("1.0", tk.END).strip())
    counter_label.config(text=f"Characters: {count}")

def swap_languages():
    s = source_box.get()
    t = target_box.get()
    source_box.set(t)
    target_box.set(s)

def clear_all():
    input_text.delete("1.0", tk.END)

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.config(state="disabled")

    update_counter()
    status_bar.config(text="Ready")

def clear_history():
    history_box.delete("1.0", tk.END)
    open("history.txt", "w", encoding="utf-8").close()
    messagebox.showinfo("History", "History cleared successfully!")

def copy_text():
    text = output_text.get("1.0", tk.END).strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Copied successfully!")

def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter text")
        return

    source = languages[source_box.get()]
    target = languages[target_box.get()]

    try:
        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        # Output
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
        output_text.config(state="disabled")

        # Timestamp
        time_now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        history_entry = (
            f"[{time_now}]\n"
            f"{source_box.get()} ➜ {target_box.get()}\n"
            f"Original: {text}\n"
            f"Translated: {translated}\n"
            + "-" * 70 + "\n"
        )

        history_box.insert(tk.END, history_entry)
        history_box.see(tk.END)

        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(history_entry)

        status_bar.config(text="Translation Successful ✓")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_bar.config(text="Error Occurred")

# ==========================
# GUI
# ==========================

root = tk.Tk()
root.title("AI Multi-Language Translator")
root.geometry("950x800")
root.configure(bg="#1E1E2F")
root.resizable(True,True)

# TITLE
title = tk.Label(
    root,
    text="🌍 AI MULTI-LANGUAGE TRANSLATOR",
    font=("Segoe UI", 24, "bold"),
    bg="#1E1E2F",
    fg="#00D4FF"
)
title.pack(pady=15)

# INPUT
tk.Label(root, text="Enter Text", bg="#1E1E2F", fg="white",
         font=("Segoe UI", 11, "bold")).pack()

input_text = tk.Text(
    root,
    height=7,
    width=90,
    font=("Segoe UI", 11),
    bg="#2D2D44",
    fg="white",
    insertbackground="white"
)
input_text.pack(pady=8)
input_text.bind("<KeyRelease>", update_counter)

counter_label = tk.Label(
    root,
    text="Characters: 0",
    bg="#1E1E2F",
    fg="#BBBBBB"
)
counter_label.pack()

# LANGUAGES
frame = tk.Frame(root, bg="#1E1E2F")
frame.pack(pady=10)

tk.Label(frame, text="Source", bg="#1E1E2F", fg="white").grid(row=0, column=0)
tk.Label(frame, text="Target", bg="#1E1E2F", fg="white").grid(row=0, column=1)

source_box = ttk.Combobox(frame, values=list(languages.keys()), state="readonly")
source_box.grid(row=1, column=0, padx=10)
source_box.set("Auto Detect")

target_box = ttk.Combobox(frame, values=list(languages.keys()), state="readonly")
target_box.grid(row=1, column=1, padx=10)
target_box.set("Urdu")

# BUTTONS
btn_frame = tk.Frame(root, bg="#1E1E2F")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Translate", command=translate_text,
          bg="#4CAF50", fg="white", width=14).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Copy", command=copy_text,
          bg="#FF9800", fg="white", width=14).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Clear", command=clear_all,
          bg="#F44336", fg="white", width=14).grid(row=0, column=2, padx=5)

tk.Button(btn_frame, text="Swap ⇄", command=swap_languages,
          bg="#2196F3", fg="white", width=14).grid(row=0, column=3, padx=5)

tk.Button(btn_frame, text="Clear History", command=clear_history,
          bg="#9C27B0", fg="white", width=14).grid(row=0, column=4, padx=5)

# OUTPUT
tk.Label(root, text="Translated Text", bg="#1E1E2F", fg="white",
         font=("Segoe UI", 11, "bold")).pack()

output_text = tk.Text(
    root,
    height=7,
    width=90,
    font=("Segoe UI", 11),
    bg="#2D2D44",
    fg="#00FF99"
)
output_text.pack(pady=8)
output_text.config(state="disabled")

# HISTORY
tk.Label(root, text="Translation History", bg="#1E1E2F", fg="white",
         font=("Segoe UI", 11, "bold")).pack()

history_box = tk.Text(
    root,
    height=10,
    width=90,
    font=("Segoe UI", 10),
    bg="#25253A",
    fg="#CCCCCC"
)
history_box.pack(pady=8)

# LOAD OLD HISTORY
try:
    with open("history.txt", "r", encoding="utf-8") as f:
        history_box.insert(tk.END, f.read())
except:
    pass

# STATUS BAR
status_bar = tk.Label(
    root,
    text="Ready",
    bg="#111827",
    fg="white",
    anchor="w"
)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()