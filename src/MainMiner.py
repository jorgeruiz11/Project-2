from Miner import Miner
from DataBase import DataBase

def main():
    db = DataBase()
    db.connect()
    m = Miner()
    m.get_files()
    m.get_tags()
    m.insert()

if __name__ == '__main__':
    main()
