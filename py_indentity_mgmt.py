# import dio
import os


# incijalizacija
users_db = {
    'administrator': {
        'first_name': 'Pero',
        'last_name': 'Peric',
        'password': 'Pa$$w0rd!'
    }
}


def home_screen(message = ''):
    os.system('cls' if os.name == 'nt' else 'clear')    
    print('\nDobro dosli u APPLIKACIJU\n')
    print('Za pocetak se trebate prijaviti u sustav\n')
    
    print(message)

    username = input('Upisite Vase korisnicko ime: ')
    password = input('Upisite Vas u lozinku: ')
    print()

    if login(username, password):
        menu(username)
    else:
        home_screen('Pogresan unos!\n')


def menu(username: str):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n')
        print(f'Dobro dosli {users_db[username]['first_name']} {users_db[username]['last_name']}')
        print('\n')
        print('1. Ime Prezime Profil')
        print('2. Uredi profil')
        print('3. Dodaj novog korisnika')
        print('4. Odjavi se\n')

        izbor = int(input('Izaberite jedan broj iz izbornika: '))
        if izbor == 1:
            profile()
        elif izbor == 2:
            edit_user()
        elif izbor == 3:
            add_user()
        elif izbor == 4:
            logout()


def user_profile():
    print('PROFILE')


def login(user_name: str, password: str) -> bool:
    if user_name in users_db.keys():
        if password == users_db[user_name]['password']:
            return True
    else:
        return False


def logout():
    home_screen()


def add_user():
    global users_db

    username = input('Upisite username korisnika: ')
    first_name = input('Upisite ime korisnika: ')
    last_name = input('Upisite prezime korisnika: ')
    password = input('Upisite lozinku korisnika: ')
    
    users_db[username] = {
        'first_name' : first_name,
        'last_name' : last_name,
        'password' : password
    }


def edit_user():
    print('EDIT USER')

    

# main
home_screen()





# kraj

