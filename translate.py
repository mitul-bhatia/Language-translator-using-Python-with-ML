from translate import Translator
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('400x550')
root.title('Language Translator')

img = ImageTk.PhotoImage(Image.open("langtrans.jpg"))
lbi = tk.Label(root, image=img)
lbi.pack()

hd = tk.Label(root, text='Language Translator', font='sans 14 bold', bg='yellow', fg='blue')
hd.pack(fill='both')

LANGUAGES = ['en', 'fr', 'de', 'es', 'hi', 'it', 'ja']

l1 = tk.Label(root, text='From', font='sans 12 bold')
l1.pack()
from_lang = ttk.Combobox(root, values=LANGUAGES, font='sans 12', state='readonly')
from_lang.set('en')
from_lang.pack()

l2 = tk.Label(root, text='To', font='sans 12 bold')
l2.pack()
to_lang = ttk.Combobox(root, values=LANGUAGES, font='sans 12', state='readonly')
to_lang.set('es')
to_lang.pack()

l3 = tk.Label(root, text='Enter text', font='sans 12 bold')
l3.pack()
text_input = tk.Entry(root, font='sans 12', width=30)
text_input.pack()

output_label = tk.Label(root, text='Translation', font='sans 12 bold')
output_label.pack()
output_text = tk.Entry(root, font='sans 12', width=30, state='readonly')
output_text.pack()

def translate_text():
    source_lang = from_lang.get()
    target_lang = to_lang.get()
    text = text_input.get()
    
    if not text.strip():
        messagebox.showerror("Error", "Please enter text to translate.")
        return

    try:
        translator = Translator(from_lang=source_lang, to_lang=target_lang)
        translation = translator.translate(text)
        output_text.config(state='normal')
        output_text.delete(0, tk.END)
        output_text.insert(tk.END, translation)
        output_text.config(state='readonly')
    except Exception as e:
        messagebox.showerror("Translation Error", f"Could not translate text: {str(e)}")

b1 = tk.Button(root, text='Translate', command=translate_text, font='sans 12 bold', bg='blue', fg='yellow')
b1.pack(fill='both', pady=10)

root.mainloop()
