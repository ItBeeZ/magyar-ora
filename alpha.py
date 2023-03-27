import random

lista = ['Szalay Balázs', 'Czene Bálint', 'Hrabovszki Bálint', 'Erdélyi Barnabás', 'Kőszegi Bence', 'Lajos Boton', 'Kovács Dávid', 'Eszenyi Panna', 'Zátonyi Gábor', 'Gál Gréta', 'Szijjárto Gyula', 'Halász Sándor', 'Dudaszeg Krisztián', 'Kurtucz Krisztián', 'Nagy László Krisztián', 'Gaál Levente', 'Varga Levente', 'Madarász Máté', 'Zsuzsa Mihály', 'Miklos Dávid', 'Molnár Norman', 'Szendy Norbert', 'Beke Richárd', 'Szegedi Richárd', 'Rostás Szilárd', 'Tiba Bálint', 'Vicze Sándor', 'Balassa Zalán', 'Futaki Zoltán', 'Kiss Zoltán', 'Somogyi Zsombor']

upper = [i.upper() for i in lista]

gen = random.choice(upper)

while len(upper) > 0:
    #print(len(upper))
    beker = input('A név sorsoláshoz kérem nyomjon egy Enter-t\t')
    if len(upper) == 1:
        print(f'Az utolsó felelő {upper[0]} lesz\n')
        break
    elif gen in upper:
        if len(upper) == 31:
            print(f'Az első felelő {gen} lesz\n')
            upper.remove(gen)
        elif len(upper) < 31:
            print(f'Az következő felelő {gen} lesz\n')
            upper.remove(gen)
        gen = random.choice(upper)
    if not gen in upper:
        gen = random.choice(upper)

print('Reméljük mindenki sikeresen lefelelt!')

input()
input()
input()
