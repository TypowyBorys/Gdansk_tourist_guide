class Droga_Krolewska(object):
    import time

    print("Cześć. Jak masz na imię?")
    imie = input()
    print(imie, "przećwiczymy dziś razem Drogę Królewską.")
    print("Na początek prośba. Wszystkie daty i wieki wpisuj w formie liczby Arabskich a nie Rzymskich np. wiek 10 a nie X. Słowa i nazwiska rozpoczynaj od wielkiej litery.")
    time.sleep(2)


    print("W którym wieku zbudowano renesansową Złotą Bramę wzniesioną na miejscu średniowecznej Bramy Długoulicznej?")
    BZ1 = input()
    BZ1 = int(BZ1)
    time.sleep(1)

    if BZ1 == 17:
        print("Zgdza się! Została zbudowana w wieku XVII na postawie projektu Abrahama van den Block'a.")
    else: print("Jednak nie. Została zbudowana w wieku XVII na postawie projektu Abrahama van den Block'a.")
    time.sleep(2)

    print("Na attyce od strony Przedbramia (połódniowej) wyrastają rzeźby dłuta Piotra Ringeringa sybolizujące Pokój, Wolność, Bogactwo i ... (?)")

    BZ2 = input()

    if BZ2 == "Sławę":
        print("Dokłądnie tak :)")
    else: print("Obawiam się że nie. Czwarta figura symbolizuje Sławę.")
    time.sleep(1)

    print("Od strony ul. Długiej (wschodniej) nad bramą królują: Zgoda, Sprawiedliwość, Pobożność i ... (?)")

    BZ3 = input()

    if BZ3 == "Roztroponość":
        print("Dokłądnie tak :)")
    else: print("Jednak nie. Ostatnia figura symbolizuje Roztroponość.")
    time.sleep(2)

    print("Dzięki! To już koniec tej część współnego zwiedzania ale uszy do góry jescze wiele wycieczek przed nami. :)")





    time.sleep(10)
    exit()
