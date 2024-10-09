import spectronote.resources as resources
from broken import BrokenProject

SPECTRONOTE = BrokenProject(
    package=__file__,
    name="SpectroNote",
    author="BrokenSource",
    resources=resources,
)
