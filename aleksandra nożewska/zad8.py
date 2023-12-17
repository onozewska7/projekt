import os
import random
import datetime

def losowo_generuj():
    return bytes([random.randint(0, 255) for _ in range(100)])

def zapisz_binarnie(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)

def tworz_i_zapisz():
    for i in range(10):
        timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")[:-3]
        nazwa_pliku = f"{timestamp}.bin"
        file_path = os.path.join(os.getcwd(), nazwa_pliku)
        data = losowo_generuj()
        zapisz_binarnie(file_path, data)
        print(f"Plik {nazwa_pliku} został utworzony z losowymi danymi.")

if __name__ == "__main__":
    tworz_i_zapisz()
