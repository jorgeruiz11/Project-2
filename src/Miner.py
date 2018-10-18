import os
from Rola import Rola
from mutagen.id3 import ID3

class Miner():

    def __init__(self):
        self.files = []
        self.songs = []

    def get_files(self):
        route = os.path.expanduser('~/Música')

        for root, directoryname, filename in os.walk(route):
            for file in filename:
                self.files.extend([os.path.join(root, file)])

    # Método que dada la ruta absoluta de una canción intenta obtener sus
    # etiquetas. Si tiene las etiquetas, las regresa. En caso de no tenerlas
    # le asignará un valor predeterminado.
    def get_tags(self):
        for i in self.files:
            audio = ID3(i)
            rola = Rola()

            path_rola = rola.property_path(i)

            if 'TIT2' in audio:
                title = rola.property_title(audio['TIT2'])
            else:
                title = rola.property_title('Unknown')

            if 'TPE1' in audio:
                artist = rola.property_artist(audio['TPE1'])
            else:
                artist = rola.property_artist('Unknown')

            if 'TALB' in audio:
                album = rola.property_albumname(audio['TALB'])
            else:
                album = rola.property_albumname('Unknown')

            if 'TDRC' in audio:
                year = rola.property_year(audio['TDRC'])
            else:
                year = rola.property_year(0)

            if 'TCON' in audio:
                genre = rola.property_genre(audio['TCON'])
            else:
                genre = rola.property_genre('Unknown')

            if 'TRCK' in audio:
                number = rola.property_albumnumer(audio['TRCK'])
            else:
                number = rola.property_albumnumer(0)

            self.songs.append(rola)

            print(rola.property_title(title))
            print(rola.property_artist(artist))
            print(rola.property_albumname(album))
            print(rola.property_year(year))
            print(rola.property_genre(genre))
            print(rola.property_albumnumer(number))
            print('-------------------------------')
