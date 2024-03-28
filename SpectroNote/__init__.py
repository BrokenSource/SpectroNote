import Broken
import SpectroNote.Resources as SpectroNoteResources
from Broken.Project import BrokenProject

SPECTRONOTE = BrokenProject(
    PACKAGE=__file__,
    APP_NAME="SpectroNote",
    APP_AUTHOR="BrokenSource",
    RESOURCES=SpectroNoteResources,
)

Broken.set_project(SPECTRONOTE)
