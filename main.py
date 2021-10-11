def prim(numar):
    """
    Verifica daca un numar intreg este prim
    :param numar: o valoare intreaga "numar"
    :return: True, daca "numar" este prim, iar False in caz contrar
    """
    if numar < 2:
        return False
    else:
        for i in range(2, numar // 2):
            if numar % i == 0:
                return False
        return True


def invers(numar):
    """
    Calculeaza inversul unui numar
    :param numar: o valoare intreaga "numar"
    :return: o valoare intreaga "oglindit", reprezentand inversul lui "numar"
    """
    oglindit = 0
    while numar != 0:
        oglindit = (oglindit * 10) + (numar % 10)
        numar = numar // 10
    return oglindit


def get_largest_prime_below(numar):
    """
    Calculeaza ultima valoare prima, mai mica decat "numar"
    :param numar: o valoare intreaga "numar"
    :return: o valoare intreaga
    """
    for i in range(numar, 1, -1):
        verificare = prim(i)
        if verificare is True:
            return i


def is_palindrome(numar):
    """
    Verifica daca un numar este palindrom
    :param numar: o valoare intreaga "numar"
    :return: True, daca "numar" este palindrom, respectiv False in caz contrar
    """
    oglindit = invers(numar)
    if oglindit == numar:
        return True
    return False


def is_superprime(numar):
    """
    Verifica daca un numar este superprim
    :param numar: o valoare intreaga "numar"
    :return: True, daca "numar" este superprim, resprectiv False in caz contrar
    """
    putere = 1
    numar_nou = 0
    while putere * 10 <= numar:
        putere = putere * 10
    while putere != 0:
        cifra = numar // putere
        numar_nou = (numar_nou * 10) + cifra
        verificare = prim(numar_nou)
        if verificare is False:
            return False
        numar = numar % putere
        putere = putere // 10
    return True


def test_get_largest_prime_below():
    assert get_largest_prime_below(25) == 23
    assert get_largest_prime_below(9) == 7
    assert get_largest_prime_below(5) == 5


def test_is_palindrome():
    assert is_palindrome(123) is False
    assert is_palindrome(111) is True
    assert is_palindrome(7) is True


def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(237) is False
    assert is_superprime(7) is True


def meniu():
    print("1. Gasește ultimul numar prim mai mic decat un numar dat.")
    print("2. Determina daca un numar dat este palindrom.")
    print("3. Determina daca un numar este superprim.")
    print("4. Iesire")
    rulare = True
    while rulare is True:
        valoare = int(input("Dati o valoare de la 1 la 4: "))
        if valoare == 1:
            numar = int(input("Introduceti numarul: "))
            rezultat = get_largest_prime_below(numar)
            print("Rezultatul este: ", rezultat)
        elif valoare == 2:
            numar = int(input("Intoduceti numarul: "))
            rezultat = is_palindrome(numar)
            if rezultat is True:
                print("Este palindrom")
            else:
                print("Nu este palindrom")
        elif valoare == 3:
            numar = int(input("Intoduceti numarul: "))
            rezultat = is_superprime(numar)
            if rezultat is True:
                print("Este superprim")
            else:
                print("Nu este superprim")
        elif valoare == 4:
            rulare = False
        else:
            print("Valoare gresita! Incercati din nou!")


def main():
    test_get_largest_prime_below()
    test_is_palindrome()
    test_is_superprime()
    meniu()


if __name__ == '__main__':
    main()
