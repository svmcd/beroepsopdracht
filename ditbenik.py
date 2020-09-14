#python hello you beroepsopdracht

import time

print("\u001b[37mHello You! Ik ben Samed")

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
else: print("\u001b[31mFout! Het antwoord was Bosgroen.\u001b[37m")
time.sleep(2)

print("Volgende vraag!\n")

answer2 = input("\u001b[37mWelke kant ga ik op? \na. Media \nb. Game \nc. Weet ik nog niet \nAntwoord: ")

if answer2 == "a" or answer2 == "Media" :
    print("\u001b[32mCorrect!\u001b[37m")
    print("\n")
else: print("\u001b[31mFout! Het antwoord was Media.\u001b[37m")
time.sleep(2)

print("Laatste vraag!\n")

answer3 = input("\u001b[37mWaar woon ik? \na. Amsterdam \nb. Utrecht \nc. Zaandam \nAntwoord: ")

if answer3 == "c" or answer3 == "Zaandam" :
    print("\u001b[32mCorrect!\u001b[37m")
    print("\n")
else: print("\u001b[31mFout! Het antwoord was Zaandam.\u001b[37m")
time.sleep(2)

