from . import *


def main():
    with BrokenProfiler("SPECTRONOTE"):
        SPECTRONOTE.welcome()
        spectronote = SpectroNoteScene()
        spectronote.cli(sys.argv[1:])

if __name__ == "__main__":
    main()
