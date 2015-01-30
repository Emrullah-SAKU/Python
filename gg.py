"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""
## TimeoutError hatasý exception ile alýnsýn
## try cath yapýsýna çevirilsin yapý
## ``Microphone(device_index = None)`` kullanýlsýn

""" Mikrofon deðerlerini belirlemek için
``recognizer_instance.energy_threshold = 100``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Represents the energy level threshold for sounds. Values below this threshold are considered silence. Can be changed.

This threshold is associated with the perceived loudness of the sound, but it is a nonlinear relationship. Typical values for a silent room are 0 to 1, and typical values for speaking are between 150 and 3500.

If you're having trouble with the recognizer trying to recognize words even when you're not speaking, try tweaking this to a higher value. For example, a sensitive microphone or microphones in louder rooms might have a baseline energy level of up to 4000:

.. code:: python

import speech_recognition as sr
r = sr.Recognizer()
r.energy_threshold = 4000
# rest of your code goes here

The actual energy threshold you will need depends on your microphone or audio data.
----------------------------------------------------------------------------------
"""

""" Google API vs çalýþmayacaðý zaman try cath ile yakalamamýz gereken hatalar
Performs speech recognition, using the Google Speech Recognition API, on ``audio_data`` (an ``AudioData`` instance).

Returns the most likely transcription if ``show_all`` is ``False``, otherwise it returns a ``dict`` of all possible transcriptions and their confidence levels.

Note: confidence is set to 0 if it isn't given by Google

Also raises a ``LookupError`` exception if the speech is unintelligible, or a ``KeyError`` if the key isn't valid or the quota for the key has been maxed out.

Note: ``KeyError`` is a subclass of ``LookupError`` so a ``LookupError`` will catch both. To catch a ``KeyError`` you must place it before ``LookupError`` eg:

.. code:: python

import speech_recognition as sr
r = sr.Recognizer()
with sr.WavFile("test.wav") as source: # use "test.wav" as the audio source
audio = r.record(source) # extract audio data from the file

try:
print("You said " + r.recognize(audio)) # recognize speech using Google Speech Recognition
except KeyError: # the API key didn't work
print("Invalid API key or quota maxed out")
except LookupError: # speech is unintelligible
print("Could not understand audio")
--------------------------------------------------------------------------------
"""

##  Parametreler
# - open door
# - close door
#

import pyaudio
import wave
import speech_recognition as sr
"""
RECORD_SECONDS = 3
CHUNK = 1024
RATE = 44100"""

r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    print "Komutu verin lütfen: "
    audio = r.listen(source,timeout = 3)#timeout is time of recording # listen for the first phrase and extract it into audio data

try:
    print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
    if r.recognize(audio) == 'open door':
        print '     Kapý açýlýyor'
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
"""
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
"""
