from dearlog import logger  # isort: split

from importlib.metadata import metadata

__meta__    = metadata(str(__package__))
__about__   = __meta__.get("Summary")
__author__  = __meta__.get("Author")
__version__ = __meta__.get("Version")

from pathlib import Path

resources: Path = Path(__file__).parent/"resources"

from spectronote.scene import SpectroScene