import sqlite3
DB_NAME="users.db"
def create_database():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS role(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        role WARCHAR(25)
                        )
                    """)
    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS users(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        login VARCHAR(25),
                        password VARCHAR(8),
                        role_fk INTEGER,
                        FOREIGN KEY(role_fk) REFERENCES role(id) ON DELETE CASCADE
                        );
                    """)
    connect.commit()
    cursor.close()
#create_database()
def insert_into():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    roles=[("Администратор",),
    ("Модератор",),
    ("Пользователь",),
    ("Гость",)]


    #INSERT INTO role (role) VALUES("Admin");
    for role in roles:
        cursor.execute("""
                        INSERT INTO role (role) 
                        VALUES(?)
                    """,role)
        

    users=[
            ("user1", "Pass1",1),
            ("user2", "Pass2",2),
            ("user3", "Pass3",3),
            ("user4", "Pass4",1),
            ("user5", "Pass5",2),
            ("user6", "Pass6",3),
            ("user7", "Pass7",1)
        ]
    for user in users:
        cursor.execute("""
                        INSERT INTO users(login,password,role_fk) 
                        VALUES(?,?,?)
                    """,user)
    connect.commit()
    cursor.close()
#insert_into()
def select():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute(
        """
        SELECT login,password FROM users WHERE id < 4
        """
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connect.commit()
    cursor.close()
def update():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute(
        """
        UPDATE users SET password="p@ssw0rd" WHERE 1
        """
    )
    connect.commit()
    cursor.close()
def delete():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute(
        """
        DELETE FROM users WHERE 1 
        """
    )
    connect.commit()
    cursor.close()
def select_role():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute(
        """
        SELECT * FROM role WHERE 1
        """
    )
    rows = cursor.fetchall()
    connect.commit()
    cursor.close()
    return rows
def insert_users():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute(
        """
        SELECT * FROM role WHERE 1
        """
    )
    rows = cursor.fetchall()
    connect.commit()
    cursor.close()
    return rows
def insert_into():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute(
        """
        SELECT * FROM role WHERE 1
        """
    )
    rows = cursor.fetchall()
    connect.commit()
    cursor.close()
    return rows
def select_user():
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute(
        """
        SELECT * FROM role WHERE 1
        """
    )
    rows = cursor.fetchall()
    connect.commit()
    cursor.close()
    return rows
def select_avtoriz(login,password):
    connect = sqlite3.connect(DB_NAME)
    cursor = connect.cursor()
    cursor.execute(
        """
        SELECT * FROM users WHERE login=? AND password=?
        """,(login, password)
    )
    rows = cursor.fetchall()
    connect.commit()
    cursor.close()
    return rows
#insert_into()
#update()
#select()
#delete
