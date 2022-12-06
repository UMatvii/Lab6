def z1(imię, wiek = 20):
    ''' Funkcja wypisuje imię oraz wiek.

    :param imię:
    :param wiek:
    :return:
    '''
    print(imię, wiek)

z1("Matvii", 17)
z1("Oleksandr", 20)
z1(19, "Alex")
z1(wiek= 16, imię= "Bond")
print(z1.__doc__)
print(help(z1))
z1("Maxim")