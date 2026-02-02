class Database:
    def __init__(self, db_path: str = "users.db"):
        self.db_path = db_path
        self.init_db()
         
      
    def connection(self):
        conn = sglite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            finaly:
                conn.close()
                
    def init_db(self):
        with self.connection() as conn:
             conn.execute('''
                 CREATE TABLE IF NOT EXISTS (
                  id INTEGER PRIMARI KEY AUTOINCREMENT,
                  user_id INTEGER NOT NULL,
                  first_name varchar(50),
                  last_name varchar(50),
                  user_name varchar(100),
                  language varchar(5)  
                 )     
                 ''')
             
             
             
             conn.commit()    
    
    def create_user(self, useer_info: list)
    with self.connegtion() as conn:
        cursor = conn.execute(
            'INSERT INFO users(user_id, first_name, last_name language)VALUES(?,?,??)'
        )
        conn.commit()