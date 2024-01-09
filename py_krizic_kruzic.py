import os


polja_na_ploci = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def iscrtaj_plocu():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('\tKrizic Kruzic\n\n')
    print('IGRAC 1 (X)\tIGRAC 2 (O)\n')

    print(f'\t {polja_na_ploci[1]} | {polja_na_ploci[2]} | {polja_na_ploci[3]}')
    print(f'\t---|---|---')
    print(f'\t {polja_na_ploci[4]} | {polja_na_ploci[5]} | {polja_na_ploci[6]}')
    print(f'\t---|---|---')
    print(f'\t {polja_na_ploci[7]} | {polja_na_ploci[8]} | {polja_na_ploci[9]}')
    print('\n')

igrac = 1
status_igre = -1 # -1 igraj; 1 pobjeda; 0 nerjeseno
while status_igre == -1:
    iscrtaj_plocu()

    print(f'Igrac {igrac}')
    izabrano_polje = int(input('Unesite broj polja na ploci: '))

    if igrac == 1:
        oznaka_igraca = 'X'
    else:
        oznaka_igraca = 'O'

    if izabrano_polje == 1:
        polja_na_ploci[1] = oznaka_igraca
    elif izabrano_polje == 2:
        polja_na_ploci[2] = oznaka_igraca
    elif izabrano_polje == 3:
        polja_na_ploci[3] = oznaka_igraca
    elif izabrano_polje == 4:
        polja_na_ploci[4] = oznaka_igraca
    elif izabrano_polje == 5:
        polja_na_ploci[5] = oznaka_igraca
    elif izabrano_polje == 6:
        polja_na_ploci[6] = oznaka_igraca
    elif izabrano_polje == 7:
        polja_na_ploci[7] = oznaka_igraca
    elif izabrano_polje == 8:
        polja_na_ploci[8] = oznaka_igraca
    elif izabrano_polje == 9:
        polja_na_ploci[9] = oznaka_igraca

