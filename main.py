import string


def read_file(file_path):
    continut = open("exemplu.txt", "r").read()
    return continut

def proceseaza_continut(continut, alegere):
    tab = str.maketrans(".", " ") #un fel de strtok, cu despartirea "."
    continut = continut.translate(tab)#aici face strtok si am un fel de vector cu toate cuvintele

    if alegere == 1:  # fac toate literele mici
        continut = continut.lower()
    if alegere == 3:  # scap de spatiile in plus
        continut = ' '.join(continut.split())
    if alegere == 2:  # fac toate literele mari
        continut = continut.upper()
    if alegere > 3:
        y = int(input("Numarul magic este:"))
        if alegere == 4:  # sortez cuvintele care au y litere
            aux = continut.split()  # In aux am toate cuvintele din continut
            for b in aux:
                if len(b) == y:
                    print(b)

        if alegere == 5:
            numere = []
            for b in continut:
                if b.isdigit():
                    numere.append(int(b))
            for b in numere:
                if b > y:
                    print(b)
    return continut


def main():
    fisier = 'exemplu.txt'
    continut = read_file(fisier)
    x = int(input("Introduce regula speciala:"))
    continut_nou = proceseaza_continut(continut, x)
    if x <= 3:
        print("Continutul nou este:", continut_nou)
if __name__ == "__main__":
    main()