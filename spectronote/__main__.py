import sys

from broken import BrokenProfiler
from spectronote import SpectroScene

def main():
    with BrokenProfiler("SPECTRONOTE"):
        spectronote = SpectroScene()
        spectronote.cli(sys.argv[1:])

if __name__ == "__main__":
    main()
