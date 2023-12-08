import pickle
import argparse

from models import Note

# Note.load_db()
#
# def take_note():
#     parser = argparse.ArgumentParser(prog='CoWNote')
#     parser.add_argument('-t', '--title', type = str)
#     # parser.add_argument('-ls', '--list', action='store_true')
#     args = parser.parse_args()
#
#     # if args.list:
#     #     print(Note.get_all())
#     #     return 0
#
#     if args.title:
#         n = Note.save(args.title)
#         return n
#     return 0


# take_note()

# Load db when start
# db = open('db', 'rb')
# a =  pickle.load(db)
# print(a)
#
#
Note.load_db()

Note.save('Project Idia', 'Make local dashboard with docker')

# # Write db at the end

notes = Note.get_all()
print(notes)

Note.write_db()
