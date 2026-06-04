import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# ==========================
# LANGUAGES (25+)
# ==========================
languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Urdu": "ur",
    "Hindi": "hi",
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
    "Punjabi (Gurmukhi)": "pa",
    "Greek": "el",
    "Polish": "pl",
    "Swedish": "sv",
    "Norwegian": "no",
    "Danish": "da",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Pashto": "ps",
}

# ==========================
# TRANSLATE FUNCTION
# ==========================
def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Warning", "Please enter text to translate.")
        return

    source = languages[source_box.get()]
    target = languages[target_box.get()]

    try:
        translated = GoogleTranslator(
            source=source,
            target=target
        ).translate(text)

        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
        output_text.config(state="disabled")

        status_bar.config(text="✅ Translation completed successfully")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_bar.config(text="❌ Translation failed")

# ==========================
# COPY FUNCTION
# ==========================
def copy_text():
    text = output_text.get("1.0", tk.END).strip()

    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        messagebox.showinfo("Copied", "Translated text copied successfully!")

# ==========================
# CLEAR FUNCTION
# ==========================
def clear_all():
    input_text.delete("1.0", tk.END)

    output_text.config(state="normal")
    output_text.delete("1.0", tk.END)
    output_text.config(state="disabled")

    update_counter()
    status_bar.config(text="Ready")

# ==========================
# SWAP LANGUAGES
# ==========================
def swap_languages():
    source = source_box.get()
    target = target_box.get()

    source_box.set(target)
    target_box.set(source)

# ==========================
# CHARACTER COUNTER
# ==========================
def update_counter(event=None):
    count = len(input_text.get("1.0", tk.END).strip())
    counter_label.config(text=f"Characters: {count}")

# ==========================
# GUI
# ==========================
root = tk.Tk()
root.title("AI Multi-Language Translator")
root.geometry("950x760")
root.configure(bg="#1E1E2F")
root.resizable(False, False)

# ==========================
# TITLE
# ==========================
title = tk.Label(
    root,
    text="🌍 AI MULTI-LANGUAGE TRANSLATOR",
    font=("Segoe UI", 24, "bold"),
    bg="#1E1E2F",
    fg="#00D4FF"
)
title.pack(pady=20)

# ==========================
# INPUT LABEL
# ==========================
input_label = tk.Label(
    root,
    text="Enter Text",
    font=("Segoe UI", 12, "bold"),
    bg="#1E1E2F",
    fg="white"
)
input_label.pack()

# ==========================
# INPUT TEXT
# ==========================
input_text = tk.Text(
    root,
    height=8,
    width=90,
    font=("Segoe UI", 11),
    bg="#2D2D44",
    fg="white",
    insertbackground="white",
    relief="flat"
)
input_text.pack(pady=10)

input_text.bind("<KeyRelease>", update_counter)

# ==========================
# CHARACTER COUNTER
# ==========================
counter_label = tk.Label(
    root,
    text="Characters: 0",
    bg="#1E1E2F",
    fg="#BBBBBB",
    font=("Segoe UI", 9)
)
counter_label.pack()

# ==========================
# LANGUAGE FRAME
# ==========================
lang_frame = tk.Frame(root, bg="#1E1E2F")
lang_frame.pack(pady=15)

# SOURCE
tk.Label(
    lang_frame,
    text="Source Language",
    bg="#1E1E2F",
    fg="white",
    font=("Segoe UI", 10, "bold")
).grid(row=0, column=0, padx=20)

source_box = ttk.Combobox(
    lang_frame,
    values=list(languages.keys()),
    state="readonly",
    width=25
)
source_box.grid(row=1, column=0, padx=20)
source_box.set("Auto Detect")

# TARGET
tk.Label(
    lang_frame,
    text="Target Language",
    bg="#1E1E2F",
    fg="white",
    font=("Segoe UI", 10, "bold")
).grid(row=0, column=1, padx=20)

target_box = ttk.Combobox(
    lang_frame,
    values=list(languages.keys()),
    state="readonly",
    width=25
)
target_box.grid(row=1, column=1, padx=20)
target_box.set("Urdu")

# ==========================
# BUTTONS
# ==========================
btn_frame = tk.Frame(root, bg="#1E1E2F")
btn_frame.pack(pady=20)

translate_btn = tk.Button(
    btn_frame,
    text="Translate",
    command=translate_text,
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15,
    relief="flat"
)
translate_btn.grid(row=0, column=0, padx=8)

copy_btn = tk.Button(
    btn_frame,
    text="Copy",
    command=copy_text,
    bg="#FF9800",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15,
    relief="flat"
)
copy_btn.grid(row=0, column=1, padx=8)

clear_btn = tk.Button(
    btn_frame,
    text="Clear",
    command=clear_all,
    bg="#F44336",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15,
    relief="flat"
)
clear_btn.grid(row=0, column=2, padx=8)

swap_btn = tk.Button(
    btn_frame,
    text="⇄ Swap",
    command=swap_languages,
    bg="#2196F3",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15,
    relief="flat"
)
swap_btn.grid(row=0, column=3, padx=8)

# ==========================
# OUTPUT LABEL
# ==========================
output_label = tk.Label(
    root,
    text="Translated Text",
    font=("Segoe UI", 12, "bold"),
    bg="#1E1E2F",
    fg="white"
)
output_label.pack()

# ==========================
# OUTPUT TEXT
# ==========================
output_text = tk.Text(
    root,
    height=8,
    width=90,
    font=("Segoe UI", 11),
    bg="#2D2D44",
    fg="#00FF99",
    relief="flat"
)
output_text.pack(pady=10)
output_text.config(state="disabled")

# ==========================
# FOOTER
# ==========================
footer = tk.Label(
    root,
    text="Developed using Python • Tkinter • Google Translator API",
    bg="#1E1E2F",
    fg="#888888",
    font=("Segoe UI", 9)
)
footer.pack(pady=10)

# ==========================
# STATUS BAR
# ==========================
status_bar = tk.Label(
    root,
    text="Ready",
    bd=1,
    relief=tk.SUNKEN,
    anchor=tk.W,
    bg="#111827",
    fg="white",
    font=("Segoe UI", 9)
)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()