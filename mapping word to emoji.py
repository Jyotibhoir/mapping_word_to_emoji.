import tkinter as tk

emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "angry": "😠",
    "love": "❤",
    "surprised": "😲",
    "laugh": "😂",
    "cool": "😎",
    "cry": "😭",
    "sleep": "😴",
    "fear": "😨"
}

def show_emoji(event=None):
    word = entry.get().strip().lower()
    emoji = emoji_dict.get(word, "❓")
    emoji_label.config(text=emoji)


window = tk.Tk()
window.title("Word to Emoji")
window.geometry("350x250")
window.config(bg="#f0c1ff")  


tk.Label(window, text="Type a word to see the emoji", font=("Arial", 14, "bold"), bg="#f0c1ff", fg="#333").pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14), justify="center")
entry.pack(pady=5)

show_btn = tk.Button(window, text="Show", command=show_emoji,
                     font=("Arial", 12, "bold"), bg="#ff6f61", fg="white",
                     activebackground="#ff3b2e", activeforeground="white",
                     relief="raised", bd=3, padx=20, pady=5)
show_btn.pack(pady=5)

emoji_label = tk.Label(window, text="", font=("Arial", 50), bg="#f0c1ff")
emoji_label.pack(pady=20)


entry.bind("<KeyRelease>", show_emoji)

window.mainloop()