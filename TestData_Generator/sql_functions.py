from test import table_name

#------- SQL CODE GENERATION (sql formatted)


table_name = 'partygaeste'
column_name = 'name'
item_list = ['Jessica Jones', 'Heribert Pokemüller', 'Harry Potter']

#prototype for single column string inserts
def insert_column_string(table_name, column_name, item_list):

    print(f"INSERT INTO {table_name} ({column_name}) VALUES")

    for item in item_list[:-1]:
            print(f"('{item}'),")
    print (f"('{item_list[-1]}');")

insert_column_string(table_name, column_name, item_list)




table_name = 'partygaeste'
column_name = 'ID'
item_list = [1,2,3,4,5,6,7,8,9,10]

def insert_column_num(table_name, column_name, item_list):

    print(f"INSERT INTO {table_name} ({column_name}) VALUES")

    for item in item_list[:-1]:
            print(f"({item}),")
    print (f"({item_list[-1]});")

insert_column_num(table_name, column_name, item_list)
