def prim(numar):
    """
    Verifica daca un numar este prim
    :param numar: o valoare intreaga "numar"
    :return: True, daca "numar" este prim, False in caz contrar
    """
    if numar < 2:
        return False
    else:
        for i in range (2, numar // 2):
            if numar % i == 0:
                return False
        return True

def is_palindrome(n):
    """
    Verifica daca un numar n este palindrom
    :param n: un numar intreg n
    :return: True, daca n este palindrom, respectiv False in caz contrar
    """
    oglindit = 0
    copie = n
    while copie != 0:
        oglindit = oglindit * 10 + copie % 10
        copie = copie // 10
    if oglindit == n:
        return True
    return False

def test_is_palindrome(n):
    """
    Verifica daca un numar n este palindrom
    :param n: un numar intreg n
    :return: True, daca n este palindrom, respectiv False in caz contrar
    """
    oglindit = 0
    copie = n
    while copie != 0:
        oglindit = oglindit * 10 + copie % 10
        copie = copie // 10
    if oglindit == n:
        return True
    return False

def is_superprime(n):
    """
    Verifica daca un numar este superprim
    :param n: o valoare intreaga n
    :return: True, daca n este superprim, iar False in caz contrar
    """
    putere = 1
    copie = 0
    verificare = 1
    while putere * putere <= n:
        putere = putere * 10
    while putere != 0:
        cifra = n / putere
        copie = (int)(copie * 10 + cifra)
        ok = prim (copie)
        if ok == False:
            verificare = 0
        n = n % putere
        putere = putere // 10
    if verificare == 1:
        return True
    return False

def get_largest_prime_below(n):
    """
    Calculeaza ultimul numar prim de inaintea lui n
    :param n: un numar intreg n
    :return: o valoare intreaga
    """
    for i in range (n, 1, -1):
        verificare = prim(i)
        if verificare == True:
            return i

def test_get_largest_prime_below(n):
    """
    Calculeaza ultimul numar prim de inaintea lui n
    :param n: un numar intreg n
    :return: o valoare intreaga
    """
    for i in range (n, 1, -1):
        verificare = prim(i)
        if verificare == True:
            return i

def test_is_superprime(n):
    """
    Verifica daca un numar este superprim
    :param n: o valoare intreaga n
    :return: True, daca n este superprim, iar False in caz contrar
    """
    putere = 1
    copie = 0
    verificare = 1
    while putere * putere <= n:
        putere = putere * 10
    while putere != 0:
        cifra = n / putere
        copie = (int)(copie * 10 + cifra)
        ok = prim (copie)
        if ok == False:
            verificare = 0
        n = n % putere
        putere = putere // 10
    if verificare == 1:
        return True
    return False

assert test_is_superprime(237)
assert test_is_superprime(1024)
assert test_is_superprime(1000)
assert test_is_palindrome(1221)
assert test_is_palindrome(9)
assert test_is_palindrome(123)
assert test_get_largest_prime_below(7)
assert test_get_largest_prime_below(100)
assert test_get_largest_prime_below(25)

def main():
    print("1. Găsește ultimul număr prim mai mic decât un număr dat.")
    print("2. Determină dacă un număr dat este palindrom.")
    print("3. Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime.")
    print("4. Iesire")
    merge = 1
    while merge == 1:
        n = int(input("Dati o valoare de la 1 la 4: "))
        if n == 1:
            numar1 = int(input("1. Dati o valoare"))
            rezultat1 = get_largest_prime_below(numar1)
            print("Rezultatul este: ", rezultat1)
        elif n == 2:
            numar2 = int(input("Dati o valoare: "))
            rezultat2 = is_palindrome(numar2)
            if rezultat2 == True:
                print("Este palindrom")
            else:
                print("Nu este palindrom")
        elif n == 3:
            numar3 = int(input("Dati o valoare: "))
            rezultat3 = is_superprime(numar3)
            if rezultat3 == True:
                print("Este superprim")
            else:
                print("Nu este superprim")
        elif n == 4:
            merge = 0
        else:
            print("Valoare gresita! Incercati din nou!")

if __name__ == '__main__':
  main()