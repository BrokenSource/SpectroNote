from dearlog import logger  # isort: split

__about__   = "🎧 Piano-perfect audio spectrogram"
__package__ = "spectronote"
__version__ = "0.11.0"
__license__ = "AGPL-3.0"

from pathlib import Path

resources: Path = Path(__file__).parent/"resources"

from spectronote.scene import SpectroScene
