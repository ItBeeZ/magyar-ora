import random
from colorama import Fore, Style

lista = ['Kőszegi Bence', 'Czene Bálint', 'Kurtucz Krisztián']


gen = random.choice(lista)

while len(lista) > 0:
    #print(len(lista))
    beker = input('A név sorsoláshoz kérem nyomjon egy Enter-t\t')
    if len(lista) == 1:
        print(f'Az utolsó felelő \033[95m{lista[0]}\033[0m lesz\n')
        break
    elif gen in lista:
        if len(lista) == 3:
            print(f'Az első \033[95m{gen}\033[0m lesz\n')
            lista.remove(gen)
        elif len(lista) < 3:
            print(f'Az következő \033[95m{gen}\033[0m lesz\n')
            lista.remove(gen)
        gen = random.choice(lista)
    if not gen in lista:
        gen = random.choice(lista)
        

