import tkinter as tk
from tkinter import messagebox
import pandas as pd

# ...

# Créer une classe Login pour gérer l'interface de connexion
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Connexion")

        # Labels et Entry pour le nom d'utilisateur et le mot de passe
        self.username_label = tk.Label(root, text="Nom d'utilisateur:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Mot de passe:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")  # Pour masquer le mot de passe
        self.password_entry.pack()

        # Bouton de connexion
        self.login_button = tk.Button(root, text="Se connecter", command=self.authenticate)
        self.login_button.pack()

        # Attribut pour stocker le nom d'utilisateur actuel
        self.current_user = None

    def authenticate(self):
        # Récupérer le nom d'utilisateur et le mot de passe entrés par l'utilisateur
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Lire le fichier Excel pour vérifier la connexion
        try:
            df = pd.read_excel('noms.xlsx')  # Remplacez 'noms.xlsx' par le nom de votre fichier Excel
            if not df.empty:
                if (username in df['Nom dutilisateur'].values) and (password in df['Mot de passe'].values):
                    self.current_user = username  # Définir l'utilisateur actuel
                    self.open_new_window()
                else:
                    messagebox.showerror("Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect.")
            else:
                messagebox.showerror("Erreur de connexion", "Aucun utilisateur enregistré.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

    def open_new_window(self):
        # Créer une nouvelle fenêtre
        new_window = tk.Toplevel(self.root)
        new_window.title("Nouvelle fenêtre")

        # Bouton pour changer le mot de passe
        change_password_button = tk.Button(new_window, text="Changer le mot de passe", command=self.change_password)
        change_password_button.pack()

    def change_password(self):
        # Ouvrir la fenêtre de changement de mot de passe en passant le nom d'utilisateur actuel
        change_password_window = tk.Toplevel(self.root)
        change_password_window.title("Changer le mot de passe")
        change_password_screen = ChangePassword(change_password_window, self.current_user)

# ...

# Créer une classe ChangePassword pour changer le mot de passe
class ChangePassword:
    def __init__(self, root, current_user):
        self.root = root
        self.current_user = current_user  # Récupérer le nom d'utilisateur actuel

        # Labels et Entry pour le nouveau mot de passe
        self.new_password_label = tk.Label(root, text="Nouveau mot de passe:")
        self.new_password_label.pack()
        self.new_password_entry = tk.Entry(root, show="*")  # Pour masquer le mot de passe
        self.new_password_entry.pack()

        # Bouton pour enregistrer le nouveau mot de passe
        self.save_button = tk.Button(root, text="Enregistrer", command=self.save_password)
        self.save_button.pack()

    def save_password(self):
        new_password = self.new_password_entry.get()

        # Assurez-vous que 'noms.xlsx' est le nom du fichier Excel où vous stockez les informations d'identification.
        # Assurez-vous également que les colonnes 'Nom dutilisateur' et 'Mot de passe' existent dans le fichier.
        try:
            df = pd.read_excel('noms.xlsx')
            if not df.empty:
                # Utilisez self.current_user pour trouver l'utilisateur actuel
                if self.current_user in df['Nom dutilisateur'].values:
                    # Mettez à jour le mot de passe pour l'utilisateur actuel
                    df.loc[df['Nom dutilisateur'] == self.current_user, 'Mot de passe'] = new_password

                    # Maintenant, sauvegardez le DataFrame mis à jour dans le fichier Excel
                    df.to_excel('noms.xlsx', index=False)

                    # Affichez un message de confirmation
                    messagebox.showinfo("Succès", "Mot de passe mis à jour avec succès.")
                else:
                    messagebox.showerror("Erreur", "Utilisateur actuel introuvable.")
            else:
                messagebox.showerror("Erreur", "Aucun utilisateur enregistré.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

        # Fermer la fenêtre de changement de mot de passe
        self.root.destroy()

# ...

# Créer une fenêtre principale
root = tk.Tk()
login_screen = Login(root)

root.mainloop()

