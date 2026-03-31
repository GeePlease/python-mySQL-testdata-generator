#create insert into

#note: vorerst 1 Spalte!

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






