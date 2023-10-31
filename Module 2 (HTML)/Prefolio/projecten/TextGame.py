import os
import time
from termcolor import colored
from art import *
import random
import keyboard

stats = {
    "HuisjeGezien": 1,
    "BijHuisjeGeweest": False
}
intro = '''Welkom bij het avontuur!

Je bevindt je in een mysterieuze bos vol uitdagingen en avonturen.
Je hebt geen eten of drinken meer.
Als speler heb jij de touwtjes in handen en elke beslissing die je neemt, zal het verloop van het verhaal beïnvloeden. 
Maar wees gewaarschuwd, want voor elke uitdaging die voor je ligt, moet je zorgvuldig je keuzes maken.

Om te antwoorden op de verschillende situaties die je tegenkomt, gebruik je de toetsen A, B, C of 1, 2 en 3
Dit is hoe je de richting van jouw avontuur bepaalt.

Bereid je voor op een spannende reis vol verrassingen, beslissingen en ontdekkingen.
Jouw lot ligt in jouw handen. Laten we beginnen!
'''
sleeptime = 0.03

def slowprint(str):
    global sleeptime
    waitlist = [".", "!", "?"]
    for letter in str:
        if keyboard.is_pressed("space"):
            sleeptime = 0
        else:
            if letter in waitlist:
                sleeptime = 0.7
            else:
                sleeptime = 0.03
        # sleeptime = 0 # Delete later
        print(letter, end='', flush=True)
        time.sleep(sleeptime)
    print("\n")
    keyboard.unhook_all()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def Screen_Death(reason):
    clear_screen()
    tprint("YOU  DIED")
    print(f"           {reason}")
    print()
    input("Druk op enter om opnieuw te beginnen")
    clear_screen()
    slowprint(intro)
    input("Druk op enter om te starten")
    GoToVraag(1)

def Vraag(vraag, opties):
    if len(opties) == 2:
        UserAntwoord = ["1", "2", "a", "b"]
        beantwoordttxt = "beantwoord met A, B, 1 of 2"
    else:
        UserAntwoord = ["1", "2", "3", "a", "b", "c"]
        beantwoordttxt = "beantwoord met A, B, C, 1, 2 of 3"
    optieVragen = ""
    for i in opties:
        optieVragen = optieVragen + str(opties.index(i) +1) + ". " + i + "\n"

    while True:
        slowprint(f'''{vraag}
Wat doe je? ({beantwoordttxt})

{optieVragen}''')
        UserInput = input().replace(" ", "").lower()
        if UserInput in UserAntwoord:
            return UserInput
        else:
            clear_screen()
            slowprint(colored(f"{UserInput} is geen geldig antwoord.\n{beantwoordttxt}", "red"))


