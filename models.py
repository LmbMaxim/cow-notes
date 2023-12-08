import pickle

from datetime import datetime

class Note:
    db = {'id_': -1, 'notes':{}}

    def __init__(self, title, id_=None):
        self.id = id_
        self.title = title
        self.date_created = datetime.now()
        self.content = "<CONTENT>"


    @classmethod
    def save(self, title):
        id_ = self.db['id_'] + 1
        self.db['notes'][id_] = Note(title, id_ = id_)
        self.db['id_'] = id_
        return 1

    @classmethod
    def get(self, id_):
        return self.db['notes'][id_]

    @classmethod
    def get_all(self):
        return self.db

    @classmethod
    def load_db(self):
        with open('db', 'rb') as f:
            try:
                data = pickle.load(f)
            except EOFError:
                return 0
        self.db = data
        return f.close()

    @classmethod
    def write_db(self):
        db_file = open('db', 'wb')
        self.db = pickle.dump(self.db, db_file)
        return db_file.close()




    # def __str__(self):
    #     return f'{self.date_created}\n{self.title}\n\n{self.content}\n'
    #
    def __repr__(self):
        return f'\n{self.id}\t{self.date_created}\t{self.title}\t{self.content}\n'


