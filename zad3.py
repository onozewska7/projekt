def czytajplik(file_path):
    numery2 = []
    with open(file_path, 'r') as file:
        for line in file:
            numery = int(line.strip())
            numery2.append(numery)
    return numery2

def licz_srednia(numery2):
    return sum(numery2) / len(numery2)

def licz_odchylenie(numery2, srednia):
    wariancja = sum((x - srednia) ** 2 for x in numery2) / len(numery2)
    odchylenie = wariancja ** 0.5
    return odchylenie

def calculate_max_min(numery2):
    return max(numery2), min(numery2)

def display_statistics(numery2):
    srednia = licz_srednia(numery2)
    odchylenie = licz_odchylenie(numery2, srednia)
    maksimum, minimum = calculate_max_min(numery2)

    print(f"Średnia: {srednia}")
    print(f"Odchylenie standardowe: {odchylenie}")
    print(f"Maksymalna wartość: {maksimum}")
    print(f"Minimalna wartość: {minimum}")

def pokaz_posortowane_numery(numery2):
    posortowanenumery2 = sorted(numery2, reverse=True)
    print("Posortowane malejąco:")
    for number in posortowanenumery2:
        print(number)

if __name__ == "__main__":
    file_path = "zad2plik.txt"

    numery2 = czytajplik(file_path)

    display_statistics(numery2)

    pokaz_posortowane_numery(numery2)