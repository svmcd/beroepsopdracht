import sys
import time

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