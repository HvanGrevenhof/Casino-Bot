from datetime import date, datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

players = {
    "Jan": {
        "naam": "Jan",
        "geboortedatum": "15-06-1995",
        "gender": "m",
        "saldo": 100.00,
        "gespeelde_spellen": {}
    },
    "Lisa": {
        "naam": "Lisa",
        "geboortedatum": "22-03-1998",
        "gender": "v",
        "saldo": 150.00,
        "gespeelde_spellen": {}
    },
    "Piet": {
        "naam": "Piet",
        "geboortedatum": "22-03-1998",
        "gender": "m",
        "saldo": 150.00,
        "gespeelde_spellen": {}
    },
}

current_player = None
MIN_AGE = 18

def calculate_age(birthdate):
    birthdate_value = datetime.strptime(birthdate, "%d-%m-%Y").date()

    today_value = date.today()

    if birthdate_value > today_value:
        raise ValueError("De geboortedatum mag niet in de toekomst liggen.")

    age = today_value.year - birthdate_value.year

    if (today_value.month, today_value.day) < (birthdate_value.month, birthdate_value.day):
        age = age - 1

    return age

def check_age(birthdate):
    age = calculate_age(birthdate)

    if age < MIN_AGE:
        exit("Je bent te jong om het Casino te betreden.")

    return birthdate

def determine_salutation(name, gender):
    if gender == "m":
        return f"Heer {name}"
    elif gender == "v":
        return f"Mevrouw {name}"
    else:
        return f"X {name}"

def create_account(total_cost, name=None):
    global players
    global current_player

    if name is None:
        name = input("Naam voor het nieuwe account:  ").capitalize()

        if name in players:
            console.print("dit account bestaat al, Gebruik wissel account om het te openen.")
            return

    birthdate = input("Wat is uw geboortedatum ? (dd-mm-yyyy) ")
    check_age(birthdate)

    gender = input("Wat is uw geslacht ? M / V / Anders").lower()

    start_balance = float(input("Met hoeveel geld wilt u beginnen ? € "))

    if start_balance < total_cost:
        console.print("Je hebt niet genoeg geld om de kosten te betallen")
        return

    balance = start_balance - total_cost

    profile = {
        "naam": name,
        "geboortedatum": birthdate,
        "gender": gender,
        "saldo": balance,
        "gespeelde_spellen": {}

    }

    players[name] = profile
    current_player = name

def initialize_player(total_cost):
    global players
    global current_player

    name = input("Wat is je naam ?  ").capitalize()
    current_player = name

    if name in players:
        profile = players[current_player]
        salutation = determine_salutation(current_player, profile["gender"])
        balance = profile["saldo"]

        message = f"""welkom terug, {salutation}

huidig saldo: €{balance:.2f}"""

        console.print(
            Panel(
                message,
                title="Casino van Grevenhof"
            )
        )
    else:
        create_account(total_cost, name)

        if name not in players:
            return

        profile = players[current_player]
        balance = profile["saldo"]
        start_balance = balance + total_cost
        salutation = determine_salutation(current_player, profile["gender"])
        message = f"""Welkom, {salutation}
Startbudget: €{start_balance:.2f}
Vaste kosten: €{total_cost:.2f}
Saldo: {balance:.2f}"""
        console.print(
            Panel(
                message,
                title="Casino van Grevenhof"
            )
        )
def get_current_balance():
    return players[current_player]["saldo"]

def get_played_games():
    return players[current_player]["gespeelde_spellen"]

def update_current_balance(balance):
    players[current_player]["saldo"] = balance

def register_played_game(game_name):
    played_games = get_played_games()

    if game_name in played_games:
        played_games[game_name] += 1
    else:
        played_games[game_name] = 1

def show_account():
    profile = players[current_player]

    message = f"""Naam: {profile['naam']}
Saldo: € {profile["saldo"]:.2f}
Gespeelde spellen: {profile["gespeelde_spellen"]}
Beschikbare spelers: {list(players.keys())}"""

    console.print(
        Panel(
            message,
            title="Casino van Grevenhof - Account"
        )
    )



def show_all_players():
    table = Table(expand=True)

    table.add_column("Naam")
    table.add_column("Saldo")

    for name, profile in players.items():
        table.add_row(name, f"€ {profile['saldo']:.2f}")

    console.print(
        Panel.fit(
            table,
            title="Casino van Grevenhof - Alle accounts"
        )
    )

def switch_account():
    global current_player

    name = input("Naar welk account wilt u wisselen ?  ").capitalize()

    if name not in players:
        console.print("Dit account bestaat niet")
        return
    current_player = name
    console.print(f"Gewisseld naar account: {current_player}")

def remove_account():
    global current_player

    name = input("Welk account wilt u verwijderen ?  ").capitalize()

    if name not in players:
        print("Dit account bestaat niet")
        return

    if len(players) == 1:
        console.print("Het Laatste Account kan niet verwijderd worden")
        return

    del players[name]

    if name == current_player:
        current_player = list(players.keys())[0]

    console.print(f"Account {name} is verwijderd.")






