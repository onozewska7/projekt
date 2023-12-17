import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
def wczytaj_dane_z_pliku(nazwa_pliku):
    time_from_start = []
    pos_x = []
    pos_y = []
    pos_z = []
    vel_x = []
    vel_y = []
    vel_z = []
    with open(nazwa_pliku, 'r') as plik:
        plik.readline()

        for linia in plik:
            dane = linia.strip().split(',')
            if len(dane) >= 7:
                time_from_start.append(float(dane[0]))
                pos_x.append(float(dane[1]))
                pos_y.append(float(dane[2]))
                pos_z.append(float(dane[3]))
                vel_x.append(float(dane[4]))
                vel_y.append(float(dane[5]))
                vel_z.append(float(dane[6]))
    return time_from_start, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z

nazwa_pliku = 'zad9plik.txt'

time_from_start, pos_x, pos_y, pos_z, vel_x, vel_y, vel_z = wczytaj_dane_z_pliku(nazwa_pliku)

srednia_pos_x = np.mean(pos_x)
srednia_pos_y = np.mean(pos_y)
srednia_pos_z = np.mean(pos_z)

print(f"Średnia pozycja w osi X: {srednia_pos_x}")
print(f"Średnia pozycja w osi Y: {srednia_pos_y}")
print(f"Średnia pozycja w osi Z: {srednia_pos_z}")

szybkosc = np.sqrt(np.square(vel_x) + np.square(vel_y) + np.square(vel_z))

with open('velocity.csv', 'w') as plik_wyjsciowy:
    for v in szybkosc:
        plik_wyjsciowy.write(f"{v}\n")

print("Dane zapisano do pliku velocity.csv.")

gs = GridSpec(3, 1, height_ratios=[2, 1, 1])

plt.subplot(gs[0])
plt.plot(time_from_start, pos_x, '-', linewidth=1)
plt.xlabel('Time from Start')
plt.ylabel('Pos X')

plt.subplot(gs[1])
plt.plot(time_from_start, pos_y, '-', color='green', linewidth=0.8)
plt.xlabel('Time from Start')
plt.ylabel('Pos Y')

plt.subplot(gs[2])
plt.plot(time_from_start, pos_z, '-', color='red', linewidth=0.8)
plt.xlabel('Time from Start')
plt.ylabel('Pos Z')

plt.tight_layout()
plt.show()
