from . import *


@define
class SpectroNoteScene(ShaderScene):
    """🎧 Piano-Perfect Audio Spectrogram. Unlock a hidden Absolute Pitch in you. Lightning fast, reliable, customizable."""
    __name__ = "SpectroNote"

    # Scene parameters
    piano_bins:   bool  = False
    piano_range:  bool  = False
    piano_size:   float = 0.05
    black_ratio:  float = 0.5
    border_ratio: float = 0.1
    vertical:     bool  = False

    def build(self):
        ShaderScene.build(self)
        self.audio = ShaderAudio(scene=self.scene, name="Audio", file="/path/to/audio.ogg")
        self.spectrogram = ShaderSpectrogram(scene=self.scene, audio=self.audio, smooth=True)

        # Act immediately, good visuals and precision
        self.spectrogram.dynamics.frequency = 20
        self.spectrogram.sample_rateio = 2
        self.spectrogram.fft_n = 13

        # # Define ranges
        PIANO_RANGE = dict(start=21, end=108)
        FULL_RANGE = dict(start=20.0, end=20000.0)

        self.spectrogram.from_notes(
            **(PIANO_RANGE if self.piano_range else FULL_RANGE),
            piano=self.piano_bins,
            bins=1440,
        )

        self.shader.fragment = SPECTRONOTE.RESOURCES.SHADERS/"SpectroNote.frag"

    def pipeline(self):
        yield from ShaderScene.pipeline(self)
        yield ShaderVariable("uniform", "float", "iPianoSize",   self.piano_size)
        yield ShaderVariable("uniform", "float", "iBlackRatio",  self.black_ratio)
        yield ShaderVariable("uniform", "float", "iBorderRatio", self.border_ratio)
        yield ShaderVariable("uniform", "bool",  "iVertical",    self.vertical)
