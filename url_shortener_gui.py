import tkinter as tk
from tkinter import messagebox
import pyshorteners

def shorten_url():
    long_url = entry.get()
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        generated_url.set(short_url)
        copy_button.config(state=tk.NORMAL)
    except:
        messagebox.showerror("Error", "An error occurred while shortening the URL.")

def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(generated_url.get())
    app.update()

app = tk.Tk()
app.title("URL Shortener")
app.geometry("400x300")  # Set initial window size

# Styling
bg_color = "#f0f0f0"
font_style = "Helvetica 12"

app.configure(bg=bg_color)

# Create a centered frame
center_frame = tk.Frame(app)
center_frame.pack(expand=True)

entry = tk.Entry(center_frame, font=font_style, width=30)
entry.pack(pady=20)

shorten_button = tk.Button(center_frame, text="Shorten URL", font=font_style, command=shorten_url)
shorten_button.pack()

generated_url = tk.StringVar()

generated_url_box = tk.Entry(center_frame, font=font_style, width=30, textvariable=generated_url, state='readonly')
generated_url_box.pack(pady=10)

copy_button = tk.Button(center_frame, text="Copy to Clipboard", font=font_style, command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=10)

app.mainloop()
