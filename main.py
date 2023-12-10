import argparse
import curses

from models import Note


Note.load_db()
def take_note():
    parser = argparse.ArgumentParser(prog='CoWNote')
    parser.add_argument('-ls', '--list', action='store_true')
    parser.add_argument('-id', '--note_id', type=int)
    # parser.add_argument('-add', '--title', type=str)
    # parser.add_argument('-edit', '--note_id_edit', type=int)
    args = parser.parse_args()

    # if args.title:
    #     Note.save(args.title)
    #     print(Note.get_all())
    #     return 0
    msg = []
    if args.list:
        for note in (Note.get_all()):
            msg.append(str(note))
        return msg
    
    # Bug. 0 id no show up
    if args.note_id:
         m = Note.get(args.note_id)
         msg.append(str(m))
         # print(args.note_id)
         return msg

    # if args.note_id_edit:
    #     print(Note.get(args.note_id_edit)) 
    #     n = Note.edit(args.note_id_edit)
    # return 0
#

# title, content = 'article', 'lorumipsum'
# print(Note.update(id_=4, title=title, content=content))



# Note.save('Project Idia', 'Make local dashboard with docker')
# Note.save('Project Idia', 'Make game in webasm')

# Note.save(title='Idia For Plugin', content='Tmux tabs for waybar')
# Note.save(title='Best Game', content='''Make game where you need manage resourcesMake game where you need manage resourcesMake game where you need manage resourcesMake game where you need manage resourcesMake game where you need manage resourcesMake game where you need manage resources''')
# Note.update(title='Project Idia million bucks', content='Make game BBB', id_=0)
# Note.update(title='Project Idia million bucks', content='Make game BBB', id_=1)
# Note.update(title='Suckless Project', content='Make game ', id_=2)
# a  = Note.update(title='Project Idia2', content='Make game')

msg = take_note()
# for m in msg:
#     print(m)
def main(stdscr):

    def win_left(msg):
        win = curses.newwin(5,0,0, 0)
        win.clear()
        for m in msg:
            win.addstr(m)
        win.refresh()
        win.getch()

    # win2 = curses.newwin(5, curses.COLS - (curses.COLS//2) ,0,60)
    def win_right(id_):
        id_=id_
        win2 = curses.newwin(5,0,0, curses.COLS //2)
        win2.clear()
        m = Note.db['notes'][id_]
        win2.addstr(m.content)
        win2.refresh()
        win2.getch()

    win_left(msg)
    id_ = 2
    if id_ != None:
        win_right(id_)

    # stdscr.clear()
    # for m in msg:
    #     stdscr.addstr(m)
    #
    # stdscr.refresh()
    # stdscr.getch()



curses.wrapper(main)
Note.write_db()
