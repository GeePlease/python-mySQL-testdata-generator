
import input_functions as inptf
import generator_functions as gf


def show_menu():

        data_category = inptf.get_data_category()
        data_amount = inptf.get_number_generations(data_category)

        if data_category == "Zahlen":
            gf.gen_name(data_amount)

        if data_category == "Telefonnummern":
            gf.gen_phone(data_amount)

        if data_category == "Namen":
            gf.gen_name(data_amount)

        if data_category == "Email-Adressen":
            gf.gen_email(data_amount)