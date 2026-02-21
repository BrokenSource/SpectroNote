from typing import Annotated, Iterable

from attrs import Factory, define
from pydantic import BaseModel, ConfigDict
from shaderflow.audio import ShaderAudio, ShaderSpectrogram
from shaderflow.scene import ShaderScene
from shaderflow.variable import Uniform
from typer import Option

import spectronote


class SpectroConfig(BaseModel):
    model_config = ConfigDict(use_attribute_docstrings=True)

    # ---------------------------------|
    # Inputs

    audio: Annotated[str, Option("--audio", "-a")] = "/path/to/audio.ogg"
    """Path to the audio file to visualize or export video"""

    # Todo: Audio capture on shaderflow.audio overhaul

    # ---------------------------------|
    # Spectrogram

    length: Annotated[float, Option("--length", "-l")] = 5.0
    """Length of the spectrogram in seconds"""

    interpolate: Annotated[bool, Option(" /--step")] = True
    """Don't interpolate frequencies between piano notes"""

    # ---------------------------------|
    # Mathematics

    min: Annotated[str, Option("--min")] = "20.0"
    """Minimum frequency (float) or piano note (int, 21 is A0) to display"""

    max: Annotated[str, Option("--max")] = "20000.0"
    """Maximum frequency (float) or piano note (int, 108 is C8) to display"""

    tuning: Annotated[float, Option("--tuning", "-t")] = 440.0
    """Frequency of the A4 note for telling notes"""

    bins: Annotated[int, Option("--bins", "-b")] = 1440
    """Number of frequency bins in the spectrogram"""

    fft_n: Annotated[int, Option("--fft-n", "-n")] = 13
    """Context length for FFT (2**n samples)"""

    # ---------------------------------|
    # Piano helper

    horizontal: Annotated[bool, Option("--horizontal", "-h")] = False
    """Orient the piano horizontally instead of vertically"""

    piano: Annotated[float, Option("--piano")] = 0.05
    """Relative size of the piano keys on the sides"""

    black: Annotated[float, Option("--black")] = 0.5
    """How long are black keys compared to white keys"""

    border: Annotated[float, Option("--border")] = 0.1
    """Relative size of the border between white keys"""


@define
class SpectroScene(ShaderScene):
    config: SpectroConfig = Factory(SpectroConfig)

    def commands(self):
        self.cli.description = spectronote.__about__
        self.cli.command(self.config, name="config")

    def build(self):
        self.shader.fragment = (spectronote.resources/"spectronote.glsl")
        self.audio = ShaderAudio(scene=self, name="Audio", file=self.config.audio)
        self.spectrogram = ShaderSpectrogram(scene=self, audio=self.audio,
            smooth=self.config.interpolate)

        # Act immediately, good visuals and precision
        self.spectrogram.dynamics.frequency = 20
        self.spectrogram.length = self.config.length
        self.spectrogram.fft_n = self.config.fft_n

        _eval = lambda x: eval(x) if isinstance(x, str) else x

        self.spectrogram.from_notes(
            start=_eval(self.config.min),
            end=_eval(self.config.max),
            tuning=self.config.tuning,
            bins=self.config.bins,
        )

    def pipeline(self) -> Iterable[Uniform]:
        yield from ShaderScene.pipeline(self)
        yield Uniform("float", "iPianoSize",   self.config.piano)
        yield Uniform("float", "iBlackRatio",  self.config.black)
        yield Uniform("float", "iBorderRatio", self.config.border)
        yield Uniform("bool",  "iHorizontal",  self.config.horizontal)
