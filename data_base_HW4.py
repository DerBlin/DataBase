import psycopg2
def create_structure(conn):
    with conn.cursor() as cur: 
        cur.execute('''
                DROP TABLE clients_info, clients_number
                ''')
        cur.execute('''
                    CREATE TABLE if not exists clients_info(
                        id SERIAL PRIMARY KEY, 
                        first_name varchar(120),
                        last_name varchar(120), 
                        email varchar(120)
                    );
                    ''')
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS clients_number(
                        id_client integer references clients_info(id),
                        phone_number varchar(11),
                        constraint pk_clients_number primary key(id_client, phone_number)
                    );
                    ''')
        conn.commit() 
    conn.close() 

def add_client(conn, id, first_name, last_name, email, phone_number = None):
    with conn.cursor() as cur:
        cur.execute('''
                    INSERT INTO clients_info (id, first_name, last_name, email)
                    VALUES (%s, %s, %s, %s);
                    ''', (id, first_name, last_name, email))
        if phone_number != None:
            cur.execute('''
                        INSERT INTO clients_number (id_client, phone_number)
                        VALUES (%s, %s);
                        ''', (id, phone_number))
        conn.commit()
    conn.close()

def add_phone(conn, id, phone_number):
    with conn.cursor() as cur:
        cur.execute('''
                    INSERT INTO clients_number (id_client, phone_number)
                    VALUES (%s, %s);
                    ''', (id, phone_number))
        conn.commit()
    conn.close()

def update_client(conn, id, first_name = None, last_name = None, email = None, phone_number = None):
    with conn.cursor() as cur:
        cur.execute('''
                    UPDATE clients_info
                    SET first_name = %s, last_name = %s, email = %s
                    WHERE id = %s;
                    ''', (first_name, last_name, email, id))
        if phone_number != None:
            cur.execute('''
                        UPDATE clients_number
                        SET phone_number = %s
                        where id_client = %s
                        ''', (phone_number, id))
        conn.commit()      
    conn.close()

def delete_phone(conn, id_client, phone_number):
    with conn.cursor() as cur:
        cur.execute('''
                    DELETE FROM clients_number
                    WHERE id_client = %s and phone_number = %s
                    ''', (id_client, phone_number))
        conn.commit()
    conn.close()

def delete_client(conn, id):
    with conn.cursor() as cur:
        cur.execute('''
                    DELETE FROM clients_number
                    WHERE id_client = %s
                    ''', [id])
        cur.execute('''
                    DELETE FROM clients_info
                    WHERE id = %s
                    ''', [id])
        conn.commit()
    conn.close()

def find_client(conn, first_name = None, last_name = None, email = None, phone_number = None):
    with conn.cursor() as cur:
        cur.execute('''
                SELECT * FROM clients_info
                JOIN clients_number on clients_info.id = clients_number.id_client 
                WHERE (first_name = %(first_name)s or %(first_name)s IS NULL)
                AND (last_name = %(last_name)s or %(last_name)s IS NULL)
                AND (email = %(email)s or %(email)s IS NULL)
                AND (phone_number = %(phone)s or %(phone)s IS NULL)
                ''', {'first_name': first_name, 'last_name': last_name, 'email': email, 'phone': phone_number})
        # conn.commit() 
        x = cur.fetchall()     
    conn.close()
    return x


create_structure(psycopg2.connect(database = 'clients_info', user = 'postgres', password = 'tdutybq8076'))
add_client(psycopg2.connect(database = "clients_info", user = "postgres", password = "tdutybq8076"), 1, 'Bob', 'Marley', 'nicebobby@yandex.ru')
add_client(psycopg2.connect(database = "clients_info", user = "postgres", password = "tdutybq8076"), 2, 'Bob', 'Dylan', 'notnicebob@gmail.com', '11111111111')
add_phone(psycopg2.connect(database = "clients_info", user = "postgres", password = "tdutybq8076"), 1, '89012345678')
add_phone(psycopg2.connect(database = "clients_info", user = "postgres", password = "tdutybq8076"), 2, '81234567890')
update_client(psycopg2.connect(database = "clients_info", user = "postgres", password = "tdutybq8076"), 1, 'Bobby', 'asdasd', 'asdfsdf@sf.ru', '77777777777')
update_client(psycopg2.connect(database = "clients_info", user = "postgres", password = "tdutybq8076"), 2, 'Bobby', 'qwerty', 'lalala@sf.ru')
delete_phone(psycopg2.connect(database = "clients_info", user = "postgres", password = "tdutybq8076"), 1, '77777777777')
delete_client(psycopg2.connect(database = "clients_info", user = "postgres", password = "tdutybq8076"), 1)
print(find_client(psycopg2.connect(database = "clients_info", user = "postgres", password = "tdutybq8076"), None, None, None, '11111111111'))






# conn = psycopg2.connect(database = 'clients_info', user = 'postgres', password = 'tdutybq8076') #подключение к БД
# with conn.cursor() as cur: #контекстный менеджер для курсора (можно не закрывать курсор). В курсоре пишем запросы.
#     cur.execute('''
#                 INSERT INTO clients_info
#                 VALUES
#                 (1, 'Bob', 'Marley', 'nicebobby@yandex.ru'),
#                 (2, 'Bob', 'Dylan', 'notnicebob@gmail.com'),
#                 (3, 'Garry', 'Oldman', 'notyoung@mail.ru');
#                 ''')
#     cur.execute('''
#                 INSERT INTO phone_numbers
#                 VALUES
#                 (1, '89012345678'),
#                 (2, '81234567890'),
#                 (3, '89102834756'),
#                 (4, '89518764563'),
#                 (5, '86514533567'),
#                 (6, '89785674534');
#                 ''')
#     cur.execute('''
#                 INSERT INTO clients_number
#                 VALUES
#                 (1, 1),
#                 (1, 2),
#                 (1, 3),
#                 (2, 4),
#                 (2, 5),
#                 (1, 6);
#                 ''')
#     conn.commit() #применит все курсоры к базе данных
# conn.close() # Обязательно ЗАКРЫТЬ СОЕДИНЕНИЕ!!!!!