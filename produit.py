from db import BoutiqueDatabase

class Produit():
    def __init__(self, database):
        self.database = database

    def ajouter(self, nom, description, prix, quantite, id_categorie):
        conn = self.database.create_conn()
        cursor = conn.cursor()
        cursor.execute("USE boutique")
        cursor.execute("INSERT INTO produit (nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s)", (nom, description, prix, quantite, id_categorie))
        conn.commit()
        cursor.close()
        conn.close()

    def modifier(self, id, nom, description, prix, quantite, id_categorie):
        conn = self.database.create_conn()
        cursor = conn.cursor()
        cursor.execute("USE boutique")
        cursor.execute("UPDATE produit SET nom=%s, description=%s, prix=%s, quantite=%s, id_categorie=%s WHERE id=%s", (nom, description, prix, quantite, id_categorie, id))
        conn.commit()
        cursor.close()
        conn.close()

    def supprimer(self, id):
        conn = self.database.create_conn()
        cursor = conn.cursor()
        cursor.execute("USE boutique")
        cursor.execute("DELETE FROM produit WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()

    def recuperer_tous(self):
        conn = self.database.create_conn()
        cursor = conn.cursor()
        cursor.execute("USE boutique")
        cursor.execute("SELECT * FROM produit")
        produits = cursor.fetchall()
        cursor.close()
        conn.close()
        return produits
    
    def supprimer_tous(self):
        conn = self.database.create_conn()
        cursor = conn.cursor()
        cursor.execute("USE boutique")
        cursor.execute("DELETE FROM produit")
        conn.commit()
        cursor.close()
        conn.close()