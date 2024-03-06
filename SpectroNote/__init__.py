import SpectroNote.Resources as SpectroNoteResources
from ShaderFlow import *

import Broken
from Broken import *

SPECTRONOTE = BrokenProject(
    PACKAGE=__file__,
    APP_NAME="SpectroNote",
    APP_AUTHOR="BrokenSource",
    RESOURCES=SpectroNoteResources,
)

Broken.PROJECT = SPECTRONOTE

from .SpectroNote import *
