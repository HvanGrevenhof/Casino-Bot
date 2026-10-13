from random import randint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


console = Console()

def show_roulette_options():
    table = Table(expand=True)

    table.add_column("Optie")
    table.add_column("Keuze")

    table.add_row("1", "Rood")
    table.add_row("2", "Zwart")
    table.add_row("3", "Even")
    table.add_row("4", "Oneven")
    table.add_row("0", "Stop")

    console.print(
        Panel.fit(
            table,
            title="Casino van Grevenhof -  Roulette"
        )
    )


def ask_for_bet(balance):
    while True:
        stake = float(input("Hoeveel wil je inzetten ? €  "))

        if stake <= 0:
            console.print("Ongeldige inzet.")
            continue

        if stake > balance:
            console.print("Je hebt niet genoeg saldo.")
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
    while True:
        show_roulette_options()

        choice = input("Maak een keuze:  ")

        if choice == "0":
            return balance

        if choice not in ["1", "2", "3", "4"]:
            console.print("Ongeldige Keuze.")
            continue

        stake = ask_for_bet(balance)

        balance = balance - stake

        spin = randint(0, 36)

        color = determine_color(spin)

        odd_even = determine_odd_even(spin)

        win = determine_win(choice, color, odd_even)
        if win:
            balance = balance + (stake * 2)
            message = f"""De roulette landt op: {spin}
De kleur is :{color}
Je hebt gewonnen ! 

Nieuw Saldo : € {balance:.2f}"""
        else:
            message = f"""De roulette landt op: {spin}
De kleur is: {color}
Je hebt Verloren !

Nieuw Saldo: €{balance:.2f}"""

        console.print(
            Panel(
                message,
                title="Casino van Grevenhof - Roulette Resultaat"
            )
        )



