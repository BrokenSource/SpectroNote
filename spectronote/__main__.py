import sys

from spectronote import SpectroScene


def main():
    spectronote = SpectroScene()
    spectronote.cli(*sys.argv[1:])

if __name__ == "__main__":
    main()
