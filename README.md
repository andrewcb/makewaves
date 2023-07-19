# makewaves

A simple Python library for generating wavetables for software synthesisers. `makewaves` creates a WAV file formatted as a wavetable from an array of functions producing the individual waveform cycles to put in the wavetable. The WAV file consists of one cycle of each waveform, at a standard length.

## Example usage

The following example generates a wavetable consisting of sine, triangle, sawtooth and square waves in that order (equivalent to the “Basic Shapes” wavetable in the Ableton Wavetable instrument) and writes it to the file `wavetable.wav`:

```python

import math
import makewaves

waves = [
    # sine
    lambda p: math.sin(p*2*math.pi),
    # triangle
    lambda p: (4*p) * (p>0.25 and p<=0.75 and -1 or 1) + (p>0.75 and -4 or (p>0.25 and 2) or 0),
    # sawtooth
    lambda p: (((p+0.5)*2)%2)-1, 
    # square
    lambda p: p<0.5 and 1 or -1,
]

makewaves.make_wavetable("wavetable.wav", waves)

```

## Usage

`makewaves` contains one function: `make_wavetable`. This function takes the following arguments:

- `file` (required): The output file to write the wavetable to. This is either a string containing a path or a writeable file-like object (as accepted by the `wave` module)
- `waves`(required): An array of functions that generate waveforms. Each function takes one input: a `float` phase value from 0 to 1, and for each phase returns an amplitude value from -1 to 1. Each function is called to generate one cycle for the wavetable.
- `wave_samples`(optional; default is 1024): the number of samples each cycle consists of. For most systems this will be a power of two. Ableton Live's Wavetable instrument (with which this was tested) uses 1024; while Xfer Serum uses 2048 and u-he Hive can use a variety of values specified in the filename.

## Compatibility

`makewaves` was developed on Python 3.9 (i.e., the system Python on macOS 13.4.1), though should run on most recent Python 3.x versions.

## Author
Andrew Bulhak (https://github.com/andrewcb/)
