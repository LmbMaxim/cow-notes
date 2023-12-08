import argparse

from models import Note

Note.load_db()

# n = Note.get(0)
# print(n)

def take_note():
    parser = argparse.ArgumentParser(prog='CoWNote')
    parser.add_argument('-ls', '--list', action='store_true')
    parser.add_argument('-id', '--note_id', type=int)
    args = parser.parse_args()

    if args.list:
        print(Note.get_all())
        return 0

    if args.note_id:
        n = Note.get(args.note_id)
        print(n)
    return 0


take_note()

# Load db when start
# db = open('db', 'rb')
# a =  pickle.load(db)
# print(a)
#
#

# Note.load_db()

Note.save('Project Idia', 'Make local dashboard with docker')
Note.save('Project Idia', 'Make game in webasm')

Note.write_db()
