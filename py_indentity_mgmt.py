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
        menu()
    else:
        home_screen('Pogresan unos!\n')


def menu():
    print('\n')
    print('1. Ime Prezime Profil')
    print('2. Uredi profil')
    print('3. Dodaj novog korisnika')
    print('4. Odjavi se\n')

    izbor = input('Izaberite jedan broj iz izbornika: ')
    if izbor == 1:
        profile()
    elif izbor == 2:
        edit_user()
    elif izbor == 3:
        add_user()
    elif izbor == 4:
        logout()
    else:
        print('Pogresan unos')


def user_profile():
    pass


def login(user_name: str, password: str) -> bool:
    if user_name in users_db.keys():
        if password == users_db[user_name]['password']:
            return True
    else:
        return False


def logout():
    pass


def add_user():
    pass


def edit_user():
    pass

    

# main
home_screen()





# kraj

