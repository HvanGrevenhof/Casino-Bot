#Imports
from datetime import date
from games.roulette import play_roulette
from games.fruitmachine import play_fruitmachine

# Variabelen Los
ticketprijs = 25.00
gok_belasting = 10.00
vaste_kosten = ticketprijs + gok_belasting

# Def Statements
def calculate_age(birthdate):
    day, month, year = map(int, birthdate.split("-"))

    today = date.today()

    age = today.year - year

    if (today.month, today.day) < (month, day):
        age = age - 1

    return age
def check_age(birthdate):
    age = calculate_age(birthdate)

    if age < 18:
        exit("Je bent te jong om het Casino te betreden.")

    return birthdate

def determine_salutation(name, gender):
    if gender == "m":
        return f"Heer {name}"
    elif gender == "v":
        return f"Mevrouw {name}"
    else:
        return f"X {name}"

def show_welcome_message(startbudget, balance, salutation):
    print(f"""
Casino van Grevenhof
-----------------------------
Welkom, {salutation}

Startbudget: € {startbudget:.2f}
Saldo:       € {balance:.2f}
""")

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

def show_account(name, birthdate, salutation):
    age = calculate_age(birthdate)

    print(f"""
    Accountgegevens
    ----------------
    Naam: {name}
    Aanspreekvorm: {salutation}
    Geboortedatum: {birthdate}
    Leeftijd: {age}
    """)

def show_games_menu():
    print("""
    Casino van Grevenhof-Spellen!
    ---------------------
    1.Fruitmachine
    2.Roulette
    0.Terug
    """)
    game_choice = input("Kies een Spel:  ")

    return game_choice


def main():
    print("Welkom Bij Casino van Grevenhof!")

    name = input("Wat is uw naam ?  ")
    birthdate = check_age(input("Wat is je Geboortedatum ? (dd-mm-yyyy)  "))
    gender = input("Wat is uw geslacht ? M/V/anders").lower()

    startbudget = float(input("Met Hoeveel geld wilt u beginnen ? € "))
    if startbudget < vaste_kosten:
        exit("Je hebt niet genoeg geld om de vaste kosten te betalen.")
    balance = startbudget - vaste_kosten

    salutations = determine_salutation(name, gender)

    show_welcome_message(startbudget, balance, salutations)

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
                    balance = play_fruitmachine(balance)

                elif game_choice == "2":
                    balance = play_roulette(balance)
                else:
                    print("Ongeldige keuze.")

        elif choice == "2":
            show_balance(balance)
        elif choice == "3":
            show_account(name, birthdate, salutations)
        else:
            print("Ongeldige Keuze.")

main()

