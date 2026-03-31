

#------- OUTPUT: all Items in generated data list of items in chosen data category

def print_generated_data(data_category,item_list):
    print("")
    for item in item_list:
        print(f"{item}")

    # TODO: korrekte sql taugliche output formatierung gemäß datentyp! (zahlen u stringformate unterscheiden)