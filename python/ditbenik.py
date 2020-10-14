#python hello you beroepsopdracht

import time

print("\u001b[37mHello You! Ik ben Samed, 16 jaar oud")

time.sleep(1)
print("En wie ben jij?")

time.sleep(1)
naam = input("Ik ben: ")

time.sleep(1)
print("Welkom! " + naam)

time.sleep(1)
print("Wat is je favoriete kleur?")

time.sleep(1)
kleur = input("Mijn favoriete kleur is: ")

time.sleep(1)
print(kleur + " is een mooi kleur!")

time.sleep(1)
print("Mijn favoriete kleur is \u001b[32mbosgroen!\u001b[37m")
print("\n")
time.sleep(1)
print("Oke, nu gaan we een kort quiz doen om mij beter te leren kennen!")
print("\n")
time.sleep(2)

answer1 = input("\u001b[37mWat is mijn favoriete kleur? \na. Rood \nb. Bosgroen \nc. Lichtblauw \nAntwoord: ")

if answer1 == "b" or answer1 == "Bosgroen" :
    print("\u001b[32mCorrect!\u001b[37m")
    print("\n")
else: print("\u001b[31mFout! Het antwoord was Bosgroen.\n\u001b[37m")
time.sleep(2)

print("Volgende vraag!\n")

answer2 = input("\u001b[37mWelke kant ga ik op? \na. Media \nb. Game \nc. Weet ik nog niet \nAntwoord: ")

if answer2 == "a" or answer2 == "Media" :
    print("\u001b[32mCorrect!\u001b[37m")
    print("\n")
else: print("\u001b[31mFout! Het antwoord was Media.\n\u001b[37m")
time.sleep(2)

answer3 = input("\u001b[37mWaar woon ik? \na. Amsterdam \nb. Utrecht \nc. Zaandam \nAntwoord: ")

if answer3 == "c" or answer3 == "Zaandam" :
    print("\u001b[32mCorrect!\u001b[37m")
    print("\n")
else: print("\u001b[31mFout! Het antwoord was Zaandam.\n\u001b[37m")
time.sleep(1)

print("Laatste vraag!\n")
time.sleep(1)

answer4 = input("Ik twijfel tussen 2 vragen die ik aan jou wil stellen, dus ik laat jou het kiezen. Wil je een vraag over hoe oud ik ben, of een vraag over wat mijn favoriete game is? \na. Leeftijd \nb. Favoriete game\nAntwoord: ")

print("\n")

time.sleep(1)

if answer4 == "a" :
	answer = input("Hoe oud ben ik? \na. 17 \nb. 15 \nc. 16\nAntwoord: ")
	if answer ==  "c" or answer == "16" : print("\u001b[32mCorrect!\u001b[37m")
	else: print("\u001b[31mFout! Het antwoord was C.\u001b[37m")
elif answer4 == "b" :
	answer = input("Wat is mijn favoriete game? \na. Detroit: Become Human \nb. Gta v \nc. Minecraft\n Antwoord: ")
	if answer == "c" or answer == "Minecraft" : print("\u001b[32mCorrect!\u001b[37m")
	else: print("\u001b[31mFout! Het antwoord was C.\u001b[37m")

print("Dit was het, hoop dat je het leuk vond!")
	
