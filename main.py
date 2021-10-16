def citireLista():
    l = []
    givenString = input("Dati lista de nr float, despartite prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(float(x))
    return l


def nrIntregiLista(l):
    '''
    Determina nr intregi dintr-o lista de float-uri
    :param l: lista de float-uri
    :return: nr intregi din lista
    '''
    rezultat = []
    for x in l:
        # if x.is_integer()
        if x == int(x):
            rezultat.append(x)
    return rezultat


def test_nrIntregiLista():
    assert (nrIntregiLista([4.1, 5.99]) == []) is True
    assert (nrIntregiLista([2.12, 3.0, 9.9, 11.6, 10.0]) == [3.0, 10.0]) is True


def celMaiMareNrDiv(l, x):
    '''
    Determina cel mai mare nr dintr-o lista care este divizibil cu un nr dat
    :param l: lista de float-uri
    :param x: nr intreg
    :return: cel mai mare nr din lista care este divizibil cu x
    '''

    ''' modul 1
    max = None
    for y in l:
        if y % x and (max is None or y > max):
            max = y
    return max
    
    modul 2
    nrDivCuX = []
    max = None
    for y in l:
        if y % x == 0:
            nrDivCuX.append(y)
    for y in NrDivCuX:
        if max is None or y > max:
            max = y
    return max
    '''

    reversedList = l[:]
    reversedList.sort(reverse=True)
    for y in reversedList:
        if y % x == 0:
            return y


def test_celMaiMareNrDiv():
    assert celMaiMareNrDiv([2.2, 3.0, 5.0, 8.8], 2) is None
    assert celMaiMareNrDiv([7.0, 6.0, 3.2], 3) == 6.0
    assert celMaiMareNrDiv([9.0, 5.5, 12.0, 6.0, 11], 3) == 12.0


def pfPalindrom(l):
    '''
    Determina nr a caror parte fractionara este nr palindrom
    :param l: lista de float-uri
    :return: nr din l a caror parte fractionara este nr palindrom
    '''
    rezultat = []
    for x in l:
        xStr = str(x)
        "3.45 => [3, 45]"
        pf = xStr.split(".")[1]
        # pf[::-1] este pf inversat (ex: "123" => "321")
        if pf == pf[::-1]:
            rezultat.append(x)
    return rezultat


def test_pfPalindrom():
    assert pfPalindrom([1.34, 4.35, 9.19]) == []
    assert pfPalindrom([2.0, 5.66, 7.31, 9.818]) == [2.0, 5.66, 9.818]


def proceseazaLista(l):
    '''
    Determina lista obtinuta din lista initiala in care float-urile cu partea intreaga a radicalului
    nr prim sunt puse ca string-uri cu caracterele in ordine inversa
    :param l:
    :return:
    '''
    rezultat = []
    for x in l:
        radical = x**0.5
        pi = int(radical)
        ok = True
        if pi < 2:
            ok = False
        else:
            for i in range(2, pi//2 + 1):
                if pi % i == 0:
                    ok = False
        if ok:
            rezultat.append(str(x)[::-1])
        else:
            rezultat.append(x)
    return rezultat


def test_proceseazaLista():
    assert proceseazaLista([10.0, 100.0, 12.45, 50.0, 101.2]) == ['0.01', 100.0, '54.21', '0.05', 101.2]


def toateNrPozImpareDescresc(l):
    '''

    :param l:
    :return:
    '''
    '''
    for i in range(3, len(l), 2):
        if l[i-2] < l[i]:
            return False
    return True
    '''

    nrPozImpare = l[1::2]
    for i in range(len(nrPozImpare)-1):
        if nrPozImpare[i] < nrPozImpare[i+1]:
            return False
    return True


def test_toateNrPozImpareDescresc():
    assert toateNrPozImpareDescresc([1, 6, 2, 5]) is True
    assert toateNrPozImpareDescresc([1, 5, 2, 6]) is False
    assert toateNrPozImpareDescresc([1, 6, 2, 5, 7]) is True
    assert toateNrPozImpareDescresc([1, 6, 2, 5, 7, 4]) is True


def nrCifreInserate(l):
    '''

    :param l:
    :return:
    '''
    rezultat = []
    for x in l:
        rezultat.append(x)
        nrCifre = len(str(x))-1
        rezultat.append(nrCifre)
    return rezultat


def test_nrCifreInserate():
    assert nrCifreInserate([4.5, 6.7, 8.91]) == [4.5, 2, 6.7, 2, 8.91, 3]


def main():
    test_nrIntregiLista()
    test_celMaiMareNrDiv()
    test_pfPalindrom()
    test_proceseazaLista()
    test_toateNrPozImpareDescresc()
    test_nrCifreInserate()
    l = []
    while True:
        print("1. Citire lista float-uri")
        print("2. Afisare nr intregi din lista")
        print("3. Afisare cel mai mare nr divizibil cu un nr citit")
        print("4. Afisare nr a caror p.f este palindrom")
        print("5. Afisarea listei obtinute din lista initiala "
            "in care float-urile cu partea intreaga a radicalului nr prim sunt puse ca "
            "string-uri cu caracterele in ordine inversa")
        print("------------------")
        print("6. Sa se determine daca toate nr de pe pozitii impare sunt in ordine descrescatoare")
        print("7. Sa se determine lista formata din lista initiala in care se adauga dupa fiecare nr nr de cifre "
              "din care este format")
        print("a. Afisare lista")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")

        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(nrIntregiLista(l))
        elif optiune == "3":
            x = int(input("Dati un nr: "))
            print(celMaiMareNrDiv(l, x))
        elif optiune == "4":
            print(pfPalindrom(l))
        elif optiune == "5":
            print(proceseazaLista(l))
        elif optiune == "6":
            if (toateNrPozImpareDescresc(l)):
                print("Da")
            else:
                print("Nu")
        elif optiune == "7":
            print(nrCifreInserate(l))
        elif optiune == 'a':
            print(l)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")


main()