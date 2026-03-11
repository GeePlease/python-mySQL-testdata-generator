from test import table_name

#------- SQL CODE GENERATION (sql formatted)


table_name = 'partygaeste'
column_name = 'name'
item_list = ['Jessica Jones', 'Heribert Pokemüller']

def insert_column_string(table_name, column_name, item_list):
    print(f"INSERT INTO {table_name} {column_name} VALUES")
    for item in item_list:
        print(f"('{item}')")


insert_column_string(table_name, column_name, item_list)