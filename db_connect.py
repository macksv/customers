"""Create a database connection string.
   The DB credentials are stored here so it is important to secure this
   file so only authorised users are able to read it. 
   This should also not be included in the GIT repository (only included here for demo purposes.) 
"""


def get_connect_str():
    DRIVER = "{ODBC Driver 17 for SQL Server}"
    SERVER_NAME = "localhost"  # "michael-HP-Notebook"
    DATABASE_NAME = "TestDB"
    USER_NAME = "TestUser1"
    PASSWORD = "PassUser1"
    conn_str = "DRIVER=" + DRIVER + \
        ";SERVER=" + SERVER_NAME + \
        ";DATABASE=" + DATABASE_NAME + \
        ";UID=" + USER_NAME + \
        ";PWD=" + PASSWORD

    return(conn_str)
