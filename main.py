# from tkinter import *
# from tkinter import ttk
import json
from models import Note

# def take_note():
#     parser = argparse.ArgumentParser(prog='CoWNote')
#     parser.add_argument('title', type = str)
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
#
#
#
# take_note()

Note.save('New Note2')
Note.save('New Note2')
Note.save('New Note2')
notes = Note.get_all()
print(notes)
for note in notes.values():
    print(note.__dict__)





