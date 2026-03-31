#TODO: wenn zu viele, aufteilen/ auslagern: alpha gen, num gen, alphanum gen, bool gen....


import itertools as it
import random as rn


"""
=======================
    NUMBER GENERATOR
=======================
"""

def gen_number(data_amount):

    numbers = []
    count = 1

    data_category = 'Zahlen'

    for i in range(data_amount):
        numbers.append(count)
        count += 1

    return numbers


'''
=======================
    PHONE GENERATOR 
=======================
'''
def gen_phone(data_amount):

    phone_numbers = []
    phone1 = "0660 0000 10"

    #--create full phone_numbers by appending numbers in range of amount
    for i in range(data_amount):
        phone = phone1 + str(i+1)
        phone_numbers.append(phone)

    return phone_numbers

"""
======================
    NAME GENERATOR
======================
"""

def gen_name(data_amount):

    #leichte Abwechslung durch unterschiedlich lange Listen
    first_names=["Heribert", "Luca", "Emma", "Jessica"]
    last_names=["Pokemüller", "Potter", "Skywalker", "Zoidberg", "Jones"]
    cycled_1names = it.cycle(first_names)
    cycled_2names = it.cycle(last_names)
    names = []

    # generate name
    for i in range(data_amount):
        name = next(cycled_1names)  +" " +  next(cycled_2names)
        names.append(name)

    return names

"""
=====================
    EMAIL GENERATOR 
=====================
"""

def gen_email(data_amount):

    mails = []
    domains = ["@gmail.com", "@outlook.com", "@gmx.at"]
    cycled_domains = it.cycle(domains)

    data_category = 'Email-Adressen'

    #generate and format names as part of email adresses
    names = gen_name(data_amount)
    names = [name.replace(" ", "") for name in names]

    #combined new list
    for name in names:
        mails.append(name + next(cycled_domains))

    return mails

"""
=======================
    LOCATION GENERATOR 
=======================
"""

def gen_location(data_amount):

    locations1=["Klein", "Alt", "Neu", "Unter"]
    locations2=["kirchen", "dorf", "hausen", "stein", "burg"]
    cycled_locations1 = it.cycle(locations1)
    cycled_locations2 = it.cycle(locations2)
    locations_list = []

    # generate name
    for i in range(data_amount):
        location= next(cycled_locations1)  +  next(cycled_locations2)
        locations_list.append(location)

    return locations_list

"""
=======================
    DATE GENERATOR 
=======================
"""

def gen_date(data_amount):

    years = ['1995-', '2000-', '2008-', '2016-', '2020-', '2022-', '2026-']
    months = ['01-', '02-', '03-', '04-', '05-', '06-', '07-', '08-', '09-', '10-', '11-', '12-']
    days = ['06', '08', '10', '12', '03', '20', '10', '11', '01', '15', '28']

    cycled_years = it.cycle(years)
    cycled_months = it.cycle(months)
    cycled_days = it.cycle(days)

    date_list = []

    for i in range(data_amount):
        date = next(cycled_years) + next(cycled_months) + next(cycled_days)
        date_list.append(date)

    return date_list

"""
=======================
    YES/NO GENERATOR 
=======================
"""

def gen_yes_no(data_amount):

    choices = ["ja", "nein"]
    choices_list = []

    for i in range(data_amount):
        chosen = rn.choice(choices)
        choices_list.append(chosen)

    return choices_list

"""
=======================
    WEIGHT GENERATOR
=======================
"""
def gen_weight(data_amount):
    kilo_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    gram_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    cycled_kilos = it.cycle(kilo_list)
    cycled_gram_list = it.cycle(gram_list)

    weight_list = []

    for i in range (data_amount):#
        kilo = next(cycled_kilos)
        gram = next(cycled_gram_list)
        weight = f"{kilo}.{gram}"
        weight_list.append(weight)

    return weight_list

"""
=======================
    PRICE GENERATOR
=======================
"""
def gen_price(data_amount):
    euro_list = [2, 4, 6, 7, 9, 12, 14, 16, 19, 29, 49, 98]
    cent_list = [00, 49, 50, 90, 95, 99]

    cycled_euro_list = it.cycle(euro_list)
    cycled_cent_list = it.cycle(cent_list)

    price_list = []


    for i in range(data_amount):
        euro = next(cycled_euro_list)
        cent = next(cycled_cent_list)
        price =  f"{euro}.{cent}"
        price_list.append(price)

    return price_list