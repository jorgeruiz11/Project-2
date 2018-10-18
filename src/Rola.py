# Clase para manejar correctamente los atributos de las rolas.
class Rola():

    def __init__(self):
        self.artist = ""
        self.title = ""
        self.albumname = ""
        self.year = ""
        self.genre = ""
        self.albumnumer = ""
        self.path = ""

    def property_artist(self, artist):
        self.artist = artist
        return artist

    def property_title(self, title):
        self.title = title
        return title

    def property_albumname(self, albumname):
        self.albumname = albumname
        return albumname

    def property_year(self, year):
        self.year = year
        return year

    def property_genre(self, genre):
        self.genre = genre
        return genre

    def property_albumnumer(self, albumnumer):
        self.albumnumer = albumnumer
        return albumnumer

    def property_path(self, path):
        self.path = path
        return self.path
