import ibm_db
# Chaîne de connexion à la base de données
conn_str = "DATABASE=my_database;HOSTNAME=my_hostname;PORT=my_port;PROTOCOL=TCPIP;UID=my_username;PWD=my_password"

# Établir une connexion à la base de données
conn = ibm_db.connect(conn_str, "", "")

# Préparer et exécuter une requête SQL
sql = "SELECT * FROM ma_table"
stmt = ibm_db.prepare(conn, sql)
ibm_db.execute(stmt)

# Récupérer les résultats
result = ibm_db.fetch_assoc(stmt)
while result:
    print(result)
    result = ibm_db.fetch_assoc(stmt)

# Fermer la connexion à la base de données
ibm_db.close(conn)
