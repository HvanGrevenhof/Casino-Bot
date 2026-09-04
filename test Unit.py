geld = 100
round_number = 1

while geld > 0:

    print("1. Rood")
    print("2. Zwart")
    print("3. Even")
    print("4. Oneven")
    print("0. Stop")

    keuze = input("Maak een keuze: ")

    if keuze == "0":
        break

    inzet = float(input("Hoeveel wil je inzetten? €"))

    if inzet <= 0:
        print("Ongeldige inzet.")
        continue

    if inzet > geld:
        print("Je hebt niet genoeg geld.")
        continue

    geld = geld - inzet

    spin = (round_number * 7 ) % 37
    print("De roulette landt op:", spin)

    rode_nummers = [
        1, 3, 5, 7, 9, 12, 14, 16, 18,
        19, 21, 23, 25, 27, 30, 32, 34, 36
    ]

    if spin == 0:
        print("De Spin is Groen!")
    elif spin in rode_nummers:
        print("De Spin is Rood!")
    else:
        print("De Spin is Zwart!")

    if keuze == "1" and spin in rode_nummers:
        print(f"Je hebt Gewonnen !je saldo is {geld}")
        geld = geld + (inzet * 2)
    elif keuze == "2" and spin not in rode_nummers and spin != 0:
        print(f"Je hebt Gewonnen ! je saldo is {geld}")
        geld = geld + (inzet * 2)
    elif keuze == "3" and spin !=0 and spin % 2 == 0:
        print(f"Je hebt Gewonnen ! je saldo is {geld}")
        geld = geld + (inzet * 2)
    elif keuze == "4" and spin != 0 and spin % 2 != 0:
        print(f"Je hebt Gewonnen ! je saldo is {geld}")
        geld = geld + (inzet * 2)
    else:
        print(f"Je hebt Verloren! je saldo is {geld}")

    round_number = round_number + 1

print("Je eindsaldo is:", geld)
