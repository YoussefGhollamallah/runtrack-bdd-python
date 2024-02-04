from tkinter import *
from tkinter import messagebox
from produit import *

screen = Tk()
screen.title("Gestionnaire de stock")
screen.geometry("1000x790")
screen.maxsize(1500, 800)

produits_instance = Produits(nom="", description="", prix="", quantite="", id_categorie="")

fenetre_stock = Frame(screen, bg="gray")
fenetre_stock.place(x=5, y=5, width=700, height=470)

fenetre_ajout = Frame(screen, bg="red")
fenetre_ajout.place(x=5, y=480, width=900, height=300)

nom_produit = Label(fenetre_ajout, text="Nom")
nom_produit.place(x=5, y=5, width=100, height=30)
nom = Entry(fenetre_ajout, width=100)
nom.place(x=5, y=40, height=30, width=100)

prix_produit = Label(fenetre_ajout, text="Prix")
prix_produit.place(x=110, y=5, width=100, height=30)
prix = Entry(fenetre_ajout, width=100)
prix.place(x=110, y=40, height=30, width=100)

id_produit = Label(fenetre_ajout, text="ID Produit")
id_produit.place(x=215, y=5, width=100, height=30)
id_entry = Entry(fenetre_ajout, width=100)
id_entry.place(x=215, y=40, height=30, width=100)

quantite_produit = Label(fenetre_ajout, text="Quantité")
quantite_produit.place(x=320, y=5, width=100, height=30)
quantite = Entry(fenetre_ajout, width=100)
quantite.place(x=320, y=40, height=30, width=100)

description_produit = Label(fenetre_ajout, text="Description")
description_produit.place(x=5, y=75, width=100, height=30)
description = Text(fenetre_ajout, width=100, height=70)
description.place(x=5, y=110, width=315, height=70)

success_label = Label(fenetre_ajout, text="", fg="green")
success_label.place(x=5, y=220, width=400, height=30)

listbox = Listbox(fenetre_stock, width=50, height=15)
listbox.place(x=10, y=10, width=680, height=450)

# Affichage des catégories
selected_category = StringVar()
categories_list = ["1 : Fruit", "2 : Legume", "3 : Electronique", '4 : Livre']
category_label = Label(fenetre_ajout, text="LISTE DES CATEGORIES")
category_label.place(x=500, y=5, width=250, height=30)
category_dropdown = OptionMenu(fenetre_ajout, selected_category, *categories_list)
category_dropdown.place(x=500, y=40, width=250, height=30)


def update_produit_list():
    listbox.delete(0, END)
    all_produits = produits_instance.get_all_produits()
    for produit in all_produits:
        listbox.insert(END, f"- Nom: {produit['nom']}, description: {produit["description"]} Prix: {produit['prix']}, Quantité: {produit['quantite']}, Catégories : {produit['noms']}")

def test():
    try:
        add = Produits(nom=nom.get(), description=description.get("1.0", "end-1c"),
                       prix=prix.get(), quantite=quantite.get(), id_categorie=id_entry.get())
        add.connect()
        add.add_produit()
        success_label.config(text="Produit ajouté avec succès!", fg="green")
        update_produit_list()
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite lors de l'ajout du produit : {str(e)}")
    finally:
        try:
            # Disconnect only if the connection is established
            if add.connection:
                add.disconnect()
        except Exception as e:
            print(f"Erreur lors de la déconnexion : {str(e)}")


add_button = Button(fenetre_ajout, text="Ajouter Produit", command=test)
add_button.place(x=5, y=185, width=200, height=30)

nom_produit_supprimer = Label(fenetre_ajout, text="Nom du Produit à Supprimer")
nom_produit_supprimer.place(x=530, y=185, width=200, height=30)
nom_supprimer = Entry(fenetre_ajout, width=150)
nom_supprimer.place(x=530, y=220, height=30, width=200)

def delete_produit_by_name():
    nom_produit_a_supprimer = nom_supprimer.get()
    if nom_produit_a_supprimer:
        try:
            produits_instance.connect() 
            if produits_instance.delete_product_by_name(nom_produit_a_supprimer):
                success_label.config(text="Produit supprimé avec succès!", fg="red")
                update_produit_list()
            else:
                messagebox.showerror("Erreur", f"Aucun produit trouvé avec le nom '{nom_produit_a_supprimer}'.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite lors de la suppression du produit: {str(e)}")
        finally:
            produits_instance.disconnect() 
    else:
        messagebox.showwarning("Avertissement", "Veuillez saisir le nom du produit à supprimer.")



delete_button = Button(fenetre_ajout, text="Supprimer Produit par Nom", command=delete_produit_by_name)
delete_button.place(x=530, y=260, width=200, height=30)


produits_instance.connect()
update_produit_list()
produits_instance.disconnect()

screen.mainloop()
