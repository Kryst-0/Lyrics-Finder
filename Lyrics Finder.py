import requests
from bs4 import BeautifulSoup
import re
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import scrolledtext, messagebox

def format_song_title(song_title):
    # Remove special characters and spaces
    song_title = re.sub(r'[^A-Za-z0-9]', '', song_title)
    return song_title.lower()

def format_artist_name(artist_name):
    # Remove special characters and spaces
    artist_name = re.sub(r'[^A-Za-z0-9]', '', artist_name)
    return artist_name.lower()

def get_lyrics(song_title, artist_name):
    try:
        # Format song title and artist name for the AZLyrics URL pattern
        song_title_formatted = format_song_title(song_title)
        artist_name_formatted = format_artist_name(artist_name)
        
        # Construct URL
        url = f"https://www.azlyrics.com/lyrics/{artist_name_formatted}/{song_title_formatted}.html"
        
        # Request the page
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the page
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the lyrics div by class (based on AZLyrics structure)
        lyrics_div = soup.find("div", class_=None, id=None)
        
        if lyrics_div:
            lyrics = lyrics_div.get_text(separator="\n").strip()
            return lyrics
        else:
            return "Lyrics not found."
    except requests.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as e:
        return f"An error occurred: {e}"

def search_lyrics():
    song_title = song_title_entry.get()
    artist_name = artist_name_entry.get()
    
    if not song_title or not artist_name:
        messagebox.showwarning("Input Required", "Please enter both the song title and artist name.")
        return
    
    lyrics = get_lyrics(song_title, artist_name)
    lyrics_display.delete(1.0, "end")
    lyrics_display.insert("end", lyrics)

# Initialize the GUI with ttkbootstrap
app = ttk.Window(themename="superhero")
app.title("Lyrics Finder")
app.geometry("600x700")

# Song Title
ttk.Label(app, text="Song Title:", font=("Arial", 12)).pack(pady=5)
song_title_entry = ttk.Entry(app, font=("Arial", 12), width=30)
song_title_entry.pack(pady=5)

# Artist Name
ttk.Label(app, text="Artist Name:", font=("Arial", 12)).pack(pady=5)
artist_name_entry = ttk.Entry(app, font=("Arial", 12), width=30)
artist_name_entry.pack(pady=5)

# Search Button
search_button = ttk.Button(app, text="Search Lyrics", bootstyle=SUCCESS, command=search_lyrics)
search_button.pack(pady=10)

# Lyrics Display (Scrollable Text Area)
lyrics_display = scrolledtext.ScrolledText(app, wrap="word", font=("Arial", 10), width=55, height=20)
lyrics_display.pack(pady=10)

# Run the application
app.mainloop()
