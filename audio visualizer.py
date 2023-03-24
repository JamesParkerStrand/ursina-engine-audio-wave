import wave
import numpy as np
from scipy.io.wavfile import read
from ursina import *
import AudioPlayer

app = Ursina()

file = "first snow antent"

audioData = AudioPlayer.AudioPlay(file + ".wav")

audio = Audio(file + ".mp3")

#audio_entity = Entity(model="cube")

#audio_entity2 =  Entity(model="cube",position= (2,0,0))

pointMeshes = Mesh(vertices = [], mode='point', thickness=0.5)

pointsToGraph = audioData.incrementor

for i in range(pointsToGraph):
    pointMeshes.vertices.append([0,0,0])

pointGraph = Entity(model=pointMeshes, position=(-pointsToGraph / 2,0,0))

def update():

    audioData.incrementByFrameRateTick()

    leftChannel, rightChannel = audioData.sampleAmplitudeDataAtPosition()

    sampleData = leftChannel[len(leftChannel) - pointsToGraph + 1: len(leftChannel) - 1]

    for x in range(len(sampleData)):
        pointMeshes.vertices[x] = [x,0.01 * sampleData[x],0]

    pointMeshes.generate()

    pointGraph.model = pointMeshes

EditorCamera()

app.run()


# alternative code
#wav_obj = wave.open("first snow antent.wav","rb")

'''
this is just alternative code

sample_freq = wav_obj.getframerate()

n_channels = wav_obj.getnchannels()

n_samples = wav_obj.getnframes()

signal_wave = wav_obj.readframes(n_samples)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

l_channel = signal_array[0::2]
r_channel = signal_array[1::2]
'''
