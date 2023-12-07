from datetime import datetime

class Note:
    def __init__(self, title):
        self.title = title
        self.date_created = datetime.now()
        self.content = "<CONTENT>"

    def __str__(self):
        return f'{self.date_created}\n{self.title}\n\n{self.content}\n'

    def __repr__(self):
        return f'{self.date_created}\n{self.title}\n\n{self.content}\n'


