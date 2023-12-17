from matplotlib import pyplot as plt
def fibonaczi(i):
    wynik=[0,1]
    for i in range(2,i):
        wynik.append(wynik[-1]+wynik[-2])
    print(wynik)
    return(wynik)

def plot_fibonacci(a):
    wynik2 = fibonaczi(a)

    plt.plot(range(1, a + 1), wynik2, marker='o')
    plt.title('Ciąg Fibonacciego')
    plt.xlabel('Indeks')
    plt.ylabel('Wartość')
    plt.show()

if __name__ == "__main__":
    n = int(input("Podaj liczbę elementów ciągu Fibonacciego do wygenerowania: "))
    plot_fibonacci(n)