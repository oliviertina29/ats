import sqlite3

# Connectez-vous à la base de données
conn = sqlite3.connect('instance/ats.db')
cursor = conn.cursor()

# Obtenez la liste des tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table_name in tables:
    table_name = table_name[0]
    print(f"\nContenu de la table {table_name}:")
    
    # Sélectionnez tout le contenu de la table
    cursor.execute(f"SELECT * FROM {table_name}")
    
    # Affichez les en-têtes des colonnes
    column_names = [description[0] for description in cursor.description]
    print(", ".join(column_names))
    
    # Affichez les données
    for row in cursor.fetchall():
        print(", ".join(map(str, row))) 

conn.close()