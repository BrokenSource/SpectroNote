import importlib.metadata

from broken import BrokenProject

__version__ = importlib.metadata.version(__package__)

SPECTRONOTE = BrokenProject(
    PACKAGE=__file__,
    APP_NAME="SpectroNote",
)

from spectronote.scene import SpectroScene
