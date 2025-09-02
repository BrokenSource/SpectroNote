from typing import Iterable

from attrs import define
from shaderflow.modules.audio import ShaderAudio
from shaderflow.modules.spectrogram import ShaderSpectrogram
from shaderflow.scene import ShaderScene
from shaderflow.variable import ShaderVariable, Uniform

from spectronote import SPECTRONOTE


@define
class SpectroScene(ShaderScene):
    """🎧 Piano-Perfect Audio Spectrogram. Unlock a hidden Absolute Pitch in you. Lightning fast, reliable, customizable"""

    # Scene parameters
    piano_bins:   bool  = False
    piano_range:  bool  = False
    piano_size:   float = 0.05
    black_ratio:  float = 0.5
    border_ratio: float = 0.1
    vertical:     bool  = False
    tuning:       float = 440

    def build(self):
        self.shader.fragment = SPECTRONOTE.RESOURCES.SHADERS/"spectronote.frag"
        self.audio = ShaderAudio(scene=self, name="Audio", file="/path/to/audio.ogg")
        self.spectrogram = ShaderSpectrogram(scene=self, audio=self.audio, smooth=True)

        # Act immediately, good visuals and precision
        self.spectrogram.dynamics.frequency = 20
        # self.spectrogram.sample_rateio = 2
        self.spectrogram.length = 5
        self.spectrogram.fft_n = 13

        # # Define ranges
        PIANO_RANGE = dict(start=21, end=108)
        FULL_RANGE = dict(start=20.0, end=20000.0)

        self.spectrogram.from_notes(
            **(PIANO_RANGE if self.piano_range else FULL_RANGE),
            piano=self.piano_bins,
            tuning=self.tuning,
            bins=1440,
        )

    def pipeline(self) -> Iterable[ShaderVariable]:
        yield from ShaderScene.pipeline(self)
        yield Uniform("float", "iPianoSize",   self.piano_size)
        yield Uniform("float", "iBlackRatio",  self.black_ratio)
        yield Uniform("float", "iBorderRatio", self.border_ratio)
        yield Uniform("bool",  "iVertical",    self.vertical)
