import sys
import time

#VRAAG22------------------------------------------------------------------
def vraag22():
    tekst = "\n22. Je vertrouwt hem niet en zegt dat je uit de auto wilt. De agent stopt de auto en laat foto’s zien van hem en de vluchtelingenorganisaties waar hij mee samenwerkt. “Het ligt aan jou of je me vertrouwt of niet” zegt de agent. Je vertrouwt hem en zegt dat je erheen wilt gaan. Na een half uur zijn jullie er. Je stapt uit en bedankt hem. Je gaat naar binnen en er komt al een vrijwilliger die voor de vluchtelingenorganisatie werkt. Je vraagt aan haar of ze je naar Nederland kunnen brengen. Ze zegt dat de bus die naar Nederland gaat elke vrijdag komt, en de vluchtelingen die naar Nederland willen daarnaartoe brengt. “Morgen dus?” vraag je. Ja, zegt de mevrouw. Je belt meteen je familie en zegt dat je over een paar dagen in Nederland bent. “En wat moet ik doen als ik eenmaal in Nederland ben?” vraag je nog. “De vrijwilligers van VluchtelingenWerk in Nederland gaan je daar helpen!” zegt ze. Nu weet je tenminste dat alles goed gaat komen, en slaapt zonder je zorgen te maken over morgen."
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n\u001b[32mEINDE")

#VRAAG21------------------------------------------------------------------
def vraag21():
    tekst = "\n21. Je vertrouwt hem en zegt dat je erheen wilt gaan. Na een half uur zijn jullie er. Je stapt uit en bedankt hem. Je gaat naar binnen en er komt al een vrijwilliger die voor de vluchtelingenorganisatie werkt. Je vraagt aan haar of ze je naar Nederland kunnen brengen. Ze zegt dat de bus die naar Nederland gaat elke vrijdag komt, en de vluchtelingen die naar Nederland willen daarnaartoe brengt. “Morgen dus?” vraag je. Ja, zegt de mevrouw. Je belt meteen je familie en zegt dat je over een paar dagen in Nederland bent. “En wat moet ik doen als ik eenmaal in Nederland ben?” vraag je nog. “De vrijwilligers van VluchtelingenWerk in Nederland gaan je daar helpen!” zegt ze. Nu weet je tenminste dat alles goed gaat komen, en slaapt zonder je zorgen te maken over morgen."
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n\u001b[32mEINDE")

#VRAAG20------------------------------------------------------------------
def vraag20():
    tekst = "\n20. 	Je besluit om in te stappen. De agent vraagt uit welke land je hebt vlucht. Je probeert te liegen en zegt dat je hier woont. De agent zegt dat je eerlijk mag zijn en hij je kan helpen. Je twijfelt eerst maar geeft het uiteindelijk toe. “Ik kan je naar een asiel brengen waar je tijdelijk kan blijven, er zijn daar ook vluchtelingenorganisaties die je kunnen helpen” zegt de agent.  "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.	...Je vertrouwt hem.        \nB.   ...Je vertrouwt hem niet.       \n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag19() #gaat naar vraag 21
    elif antw == "B" :
        vraag20() #gaat naar vraag 22
    else:
        print("ongeldig antwoord") 

#VRAAG19------------------------------------------------------------------
def vraag19():
    tekst = "\n19. Je besluit om de bus te nemen. De bus die jij gaat nemen komt over 10 minuten. Na ongeveer 10 minuten is de bus er al. Er gaan best veel mensen in de bus dus het zal niet opvallen als je niet betaald. Je gaat snel langs de chauffeur en gaat achterin zitten. Je ziet een man jou aanwijzen terwijl hij met de buschauffeur praat. Je staat meteen op en probeert weg te komen. De chauffeur roept naar je dat je moet blijven. Je gaat de bus uit en ziet agenten naar je toekomen. “Stop of we schieten!” schreeuwen ze. Je hebt geen andere optie dan te stoppen. De agenten houden je aan en nemen je mee naar het politiebureau."
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n\u001b[32mGAME OVER")

#VRAAG18------------------------------------------------------------------
def vraag18():
    tekst = "\n18. Je besluit om nog te gaan wachten met de andere vluchtelingen. Na precies een half uur zien jullie paar mensen van de organisatie VluchtelingenWerk Nederland staan. Jullie gaan naar ze toe en vragen om hulp. Ze brengen jullie naar een asiel waar je tijdelijk kan blijven. Je vraagt aan iemand die in de organisatie werkt of ze je naar Nederland kunnen brengen. Ze zegt dat de bus die naar Nederland gaat elke vrijdag komt, en de vluchtelingen die naar Nederland willen daarnaartoe brengt. ‘Morgen dus?’ vraag je. Ja, zegt de mevrouw. Je belt meteen je familie en zegt dat je over een paar dagen in Nederland bent. ‘En wat moet ik doen als ik eenmaal in Nederland ben?’ vraag je nog. ‘De vrijwilligers van VluchtelingenWerk in Nederland gaan je daar helpen!’ zegt ze. Nu weet je tenminste dat alles goed gaat komen, en slaapt zonder je zorgen te maken over morgen"
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n\u001b[32mEINDE")

#VRAAG17------------------------------------------------------------------
def vraag17():
    tekst = "\n17. Je besluit om met ze mee te gaan en wenst de anderen succes. Jullie stappen in de trein, en gaan helemaal achterin zitten, waar het best leeg is. Jullie zijn al 1 uur onderweg en tot nu toe gaat het goed, maar diep vanbinnen voel je dat het fout gaat. De persoon naast je zegt dat er iemand aankomt, en denkt dat het een treinconducteur is. Hij komt dichterbij en het is inderdaad een treinconducteur. Hij merkt dat jullie vluchtelingen zijn en vraagt om identificatie. Je vraagt hem of hij het door te vingers kan zien, maar de treinconducteur weigert. De trein is al gestopt en het is tijd om af te stappen, maar jullie moeten nog blijven. Vervolgens komen er politieagenten binnen en nemen ze ons mee.   "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n\u001b[31mGAME OVER")

#VRAAG16------------------------------------------------------------------
def vraag16():
    tekst = "\n16. Jullie besluiten om te wachten op de chauffeur. De chauffeur komt terug en zegt dat hij heeft gefaald. De agent vraagt om jullie ID, en belt ondertussen met iemand. Na 10 minuten komt er een politiebusje. Je verliest alle hoop. Jullie stappen in de politiebus, en gaan naar het bureau.   "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n\u001b[31mGAME OVER")

#VRAAG15------------------------------------------------------------------
def vraag15():
    tekst = "\n15. 	Je staat al een half uur langs de weg, maar niemand stopt. Je denkt nog aan je plan B om zwart te gaan rijden met een bus, maar lijkt je geen goed idee. Er stopt eindelijk een auto, en als het dichterbij komt zie je dat het een politieauto is. Hij stopt en vraagt of je een lift nodig hebt. Je besluit om… "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.	...toch te gaan zwartrijden met een bus        \nB.   ...in te stappen        \n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag19() #gaat naar vraag 19
    elif antw == "B" :
        vraag20() #gaat naar vraag 20
    else:
        print("ongeldig antwoord") 

#VRAAG14------------------------------------------------------------------
def vraag14():
    tekst = "\n14. 	Je besluit om te gaan eten in een restaurant. Nadat je hebt gegeten ga je weer naar buiten. Er is dichtbij een busstation en het lijkt je een goed idee om met een bus te gaan reizen, maar je denkt dat het beter is om je geld te besparen voor tijden wanneer je het echt nodig zal hebben. Je besluit om… "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.	...zwart te gaan rijden met de bus        \nB.   ...langs de weg te staan totdat er een auto voor je stopt.       \n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag19() #gaat naar vraag 19
    elif antw == "B" :
        vraag15() #gaat naar vraag 15
    else:
        print("ongeldig antwoord") 

#VRAAG13------------------------------------------------------------------
def vraag13():
    tekst = "\n13. 	Na een paar uur rijden zijn jullie aangekomen bij de grens tussen Griekenland en Macedonië. Jullie zijn via een ander weg gekomen dus hoeven niet langs een douane te gaan. Na een lange reis door Macedonië en Servië zijn jullie al in Budapest, hoofdstad van Hongarije aangekomen. Je hebt gehoord dat vluchtelingen help organisaties meestal bij grote treinstations staan om daar vluchtelingen te helpen. Dus het leek jullie een goed idee om naar het centraal station van Budapest te gaan. Na een uur wachten en zoeken werden er een paar ongeduldig en zeiden ze willen zwartrijden naar Oostenrijk. Je besluit om…"
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.	...met ze mee te gaan        \nB.   ...nog te gaan wachten       \n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag17() #gaat naar vraag 17
    elif antw == "B" :
        vraag18() #gaat naar vraag 18
    else:
        print("ongeldig antwoord") 

#VRAAG12------------------------------------------------------------------
def vraag12():
    tekst = "\n12. Je zegt dat je ook wilt gaan eten, dus de meerderheid wilt eten. De chauffeur brengt jullie naar een restaurant. Na het eten gaan jullie weer het busje in. Net voordat de chauffeur wil rijden, komt er een politieagent aan en vraagt of de chauffeur wil uitstappen. Je krijgt hier al een slecht gevoel over. De politieagent vraagt hem wat en de chauffeur lijkt in paniek te raken. Paar mensen achterin zeggen dat we hem moeten achterlaten of anders wij ook gepakt zullen worden. Ze vragen jou wat het beste idee is. Je besluit om…"
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.	...de chauffeur achter te laten.       \nB.   ...te wachten op de chauffeur       \n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag13() #gaat naar vraag 13
    elif antw == "B" :
        vraag16() #gaat naar vraag 16
    else:
        print("ongeldig antwoord") 

#VRAAG11------------------------------------------------------------------
def vraag11():
    tekst = "\n11. Je besluit om niet te wachten, en zelf een manier te vinden om naar Nederland te gaan. Je staat langs de weg totdat er een taxi aankomt. Je stapt in en zegt dat je naar de grens van Griekenland en Macedonië wil. Na een paar uur rijden ben je er eindelijk, je betaalt de taxi en begint te lopen. Het is 12 uur in de nacht dus je kan niet makkelijk gezien worden door de douane. Je steekt de grens over via een bosje, en je bent in Macedonië. Je hebt best wel honger en langs de weg staat een klein restaurantje, je besluit om… "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.	...daar te gaan eten      \nB.   ...geen tijd te verspillen en door te gaan       \n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag14() #gaat naar vraag 14
    elif antw == "B" :
        vraag15() #gaat naar vraag 15
    else:
        print("ongeldig antwoord") 

#VRAAG10------------------------------------------------------------------
def vraag10():
    tekst = "\n10. Je besluit om te wachten en overnacht 2 dagen in een auto. Uiteindelijk bellen de broers je en geven ze je een locatie om af te spreken. Je gaat ernaartoe en ziet ze staan. De broers brengen je naar een busje waarin ook andere vluchtelingen zoals jij zitten. Ze zeggen dat ze hier nog even gaan blijven en de persoon die je nu gaat brengen vertrouwelijk is en jullie eten zal geven. Je vraagt tot waar het busje heen gaat. “Tot Duitsland” zegt de chauffeur. Je neemt afscheid van de broers en stapt in het busje. De chauffeur vraagt of jullie naar een restaurant willen om te eten, of door willen gaan. 2 mensen willen in een restaurant eten, en 2 willen geen tijd verspillen en gewoon gaan. De chauffeur vraagt dan aan jou wat jij wilt. Je… "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.	...wilt ook naar een restaurant      \nB.   ...wilt liever geen tijd verliezen en doorgaan      \n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag12() #gaat naar vraag 12
    elif antw == "B" :
        vraag13() #gaat naar vraag 13
    else:
        print("ongeldig antwoord") 

#VRAAG9------------------------------------------------------------------
def vraag9():
    tekst = "\n9. Je besluit om zelf een manier te vinden om naar Nederland te gaan, en zegt dat tegen de man. Hij wenst je succes en gaat weer weg. Je stapt weer in je oude boot en gaat richting Athene. Na een lange, vermoeiende reis ben je aangekomen in Athene. Je voelt je telefoon trillen en ziet dat je wordt gebeld. Je neemt het op en het zijn de broers. Ze zeggen dat het gewond is behandeld en dat ze over een paar dagen in Athene zijn. Aan jou laten ze de keuze over of je op hun wacht of met een beetje geld op zak zelf naar Nederland gaat. Je besluit om… "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.	...op ze te wachten     \nB.   ...niet te wachten     \n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag10() #gaat naar vraag 10
    elif antw == "B" :
        vraag11() #gaat naar vraag 11
    else:
        print("ongeldig antwoord") 

#VRAAG8------------------------------------------------------------------
def vraag8():
    tekst = "\n8. De man accepteert je horloge en zegt dat hij je veilig naar Athene zult brengen. Onderweg wordt de man gebeld door de broers. Hij neemt op en vraagt waar ze zijn. De broers zeggen dat ze in een ziekenhuis in Turkije zijn en dat ze over een paar dagen naar Athene zullen komen. De broers vragen aan je of je op hun wil wachten of met een beetje geld op zak naar Nederland wil gaan. Je besluit om… "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.	...op ze te wachten     \nB.   ...niet te wachten     \n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag10() #gaat naar vraag 10
    elif antw == "B" :
        vraag11() #gaat naar vraag 11
    else:
        print("ongeldig antwoord") 


#VRAAG7------------------------------------------------------------------
def vraag7():
    tekst = "\n7. Je zegt de broers dat het je spijt, en je door moet gaan. Na paar uur varen komen jullie bij een Grieks eiland aan, en de toestand van de gewonde broer verslechtert. Je belt meteen je familie en vertelt hun dat alles goed is gegaan en je veilig bent. Na een half uur komt er een bootje die jullie naar Athene brengt. De man in de boot ziet dat er een gewonde is en biedt snel medische hulp aan. Jullie stappen in en de gewonde broer wordt behandeld. Wanneer jullie zijn aangekomen in Athene, zeggen de broers dat je er vanaf nu alleen voor staat, omdat de gewonde echt naar het ziekenhuis moet. Je zegt tegen ze dat dat niet de afspraak was, en dat ze je op zijn minst naar Duitsland zouden brengen. Ze zeggen dat je of nog een paar dagen wacht totdat de toestand van de gewonde broer wordt verbeterd, of dat ze je nu beetje geld geven zodat je alleen kunt gaan. Je besluit om…  "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.	...op ze te wachten     \nB.   ...zelf te gaan met een beetje geld    \n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag10() #gaat naar vraag 10
    elif antw == "B" :
        vraag11() #gaat naar vraag 11
    else:
        print("ongeldig antwoord") 

#VRAAG6------------------------------------------------------------------
def vraag6():
    tekst = "\n6. Je besluit om de rubberen boot te gebruiken. Je neemt afscheid van de broers en wenst ze veel succes. 9 uur in de avond kom je bij een Grieks eiland aan. Na je aankomst bel je meteen je familie en zeg je dat je veilig bent aangekomen in Griekenland. Verder weet je niet wat je moet doen omdat de personen die dit hadden georganiseerd (de broers) naar Turkije zijn gegaan. Je ziet dat er een klein bootje naar je toe komt, je denkt dat het de kustwacht is en verstop je. De man in de boot merkt dat je een vluchteling bent en zegt dat hij je komt helpen om naar Athene te gaan. Je komt tevoorschijn en vraagt wie hij is. “Ik ben de persoon die jullie komt ophalen” zegt de man. Als hij dichtbij is ziet hij dat je alleen bent en vraagt hij waar de anderen zijn. Je vertelt hem wat er gebeurd is en dat jij de enige bent die tot hier is gekomen. De man zegt dat hij geld wil en het door de broers zou krijgen, maar aangezien die er niet zijn hij je helaas niet kan helpen. Je smeekt hem maar het antwoord blijft nog steeds nee. Je hebt een horloge om die je van je vader had gekregen, en best veel waard is. Je zou het aan de man kunnen geven. Je besluit om...  "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.	...Je horloge te geven    \nB.   ...Zelf een oplossing te vinden om naar Nederland te gaan   \n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag8() #gaat naar vraag 8
    elif antw == "B" :
        vraag9() #gaat naar vraag 9
    else:
        print("ongeldig antwoord") 

#VRAAG5------------------------------------------------------------------
def vraag5():
    tekst = "\n5. Je besluit om niet mee te gaan. Wanneer jullie in Aleppo zijn, zie je de mensen die over het vluchten praatten, afscheid nemen en vertrekken. Jij en de rest gaan door met jullie missie. Paar uur later keren jullie terug naar de basis. Onderweg rijden jullie op een landmijn geplaatst door terroristen en overlijdt iedereen in de auto.   "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n\u001b[31mGAME OVER")

#VRAAG4------------------------------------------------------------------
def vraag4():
    tekst = "\n4. Je besluit om ook te vluchten, je roept naar de 2 vluchtelingen in de reserveboot en springt ook erin. De kustwacht waarschuwt jullie dat jullie terug moeten komen. Na een aantal waarschuwing beginnen ze te schieten. Je raakt in paniek en gaat liggen zodat je niet geraakt wordt. Wanneer jullie ver genoeg zijn sta jij en de andere vluchteling op en kijken of ze jullie achtervolgen, maar zien niks. Je kijkt achter je en ziet opeens dat de andere vluchteling gewond is. Je roept de andere vluchteling en zegt dat er een gewonde is. Hij gaat naar hem toe en het blijkt dat ze broers zijn. Zijn wond is groot en medische hulp is op dit moment niet mogelijk, dus zijn overlevingskans is laag. Je probeert hem gerust te stellen. De broers zeggen dat ze naar Turkije willen gaan voor medische hulp, en zeggen dat ze nog een rubberen boot hebben die je dan zelf kan gebruiken om naar Griekenland te gaan, wat een stuk onveiliger is. Je besluit om...  "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.	...De rubberen boot te gebruiken   \nB.   ...Niet naar ze te luisteren, en door te gaan naar Griekenland  \n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag6() #gaat naar vraag 6
    elif antw == "B" :
        vraag7() #gaat naar vraag 7
    else:
        print("ongeldig antwoord") 

#VRAAG3------------------------------------------------------------------
def vraag3():
    tekst = "\n3. Je besluit om te blijven en wacht totdat de Turkse kustwacht eraan komt. Wanneer ze er zijn verzoeken ze jullie om uit jullie boot in hun schip in te stappen. Jullie luisteren en doen wat ze zeggen. Eerst wordt jullie tassen gecontroleerd of er wapens in zitten. Communiceren gaat moeilijk aangezien jullie geen Turks spreken. De Turkse agent kan gebrekkig Engels spreken en vraagt waar jullie vandaan komen. Iemand zegt dat ze uit Syrië komen en naar Europa vluchten. De agent maakt een knik gebaar en gaat naar de andere agenten. Paar uur later komt er een ander schip waar jullie weer in moeten stappen. Je vraagt aan de agent waar ze jullie heen sturen, en hij zegt dat het hem spijt en dat we terug moeten naar Syrië.   "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n\u001b[31mGAME OVER")

#VRAAG2------------------------------------------------------------------
def vraag2():
    tekst = "\n2. Je moeder was al naar Nederland gevlucht, dus je eindbestemming staat al vast. Bang was je niet. Je neemt afscheid van je familie en vrienden en je stapt in de boot die je naar Griekenland brengt. Aan boord huilen de moeders en hun kleine kinderen. “Stil maar” zeg je. “Ik weet zeker dat we de overkant zullen halen”. Jullie varen nu langs Turkije en ziet een schip achter je aan komen. Je waarschuwt de anderen en iemand zegt dat het een Turks kustwachtschip is. Het schip komt dichtbij en je hoort uit de luidsprekers iemand Turks praten. Iemand in je boot spreekt een beetje Turks en vertaalt het voor jullie. “Ze zeggen dat we moeten stoppen”. Paar mensen zijn het er oneens over en willen niet stoppen. 2 mensen pakken de reserveboot en willen vluchten. Je besluit om…   "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.	...ook te vluchten   \nB.   ...te blijven \n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag4() #gaat naar vraag 4
    elif antw == "B" :
        vraag3() #gaat naar vraag 3
    else:
        print("ongeldig antwoord") 

#VRAAG1------------------------------------------------------------------
def vraag1():
    tekst = "\n1. Na paar weken wordt het situatie in Syrië erger en moeten alle mensen boven de 18 die geen beperking hebben het leger in. Dus je wordt opgehaald van huis en gaat naar het leger. Tweede dag in het leger heb je al een missie en word je gestuurd naar Aleppo. In de gepantserde militaire auto onderweg naar Aleppo praten paar mensen over het vluchten met een boot naar Europa, en ze vragen of je mee wilt. Je besluit om…  "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.   ...mee te gaan met hun  \nB.   ...niet met hun mee te gaan\n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag2() #gaat naar vraag 2
    elif antw == "B" :
        vraag5() #gaat naar vraag 5
    else:
        print("ongeldig antwoord")  

#START------------------------------------------------------------------
def start():
    tekst = "Je woont in Syrië met je vader, en bent vrijgesteld van de militaire dienstplicht. Tot je hoorde dat de zoon van een goede huisvriend, ook enig kind, was opgepakt en het leger in moest. “Ik geef je nog een paar weken en dan wil ik dat je weg bent”, zegt je vader ongerust. Sinds de scheiding van je ouders woonde je bij hem. Je twijfelt nog of je wilt vluchten, of hier wilt blijven met je vader. Je besluit om... "
    for char in tekst:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(3)

    print("\n")
    print("A.   ...te blijven \nB.   ...te vluchten\n")
    time.sleep(1)
    antw = input("kies A of B : ")

    if antw == "A" :
        vraag1() #gaat naar vraag 1
    elif antw == "B" :
        vraag2() #gaat naar vraag 2
    else:
        print("ongeldig antwoord")    

start()