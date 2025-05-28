from broken import BrokenProject, __version__

SPECTRONOTE = BrokenProject(
    PACKAGE=__file__,
    APP_NAME="SpectroNote",
)

from spectronote.scene import SpectroScene
