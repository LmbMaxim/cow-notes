import argparse

from models import Note


Note.load_db()
def take_note():
    parser = argparse.ArgumentParser(prog='CoWNote')
    parser.add_argument('-ls', '--list', action='store_true')
    parser.add_argument('-id', '--note_id', type=int)
    parser.add_argument('-add', '--title', type=str)
    # parser.add_argument('-edit', '--note_id_edit', type=int)
    args = parser.parse_args()

    if args.title:
        Note.save(args.title)
        print(Note.get_all())
        return 0

    if args.list:
        for note in (Note.get_all()):
            print(note)
        return 0

    if args.note_id:
        n = Note.get(args.note_id)
        print(n)
    return 0

    # if args.note_id_edit:
    #     print(Note.get(args.note_id_edit)) 
    #     n = Note.edit(args.note_id_edit)
    # return 0


take_note()

# Load db when start
# db = open('db', 'rb')
# a =  pickle.load(db)
# print(a)
#
#

# Note.load_db()

# Note.save('Project Idia', 'Make local dashboard with docker')
# Note.save('Project Idia', 'Make game in webasm')



Note.write_db()
