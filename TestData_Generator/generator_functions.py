import itertools as it
import input_functions as inptf


"""
=================
    NUMBER GENERATOR
=================
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
=================
    PHONE GENERATOR 
=================
'''

def gen_phone(data_amount):

    phone_numbers = []
    phone1 = "0660 0000 10"

    #--create full phone_numbers by appending numbers in range of amount
    for i in range(data_amount):
        phone = phone1 + str(i)
        phone_numbers.append(phone)

    return phone_numbers

"""
================
    NAME GENERATOR
================
"""

def gen_name(data_amount):

    #TODO: Miniliste Vornamen, Miniliste Nachnamen, durchcyclen (?)
    count = 1
    names = []

    # generate name
    for i in range(data_amount):
        name = "Vorname Nachname " + str(count)
        count += 1
        names.append(name)

    return names
"""
===============
    EMAIL GENERATOR 
===============
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
