import argparse
from models import Note

def take_note():
    parser = argparse.ArgumentParser(
            prog='CoWNote',
            description="""The best note taking app"""
            )

    parser.add_argument(
            'title',
            type = str,
            action = 'store'
            )

    args = parser.parse_args()
    n = Note(args.title)

    return n 




# notes = []
# n = take_note()
# notes.append(n)
# print(notes)


Note.save('New Note', 0)
print(Note.get(0))



