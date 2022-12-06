def wyswietl(**kwargs):
    for i in kwargs.keys():
        print(i,kwargs[i])

wyswietl(wiek = 15, imię = "Howard", nazwisko = "Morgan")
