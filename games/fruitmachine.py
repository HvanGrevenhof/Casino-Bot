def ask_for_bet(balance):
    while True:
        stake = float(input("Hoeveel wilt u inzetten? €  "))

        if stake <= 0:
            print("Ongeldige inzet.")
            continue

        if stake > balance:
            print("Je hebt niet genoeg Saldo.")
            continue

        return stake

def determine_rolls(round_number):
    roll = round_number % 5
    if roll == 0:
        return "kers", "citroen", "ster"
    elif roll == 1:
        return "kers", "kers", "kers"
    elif roll == 2:
        return "ster", "ster", "citroen"
    elif roll == 3:
        return "citroen", "kers", "ster"
    else:
        return "ster", "ster", "ster"

def determine_payout(rol1, rol2, rol3, stake):
    if rol1 == rol2 == rol3:
        return stake * 3

    elif rol1 == rol2 or rol1 == rol3 or rol2 == rol3:
        return stake

    else:
        return 0



def play_fruitmachine(balance):
    round_number = 1

    while True:
        if balance <= 0:
            print("Je hebt geen Saldo meer om te spelen.")
            return balance

        print(f"""
Casino van Grevenhof - Fruitmachine
-----------------------------------
Huidig saldo: € {balance:.2f}
""")

        choice = input("Druk op enter om te spelen of typ stop om terug te gaan: ")

        if choice.lower() == "stop":
            return balance

        stake = ask_for_bet(balance)

        balance = balance - stake

        rol1, rol2, rol3 = determine_rolls(round_number)

        print(f"Rollen: {rol1} | {rol2} | {rol3}")

        payout = determine_payout(rol1, rol2, rol3, stake)

        if payout > 0:
            balance = balance + payout
            print(f"Je hebt gewonnen! Uitbetaling: € {payout:.2f}")
        else:
            print("Geen prijs. Je hebt verloren.")

        print(f"Nieuw saldo: € {balance:.2f}")

        round_number = round_number + 1



