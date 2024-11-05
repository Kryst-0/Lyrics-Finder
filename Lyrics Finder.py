import lyricsgenius
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Replace 'YOUR_GENIUS_ACCESS_TOKEN' with your actual Genius API access token
genius = lyricsgenius.Genius("YOUR_GENIUS_ACCESS_TOKEN")

# Function to get lyrics
def get_lyrics():
    song_title = entry_song_title.get()
    artist_name = entry_artist_name.get()
    
    if not song_title:
        messagebox.showwarning("Input Error", "Please enter a song title.")
        return
    
    try:
        if artist_name:
            song = genius.search_song(song_title, artist_name)
        else:
            song = genius.search_song(song_title)
        
        if song and song.lyrics:
            lyrics_display.config(state=tk.NORMAL)
            lyrics_display.delete(1.0, tk.END)
            lyrics_display.insert(tk.END, song.lyrics)
            lyrics_display.config(state=tk.DISABLED)
        else:
            lyrics_display.config(state=tk.NORMAL)
            lyrics_display.delete(1.0, tk.END)
            lyrics_display.insert(tk.END, "Lyrics not found.")
            lyrics_display.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to toggle dark mode
def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.configure(bg="#1c2e2e")
        title_label.config(fg="#66b2b2", bg="#1c2e2e")
        entry_song_title.config(bg="#2e4a4a", fg="white", insertbackground="white")
        entry_artist_name.config(bg="#2e4a4a", fg="white", insertbackground="white")
        lyrics_display.config(bg="#2e4a4a", fg="white")
        footer_label.config(fg="#99cccc", bg="#1c2e2e")
        btn_get_lyrics.config(bg="#66b2b2", activebackground="#558a8a", fg="white")
        toggle_button.config(text="Switch to Light Mode", bg="#66b2b2", fg="white")
    else:
        root.configure(bg="#e8f4f4")
        title_label.config(fg="#007f7f", bg="#e8f4f4")
        entry_song_title.config(bg="#ffffff", fg="#333333", insertbackground="black")
        entry_artist_name.config(bg="#ffffff", fg="#333333", insertbackground="black")
        lyrics_display.config(bg="#ffffff", fg="#333333")
        footer_label.config(fg="#006666", bg="#e8f4f4")
        btn_get_lyrics.config(bg="#007f7f", activebackground="#005f5f", fg="white")
        toggle_button.config(text="Switch to Dark Mode", bg="#007f7f", fg="white")

# Set up the main GUI window
root = tk.Tk()
root.title("🎶 Lyrics Finder 🎶")
root.geometry("600x600")

# Custom font and colors
font_title = ("Arial", 18, "bold")
font_label = ("Arial", 12)
font_text = ("Arial", 10)
button_color = "#66b2b2"

# Track dark mode state
dark_mode = False

# Title label
title_label = tk.Label(root, text="Lyrics Finder", font=font_title)
title_label.pack(pady=(20, 10))

# Labels and entry fields
tk.Label(root, text="Song Title:", font=font_label).pack(pady=5)
entry_song_title = tk.Entry(root, width=40, font=font_text, bd=2, relief="groove")
entry_song_title.pack(pady=(0, 10), ipadx=5, ipady=5)

tk.Label(root, text="Artist Name (optional):", font=font_label).pack(pady=5)
entry_artist_name = tk.Entry(root, width=40, font=font_text, bd=2, relief="groove")
entry_artist_name.pack(pady=(0, 10), ipadx=5, ipady=5)

# Button to fetch lyrics
btn_get_lyrics = tk.Button(
    root, text="Get Lyrics", font=font_label, width=15, height=1, command=get_lyrics, bd=0, relief="solid"
)
btn_get_lyrics.pack(pady=15)

# Dark mode toggle button
toggle_button = tk.Button(root, text="Switch to Dark Mode", font=("Arial", 10), command=toggle_dark_mode)
toggle_button.pack(pady=5)

# ScrolledText widget to display lyrics
lyrics_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=font_text)
lyrics_display.pack(pady=10, padx=10)
lyrics_display.config(state=tk.DISABLED)

# Footer text
footer_label = tk.Label(root, text="Powered by Genius API", font=("Arial", 8))
footer_label.pack(side=tk.BOTTOM, pady=(0, 20))

# Initialize in light mode
toggle_dark_mode()  # Call once to set initial colors based on `dark_mode` value

# Start the Tkinter event loop
root.mainloop()
