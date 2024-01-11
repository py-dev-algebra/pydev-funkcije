# SIMULACIJA BANKOVNOG RAČUNA
# Zadatak je započet tako da bi korisnici trebali moci nastaviti dalje po ovom predlošku
# firma (naziv, adresa, oib, odgovorna osoba) unos ispis

# 1. len(oib) provjeri je li OIB točno unesen - za sada koristimo samo provjeru je li ima 11 znakova
# 2. simulacija rada računa u banci. kreirati funkcije za
#     polog novca
#     podizanje novca
#     provjeru je li ima dovoljno novca na računu
#     prikaz stanja na računu
#     mogućnost oročenja
#       transakcija - ID    datum, vrijeme, iznos, stanje, broj racuna, opis, korisnik

import random
import datetime
import os

# GLOBALNE VARIJABLE
company_name = ''
company_street_and_number = ''
company_postal_code = ''
company_city = ''
company_tax_id = ' '
company_manager = ''
currency = ' hr'

# Prazan Dictionary u kojem ce biti pohranjene transakcije
transaction_id = 0
transactions = { }

# Format broja racuna: BA-GODINA-MJESEC-Redni_broj 
# BA - Business Account
# Redni_broj - 00001 - 5 znamenki
account_number = ''
account_balance = 0.00

def create_transaction():
    pass


def generate_account_number():
    global account_number

    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    if month < 10:
        month = str('0' + str(month))
    else:
        month = str(month)

    if account_number == '':
        account_number = 'BA-' + str(year) + '-' + month + '-00001'
    else:
        number_str = account_number.split('-')[-1]
        number = int(number_str)

        if number < 9:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-0000' + str(number)
        elif number < 99:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-000' + str(number)
        elif number < 999:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-00' + str(number)
        elif number < 9999:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-0' + str(number)
        else:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-' + str(number)
    
    return account_number

def open_account():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('KREIRANJE RACUNA\n'.center(65))
    print('Podaci o vlasniku racuna\n'.center(65))

    global company_name
    global company_street_and_number 
    global company_postal_code
    global company_city
    global company_tax_id
    global company_manager
    global currency
    global transactions
    global account_balance

    company_name = input('Naziv Tvrtke:\t\t\t\t')
    company_street_and_number = input('Ulica i broj sjedista Tvrtke:\t\t')
    company_postal_code = input('Postanski broj sjedista Tvrtke:\t\t')
    company_city = input('Grad u kojem je sjediste Tvrtke:\t')
    while True:
        company_tax_id = input('OIB Tvrtke:\t\t\t\t')
        # string.isdigit() vraca Ture ako su sve znamenke u stringu brojke
        if len(company_tax_id) != 11 and company_tax_id.isdigit():
            print('OIB mora imati tocno 11 znamenki i moraju biti samo brojke.\nMolimo Vas ponovite unos\n')
        else:
            break
    company_manager = input('Ime i prezime odgovorne osobe Tvrtke:\t')
    print()
    currency = input('Upisite naziv valute racuna (EUR ili HRK):\t')
    if currency.upper() == 'HRK':
        currency = ' hr'
    else:
        currency = ' €'
    
    input('\nSPREMI? (Pritisnite bilo koju tipku) ')    # Nece spremiti nista, jer su sve izmjene vec spremljene, 
                                                        # ali dobro izgleda :-)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('KREIRANJE RACUNA\n'.center(65))
    print(f'Podaci o vlasniku racuna tvrtke {company_name}, su uspjesno spremljeni.')
    input('Za nastavak pritisnite bilo koju tipku\t')

    # Detalji o racunu
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('KREIRANJE RACUNA\n'.center(65))
    print('Stanje racuna\n'.center(65), '\n')

    print(f'Broj racuna {generate_account_number()}')

    # {account_balance:.2f} Broj account_balance zaokruzi na dvije decimale SAMO kod prikaza, broj ostaje ne promijenjen
    print(f'Trenutno stanje racuna:\t{account_balance:.2f}{currency}\n')

    print('Molimo Vas upisite iznos koji zelite poloziti na racun.\nNAPOMENA Molimo Vas koristite decimalnu tocku, a ne zarez.\n')
    amount = input('\t')
    if amount != '':
        amount = float(amount)

        transaction = []
        account_balance += amount

        # transakcija - datum, vrijeme, iznos, stanje, broj racuna, opis
        transaction.append(datetime.datetime.date)
        transaction.append(datetime.datetime.time)
        transaction.append(amount)
        transaction.append(account_balance)
        transaction.append(account_number)
        transaction.append('Polog kod otvaranja racuna')
        transaction.append(company_manager)
        transactions[transaction_id + 1] = transaction

    else:
        amount = 0.00




def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = -1

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('GLAVNI IZBORNIK\n'.center(65))

    if company_name == '':
        print('1. Kreiranje racuna')        # Kreiranje podataka
    else:
        print('1. Azuriranje racuna')       # Azuriranje podataka

    print('2. Prikaz stanja racuna')        # Trenutno stanje
    print('3. Prikaz prometa po racunu')    # Dictionary

    print('4. Polog novca na racun')        # Dodaj na racun i kreiraj transakciju
    print('5. Podizanje novca s racuna')    # Oduzmi s racuna i kreiraj transakciju

    print('0. Izlaz')                       # Izadi iz while petlje

    print('_' * 65)
    if company_name == '':
        while choice != 1 and choice != 0:  # Ako korisnik odustane, treba izaci iz programa
            print('Jos niste otvorili racun. Molimo prvo kreirajte racun. Hvala!')
            print('-' * 65)
            choice = int(input('Vas izbor:\t'))
            print()
    else:
        print('Molimo Vas upisite samo broj ispred opcije koju zelite odabrati')
        print('-' * 65)
        choice = int(input('Vas izbor:\t'))
        print()

    return choice

def display_account_balance():
    # Detalji o racunu
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('PRIKAZ STANJA RACUNA\n'.center(65), '\n')

    print(f'Broj racuna:\t{account_number}')
    print(f'Datum i vrijeme:\t{datetime.datetime.today()} {datetime.datetime.now()}\n')
    
    print(f'Trenutno stanje racuna:\t{account_balance:.2f}{currency}\n\n')
    print('-' * 65)
    input('Za Povratak u Glavni izbornik pritisnite bilo koju tipku\t')



choice = main_menu()

while choice != 0:
    if choice == 1 and company_name == '':
        open_account()
    if choice == 1 and company_name != '':
        # update_account()
        pass
    if choice == 2:
        display_account_balance()
    
    
    choice = main_menu()