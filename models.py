import pickle
from datetime import datetime


class Note:
    db = {'id_': -1, 'notes':{}}

    def __init__(self, title, content, id_ = None, date_updated=None):
        self.id = id_
        self.title = title
        self.date_created = datetime.now()
        self.date_updated = date_updated
        self.content = content

    @classmethod
    def save(self, **kwargs):
        # title id_ content

        if 'id_' in kwargs:
            id_ = kwargs['id_']
        else:
            id_ = self.db['id_'] + 1

        title = kwargs['title']
        content = kwargs['content']
        self.db['notes'][id_] = Note(title, content, id_)
        self.db['id_'] = id_
        return 1

    @classmethod
    def update(self, **kwargs):
        id_ = kwargs['id_']
        n = Note()
        date_updated = datetime.now()
        return 1

    @classmethod
    def get(self, id_):
        return self.db['notes'][id_]

    @classmethod
    def get_all(self):
        return self.db['notes'].values()

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
        # db_file = open('db', 'wb')
        # self.db = pickle.dump(self.db, db_file)
        with open('db', 'wb') as f:
            self.db = pickle.dump(self.db, f)
        return f.close()


    # def __str__(self):
    #     return f'{self.date_created}\n{self.title}\n\n{self.content}\n'
    #
    def __repr__(self):
        return f'\n{self.id}\t{self.date_created}\t{self.title}\t{self.content}\n'


