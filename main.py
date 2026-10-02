#Imports
from games.roulette import play_roulette
from games.fruitmachine import play_fruitmachine
from games.blackjack import play_blackjack
import profiles

# Variabelen Los
ticketprijs = 25.00
gok_belasting = 10.00
vaste_kosten = ticketprijs + gok_belasting

# Def Statements

def show_main_menu():
    print("""
    Casino van Grevenhof - Hoofdmenu
    
    ---------------------------------
    1. Spellen
    2. Saldo
    3. Account
    0. Stop
    """)

    choice = input("Kies een Optie: ")

    return choice

def show_balance(balance):
    print(f"Huidig Saldo: € {balance:.2f}")

def show_games_menu():
    print("""
    Casino van Grevenhof-Spellen!
    ---------------------
    1.Fruitmachine
    2.Roulette
    3.Blackjack
    0.Terug
    """)
    game_choice = input("Kies een Spel:  ")

    return game_choice

def show_account_menu():
    print("""
    Casino van Grevenhof - Account
    -------------------------------
    1. Toon alle accounts
    2. Nieuw Account
    3. Wissel account
    4. Verwijder account
    0. Terug
    """)

    account_choice = input("Kies een optie:  ")

    return account_choice


def main():
    print("Welkom Bij Casino van Grevenhof!")

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
                    print("Ongeldige keuze.")

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
                    print("Ongeldige keuze.")

        else:
            print("Ongeldige Keuze.")

main()

