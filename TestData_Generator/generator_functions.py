import itertools as it


"""
=================
    NUMBER GENERATOR
=================
"""

def gen_number(data_amount):

    numbers = []
    count = 1

    data_category = 'Zahlen'
    amount = inptf.get_number_generations(data_category)

    for i in range(data_amount):
        numbers.append(count)
        count += 1

    for num in numbers:
        print(num)

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

    for number in phone_numbers:
        print(number)

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

    # print name
    for name in names:
        print(name)

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

    for mail in mails:
        print(mail)
