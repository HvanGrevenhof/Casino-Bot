from random import choice
from rich.console import Console
from rich.panel import Panel

console = Console()

SYMBOLS = ["kers", "citroen", "ster", "bel", "diamant"]

def ask_for_bet(balance):
    while True:
        stake = float(input("Hoeveel wilt u inzetten? €  "))

        if stake <= 0:
            console.print("Ongeldige inzet.")
            continue

        if stake > balance:
            console.print("Je hebt niet genoeg Saldo.")
            continue

        return stake

def determine_rolls():
    rol1 = choice(SYMBOLS)
    rol2 = choice(SYMBOLS)
    rol3 = choice(SYMBOLS)

    return rol1, rol2, rol3

def determine_payout(rol1, rol2, rol3, stake):
    if rol1 == rol2 == rol3:
        return stake * 3

    elif rol1 == rol2 or rol1 == rol3 or rol2 == rol3:
        return stake

    else:
        return 0



def play_fruitmachine(balance):

    while True:
        if balance <= 0:
            console.print("Je hebt geen Saldo meer om te spelen.")
            return balance

        message = f"Huidig saldo:€ {balance:.2f}"

        console.print(
            Panel(
                message,
                title="Casino van Grevenhof - Fruitmachine"
            )

        )

        player_choice = input("Druk op enter om te spelen of typ stop om terug te gaan: ")

        if player_choice.lower() == "stop":
            return balance

        stake = ask_for_bet(balance)

        balance = balance - stake

        rol1, rol2, rol3 = determine_rolls()



        payout = determine_payout(rol1, rol2, rol3, stake)

        if payout > 0:
            balance = balance + payout
            message = f""" Rollen: {rol1} | {rol2} | {rol3}

je hebt Gewonnen!
Uitbetaling: € {payout:.2f}
Nieuw Saldo : € {balance:.2f}"""
        else:
            message = f"""Rollen: {rol1} | {rol2} | {rol3}
Geen prijs. je hebt verloren.
Nieuw Saldo: € {balance:.2f}"""

        console.print(
            Panel(
                message,
                title="Casino van Grevenhof - Fruitmachine Resultaat"
            )
        )





