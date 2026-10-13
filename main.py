#Imports
from games.roulette import play_roulette
from games.fruitmachine import play_fruitmachine
from games.blackjack import play_blackjack
import profiles
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Variabelen Los
ticketprijs = 25.00
gok_belasting = 10.00
vaste_kosten = ticketprijs + gok_belasting

# Def Statements

def show_main_menu():
    table = Table(expand=True)

    table.add_column("Optie")
    table.add_column("Actie")

    table.add_row("1", "Spellen")
    table.add_row("2", "Saldo")
    table.add_row("3", "Account")
    table.add_row("0", "Stop")

    console.print(
        Panel.fit(
            table,
            title="Casino van Grevenhof - Hoofdmenu"
        )
    )

    choice = input("Kies een Optie: ")

    return choice

def show_balance(balance):
    console.print(
        Panel(
            f"Huidig saldo: € {balance:.2f}",
            title="Casino van Grevenhof - Saldo"
        )
    )

def show_games_menu():
    table = Table(expand=True)

    table.add_column("Optie")
    table.add_column("Spel")

    table.add_row("1", "Fruitmachine")
    table.add_row("2", "Roulette")
    table.add_row("3", "Blackjack")
    table.add_row("0", "Terug")

    console.print(
        Panel.fit(
            table,
            title="Casino van Grevenhof - Spellen"
        )
    )


    game_choice = input("Kies een Spel:  ")

    return game_choice

def show_account_menu():
    table = Table(expand=True)

    table.add_column("Optie")
    table.add_column("Actie")

    table.add_row("1", "Toon alle accounts")
    table.add_row("2", "Nieuw Account")
    table.add_row("3", "Wissel Account")
    table.add_row("4", "Verwijder Account")
    table.add_row("0", "Terug")

    console.print(
        Panel.fit(
            table,
            title="Casino van Grevenhof - Account"
        )
    )

    account_choice = input("Kies een Optie:  ")

    return account_choice


def main():
    console.print("Welkom Bij Casino van Grevenhof!")

    profiles.initialize_player(vaste_kosten)

    while True :
        choice = show_main_menu()

        if choice == "0":
            break
        elif choice == "1":
            while True:
                game_choice = show_games_menu()

                if game_choice == "0":
                    break
                elif game_choice == "1":
                    balance = profiles.get_current_balance()
                    balance = play_fruitmachine(balance)
                    profiles.update_current_balance(balance)
                    profiles.register_played_game("fruitmachine")

                elif game_choice == "2":
                    balance = profiles.get_current_balance()
                    balance = play_roulette(balance)
                    profiles.update_current_balance(balance)
                    profiles.register_played_game("roulette")

                elif game_choice == "3":
                    balance = profiles.get_current_balance()
                    balance = play_blackjack(balance)
                    profiles.update_current_balance(balance)
                    profiles.register_played_game("blackjack")
                else:
                    console.print("Ongeldige keuze.")

        elif choice == "2":
            show_balance(profiles.get_current_balance())
        elif choice == "3":
            while True:
                profiles.show_account()
                account_choice = show_account_menu()

                if account_choice == "0":
                    break
                elif account_choice == "1":
                    profiles.show_all_players()
                elif account_choice == "2":
                    profiles.create_account(vaste_kosten)
                elif account_choice == "3":
                    profiles.switch_account()
                elif account_choice == "4":
                    profiles.remove_account()
                else:
                    console.print("Ongeldige keuze.")

        else:
            console.print("Ongeldige Keuze.")

main()

