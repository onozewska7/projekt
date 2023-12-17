def generuj_slownik(n):
    slownik = {x: x**2 for x in range(1, n + 1)}
    return slownik

if __name__ == "__main__":
    wynikx=0
    n = int(input("Podaj wartość n: "))
    wynik = generuj_slownik(n)
    print("Wygenerowany słownik:")

    for klucz, wartosc in wynik.items():
        print(f"{klucz}: {wartosc}")
        wynikx+=wartosc

    print("Suma słownika: ", wynikx)