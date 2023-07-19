"""
makewaves — a simple toolkit for making wavetable WAV files for 
software synthesisers
"""

import struct
import wave

def make_wavetable(file, waves, wave_samples=1024):
	"""
	Write a wavetable to a WAV file from a set of functions generating 
	waveforms.

	Arguments:
		file: the file to write the WAV data to, either a string path 
			or a file-like object
		waves: an array of functions, each taking a floating-point phase
			between 0 and 1 and returning a sample value between -1 and 1
		wave_samples: the number of samples to be generated for each 
			waveform. For most systems this should be a power of 2. 
			For example, Ableton Live's Wavetable instrument uses 1024,
			and Xfer Serum uses 2048.
	"""
	output = wave.open(file, "wb")
	output.setnchannels(1)
	output.setsampwidth(2)
	output.setframerate(44100)
	output.setnframes(wave_samples*len(waves))

	for (waveindex, func) in enumerate(waves):
		buf = bytearray()
		for s in range(wave_samples):
			phase = s/wave_samples
			v = func(phase)
			try:
				buf += struct.pack("<h", int(v * 0x7fff))
			except struct.error:
				raise ValueError("Wave %i, phase %f: invalid value: %f"%(waveindex, phase, v))
		output.writeframes(buf)
	output.close()

