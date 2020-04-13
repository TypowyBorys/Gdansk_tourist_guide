import sys
import tkinter

okno = tkinter.Tk()


def koniec():
    sys.exit()


def odpowiedz0():
    x = e1.get()
    l1.config(text=x + " przećwiczymy dziś razem Drogę Królewską.")
    b2.config(command=prosba)


def prosba():
    l1.config(
        text="Na początek prośba. Wszystkie daty i wieki wpisuj w formie liczb Rzymskich a nie Arabskich "
             "np. wiek X a nie 10. Słowa i nazwiska rozpoczynaj od wielkiej litery.")
    b2.config(command=pytanie1)


def pytanie1():
    l1.config(
        text="W którym wieku zbudowano renesansową Złotą Bramę wzniesioną na miejscu "
             "średniowecznej Bramy Długoulicznej?")
    b2.config(command=odpowiedz1)


def odpowiedz1():
    x = e1.get()
    if x == "XVII":
        l1.config(text="Zgdza się! Została zbudowana w wieku XVII na postawie projektu Abrahama van den Block'a.")
    else:
        l1.config(text="Jednak nie. Została zbudowana w wieku XVII na postawie projektu Abrahama van den Block'a.")
    b2.config(command=pytanie2)


def pytanie2():
    l1.config(
        text="Na attyce od strony Przedbramia (zachodniej) wyrastają rzeźby dłuta Piotra Ringeringa sybolizujące: "
             "Pokój, Wolność, Bogactwo i ... (?)")
    b2.config(command=odpowiedz2)


def odpowiedz2():
    x = e1.get()
    if x == "Sławę":
        l1.config(text="Dokłądnie tak :)")
    else:
        l1.config(text="Obawiam się że nie. Czwarta figura symbolizuje Sławę.")
    b2.config(command=pytanie3)


def pytanie3():
    l1.config(text="Od strony ul. Długiej (wschodniej) nad bramą królują: Zgoda, Sprawiedliwość, Pobożność i ... (?)")
    b2.config(command=odpowiedz3)


def odpowiedz3():
    x = e1.get()
    if x == "Roztropność":
        l1.config(text="Dokłądnie tak :)")
    else:
        l1.config(text="Jednak nie. Ostatnia figura symbolizuje Roztroponość.")
    b2.config(command=pytanie4)


def pytanie4():
    l1.config(
        text="Brama Wyżynna zbudowana w XVI wieku jako fragmentu fotyfikacji mijskich, swój obecny kształ uzyskała w "
             "roku 1588, projektu autorstwa architekta... (Pełne imię i nazwisko)")
    b2.config(command=odpowiedz4)


def odpowiedz4():
    x = e1.get()
    if x == "Willem van den Blocke":
        l1.config(text="Właśnie tak! Architekt pochodzenia flamandzkiego, ojciec rodu van den Blocke.")
    else:
        l1.config(
            text="Błąd. Autorem projektu był Willem van den Blocke. Architekt pochodzenia flamandzkiego, "
                 "ojciec rodu van den Blocke.")
    b2.config(command=pytanie5)


def pytanie5():
    l1.config(
        text="Syn Willema, też rzeźbiarz i architekt autor ołtarza w kościele św. Jana "
             "oraz dekoracji Wielkiej Zbrojowni miał na imię? (Imie)")
    b2.config(command=odpowiedz5)


def odpowiedz5():
    x = e1.get()
    if x == "Abraham":
        l1.config(
            text="Zgadza się. Oprucz tego był projektantem i wykonawcą Złotej Bramy, Fontanny Neptuna, "
                 "Złotej Kamieniczki i fasady Dworu Artusa.")
    else:
        l1.config(
            text="Taki wstyd. :( Mowa o Abrahamie van den Blocke. Projektancie i wykonawcy Złotej Bramy, "
                 "Fontanny Neptuna, Złotej Kamieniczki i fasady Dworu Artusa.")
    b2.config(command=pytanie6)


def pytanie6():
    l1.config(
        text="Pomiędzy Bramą Wyżaynną a Złotą Baramą wyrasta gotycko-renesansowy Przedbramie z XIV w. wskład którego "
             "wchodzi Wieża Więzienna i...")
    b2.config(command=odpowiedz6)


def odpowiedz6():
    x = e1.get()
    if x == "Katownia":
        l1.config(text="Dobrze młody przewodniku!")
    else:
        l1.config(text="Źle... oh... źlę... oczwiście chodzi o Katownię.")
    b2.config(command=pytanie7)


def pytanie7():
    l1.config(
        text="Rokokowo-klasycystyczna kamienica pod adresem ul. Długa 12 "
             "w której mieści się Muzeum Wnętrz Mieszczańskich to...")
    b2.config(command=odpowiedz7)


def odpowiedz7():
    x = e1.get()
    if x == "Dom Uphagena":
        l1.config(
            text="Punkt bliżej zdania egzainu. Johann Wilhelm Uphagen bibliofil, miłośnik nauk i patrycjusz gdański. "
                 "Członek Towarzystwa Przyrodniczego w Gdańsku, po II rozbiorze Polski w 1793 roku,"
                 "zrezygnował z pełnienia funkcji rajcy miejskiego.")
    else:
        l1.config(
            text="Pomyłka, to Dom Uphagena. Johann Wilhelm Uphagen bibliofil, miłośnik nauk i patrycjusz gdański. "
                 "Członek Towarzystwa Przyrodniczego w Gdańsku, po II rozbiorze Polski w 1793 roku,"
                 "zrezygnował z pełnienia funkcji rajcy miejskiego.")
    b2.config(command=zakonczenie)


def zakonczenie():
    l1.config(
        text="Dzięki! To już koniec tej część współnego zwiedzania ale uszy do góry jescze wiele wycieczek przed nami. :)")


l1 = tkinter.Label(okno, text="Cześć. Jak masz na imię?")
b1 = tkinter.Button(okno, text="Zakończ", command=koniec)
b2 = tkinter.Button(okno, text="Dalej >>", command=odpowiedz0)
e1 = tkinter.Entry(okno)

l1.pack()
e1.pack()
b2.pack()

b1.pack()

okno.mainloop()
