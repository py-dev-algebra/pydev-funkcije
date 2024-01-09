import os


polja_na_ploci = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def provjeri_status_igre():
    if polja_na_ploci[1] == polja_na_ploci[2] == polja_na_ploci[3]:
        return 1
    elif polja_na_ploci[4] == polja_na_ploci[5] == polja_na_ploci[6]:
        return 1
    elif polja_na_ploci[7] == polja_na_ploci[8] == polja_na_ploci[9]:
        return 1
    elif polja_na_ploci[1] == polja_na_ploci[4] == polja_na_ploci[7]:
        return 1
    elif polja_na_ploci[2] == polja_na_ploci[5] == polja_na_ploci[8]:
        return 1
    elif polja_na_ploci[3] == polja_na_ploci[6] == polja_na_ploci[9]:
        return 1
    elif polja_na_ploci[1] == polja_na_ploci[5] == polja_na_ploci[9]:
        return 1
    elif polja_na_ploci[3] == polja_na_ploci[5] == polja_na_ploci[7]:
        return 1
    elif (polja_na_ploci[1] != 1 and
            polja_na_ploci[2] != 2 and
            polja_na_ploci[3] != 3 and
            polja_na_ploci[4] != 4 and
            polja_na_ploci[5] != 5 and
            polja_na_ploci[6] != 6 and
            polja_na_ploci[7] != 7 and
            polja_na_ploci[8] != 8 and
            polja_na_ploci[9] != 9):
        return 0
    else:
        return -1


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



igrac = 2
status_igre = -1 # -1 igraj; 1 pobjeda; 0 nerjeseno

while status_igre == -1:
    iscrtaj_plocu()
    if igrac == 1:
        igrac += 1
    else:
        igrac -= 1


    print(f'Igrac {igrac}')
    while True:
        izabrano_polje = int(input('Unesite broj polja na ploci: '))
        if izabrano_polje in list(range(1, 10)):
            break

    if igrac == 1:
        oznaka_igraca = 'X'
    else:
        oznaka_igraca = 'O'

    for number in polja_na_ploci:
        if izabrano_polje == number and polja_na_ploci[number] == number:
            polja_na_ploci[number] = oznaka_igraca

    #region DUZI NACIN
    # if izabrano_polje == 1 and polja_na_ploci[1] == 1:
    #     polja_na_ploci[1] = oznaka_igraca
    # elif izabrano_polje == 2 and polja_na_ploci[2] == 2:
    #     polja_na_ploci[2] = oznaka_igraca
    # elif izabrano_polje == 3 and polja_na_ploci[3] == 3:
    #     polja_na_ploci[3] = oznaka_igraca
    # elif izabrano_polje == 4 and polja_na_ploci[4] == 4:
    #     polja_na_ploci[4] = oznaka_igraca
    # elif izabrano_polje == 5 and polja_na_ploci[5] == 5:
    #     polja_na_ploci[5] = oznaka_igraca
    # elif izabrano_polje == 6 and polja_na_ploci[6] == 6:
    #     polja_na_ploci[6] = oznaka_igraca
    # elif izabrano_polje == 7 and polja_na_ploci[7] == 7:
    #     polja_na_ploci[7] = oznaka_igraca
    # elif izabrano_polje == 8 and polja_na_ploci[8] == 8:
    #     polja_na_ploci[8] = oznaka_igraca
    # elif izabrano_polje == 9 and polja_na_ploci[9] == 9:
    #     polja_na_ploci[9] = oznaka_igraca
    #endregion

    # provjera statusa igre
    status_igre = provjeri_status_igre()


iscrtaj_plocu()
if status_igre == 1:
    print(f'Igrac {igrac} je pobijedio\n')
else:
    print(f'Nerijeseno\n')



    