import random


def zufallszahl_generieren():
    """Generiert eine Zufallszahl zwischen 1 und 100."""
    return random.randint(1, 100)


def spiel_starten():
    """Implementiert den Spielablauf."""
    zahl = zufallszahl_generieren()
    versuche = 0

    while versuche < 6:
        eingabe = input("Gib eine Zahl zwischen 1 und 100 ein: ")

        if eingabe_prüfen(eingabe):
            eingabe = int(eingabe)
            if eingabe == zahl:
                ausgabe(
                    "Gratulation, du hast die Zahl erraten! Du hast dafür " + str(versuche) + " Versuche gebraucht.")
                break
            elif eingabe < zahl:
                ausgabe("Die gesuchte Zahl ist größer.")
            else:
                ausgabe("Die gesuchte Zahl ist kleiner.")
            versuche += 1
        else:
            ausgabe("Ungültige Eingabe. Bitte gib eine Zahl zwischen 1 und 100 ein.")

    if versuche == 6:
        ausgabe("Leider hast du die Zahl nicht erraten. Die richtige Zahl war " + str(zahl) + ".")


def eingabe_prüfen(eingabe):
    """Prüft, ob die Eingabe eine gültige Zahl ist."""
    try:
        zahl = int(eingabe)
        if 1 <= zahl <= 100:
            return True
        else:
            return False
    except ValueError:
        return False


def ausgabe(nachricht):
    """Gibt die Nachricht auf der Konsole aus."""
    print(nachricht)


spiel_starten()
