from datetime import datetime

class Note:
    db = {'id_':0}

    def __init__(self, title, id_=None):
        # Implement ID that is basically counter that updated when note saves in to db.
        self.id = id_
        self.title = title
        self.date_created = datetime.now()
        self.content = "<CONTENT>"



    @classmethod
    def save(self, title):
        id_ = self.db['id_'] + 1
        self.db[id_] = Note(title)
        self.db['id_'] = id_
        return 1

    @classmethod
    def get(self, id_):
        return self.db[id_]

    @classmethod
    def get_all(self):
        return self.db


    def __str__(self):
        return f'{self.date_created}\n{self.title}\n\n{self.content}\n'

    def __repr__(self):
        return f'{self.date_created}\n{self.title}{self.content}\n\n\n'



