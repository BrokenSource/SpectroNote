import sys

import spectronote
from spectronote import SpectroScene


def main():
    scene = SpectroScene()
    scene.cli.meta(sys.argv[1:])

if __name__ == "__main__":
    main()
