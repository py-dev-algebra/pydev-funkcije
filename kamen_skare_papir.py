# IMPORT
import random
import os


# DEKLARACIJA
broj_partija = 0
bodovi_korisnik = 0
bodovi_racunalo = 0


def menu(user_points: int, computer_points: int, broj_partija: int) -> None:
    # if os.name == 'nt':
    #     os.system('cls')
    # else:
    #     os.system('clear')
    os.system('cls' if os.name == 'nt' else 'clear')

    print()
    print(f'Korisnik: {user_points}\t:\tRacunalo: {computer_points}')
    print(f'Partija: {broj_partija}')
    print()
    print('''
        Izbornik opcija (upisite broj ispred opcije):
        1. kamen
        2. skare
        3. papir
    ''')
    print()


def status_igre(user_choice: int, computer_choice: int) -> None:
    global broj_partija
    global bodovi_korisnik
    global bodovi_racunalo

    if user_choice == computer_choice:
        broj_partija += 1
    
    elif user_choice == 1 and computer_choice == 2:
        bodovi_korisnik += 1
        broj_partija += 1
    
    elif user_choice == 1 and computer_choice == 3:
        bodovi_racunalo += 1
        broj_partija += 1

    elif user_choice == 2 and computer_choice == 1:
        bodovi_racunalo += 1
        broj_partija += 1

    elif user_choice == 2 and computer_choice == 3:
        bodovi_korisnik += 1
        broj_partija += 1

    elif user_choice == 3 and computer_choice == 1:
        bodovi_korisnik += 1
        broj_partija += 1

    elif user_choice == 3 and computer_choice == 2:
        bodovi_racunalo += 1
        broj_partija += 1


# GLAVNI PROGRAM - MAIN
while broj_partija < 3:
    menu(bodovi_korisnik, bodovi_racunalo, broj_partija)
    
    izbor_racunala = random.randint(1, 3)    
    while True:
        izbor_korisnika = int(input('Izaberite jednu od ponudenih opcija: '))

        if izbor_korisnika in [1, 2, 3]:
            break
        else:
            print('Krivo ste unijeli')


    # PROVJERA POBJEDNIKA PARTIJE
    status_igre(user_choice=izbor_korisnika, 
                computer_choice=izbor_racunala)



# KRAJ
menu(computer_points=bodovi_racunalo, 
     user_points=bodovi_korisnik,
     broj_partija=broj_partija)

if bodovi_racunalo > bodovi_korisnik:
    print("Izgubili ste")
elif bodovi_racunalo < bodovi_korisnik:
    print("Pobijedili ste")
else:
    print("Nerijeseno")
