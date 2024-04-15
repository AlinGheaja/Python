#please install pytube if error!
import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube

def download_video():
    try:
        url = entry.get()
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        save_path = filedialog.askdirectory()
        if save_path:  # Check if a directory was selected
            stream.download(output_path=save_path)
            messagebox.showinfo("Success", "Video downloaded successfully!")
        else:
            messagebox.showwarning("Warning", "No save location selected.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def paste_url():
    url = root.clipboard_get()
    entry.delete(0, tk.END)
    entry.insert(0, url)

# Create main window
root = tk.Tk()
root.title("YouTube Video Downloader")
root.resizable(False, False)  # Disable resizing

# Create label and entry
label = tk.Label(root, text="Paste YouTube video link:")
label.pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack()

# Create paste button
paste_button = tk.Button(root, text="Paste", command=paste_url)
paste_button.pack(pady=5)

# Create download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

# Run the main loop
root.mainloop()
