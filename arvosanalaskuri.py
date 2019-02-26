#tehdään "globaali" kaynnissa-muuttuja, jonka avulla ohjelma tietää jatkaa toimintaansa tai pysähtyä
kaynnissa = True
#tervehdysteksti ja muuttujien alustus kyselyä varten, tälle joku fiksumpi toteutus olis kiva
while kaynnissa:
    print("Tervetuloa Jaakon arvosanalaskuriin!")
    maxpisteet = "foo"
    lapaisyprosentti = "bar"

#tarkistetaan, onko käyttäjän syöte luku ja kysytään uudestaan, jos näin ei ole
    while not maxpisteet.isdigit():
        maxpisteet = input("Kokeen maksimipisteet: ")
    while not lapaisyprosentti.isdigit():
        lapaisyprosentti = input("Läpipääsyraja prosentteina: ")

#tehdään syötteistä kokonaisluvut
    maxpisteet = int(maxpisteet)
    lapaisyprosentti = int(lapaisyprosentti)

#luodaan laskurimetodi, joka palauttaa tiettyyn arvosanaan vaadittavan pistemäärän
    def laskuri(arvosana):
        kulmakerroin = float((10-4.75)/(maxpisteet-(maxpisteet*lapaisyprosentti)/100))
        return float((arvosana-10+kulmakerroin*maxpisteet)/kulmakerroin)

#lasketaan arvosana ja tulostetaan arvosanalista, printtaukselle voisi tehdä oman metodin
    arvosana = 10
    space = ""
    hyvaksytty = True
    print("Pts   | Arvosana\n~~~~~~~~~~~~~~~~")
    while arvosana >= 4:
    #printtausformatointi jotenkin järkeväksi
        if laskuri(arvosana)<10:
            space = " "
        print(format(laskuri(arvosana), '.2f'), space, " | ", arvosana, sep="")
        arvosana = arvosana - 0.25
        if hyvaksytty and arvosana < 4.75:
            print("-------------")
            hyvaksytty = False
    komento = ""
    while not (komento == "x" or komento == "r"):
        komento = input("\nKirjoita r laskeaksesi uudelleen, x lopettaaksesi. ")
        #kun kaynnissa muuttuu falseksi, ohjelman suorittaminen loppuu
    if komento == "x":
        kaynnissa = False
        print("Arvosanojen laskemisen teille tarjosi: Jack")
