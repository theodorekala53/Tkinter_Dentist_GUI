import tkinter as tk
import pandas as pd

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Page de Login")

        self.label_username = tk.Label(root, text="Nom d'utilisateur")
        self.label_password = tk.Label(root, text="Mot de passe")
        self.change_passwort_button = tk.Button(root, text="Change Passwort")

        self.entry_username = tk.Entry(root)
        self.entry_password = tk.Entry(root, show="*")

        self.login_button = tk.Button(root, text="Se connecter", command=self.check_login)

        self.label_username.grid(row=0, column=0)
        self.label_password.grid(row=1, column=0)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)
        self.login_button.grid(row=2, column=0, columnspan=2)

    def check_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Lisez les informations d'authentification depuis un fichier Excel
        excel_file = "noms.xlsx"
        df = pd.read_excel(excel_file)

        user_row = df[df['Nom dutilisateur'] == username]

        if not user_row.empty:
            if password == user_row.iloc[0]['Mot de passe']:
                print("Connexion réussie !")
            else:
                print("Échec de la connexion.")
        else:
            print("Nom d'utilisateur non trouvé.")
    
    def change_passwort(self):
        print("")

if __name__ == "__main__":
    root = tk.Tk()
    login_page = Login(root)
    root.mainloop()
