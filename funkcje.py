# def nazwa_funkcji(parametry):
#     #ciało
#     # kod
#     # implementacja
#     return wartosc_zwracana

# funkcja która coś wylicza
def dodawanie(x: float, y: float) -> float:
    """
    Adds two floating-point numbers and returns the result.

    This function takes two floating-point numbers as input and calculates
    their sum.

    Args:
        x: The first float value to be added.
        y: The second float value to be added.

    Returns:
        The sum of the two input float values.

    """
    return x + y


# w = dodawanie(2, 3)
# print(w)


# funkcja, która coś robi
def wypisz_n_razy(n: int, napis: str) -> None:
    """
    Prints the given string a specified number of times. The function takes
    an integer specifying the number of times the string should be printed
    and the string itself. It outputs the string on separate lines for each
    iteration.

    Args:
        n: The number of times the string should be printed.
        napis: The string to be printed.
    """
    for i in range(n):
        print(napis)


# wypisz_n_razy(3, 'mama')

def f1():
    print('nic nie zwracam')


# x = f1()
# print(x)

# globalna zmienna
x = 99


def f2():
    # lokalna zmienna
    x = 88


f2()


# print(x)

# nie ma przeciążania - overloading
def f3(x, y):
    print(x, y)


# druga definicja nadpisuje pierwszą
def f3(x):
    print(x)


# f3(1, 2)

# definiowanie parametrów wejściowych
def f4(x, y):
    print(f'{x=} {y=}')


# f4(1,2,3)

def f5(x, y, dlugosc=12, szerokosc=22):
    print(f'{x=} {y=}')
    print(f'{dlugosc=} {szerokosc=}')


# f5(1, 2, 33)
# # tak czytelniej
# f5(1, 2, dlugosc=33)
# f5(1, 2, 33, 44)
# f5(1, 2, szerokosc=44)

# funkcja ze zmienną ilością parametrów
def f6(x, y, *args):
    print(f'{x=} {y=}')
    print(f'{args=}')


# f6(1, 2, 3, 4, 5, 6, 7)
# f6(1, 2, 3, 4, 5, 6, 7, 8, 9)

def f7(x, y, *args, dlugosc=11, szerokosc=22):
    print(f'{x=} {y=}')
    print(f'{args=}')
    print(f'{dlugosc=} {szerokosc=}')


# f7(1, 2, 3, 4, 54, 4, 4, 4, 4, dlugosc=222)

def f8(x, y, *args, dlugosc=11, szerokosc=22, **kwargs):
    print(f'{x=} {y=}')
    print(f'{args=}')
    print(f'{dlugosc=} {szerokosc=}')
    print(f'{kwargs=}')


# f8(1, 2, 3, 4, 54, 4, 4, 4, 4, dlugosc=222, aaa=333, bbb=555, ccc=666)

# funkcja przyjmująca dowolne parametry wejściowe
def f9(*args, **kwargs):
    print(f'{args=}')
    print(f'{kwargs=}')


# f9(1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, aa=222, tt=888, rr=666)

# przykładowo - print n razy
def print_n(*args, ile=1, **kwargs):
    for _ in range(ile):
        print(*args, **kwargs)


print_n(1, 2, 23, 2, 2, 2, ile=12, sep=' - ')
