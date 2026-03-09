
import input_functions as inptf
import generator_functions as gf
import output_functions as of


def show_menu():

        #user input 4 data category and number of generations, avoiding none
        data_category = inptf.get_data_category()
        if data_category is not None:
            data_amount = inptf.get_number_generations(data_category)

        if data_category == "Zahlen":
            list_of_numbers = gf.gen_number(data_amount)
            of.print_generated_data(data_category, list_of_numbers)

        elif data_category == "Telefonnummern":
            list_of_phone_num = gf.gen_phone(data_amount)
            of.print_generated_data(data_category, list_of_phone_num)

        elif data_category == "Namen":
            list_of_names = gf.gen_name(data_amount)
            of.print_generated_data(data_category, list_of_names)

        elif data_category == "Email-Adressen":
            list_of_mails = gf.gen_email(data_amount)
            of.print_generated_data(data_category, list_of_mails)

        elif data_category == "Orte":
            list_of_locations = gf.gen_location(data_amount)
            of.print_generated_data(data_category, list_of_locations)

        elif data_category == "Daten":
            list_of_dates = gf.gen_date(data_amount)
            of.print_generated_data(data_category, list_of_dates)


