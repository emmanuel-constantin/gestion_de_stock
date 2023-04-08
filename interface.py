import tkinter as tk
from tkinter import messagebox, ttk
from produit import Produit
from categorie import Categorie

class GestionStockGUI:
    def __init__(self, produit, categorie):
        self.produit = produit
        self.categorie = categorie
        self.root = tk.Tk()
        self.root.title("Cdiscount")
        self.btn_supprimer_tout = tk.Button(self.root, text="Supprimer tout", command=self.supprimer_tous_produits)
        self.btn_supprimer_tout.pack()

        self.tree = ttk.Treeview(self.root, columns=("ID", "Nom", "Description", "Prix", "Quantité", "ID Catégorie"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Prix", text="Prix")
        self.tree.heading("Quantité", text="Quantité")
        self.tree.heading("ID Catégorie", text="ID Catégorie")
        self.tree.pack()

        self.btn_ajouter = tk.Button(self.root, text="Ajouter", command=self.ajouter_produit_popup)
        self.btn_ajouter.pack()

        self.btn_supprimer = tk.Button(self.root, text="Supprimer", command=self.supprimer_produit_click)
        self.btn_supprimer.pack()
        
        self.btn_modifier = tk.Button(self.root, text="Modifier", command=self.modifier_produit_popup)
        self.btn_modifier.pack()

        self.afficher_produits()

    def ajouter_produit_popup(self):
        popup = tk.Toplevel()
        popup.title("Ajouter un produit")

        label_nom = tk.Label(popup, text="Nom")
        label_nom.grid(row=0, column=0)
        entry_nom = tk.Entry(popup)
        entry_nom.grid(row=0, column=1)

        label_description = tk.Label(popup, text="Description")
        label_description.grid(row=1, column=0)
        entry_description = tk.Entry(popup)
        entry_description.grid(row=1, column=1)

        label_prix = tk.Label(popup, text="Prix")
        label_prix.grid(row=2, column=0)
        entry_prix = tk.Entry(popup)
        entry_prix.grid(row=2, column=1)

        label_quantite = tk.Label(popup, text="Quantité")
        label_quantite.grid(row=3, column=0)
        entry_quantite = tk.Entry(popup)
        entry_quantite.grid(row=3, column=1)

        label_categorie = tk.Label(popup, text="Catégorie")
        label_categorie.grid(row=4, column=0)
        combo_categorie = ttk.Combobox(popup)
        combo_categorie['values'] = [cat[1] for cat in self.categorie.recuperer_toutes()]
        combo_categorie.grid(row=4, column=1)

        def ajouter_produit_click():
            nom = entry_nom.get()
            description = entry_description.get()
            prix = entry_prix.get()
            quantite = entry_quantite.get()
            categorie = combo_categorie.get()

            id_categorie = [cat[0] for cat in self.categorie.recuperer_toutes() if cat[1] == categorie][0]

            self.produit.ajouter(nom, description, prix, quantite, id_categorie)
            messagebox.showinfo("Succès", "Produit ajouté avec succès")
            popup.destroy()
            self.afficher_produits()

        btn_ajouter = tk.Button(popup, text="Ajouter", command=ajouter_produit_click)
        btn_ajouter.grid(row=5, column=0, columnspan=2)

    def supprimer_produit_click(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Sélectionner un produit", "Veuillez sélectionner un produit à supprimer.")
            return
        item = self.tree.item(selected_item)
        self.produit.supprimer(item['values'][0])
        messagebox.showinfo("Succès", "Produit supprimé avec succès")
        self.afficher_produits()
    def afficher_produits(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for produit in self.produit.recuperer_tous():
            self.tree.insert("", "end", values=produit)

    def modifier_produit_popup(self):
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Sélectionner un produit", "Veuillez sélectionner un produit à modifier.")
            return
        item = self.tree.item(selected_item)
        popup = tk.Toplevel(self.root)
        popup.title("Modifier un produit")

        label_nom = tk.Label(popup, text="Nom")
        label_nom.grid(row=0, column=0)
        entry_nom = tk.Entry(popup)
        entry_nom.insert(0, item['values'][1])
        entry_nom.grid(row=0, column=1)

        label_description = tk.Label(popup, text="Description")
        label_description.grid(row=1, column=0)
        entry_description = tk.Entry(popup)
        entry_description.insert(0, item['values'][2])
        entry_description.grid(row=1, column=1)

        label_prix = tk.Label(popup, text="Prix")
        label_prix.grid(row=2, column=0)
        entry_prix = tk.Entry(popup)
        entry_prix.insert(0, item['values'][3])
        entry_prix.grid(row=2, column=1)

        label_quantite = tk.Label(popup, text="Quantité")
        label_quantite.grid(row=3, column=0)
        entry_quantite = tk.Entry(popup)
        entry_quantite.insert(0, item['values'][4])
        entry_quantite.grid(row=3, column=1)

        label_categorie = tk.Label(popup, text="Catégorie")
        label_categorie.grid(row=4, column=0)
        combo_categorie = ttk.Combobox(popup)
        combo_categorie['values'] = [cat[1] for cat in self.categorie.recuperer_toutes()]
        combo_categorie.set([cat[1] for cat in self.categorie.recuperer_toutes() if cat[0] == item['values'][5]][0])
        combo_categorie.grid(row=4, column=1)

        def modifier_produit_click():
            id = item['values'][0]
            nom = entry_nom.get()
            description = entry_description.get()
            prix = entry_prix.get()
            quantite = entry_quantite.get()
            categorie = combo_categorie.get()
            id_categorie = [cat[0] for cat in self.categorie.recuperer_toutes() if cat[1] == categorie][0]
            self.produit.modifier(id, nom, description, prix, quantite, id_categorie)
            messagebox.showinfo("Succès", "Produit modifié avec succès")
            self.afficher_produits()
            popup.destroy()

        btn_modifier = tk.Button(popup, text="Modifier", command=modifier_produit_click)
        btn_modifier.grid(row=5, column=0, columnspan=2)
    
    def supprimer_tous_produits(self):
        confirmation = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer tous les produits ?")
        if confirmation:
            self.produit.supprimer_tous()
            messagebox.showinfo("Succès", "Tous les produits ont été supprimés avec succès.")
            self.afficher_produits()
    
    def run(self):
        self.root.mainloop()