

def czy_jest_pierwsza(liczba):
    for i in range(2,liczba):
        if liczba % i == 0:
            return False
    return True


def test_czy_jest_pierwsza():

    assert czy_jest_pierwsza(6)==False
    assert czy_jest_pierwsza(10)==False
    assert czy_jest_pierwsza(17)==True
    assert czy_jest_pierwsza(11)==True