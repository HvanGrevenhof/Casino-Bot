import random
from rich.console import Console
from rich.panel import Panel

console = Console()

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def create_deck():
    deck = [suit + rank for suit in SUITS for rank in RANKS]

    random.shuffle(deck)

    return deck

def draw_card(deck, hand):
    card = deck.pop()
    hand.append(card)

    return card

def show_hand(label, hand, hide_card=False):
    if hide_card:
        visible_cards = hand[:1] + ["??"]
    else:
        visible_cards = hand

    console.print(
        Panel(
            " | ".join(visible_cards),
            title=label
        )
    )


def calculate_card_value(card):
    rank = card[1:]

    if rank in ["J", "Q", "K"]:
        return 10
    elif rank == "A":
        return 11
    else:
        return int(rank)

def calculate_hand_value(hand):
    total = 0
    number_of_aces = 0

    for card in hand:
        total = total + calculate_card_value(card)

        if card[1:] == "A":
            number_of_aces = number_of_aces + 1

    while total > 21 and number_of_aces > 0:
        total = total -10
        number_of_aces = number_of_aces - 1

    return total

def ask_for_bet(balance):
    while True:
        bet = float(input("Hoeveel wilt u inzetten € ? "))

        if bet <= 0:
            console.print("Ongeldige inzet.")
            continue

        if bet > balance:
            console.print("U heeft niet genoeg saldo.")
            continue

        return bet


def play_blackjack(balance):
    if balance <= 0:
        console.print("Je hebt niet genoeg Saldo meer om te spelen.")
        return balance

    bet = ask_for_bet(balance)
    balance = balance - bet

    deck = create_deck()

    player_hand = []
    dealer_hand = []

    draw_card(deck, player_hand)
    draw_card(deck, player_hand)

    draw_card(deck, dealer_hand)
    draw_card(deck, dealer_hand)

    show_hand("Jouw hand", player_hand)
    show_hand("Dealer hand", dealer_hand, True)

    console.print("Jouw Totaal: ", calculate_hand_value(player_hand))


    while calculate_hand_value(player_hand) <21:
        choice = input("Kies je Hit of Stand ?: ").lower()

        if choice == "stand":
            break

        if choice != "hit":
            console.print("Kies alleen 'Hit' of 'Stand',")
            continue

        card = draw_card(deck, player_hand)

        console.print(f"Je trekt: {card}")

        show_hand("Jouw hand", player_hand)

        console.print("Jouw Totaal: ", calculate_hand_value(player_hand))

        if calculate_hand_value(player_hand) > 21:
            message = "Je bent Bust! de dealer wint."
            console.print(
                Panel(
                    f"{message}\nNieuw Saldo: {balance:.2f}",
                    title="Blackjack resultaat"
                )
            )
            return balance

    show_hand("Dealer hand", dealer_hand)

    while calculate_hand_value(dealer_hand) < 17:
        card =  draw_card(deck, dealer_hand)

        console.print(f"Dealer trekt: {card}")
        show_hand("Dealer hand", dealer_hand)

    player_total = calculate_hand_value(player_hand)
    dealer_total = calculate_hand_value(dealer_hand)

    console.print("Jouw Totaal: ", player_total)
    console.print("Dealer Totaal: ", dealer_total)

    if dealer_total > 21:
        balance = balance + (bet * 2)
        message = "Dealer is Bust, je hebt Gewonnen!"

    elif player_total > dealer_total:
        balance = balance + (bet * 1.5)
        message = "Je hebt de hogere hand!, Je hebt Gewonnen!"

    elif player_total == dealer_total:
        balance = balance + bet
        message = "Gelijkspel!, je krijgt je inzet terug."
    else:
        message = "De Dealer wint."

    console.print(
        Panel(
            f"{message}\nNieuw saldo : {balance:.2f}",
            title="Blackjack Resultaat"
        )
    )

    return balance














