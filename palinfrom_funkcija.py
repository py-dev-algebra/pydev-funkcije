# IMPORT



# DEKLARACIJE
# FUNKCIJE
# def naziv_funkcije(argument1, argument2, ...):
#    instrukcije unutar funkcije
def is_palindrom(rijec: str) -> bool:
    obrnuta_rijec = rijec[ : : -1]
    if rijec == obrnuta_rijec:
        return True
    else:
        return False


# VARIJABLE





# GLAVNI DIO PROGRAMA - MAIN

while True:
    rijec = input('Upisite rijec za koju zelite provjeriti je li palindrom: ')

    if is_palindrom(rijec):
        print(f'Rijec {rijec} JE palindrom')
    else:
        print(f'Rijec {rijec} NIJE palindrom')



    prekid = input('Zelite li provjeriti jos jednu rijec? (Da/Ne): ')
    if prekid.lower() != 'da':
        break


# KRAJ
