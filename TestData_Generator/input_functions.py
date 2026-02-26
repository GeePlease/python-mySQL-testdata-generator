#------- USER INPUT: Data Category

def get_data_category():

    print("\nTestdaten - Kategorie:\n")
    print("[1] - Zahlen\n[2] - Telefonnummern\n[3] - Namen\n[4] - Emailadressen\n")

    data_category = int(input("Auswahl: "))

    if data_category == 1:
        return "Zahlen"
    elif data_category == 2:
        return "Telefonnummern"
    elif data_category == 3:
        return "Namen"
    elif data_category == 4:
        return "Email-Adressen"


#------- USER INPUT: Number of Generations

def get_number_generations(data_category):

    amount = int(input(f"Wie viele {data_category} generieren?: "))
    return amount
