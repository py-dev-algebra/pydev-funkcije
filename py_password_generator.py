import random


def postavke_passworda():
    while True:
        duzina_passworda = int(input('Upisite duzinu passworda (mora biti vece od 8): '))
        if duzina_passworda >= 8:
            break

    return duzina_passworda



def password_generator(password_lenght: int = 8) -> str:
    password = ''

    if password_lenght < 8:
        return 'Minimalna duzina passowrda je 8 znakova!'

    for i in range(password_lenght):
        znak = chr(random.randint(33, 126))
        if znak not in password:
            password += znak

    return password




print(password_generator(postavke_passworda()))