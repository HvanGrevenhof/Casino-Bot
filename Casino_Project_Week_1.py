#Registratie deel
print("Goeiendag bij Casino van Grevenhof !, Wij stellen even een paar vragen om u het best tot hulp te zijn !")
sex = input("Wat is uw Geslacht ? Man of Vrouw ?"  )
aanhef_per_sex = {
    "Man": "Heer",
    "Vrouw": "Mevrouw"
}
aanhef = aanhef_per_sex.get(sex, " ")

naam = input(f"En wat is uw naam {aanhef} ?  ")
geboorte_datum = input(f"En uw Geboortedatum {aanhef} {naam} ? DD/MMMM/YYYY")

print("Geweldig dankuwel voor uw gegevens, we gaan nu van start met uw Buy-in")

#berekeningsgedeelte
ticketprijs = 25.00
gokbelasting = 10.00
standaard_donatie = 5.00

print(f"Wees ervan bewust dat we een minimale Buy in hebben van 200euro na uw ticket van {ticketprijs} Euro en de {gokbelasting} euro gokbelasting!")
start_bedrag = float(input("Hoeveel wilt u vandaag uw pas opwaarderen ?"))
belasting_bedrag = start_bedrag - ticketprijs - gokbelasting
totale_kosten = ticketprijs + gokbelasting
if belasting_bedrag <= 200.00:
        print("helaas heeft u niet genoeg geld om te gaan gokken")
else:
    donatie_vraag = input(f"Had u nog een donatie willen geven van {standaard_donatie} aan ons goede doel ? Ja/Nee")

if donatie_vraag == "Ja":
    donatiebedrag = belasting_bedrag - standaard_donatie
    belasting_bedrag = belasting_bedrag - standaard_donatie
    totale_kosten = totale_kosten + standaard_donatie
    print(f"Dankuwel voor uw Donatie {aanhef} {naam}")

else:
    print("bedankt voor uw consideratie")

#Eindstatement
print(f"""
    "--------------------------------------------------------"
    Casino van Grevenhof
    Startbedrag: {start_bedrag:.2f}
    Kosten: {totale_kosten:.2f}
    Eindbedrag: {belasting_bedrag:.2f}
    Wij Wensen u een Fijne Avond en Veel Geluk, {aanhef} {naam}
    "--------------------------------------------------------"
""")











