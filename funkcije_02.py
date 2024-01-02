import datetime as dt


def hello(first_name: str, last_name: str) -> None:
    '''
    Funkcija koja izpisuje pozdrav za uneseno ime i prezime
    '''
    print(f'Hello {first_name} {last_name}!')


def time_in_Sibenik() -> str:
    # time = f'Hallo, its {dt.datetime.now().hour}:{dt.datetime.now().minute} hours in Sibenik!'
    # return time
    return f'Hallo, its {dt.datetime.now().hour}:{dt.datetime.now().minute} hours in Sibenik!'






hello('Pero', 'Peric')
# print(datetime.datetime.now().hour)

rezultat_funkcije = time_in_Sibenik()
print(rezultat_funkcije.upper())
print(time_in_Sibenik().upper())