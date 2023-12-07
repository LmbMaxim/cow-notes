import argparse
from models import Note

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
n1 = Note(args.title)
print(n1)
