import SpectroNote.Resources as SpectroNoteResources
from Broken import BrokenProject, __version__

__version__ = __version__

SPECTRONOTE = BrokenProject(
    PACKAGE=__file__,
    APP_NAME="SpectroNote",
    APP_AUTHOR="BrokenSource",
    RESOURCES=SpectroNoteResources,
)
