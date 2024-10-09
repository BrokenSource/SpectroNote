import sys

from broken import BrokenProfiler
from spectronote.spectronote import SpectroNoteScene


def main():
    with BrokenProfiler("SPECTRONOTE"):
        spectronote = SpectroNoteScene()
        spectronote.cli(sys.argv[1:])

if __name__ == "__main__":
    main()
