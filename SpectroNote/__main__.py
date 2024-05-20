import sys

from Broken import BrokenProfiler
from SpectroNote.SpectroNote import SpectroNoteScene


def main():
    with BrokenProfiler("SPECTRONOTE"):
        spectronote = SpectroNoteScene()
        spectronote.cli(sys.argv[1:])

if __name__ == "__main__":
    main()
