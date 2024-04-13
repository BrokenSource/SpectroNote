import sys

from Broken import BrokenProfiler
from SpectroNote import SPECTRONOTE
from SpectroNote.SpectroNote import SpectroNoteScene


def main():
    with BrokenProfiler("SPECTRONOTE"):
        SPECTRONOTE.welcome()
        spectronote = SpectroNoteScene()
        spectronote.cli(sys.argv[1:])

if __name__ == "__main__":
    main()
