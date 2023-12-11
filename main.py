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
            msg.append(note)
        return msg
    
    # Bug. 0 id no show up
    if args.note_id != None:
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

# Note.save(title='1Title1', content=' text text text "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"')
# Note.save(title='2Title2', content=' text text text "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"')
# Note.save(title='3Title3', content=' text text text "ccccccccccccccccccccccccccccccccccccccccc"')
# Note.save(title='4Title4', content=' text text text "ddddddddddddddddddddddddddddddddddddddddd"')
# Note.save(title='5Title5', content=' text text text "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"')
# Note.save(title='6Title6', content=' text text text "11111111111111111111111111111111111111111"')
# Note.save(title='7Title7', content=' text text text "22222222222222222222222222222222222222222"')
# Note.save(title='8Title8', content=' text text text "33333333333333333333333333333333333333333"')
# Note.save(title='9Title9', content=' text text text "44444444444444444444444444444444444444444"')
# Note.update(title='Project Idia million bucks', content='Make game BBB', id_=0)
# Note.update(title='Project Idia million bucks', content='Make game BBB', id_=1)
# Note.update(title='Suckless Project', content='Make game ', id_=2)

def main(stdscr):
    half_win = curses.COLS//2
    hg = curses.A_REVERSE

    win = curses.newwin(0, half_win -2, 0, 0)
    win2 = curses.newwin(0, half_win, 0, half_win)

    def render_win_r(win, i = 0):
        msg = Note.get(i).content
        win.clear()
        win.addstr(str(msg))
        win.refresh()
        # win.getch()

    def render_win_l(win, i = 0):
        win.clear()
        note = i
        for note in Note.get_all():
            if note == i:
                hg = curses.A_REVERSE
            else:
                hg = curses.A_DIM

            win.addstr(str(Note.get(note)), hg)
        win.refresh()
        # win.getch()

    i = 0
    while True:
        render_win_l(win, i)
        render_win_r(win2, i)
        c = win.getch()
        if c == ord('q'):
            break

        elif c == ord('j'):
            i += 1

        elif c == ord('k'):
            i -= 1


curses.wrapper(main)
Note.write_db()
