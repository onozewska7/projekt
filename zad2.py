import random

def write_random_numbers_to_file(file_path, n):
    with open(file_path, 'w') as file:
        for _ in range(n):
            random_number = random.randint(1, 100)
            file.write(str(random_number) + '\n')

if __name__ == "__main__":
    file_path = "zad2plik.txt"
    n = int(input("Podaj liczbę losowych liczb do zapisania: "))

    write_random_numbers_to_file(file_path, n)
    print(f"{n} losowych liczb zostało zapisanych do pliku o nazwie {file_path}.")