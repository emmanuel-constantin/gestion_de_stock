from db import BoutiqueDatabase
import mysql.connector

class Categorie:
    def __init__(self, database):
        self.database = database

    def ajouter(self, nom):
        conn = self.database.create_conn()
        cursor = conn.cursor()
        cursor.execute("USE boutique")
        cursor.execute("INSERT INTO categorie (nom) VALUES (%s)", (nom,))
        conn.commit()
        cursor.close()
        conn.close()

    def recuperer_toutes(self):
        conn = self.database.create_conn()
        cursor = conn.cursor()
        cursor.execute("USE boutique")
        cursor.execute("SELECT * FROM categorie")
        categories = cursor.fetchall()
        cursor.close()
        conn.close()
        return categories
    
    def supprimer_toutes_categories(self):
        conn = self.database.create_conn()
        cursor = conn.cursor()
        cursor.execute("USE boutique")

        query = """
            DELETE FROM categorie;
        """
        try:
            cursor.execute(query)
            conn.commit()
        except mysql.connector.Error as e:
            print(f"Erreur: {e}")
        finally:
            cursor.close()
            conn.close()