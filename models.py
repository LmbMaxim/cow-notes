from datetime import datetime

class Note:
    db = {}

    def __init__(self, title, id_=None):
        self.id = id_
        self.title = title
        self.date_created = datetime.now()
        self.content = "<CONTENT>"



    @classmethod
    def save(self, title, id_):
        self.db[id_] = Note(title)
        return 1

    @classmethod
    def get(self, id_):
        return self.db[id_]


    def __str__(self):
        return f'{self.date_created}\n{self.title}\n\n{self.content}\n'

    def __repr__(self):
        return f'{self.date_created}\n{self.title}\n\n{self.content}\n'


