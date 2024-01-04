ime = 'Pero'
prezime = 'Peric'


def display_user():
    global ime
    global prezime

    titula = 'dipl. ing. mr. dr. prof.'
    
    ime = ime.upper()
    prezime = prezime.upper()
    print(f'Titula: {titula}\tIme: {ime}\tPrezime: {prezime}')








display_user()
display_user()
print(ime, prezime)
print(titula)
