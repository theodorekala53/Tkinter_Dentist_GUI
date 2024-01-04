import tkinter as tk
from tkinter import ttk
import json

class LanguageChangeApp:
    def __init__(self, root):
        self.root = root
        self.current_language = "english"  # Langue par défaut
        self.translations = self.load_translations()

        self.label = ttk.Label(root, text=self.translations["label_text"], font=("Arial", 12))
        self.label.pack(pady=20)

        self.change_language_button = ttk.Button(root, text=self.translations["button_text"],
                                                 command=self.change_language)
        self.change_language_button.pack()

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12))

    def load_translations(self):
        # Charger les traductions depuis un fichier JSON
        try:
            with open(f"translations/{self.current_language}.json", "r", encoding="utf-8") as file:
                translations = json.load(file)
        except FileNotFoundError:
            # Fallback aux traductions en anglais si le fichier n'est pas trouvé
            with open("translations/english.json", "r", encoding="utf-8") as file:
                translations = json.load(file)

        return translations

    def change_language(self):
        if self.current_language == "english":
            self.current_language = "german"
        else:
            self.current_language = "english"

        self.translations = self.load_translations()

        self.label["text"] = self.translations["label_text"]
        self.change_language_button["text"] = self.translations["button_text"]

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageChangeApp(root)
    root.mainloop()
