
"""
=======================
    HARD CODED TEST TABLE
=======================
"""
# define table name
TABLE_NAME = 'partygaeste'

# define column names
COLUMNS = ['gastID', 'name', 'email', 'eingeladen']

#define matching column types
COLUM_TYPES = ['num', 'string', 'string', 'string']



"""
=======================
    SINGLE COLUMN FILLER
=======================
"""

def fill_column (column_name, num_of_generations_for_rows):
    #table header
    print(f"INSERT INTO {TABLE_NAME} ({column_name}) VALUES")

    # fill column according to chosen amount of rows
    for i in range(num_of_generations_for_rows - 1):
        print("('Test-Wert'),") # comma as seperator

    # last value ends with semicolon
    print("('Test-Wert');")



'''

INSERT INTO table_name (column_name) VALUES
#amount (of generations) times print
()
()
()


INSERT INTO users (id, name, email, birthdate)
VALUES
(1, 'Max Mustermann', 'max.mustermann@gmail.com', '1995-04-12'),
(2, 'Anna Schmidt', 'anna.schmidt@gmx.at', '1998-11-03'),
(3, 'Peter Müller', 'peter.mueller@outlook.com', '1990-07-21');

'''

item_list = ['Heribert Pokemüller', 'Jessica Jones']
table_name = 'partygaeste'

def insert_column_string(table_name, item_list):
    print(f"INSERT INTO {table_name} VALUES")
    for item in item_list:
        print(f"('{item}')")






