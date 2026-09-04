#Variabelen
ticketprijs = 25.00
gokbelasting = 10.00
standaard_donatie = 5.00
onkosten_gokken = gokbelasting + ticketprijs

#Introductie

print("""
--------------------------------------------------------------------

Welkom bij Casino van Grevenhof!
Graag zouden wij wat informatie van u willen voordat we u toelaten!
Alvast bedankt voor uw medewerking!

-------------------------------------------------------------------
""")

#registratie sex/naam/geboortedatum
#Sex
sex = input("Wat is uw Geslacht ? M/V of anders ?  ").lower()
aanhef_per_sex = {
    "m": "Heer",
    "v": "Mevrouw",
    "anders": "X."
}
aanhef = aanhef_per_sex.get(sex, " ")

#Naam
naam = input(f"en wat is uw naam {aanhef}?  ")

#geboortedatum

from datetime import date

geboorte_datum = input("En wat is uw geboortedatum? dd/mm/yyyy: ")

birth_day, birth_month, birth_year = map(int, geboorte_datum.split("/"))

huidig_jaar = date.today().year
leeftijd = huidig_jaar - birth_year

if leeftijd < 18:
    exit("Je bent te jong")
else:
    print("Je bent oud genoeg.")

#Einde registratie / Begin Buy-in

print(f"Welkom {aanhef} {naam}!  ")
print(f"wij hebben een ticket-prijs van {ticketprijs}  ")
print(f"en moeten wij een gokbelasting van {gokbelasting} hanteren  ")
print("dit wordt van uw buy-in afgeschreven  ")
print("wij hanteren een minimale Buy-In van 50 Euro  ")

#Buy-In

buy_in = float(input("met hoeveel had u vandaag willen gokken vandaag ?"))
eindbedrag = buy_in - onkosten_gokken
if eindbedrag < 50:
    exit ("sorry je hebt niet genoeg geld")
else:
    print(f"Welkom, uw huidige Saldo is, {eindbedrag}")
    donatie_check = input(f"Had u een standaard-donatie willen plegen {aanhef}{naam}? Y/N").lower()
    print(f"een standaard-donatie is {standaard_donatie}$")
    if donatie_check == "y":
        eindbedrag = eindbedrag - standaard_donatie
        onkosten_gokken = onkosten_gokken + standaard_donatie
        print("Dank u wel voor uw donatie!")
    else:
        print("Dankuwel voor uw consideratie!")

#Eindstatement 1/ Login-Succesvol

print(f"""
    "--------------------------------------------------------"
    Casino van Grevenhof
    Startbedrag: {buy_in:.2f}
    Kosten: {onkosten_gokken:.2f}
    Eindbedrag: {eindbedrag:.2f}
    Wij Wensen u een Fijne Avond en Veel Geluk, {aanhef} {naam}
    "--------------------------------------------------------"
""")

#Deel 2 ( Roulette )

round_number = 1

while eindbedrag > 0:

    print("1. Rood")
    print("2. Zwart")
    print("3. Even")
    print("4. Oneven")
    print("0. Stop")

    keuze = input("Maak een keuze: ")

    if keuze == "0":
        break

    if keuze not in ["1", "2", "3", "4"]:
      print("Ongeldige keuze")
      continue

    inzet = float(input("Hoeveel wil je inzetten? €"))

    if inzet <= 0:
        print("Ongeldige inzet.")
        continue

    if inzet > eindbedrag:
        print("Je hebt niet genoeg geld.")
        continue

    eindbedrag = eindbedrag - inzet

    spin = (round_number * 7 ) % 37
    print("De roulette landt op:", spin)

    rode_nummers = [
        1, 3, 5, 7, 9, 12, 14, 16, 18,
        19, 21, 23, 25, 27, 30, 32, 34, 36
    ]

    if spin == 0:
        print("De Spin is Groen!")
    elif spin in rode_nummers:
        print("De Spin is Rood!")
    else:
        print("De Spin is Zwart!")

    if keuze == "1" and spin in rode_nummers:
        eindbedrag = eindbedrag + (inzet * 2)
        print(f"Je hebt Gewonnen !je saldo is {eindbedrag}")
    elif keuze == "2" and spin not in rode_nummers and spin != 0:
        eindbedrag = eindbedrag + (inzet * 2)
        print(f"Je hebt Gewonnen ! je saldo is {eindbedrag}")
    elif keuze == "3" and spin !=0 and spin % 2 == 0:
        eindbedrag = eindbedrag + (inzet * 2)
        print(f"Je hebt Gewonnen ! je saldo is {eindbedrag}")
    elif keuze == "4" and spin != 0 and spin % 2 != 0:
        eindbedrag = eindbedrag + (inzet * 2)
        print(f"Je hebt Gewonnen ! je saldo is {eindbedrag}")
    else:
        print(f"Je hebt Verloren! je saldo is {eindbedrag}")

    round_number = round_number + 1

print("Je eindsaldo is:", eindbedrag)