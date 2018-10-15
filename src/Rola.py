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


    def make_artist(self, artist):
        self.artist = artist
        return artist

    def make_title(self, title):
        self.title = title
        return title

    def make_albumname(self, albumname):
        self.albumname = albumname
        return albumname

    def make_year(self, year):
        self.year = year
        return year


    def make_genre(self, genre):
        self.genre = genre
        return genre


    def make_albumnumer(self, albumnumer):
        #if(albumnumer == None or albumnumer):
        #    self.albumnumer = "Unknown"
        #else:
        self.albumnumer = albumnumer
        return albumnumer


    def make_path(self, path):
        self.path = path
        return self.path
