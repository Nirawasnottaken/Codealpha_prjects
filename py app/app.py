import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# === Get supported languages ===
translator_instance = GoogleTranslator(source='auto', target='english')
langs = translator_instance.get_supported_languages(as_dict=True)

lang_names = list(langs.keys())
lang_codes = {v: k for k, v in langs.items()}
lang_codes = langs 
# === Root window ===
root = tk.Tk()
root.title("Translator By Niranjan")
root.geometry("600x500")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

def center_window(w, h):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) // 2
    y = (sh - h) // 2
    root.geometry(f"{w}x{h}+{x}+{y}")

center_window(600, 500)

# === Colors & Fonts ===
bg_color = "#1e1e1e"
fg_color = "#f0f0f0"
input_bg = "#2d2d2d"
button_bg = "#3b82f6"
button_fg = "#ffffff"
highlight_bg = "#3a3a3a"

font_label = ("Arial", 11)
font_title = ("Arial", 12, "bold")
font_text = ("Consolas", 11)

# === Input box ===
tk.Label(root, text="Enter Text", font=font_title, bg=bg_color, fg=fg_color).pack(pady=(20, 5))
text_input = tk.Text(root, height=6, width=65, font=font_text, bg=input_bg, fg=fg_color, insertbackground="white")
text_input.pack(pady=5)

# === Language dropdowns ===
frame_lang = tk.Frame(root, bg=bg_color)
frame_lang.pack(pady=10)

tk.Label(frame_lang, text="From:", font=font_label, bg=bg_color, fg=fg_color).grid(row=0, column=0, padx=10)
src_lang = ttk.Combobox(frame_lang, values=lang_names, state="readonly", width=20)
src_lang.set("english")
src_lang.grid(row=0, column=1)

tk.Label(frame_lang, text="To:", font=font_label, bg=bg_color, fg=fg_color).grid(row=0, column=2, padx=10)
dest_lang = ttk.Combobox(frame_lang, values=lang_names, state="readonly", width=20)
dest_lang.set("hindi")
dest_lang.grid(row=0, column=3)

# === Output box ===
tk.Label(root, text="Translated Text", font=font_title, bg=bg_color, fg=fg_color).pack(pady=(15, 5))
translated_output = tk.Text(root, height=6, width=65, font=font_text, bg=input_bg, fg=fg_color, insertbackground="white")
translated_output.pack(pady=5)

# === Translate Function ===
def translate_text():
    original = text_input.get("1.0", "end-1c").strip()
    if not original:
        messagebox.showwarning("Input Missing", "Please enter some text to translate.")
        return
    try:
        src = lang_codes.get(src_lang.get())
        tgt = lang_codes.get(dest_lang.get())
        translated = GoogleTranslator(source=src, target=tgt).translate(original)
        translated_output.delete("1.0", "end")
        translated_output.insert("1.0", translated)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

# === Translate Button ===
translate_button = tk.Button(
    root, text="Translate", font=font_title,
    bg=button_bg, fg=button_fg,
    padx=20, pady=5,
    command=translate_text
)
translate_button.pack(pady=20)

# === Darken ttk Comboboxes ===
style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", fieldbackground=input_bg, background=input_bg, foreground=fg_color)

# === Run UI ===
root.mainloop()
