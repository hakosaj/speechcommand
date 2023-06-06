# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
from pydub import AudioSegment
from pydub.playback import play

# Sampling frequency
freq = 44100

# Recording duration
duration = 5


# Start recorder with the given values of 
# duration and sample frequency
print("recordin")
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)

# Record audio for the given number of seconds
sd.wait()

write("recording0.wav", freq, recording)

song = AudioSegment.from_wav("recording0.wav")
play(song)