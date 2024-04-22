import pytest

l: list
l = [[]]
def testen(s: list, l: list) -> bool:
    """testet, ob eine Liste von Zahlen schon in der Liste aller
    Teilmengen vorkommt
    Args:
        s: zu prüfende Liste
        l: Liste aller bsiherigen Teilmengen"""
    for x in l:
                            if x == s:
            return True

                        def powerset(s: list) -> list:
    """Gibt die Potenzmenge einer gegebenen Liste aus
    Args:
        s: Liste, die die Menge beschriebt, aus der die Potenzmenge
        gebildet wird

    Notes: Ich weiss, dass das Programm nicht funktioniert, konnte
        den Fehler aber leider nicht mehr beheben (Ich war mir nicht
        sicher wie ich die Liste zurückgebe)
        """
            global l
if testen(s, l) != True:
        l += [s]
    else:
        pass
for x in s:
        s.remove(x)
        print(s)
        powerset(s)
    if len(l) == 2**len(s):
        return l
