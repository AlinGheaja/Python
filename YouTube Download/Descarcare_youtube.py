#Necesar rulare: pytube
import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube

def download_video():
    try:
        url = entry.get()
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        save_path = filedialog.askdirectory()
        if save_path:  # Se verifica daca directorul de salvare a fost selectat
            stream.download(output_path=save_path)
            messagebox.showinfo("Succes", "Video a fost descarcat!")
        else:
            messagebox.showwarning("Atentie", "Nu a fost selectata nici o cale pentru salvare.")
    except Exception as e:
        messagebox.showerror("Eroare", f"A aparut o eroare: {str(e)}")

def paste_url():
    url = root.clipboard_get()
    entry.delete(0, tk.END)
    entry.insert(0, url)

#Casuta de dialog !
root = tk.Tk()
root.title("Descarcare YouTube")
root.resizable(False, False)

#Text si lipire link
label = tk.Label(root, text="Lipeste link-ul catre video YouTube:")
label.pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack()

#Butonul de lipire
paste_button = tk.Button(root, text="Lipeste", command=paste_url)
paste_button.pack(pady=5)

#Butonul de descarcare
download_button = tk.Button(root, text="Descarcare", command=download_video)
download_button.pack(pady=10)

#Se ruleaza bucla principala
root.mainloop()
