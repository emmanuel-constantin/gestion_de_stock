import mysql.connector

class Database:
    def __init__(self, host, user, password):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '****'

    def create_conn(self):
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        return connection

class BoutiqueDatabase(Database):
    def __init__(self, host, user, password):
        super().__init__(host, user, password)
        self.create_database()

    def create_database(self):
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS boutique")
        cursor.execute("USE boutique")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorie (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produit (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255),
                description TEXT,
                prix INT,
                quantite INT,
                id_categorie INT,
                FOREIGN KEY (id_categorie) REFERENCES categorie(id)
            )
        """)
        
        conn.commit()
        cursor.close()
        conn.close()