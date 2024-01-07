import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename()  # Ouvre la boîte de dialogue pour sélectionner un fichier
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  # Garde une référence à l'image pour éviter sa suppression

root = tk.Tk()
root.geometry("300x268")

image_frame = tk.Frame(root, width=180, height=180)
image_frame.place(rely=0, relx=0)
# Afficher une image de base ou une image par défaut
default_image = Image.open("sign-out-alt.png")  # Remplacez par votre image par défaut
default_image = default_image.resize((300, 268), Image.ANTIALIAS) 
default_photo = ImageTk.PhotoImage(default_image)
label = tk.Label(image_frame, image=default_photo, anchor="center")
label.pack()

# Bouton pour charger une image
load_button = tk.Button(root, text="Charger une image", command=open_image)
load_button.pack()

root.mainloop()
