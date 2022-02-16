import jsonpickle


class Profil(object):
    def __init__(self, name, guthaben):
        self.name = name
        self.guthaben = guthaben
        # bestehend aus Transaktion Objekten
        self.transaktionen = []

class Transaktion():
    def __init__(self, name, betrag, datum):
        self.name = name
        self.betrag = betrag
        self.datum = datum

    def __str__(self):
        return f'Name: {self.name} | Betrag: {self.betrag} Euro | Datum: {self.datum}'


class ProfilManager():
    # Profil Serialisierung
    def erstelle_profil(name, guthaben):
        profil = Profil(name, guthaben)
        json_profil = jsonpickle.encode(profil)

        with open(f'.\Profile\{name}.json', 'w') as f:
            f.write(json_profil)

    # Profil Deserialisierung
    def lade_profil(name):
        profil_aus_json = open(f'.\Profile\{name}.json').read()
        profil = jsonpickle.decode(profil_aus_json)

        return profil

    # Profil aktualisierung
    def update_profil(profil):
        json_profil = jsonpickle.encode(profil)

        with open(f'.\Profile\{profil.name}.json', 'w') as f:
            f.write(json_profil)


    erstelle_profil = staticmethod(erstelle_profil)
    lade_profil = staticmethod(lade_profil)
    update_profil = staticmethod(update_profil)
