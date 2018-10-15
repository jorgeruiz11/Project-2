import os
from Rola import Rola
from mutagen.id3 import ID3

class Miner():

    def __init__(self):
        self.files = []

    def get_files(self):
        route = os.path.expanduser('~/Música')

        for root, directoryname, filename in os.walk(route):
            for file in filename:
                self.files.extend([os.path.join(root, file)])

    # Método que dada la ruta absoluta de una canción intenta obtener sus
    # etiquetas. Si tiene las etiquetas, las regresa. En caso de no tenerlas
    # 
    def get_tags(self):
        for i in self.files:
            audio = ID3(i)
            rola = Rola()

            try:
                title = audio['TIT2']
            except:
                title = 'Unknown'

            try:
                artist = audio['TPE1']
            except:
                artist = 'Unknown'

            try:
                album = audio['TALB']
            except:
                album = 'Unknown'

            try:
                year = audio['TDRC']
            except:
                year = 0

            try:
                genre = audio['TCON']
            except:
                genre = 'Unknown'

            try:
                number = audio['TRCK']
            except:
                number = 0

            rola.make_title(title)
            rola.make_artist(artist)
            rola.make_albumname(album)
            rola.make_year(year)
            rola.make_genre(genre)
            rola.make_albumnumer(number)
