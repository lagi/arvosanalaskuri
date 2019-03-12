#luodaan kaynnissa-muuttuja, jonka avulla ohjelma tietää jatkaa toimintaansa tai pysähtyä
kaynnissa = True
#tervehdysteksti ja muuttujien alustus kyselyä varten
while kaynnissa:
    print("Tervetuloa Jaakon arvosanalaskuriin!")
    maxpisteet = "foo"
    lapaisyprosentti = "bar"
    arvosanat = ["10", "10-", "9½", "9+", "9", "9-", "8½", "8+", "8", "8-", "7½", "7+", "7", "7-", "6½",
                 "6+", "6", "6-", "5½", "5+", "5", "5-", "4½", "4+", "4"]

#tarkistetaan, onko käyttäjän syöte luku ja kysytään uudestaan, jos näin ei ole
    while not maxpisteet.isdigit():
        maxpisteet = input("Kokeen maksimipisteet: ")
    while not lapaisyprosentti.isdigit():
        lapaisyprosentti = input("Läpipääsyraja prosentteina: ")
        #varmistetaan myös, että läpäisyprosentti on alle 100
        if lapaisyprosentti.isdigit():
            lapaisyprosentti = int(lapaisyprosentti)
            if lapaisyprosentti >= 100:
                lapaisyprosentti = "bar"
                continue
            else:
                break

#tehdään syötteistä kokonaisluvut laskutoimituksia varten
    maxpisteet = int(maxpisteet)
    lapaisyprosentti = int(lapaisyprosentti)

#luodaan laskurimetodi, joka palauttaa tiettyyn arvosanaan vaadittavan pistemäärän
    def tarvittavaPistemaara(arvosana):
        kulmakerroin = float((10-4.75)/(maxpisteet-(maxpisteet*lapaisyprosentti)/100))
        pistemaara = float((arvosana-10+kulmakerroin*maxpisteet)/kulmakerroin)
        return pistemaara

#lasketaan arvosana aloittaen 10:stä ja tulostetaan arvosanalista yksi arvosana kerrallaan
    arvosana = 10
    #space on muokattava merkkijono tulostuksen formatointia varten
    space = ""
    hyvaksytty = True
    counter = 0
    print("Pts   | Arvosana\n~~~~~~~~~~~~~~~~")
    while arvosana >= 4:
    #jos tarvittava pistemäärä on alle kymmenen, niin space muuttuu välilyönniksi formatoinnin selkeyden vuoksi
        if tarvittavaPistemaara(arvosana)<10:
            space = " "
    #tulostetaan pistemäärä kahden desimaalin tarkkuudella, erotin ja arvosana listasta
        print(format(tarvittavaPistemaara(arvosana), '.2f'), space, " | ", arvosanat[counter], sep="")
        arvosana = arvosana - 0.25
        counter += 1
    #kun arvosana laskee kynnyksen alle, tulostetaan erotin ja hyvaksytty varmistaa, ettei tätä tehdä toiste
        if hyvaksytty and arvosana < 4.75:
            print("-----------")
            hyvaksytty = False
#tulostuksen jälkeen kysytään käyttäjältä mahdolliset jatkotoimenpiteet
    komento = ""
    while not (komento == "x" or komento == "r"):
        komento = input("\nKirjoita r laskeaksesi uudelleen, x lopettaaksesi. ")
#kun kaynnissa muuttuu falseksi, tulostetaan jäähyväisteksti ja ohjelman suorittaminen loppuu
    if komento == "x":
        kaynnissa = False
        print("Arvosanojen laskemisen teille tarjosi: Jack")
