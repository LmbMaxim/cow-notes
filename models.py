from datetime import datetime

class Note:
    def __init__(self, title):
        self.title = title
        self.date_created = datetime.now()
        self.content = None

    def __str__(self):
        return f'{self.date_created}\n{self.title}\n\n{self.content}\n'


n1 = Note("My Note")
n1.content = """Hello it is my first Note in this
beautiful application!!!"""





print(n1)

