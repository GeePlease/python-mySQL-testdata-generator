
#------- USER INPUT: Choice of Data Category

def get_data_category():

    print("\nTestdaten - Kategorie:\n")
    print("[1] - Zahlen\n[2] - Telefonnummern\n[3] - Namen\n[4] - Emailadressen\n[5]"
          " - Orte\n[6] - Daten\n[7] - Ja/ Nein\n[8] - Gewicht\n[9] - Preis\n")

    data_category = int(input("Auswahl: "))

    if data_category == 1:
        return "Zahlen"

    elif data_category == 2:
        return "Telefonnummern"

    elif data_category == 3:
        return "Namen"

    elif data_category == 4:
        return "Email-Adressen"

    elif data_category == 5:
        return "Orte"

    elif data_category == 6:
        return "Daten"

    elif data_category == 7:
        return "Ja/ Nein"

    elif data_category == 8:
        return "Gewicht"

    elif data_category == 9:
        return "Preis"

    else:
        return


#------- USER INPUT: Choice of Number of Generations per data category

def get_number_generations(data_category):

    #TODO: exception um eingabefehler abzufangen
    amount = int(input(f"Wie viele {data_category} generieren?: \n"))
    return amount
