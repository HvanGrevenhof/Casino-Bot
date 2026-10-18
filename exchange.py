import os
import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel


console = Console()
load_dotenv()
API_KEY = os.getenv("API_KEY")
EXCHANGE_RATE_URL = "https://v6.exchangerate-api.com/v6/{}/latest/{}"

def get_exchange_request():
    while True:
        currency = input("Welke Valuta wilt u wisselen ? (bijv. USD): ").strip().upper()

        if currency == "STOP":
            return None, None

        if len(currency) != 3 or not currency.isalpha():
            console.print("Ongeldige valutacode. gebruik 3 letters. ")
        else:
            break
    while True:
        try:
            foreign_currency_amount = float(input("Welk bedrag wilt u wisselen ? €"))

            if foreign_currency_amount <= 0:
                console.print("Voer een bedrag hoger dan 0 in.")
                continue

            break
        except ValueError:
            console.print("Ongeldig bedrag, vul een getal in.")

    return foreign_currency_amount, currency

def get_exchange_rate_for_currency(currency):
    if not API_KEY:
        console.print("Fout: er is geen API_sleutel gevonden.")
        return None
    url = EXCHANGE_RATE_URL.format(API_KEY, currency)
    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException:
        console.print("Fout: de wisselkoers-API is niet bereikbaar.")
        return None

    if response.status_code != 200:
        console.print("Fout: de API heeft geen succesvol antwoord gegeven.")
        return None

    data = response.json()
    exchange_rate = data.get("conversion_rates", {}).get("EUR")
    if exchange_rate is None:
        console.print("Fout: geen wisselkoers gevonden voor deze valuta.")
        return None
    return exchange_rate

def convert_to_euro(foreign_currency_amount, exchange_rate):
    euro_amount = foreign_currency_amount * exchange_rate
    return euro_amount

def print_exchange_result(foreign_currency_amount, currency, exchange_rate, euro_amount):
    console.print(
        Panel(
            f"{foreign_currency_amount:.2f} {currency} = €{euro_amount:.2f}",
            title="Wisselresultaat",
            border_style="green"
        )
    )

def run_exchange():
    foreign_currency_amount, currency = get_exchange_request()

    if currency is None:
        return None

    exchange_rate = get_exchange_rate_for_currency(currency)
    if exchange_rate is None:
        return None

    euro_amount = convert_to_euro(foreign_currency_amount, exchange_rate)
    print_exchange_result(foreign_currency_amount, currency, exchange_rate, euro_amount)
    return euro_amount




