import os, json, getpass, pyodbc

 


# Get credentials
with open(os.path.abspath('config.json'), 'r') as f:
    config = json.load(f)
    host = config['host'] if 'host' in config else input("Enter host: ")
    user = config['user'] if 'user' in config else input("Enter user: ")
    pwd  = getpass.getpass('Enter password: ')
    dns= '{IBM i Access ODBC Driver}'

# Init ODBC connection and cursor
conn = pyodbc.connect(driver=dns, system=host, uid=user, pwd=pwd)
csr = conn.cursor()
try:
    # Execute SQL string
    csr.execute(' '.join([
        "SELECT * FROM HA.LOGP"
        
    ]))
    # Output result set
    for row in csr: 
        print(row)

except Exception as e:
    print('Error occurred with DB2 query\n  ' + str(e))
finally:
    # Close cursor and ODBC connection
    csr.close()
    conn.close()