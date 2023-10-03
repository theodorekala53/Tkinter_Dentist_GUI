import tkinter as tk

def create_account():
    # Fonction pour ouvrir la fenêtre de création de compte
    registration_window.withdraw()
    create_account_window.deiconify()

def back_to_registration():
    # Fonction pour revenir à la fenêtre d'enregistrement
    create_account_window.withdraw()
    registration_window.deiconify()

def submit_registration():
    # Fonction pour soumettre les données d'enregistrement
    username = username_entry.get()
    password = password_entry.get()
    # Vous pouvez ajouter ici le code pour traiter les données d'enregistrement (par exemple, les sauvegarder dans une base de données)

# Crée la fenêtre principale d'enregistrement
registration_window = tk.Tk()
registration_window.title("Enregistrement")

# Crée les champs de saisie pour l'enregistrement
username_label = tk.Label(registration_window, text="Nom d'utilisateur:")
username_entry = tk.Entry(registration_window)
password_label = tk.Label(registration_window, text="Mot de passe:")
password_entry = tk.Entry(registration_window, show="*")

# Crée les boutons pour la création de compte et le retour
create_account_button = tk.Button(registration_window, text="Créer un compte", command=create_account)
submit_button = tk.Button(registration_window, text="Enregistrer", command=submit_registration)

# Place les éléments dans la fenêtre d'enregistrement
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
create_account_button.pack()
submit_button.pack()

# Crée la fenêtre de création de compte (initialement masquée)
create_account_window = tk.Toplevel(registration_window)
create_account_window.title("Créer un compte")
create_account_window.withdraw()

# Crée le champ de saisie pour la création de compte
create_account_label = tk.Label(create_account_window, text="Création de compte en cours...")
back_button = tk.Button(create_account_window, text="Retour à l'enregistrement", command=back_to_registration)

# Place les éléments dans la fenêtre de création de compte
create_account_label.pack()
back_button.pack()

# Lance l'application Tkinter
registration_window.mainloop()
