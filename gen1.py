import random
from colorama import Fore, Style

lista = ['Kőszegi Bence', 'Czene Bálint', 'Kurtucz Krisztián']


gen = random.choice(lista)

while len(lista) > 0:
    beker = input('A név sorsoláshoz kérem nyomjon egy Enter-t\t')
    if len(lista) == 1:
        print(f'A UTOLSÓ FELELŐ {lista[0]} LESZ\n')
        print(f"{Fore.GREEN}Ez a szöveg zöld színnel jelenik meg!{Style.RESET_ALL}")
        break
    elif gen in lista:
        print(f'A KÖVETKEZŐ FELELŐ {gen} LESZ\n')
        lista.remove(gen)
        gen = random.choice(lista)
    if not gen in lista:
        gen = random.choice(lista)
        
        