def GoToVraag(number):
    clear_screen()
    if number == 1:
        vraag = "Je hoort een geluid achter je."
        opties = ["Je rent weg.", "Je gaat kijken."]
        UserAntwoord = Vraag(vraag, opties)
        if UserAntwoord in ["1", "a"]:
            GoToVraag(2)
        elif UserAntwoord in ["2", "b"]:
            Screen_Death("Je ben opgegeten door een beer")

    elif number == 2:
        if stats["HuisjeGezien"] == 1:
            vraag = "Je ziet in de verte een huisje.\nJe rent naar het huisje toe."
            stats["HuisjeGezien"] = 2
        else:
            vraag = "Je rent terug naar het huisje."
        opties = ["Je rent naar binnen.", "Je kijkt door het raam heen.", "Je klopt aan."]
        UserAntwoord = Vraag(vraag, opties)
        if UserAntwoord in ["1", "a"]:
            Screen_Death("Je bent neergestoken door de bewoner")
        if UserAntwoord in ["2", "b"]:
            GoToVraag(3)
        if UserAntwoord in ["3", "c"]:
            GoToVraag(4)

    elif number == 3:
        vraag = "Je ziet een grote man aan het koken."
        opties = ["Je rent weg.", "Je klopt aan."]
        UserAntwoord = Vraag(vraag, opties)
        if UserAntwoord in ["1", "a"]:
            GoToVraag(5)
        if UserAntwoord in ["2", "b"]:
            GoToVraag(4)

    elif number == 4:
        if stats["BijHuisjeGeweest"] == True:
            Screen_Death("Je bent neergestoken door de bewoner, hij houd niet van mensen die belletje lellen")
        else:
            vraag = "Een Grote man met een mes in zijn handen doet de deur open."
            opties = ["Je rent weg.", "Je vraagt of je naar binnen mag."]
            UserAntwoord = Vraag(vraag, opties)
            if UserAntwoord in ["1", "a"]:
                stats["BijHuisjeGeweest"] = True
                GoToVraag(5)
            if UserAntwoord in ["2", "b"]:
                GoToVraag(6)
    
    elif number == 5:
        vraag = "Het is inmiddels super donker geworden in het bos."
        opties = ["Je probeert te slapen op wat mos en bladeren.", "Je probeert de uitgang van het bos te vinden.", "Je gaat terug naar het huisje."]
        UserAntwoord = Vraag(vraag, opties)
        if UserAntwoord in ["1", "a"]:
            Screen_Death("Je raakte onderkoelt en ging dood")
        if UserAntwoord in ["2", "b"]:
           Screen_Death("Je viel in een kuil en belanden met je hooft in een berenval")
        if UserAntwoord in ["3", "c"]:
            GoToVraag(4)

    elif number == 6:
        vraag = "Je zit tegenover de man bij de openhaard."
        opties = ["Je vraagt of je mag blijven slapen.", "Na opgewarmed te zijn bedank je de man en ga je er van door."]
        UserAntwoord = Vraag(vraag, opties)
        if UserAntwoord in ["1", "a"]:
            GoToVraag(7)
        if UserAntwoord in ["2", "b"]:
           GoToVraag(5)

    elif number == 7:
        vraag = "Je mag blijven slapen maar je voelt je niet heel veilig."
        opties = ["Je doet de deur van je kamer op slot.", "Je gaat slapen."]
        UserAntwoord = Vraag(vraag, opties)
        if UserAntwoord in ["1", "a"]:
            GoToVraag(8)
        if UserAntwoord in ["2", "b"]:
           GoToVraag(9)

    elif number == 8:
        vraag = "Je hebt je kamer deur op slot gedaan.\nJe hoort gebonk door de deur.\nJe ziet de Man met een hakbijl in zijn handen door de deur komen."
        opties = ["Je springt uit het raam.", "Je doet alsof je slaapt", "Je verstopt je onder het bed."]
        UserAntwoord = Vraag(vraag, opties)
        if UserAntwoord in ["1", "a"]:
            Screen_Death("Je werd gespiest door een hark die onder het raam stond")
        if UserAntwoord in ["2", "b"]:
            GoToVraag(9)
        if UserAntwoord in ["3", "c"]:
            Screen_Death("De man werd boos en vond je onder het bed.\nHij stak een mes door het matras in je rug")

    elif number == 9:
        vraag = "Je word waker en gaat naar beneden.\nJe ziet de man in de keuken ontbijt maken."
        opties = ["Je rent het huis uit.", "Je begroet de man en vraagt of je mag blijven ontbijten.", "Je bedankt de man en gaat naar buiten"]
        UserAntwoord = Vraag(vraag, opties)
        if UserAntwoord in ["1", "a"]:
             GoToVraag(10)
        if UserAntwoord in ["2", "b"]:
            GoToVraag(12)
        if UserAntwoord in ["3", "c"]:
           Screen_Death("Je gaat naar buiten en zoekt de uitgang van het bos.\nNa uren te lopen vries je dood")

    elif number == 10:
        vraag = "Je rent door het bos en je krijgt trek."
        opties = ["Je rent terug naar het huisje.", "Je gaat eten zoeken.", "Je zoekt door naar de uitgang van het bos."]
        UserAntwoord = Vraag(vraag, opties)
        if UserAntwoord in ["1", "a"]:
            Screen_Death("De man vond het niet leuk dat je wegrende.\nHij stak een mes tussen je ribben.")
        if UserAntwoord in ["2", "b"]:
            GoToVraag(11)
        if UserAntwoord in ["3", "c"]:
           Screen_Death("Je zocht voor uren.\nEn je vroor dood.")

    elif number == 11:
        vraag = "Je vind een bramen struik."
        opties = ["Je rent terug naar het huisje.", "Je eet wat bramen.", "Je zoekt door naar de uitgang van het bos."]
        UserAntwoord = Vraag(vraag, opties)
        if UserAntwoord in ["1", "a"]:
            Screen_Death("De man vond het niet leuk dat je wegrende.\nHij stak een mes tussen je ribben.")
        if UserAntwoord in ["2", "b"]:
            Screen_Death("De bramen waren bedorven")
        if UserAntwoord in ["3", "c"]:
           Screen_Death("Je zocht voor uren.\nEn je vroor dood.")

    elif number == 12:
        vraag = "Na het eten bedank je de man.\nJe krijgt een kaart van de man.\nJe gaat op pad."
        opties = ["Je rent terug naar het huisje.", "Je eet wat bramen.", "Je zoekt door naar de uitgang van het bos."]
        UserAntwoord = Vraag(vraag, opties)
        if UserAntwoord in ["1", "a"]:
            Screen_Death("De man vond het niet leuk dat je wegrende.\nHij stak een mes tussen je ribben.")
        if UserAntwoord in ["2", "b"]:
            Screen_Death("De bramen waren bedorven")
        if UserAntwoord in ["3", "c"]:
           Screen_Death("Je zocht voor uren.\nEn je vroor dood.")

    else:
        tprint("YOU WIN")
    
clear_screen()
slowprint(intro)
input("Druk op enter om te beginnen")

GoToVraag(1)
