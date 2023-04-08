from db import BoutiqueDatabase
from produit import Produit
from categorie import Categorie
from interface import GestionStockGUI

db = BoutiqueDatabase("localhost", "root", "password")
produit = Produit(db)
categorie = Categorie(db)
categorie.ajouter("Électronique")
categorie.ajouter("Livres")
categorie.ajouter("Vêtements")
categorie.ajouter("Musique")
categorie.ajouter("DVD")
categorie.ajouter("Jeux vidéos")
categorie.ajouter("Maison")
gui = GestionStockGUI(produit, categorie)
gui.run()



