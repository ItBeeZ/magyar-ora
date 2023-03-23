import random
from colorama import Fore, Style

lista = ['Szalay Balázs', 'Czene Bálint', 'Hrabovszki Bálint', 'Erdélyi Barnabás', 'Kőszegi Bence', 'Lajos Boton', 'Kovács Dávid', 'Eszenyi Panna', 'Zátonyi Gábor', 'Gál Gréta', 'Szijjárto Gyula', 'Halász Sándor', 'Dudaszeg Krisztián', 'Kurtucz Krisztián', 'Nagy László Krisztián', 'Gaál Levente', 'Varga Levente', 'Madarász Máté', 'Zsuzsa Mihály', 'Miklos Dávid', 'Molnár Norman', 'Szendy Norbert', 'Beke Richárd', 'Szegedi Richárd', 'Rostás Szilárd', 'Tiba Bálint', 'Vicze Sándor', 'Balassa Zalán', 'Futaki Zoltán', 'Kiss Zoltán', 'Somogyi Zsombor']


gen = random.choice(lista)

while len(lista) > 0:
    #print(len(lista))
    beker = input('A név sorsoláshoz kérem nyomjon egy Enter-t\t')
    if len(lista) == 1:
        print(f'Az utolsó felelő \033[95m{lista[0]}\033[0m lesz\n')
        break
    elif gen in lista:
        if len(lista) == 31:
            print(f'Az első felelő \033[95m{gen}\033[0m lesz\n')
            lista.remove(gen)
        elif len(lista) < 31:
            print(f'Az következő felelő \033[95m{gen}\033[0m lesz\n')
            lista.remove(gen)
        gen = random.choice(lista)
    if not gen in lista:
        gen = random.choice(lista)
        

