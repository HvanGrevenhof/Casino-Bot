#Optie scherm
def show_roulette_options():
    print("""
Casino van Grevenhof - Roulette
-------------------------------
1. Rood
2. Zwart
3. Even
4. Oneven
0. Stop
""")

#checklijsten
def ask_for_bet(balance):
    while True:
        stake = float(input("Hoeveel wil je inzetten ? €  "))

        if stake <= 0:
            print("Ongeldige inzet.")
            continue

        if stake > balance:
            print("Je hebt niet genoeg saldo.")
            continue
        return stake

def determine_color(spin):
    red_numbers = [
        1, 3, 5, 7, 9, 12, 14, 16, 18,
        19, 21, 23, 25, 27, 30, 32, 34, 36
    ]

    if spin == 0:
        return "groen"
    elif spin in red_numbers:
        return "rood"
    else:
        return "zwart"

def determine_odd_even(spin):
    if spin == 0:
        return "geen"
    elif spin % 2 == 0:
        return "even"
    else:
        return "oneven"

def determine_win(choice, color, odd_even):
    if choice == "1" and color == "rood":
        return True
    elif choice == "2" and color == "zwart":
        return True
    elif choice == "3" and odd_even == "even":
        return True
    elif choice == "4" and odd_even == "oneven":
        return True
    else:
        return False


#keuze Menu
def play_roulette(balance):
    round_number = 1
    while True:
        show_roulette_options()

        choice = input("Maak een keuze:  ")

        if choice == "0":
            return balance

        if choice not in ["1", "2", "3", "4"]:
            print("Ongeldige Keuze.")
            continue

        stake = ask_for_bet(balance)

        balance = balance - stake

        spin = (round_number * 7) % 37
        print("De roulette landt op:", spin)

        color = determine_color(spin)
        print("De kleur is: ", color)

        odd_even = determine_odd_even(spin)

        win = determine_win(choice, color, odd_even)
        if win:
            balance = balance + (stake * 2)
            print(f"Je hebt Gewonnen! Je saldo is € {balance:.2f}")
        else:
            print(f"Je hebt verloren! Je saldo is € {balance:.2f}")


        round_number = round_number + 1

